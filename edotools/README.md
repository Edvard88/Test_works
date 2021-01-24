# README #

### About project ###
This project will explore how to detect and tracking objects from a webcam indoors.

### Directory structure ###
```bash
+-- README.md.         <- The top-level README for developers using this project.
+-- requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.generated with `pip freeze > requirements.txt` 
+-- setup.py.          <- Make this project with `python setup.py build_ext --inplace`
+-- notebooks.         <- Jupyter notebooks.
+-- weights.           <- Include models's weights.
+-- darkflow. 	       <- Write.
|   +-- dark. 	       <- Write.
|   +-- net.           <- Write.
+-- config.py.         <- Login and password for connecting to the RabbitMQ 
+-- yolo_webcam.py.    <- The main program
```

### Dependencies ###
The code is compatible with Python 3 or higher. 
The following dependencies are needed to run the tracker:

* Tensorflow :I have used CPU version
* OpenCV
* VC++ build 14
* torch >= 0.4
* torchvision >= 0.1
* pillow


### Installation ###
1. Clone this repository  
`git clone https://edvard88@bitbucket.org/vimpelsoft/objecttracking.git`

2. Recommend creating a virtual environment, because **there are dependencies** from **tensorflow version** (need the **1.13.4**). Later versions don't have module tensorflow.contrib    
	2.1 Install virtual environment  
	`sudo apt install -y python3-venv`  
	2.2 Creat virtual environment    
	`python -m venv env`  
	2.3 Activate virtual environment  
	`source env/bin/activate`

3. Check all dependencies installed  
`pip install -r requirements.txt`

4. Build the code.    
`python setup.py build_ext --inplace`


### Quick Start ###
`python yolo_webcam_2.py`

You should see


Load  |  Yep!  |             Input                | (Parameters       |
----- | ------ | -------------------------------- | ----------------- |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 19, 19, 512)  |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 19, 19, 512)  |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | concat [16]                      | (?, 38, 38, 512)  |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 38, 38, 64)   |
Load  |  Yep!  | local flatten 2x2                | (?, 19, 19, 256)  |
Load  |  Yep!  | concat [27, 24]                  | (?, 19, 19, 1280) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1    linear           | (?, 19, 19, 425)  |
Running entirely on CPU


You can also see the data that is sent to RabbitMQ:    
{'timestamp': 1584033256.291286, 'fps': '0.454108', 'label': 'person', 'confidence': '0.7981056', 'x_center': '647.5', 'y_center': '378.0'}  
{'timestamp': 1584033257.1981199, 'fps': '1.324479', 'label': 'person', 'confidence': '0.8224412', 'x_center': '646.0', 'y_center': '376.0'}  
{'timestamp': 1584033257.949561, 'fps': '1.434669', 'label': 'person', 'confidence': '0.8119112', 'x_center': '646.5', 'y_center': '374.5'}  
{'timestamp': 1584033258.722261, 'fps': '1.360957', 'label': 'person', 'confidence': '0.79016924', 'x_center': '647.0', 'y_center': '373.5'}  
{'timestamp': 1584033259.452522, 'fps': '1.416902', 'label': 'person', 'confidence': '0.8129106', 'x_center': '645.5', 'y_center': '379.0'}  

* timestamp - unix timestamp
* fps - frames per second
* label - object label (just a person for this release)
* x_center, y_center - center of the object, calculated as the point intersection of box's diagonals



### Contact ###
our@mail.com

===============================================================================================================================

### О проекте ###
Проект по распознованию (object detection) и сопровождению (tracking) пользователей в закрытых посещених с помощью камеры.

### Структура директории###
```bash
+-- README.md.         <- Основной README для разработчиков, использующие этот проект.
+-- requirements.txt   <- Фаил `requirements.txt` с используемые версиями библиотек для воспроизводимости программы.
+-- setup.py.          <- Соберите проект с помощью `python setup.py build_ext --inplace`
+-- notebooks.         <- Jupyter notebooks.
+-- weights.           <- Директория для весов моделей.
+-- darkflow. 	       <- Write.
|   +-- dark. 	       <- Write.
|   +-- net.           <- Write.
+-- config.py.         <- Параметры для подключения к RabbitMQ 
+-- yolo_webcam.py.    <- Основная программа
```

### Зависимости ###
Код копилируется на версии Python 3 и выше
Для запуска проекта необходимы следующие зависимости:

* Tensorflow :I have used CPU version
* OpenCV
* VC++ build 14
* torch >= 0.4
* torchvision >= 0.1
* pillow


### Установка ###
1. Скопируйте репозиторий 
`git clone https://edvard88@bitbucket.org/vimpelsoft/objecttracking.git`

2. Рекомендуем создать виртуальное окружение, потому что есть зависимости от **версии tensorflow** (нужна **1.13.4**). В более поздних версиях нет модуля tensorflow.contrib    
      
	2.1 Установка виртуального окружения    
	`sudo apt install -y python3-venv`  
	2.2 Создание виртуального окружения    
	`python -m venv env`.  
	2.3 Активируйте виртуальное окружение    
	`source env/bin/activate`
 

3. Проверьте установлены ли все необходимые зависимости.  
`pip install -r requirements.txt`


4. Запустите код  
`python setup.py build_ext --inplace`   

### Запуск программы  
`python yolo_webcam_2.py`

Вы должны увидеть:

Load  |  Yep!  |             Input                | (Parameters       |
----- | ------ | -------------------------------- | ----------------- |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 19, 19, 512)  |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 19, 19, 512)  |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | concat [16]                      | (?, 38, 38, 512)  |
Load  |  Yep!  | conv 1x1p0_1  +bnorm  leaky      | (?, 38, 38, 64)   |
Load  |  Yep!  | local flatten 2x2                | (?, 19, 19, 256)  |
Load  |  Yep!  | concat [27, 24]                  | (?, 19, 19, 1280) |
Load  |  Yep!  | conv 3x3p1_1  +bnorm  leaky      | (?, 19, 19, 1024) |
Load  |  Yep!  | conv 1x1p0_1    linear           | (?, 19, 19, 425)  |
Running entirely on CPU


Также будут видны данные, которые отправляются в RabbitMQ:    
{'timestamp': 1584033256.291286, 'fps': '0.454108', 'label': 'person', 'confidence': '0.7981056', 'x_center': '647.5', 'y_center': '378.0'}  
{'timestamp': 1584033257.1981199, 'fps': '1.324479', 'label': 'person', 'confidence': '0.8224412', 'x_center': '646.0', 'y_center': '376.0'}  
{'timestamp': 1584033257.949561, 'fps': '1.434669', 'label': 'person', 'confidence': '0.8119112', 'x_center': '646.5', 'y_center': '374.5'}  
{'timestamp': 1584033258.722261, 'fps': '1.360957', 'label': 'person', 'confidence': '0.79016924', 'x_center': '647.0', 'y_center': '373.5'}  
{'timestamp': 1584033259.452522, 'fps': '1.416902', 'label': 'person', 'confidence': '0.8129106', 'x_center': '645.5', 'y_center': '379.0'}  

* timestamp - время в формате Unix 
* fps - кадровая частота в секунду
* label - метка объекта (в текущей реализации только человек "person")
* x_center, y_center - центр объекта, высчитывается как точка пересечения дигоналей прямоугольника

### Контакты ###
our@mail.com

