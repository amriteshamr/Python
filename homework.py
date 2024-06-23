import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

months = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
sales = np.array([1.2, 1.8, 2.6, 3.2, 3.8])

model = LinearRegression()
model.fit(months, sales)

month_9 = np.array([[9]])
sales_9_pred = model.predict(month_9)

sales_pred = model.predict(months)

print(f"Sales Prediction for 9th Month : {round(sales_9_pred[0], 3)}")

SST = np.sum((sales - np.mean(sales))**2)
SSR = np.sum((sales_pred - np.mean(sales))**2)
SSE = np.sum((sales - sales_pred)**2)
R2 = SSR / SST

print(f"Total Sum of Squares (SST): {round(SST, 3)}")
print(f"Regression Sum of Squares (SSR): {round(SSR, 3)}")
print(f"Coefficient of Determination (R²): {round(R2, 3)}")