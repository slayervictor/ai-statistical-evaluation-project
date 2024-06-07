from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleLinearRegression:
    def __init__(self, x, y):
        self.model = LinearRegression()
        self.X = x.values.reshape(-1, 1)
        self.y = y

    def fit(self):
        self.model.fit(self.X, self.y)

    def predict(self):
        return self.model.predict(self.X)

    def outlier_detection(self, threshold=2):
        residuals = self.y - self.model.predict(self.X)
        outliers = np.abs(residuals) > threshold * np.std(residuals)
        print('Number of outliers:', np.sum(outliers))
        print(f'At threshold {threshold}')

# Define the linear model
class LinearModel(nn.Module):
    def __init__(self, input_size):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return self.linear(x)
