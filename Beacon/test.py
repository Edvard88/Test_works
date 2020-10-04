import pandas as pd
import numpy as np
from datetime import timedelta
import torch

def load_data():
    beacons = pd.read_csv('beacons.csv', sep=';')
    for col in ['X', 'Y', 'Z']:
        beacons[col] = beacons[col].apply(lambda x: x.replace(',', '.')).astype(float)
    points = pd.read_csv('test data.csv', sep=',')
    points['Time'] = pd.to_datetime(points['Time.$date.$numberLong'], unit='ms')
    return beacons, points

def create_dataset(beacons, points, gateway):
    x = points[points.GatewayId.values == gateway]
    times = x.Time.unique()
    X = np.zeros((len(times), len(beacons), 3))
    w = np.zeros((len(times), len(beacons)))
    y = np.zeros((len(times), len(beacons)))
    beacons_dict = {mac.lower(): id for id, mac in enumerate(beacons.Mac)}
    for i, time in enumerate(times):
        subset = x[x.Time == time]
        assert len(subset.BeaconId.unique()) == len(subset.BeaconId)
        for j, mac in enumerate(subset.BeaconId):
            if not mac.lower() in beacons_dict.keys():
                continue
            beacon_id = beacons_dict[mac.lower()]
            X[i, beacon_id, 0] = beacons.X[beacon_id]
            X[i, beacon_id, 1] = beacons.Y[beacon_id]
            X[i, beacon_id, 2] = beacons.Z[beacon_id]
            rssi = subset['Rssi.$numberInt'].values[j]
            d = 10**((-69 - rssi) / (10*2))
            y[i, beacon_id] = d**2
            w[i, beacon_id] = 1./d
    return X, y, w, times

def optimize_positions(X, y, w, n_epochs = 2000):
    X = torch.from_numpy(X).float()
    y = torch.from_numpy(y).float()
    w = torch.from_numpy(w).float()
    #x = torch.nn.Parameter(torch.zeros(len(X), 3))
    x = torch.nn.Parameter(torch.randn(len(X), 3)*20)
    
    optimizer = torch.optim.Adam([x], lr=1e-1)
    
    losses = np.zeros(n_epochs)
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        d = (x.unsqueeze(1) - X).pow(2).sum(2)#.sqrt()
        loss = (w * (d-y)).mean()
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print('Epoch: {} loss: {:.4f}'.format(epoch, loss.item()))
        losses[epoch] = loss.item()
    
    return x.detach().numpy()

def save(name, pos, time):
    df = pd.DataFrame({'Time': time, 'X': pos[:, 0], 
                       'Y': pos[:, 1], 'Z': pos[:, 2]})
    df.to_csv(name, index=False)

beacons, points = load_data()
gateways = points.GatewayId.unique().tolist()

for gateway in gateways:
    X, y, w, time = create_dataset(beacons, points, gateway)
    pos = optimize_positions(X, y, w, n_epochs = 2000)
    save('{}.csv'.format(gateway), pos, time)
    
