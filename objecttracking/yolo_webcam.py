# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')

import time
import json 

# конфигурационные модули
import config as cfg

# Модули для считывания данных с webcam и ML
import numpy as np
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt


# Модули для записи данных в Rabbit
import pika 


# Определяем параметры модели
options = {
    'model': 'cfg/yolo.cfg',
    'load': 'weights/yolov2.weights',
    'threshold': 0.3

}

# Задаем модель
tfnet = TFNet(options)

# Определяем параметры подкючения к Rabbit
credentials = pika.PlainCredentials(cfg.rabbitMqUser, cfg.rabbitMqPassword)
parameters = pika.ConnectionParameters(cfg.rabbitMqServer,
                                       cfg.rabbitMqPort,
                                       '/',
                                       credentials)


connection = pika.BlockingConnection(parameters)  
channel = connection.channel() 
channel.queue_declare(queue="yolo2_test") 


# Захватываме данные с web камеры
cap = cv2.VideoCapture(0)
colors=[tuple(255 * np.random.rand(3)) for i in range(5)]


while(cap.isOpened()):
    stime= time.time()
    ret, frame = cap.read()
    results = tfnet.return_predict(frame)
    
    #Оставляем только людей
    results  = [data for data in results if data['label']=='person']
    
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            
            x_center = (result['topleft']['x'] + result['bottomright']['x'])/2 
            y_center = (result['topleft']['y'] + result['bottomright']['y'])/2 
            
            label = result['label']
            confidence = result['confidence']
            
            dataSendToRabbit = {
                "timestamp": time.time(),
                "fps": '{:1f}'.format(1/(time.time() - stime)),
                "label": label,
                "confidence": str(confidence),
                "x_center": str(x_center),
                "y_center": str(y_center)
            }
            
            print(dataSendToRabbit)
            message = json.dumps(dataSendToRabbit)  
            channel.basic_publish(exchange='', routing_key="yolo2_test", body=message) 

            frame= cv2.rectangle(frame, tl, br, color, 7)
            frame= cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 2)
            
            # Отрисовка центра прямоугольника: рисуем круг с радиусом 2 
            frame = cv2.circle(frame, (int(x_center),int(y_center)), 2, (0, 0, 255), -1)
            
        cv2.imshow('frame', frame)
        if cv2.waitKey(1)  & 0xFF == ord('q'):
            break
    else:
        break
          
cap.release()
cv2.destroyAllWindows()

# Закрываем соединение с Rabbit
connection.close()  