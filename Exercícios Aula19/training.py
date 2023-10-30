import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

data = pd.read_csv('C:\Programação\Python\Faculdade\Exercícios Aula19\housing.csv')
data = data.dropna()

X = data.iloc[ : , 0:8].values
y = data.iloc[ : , 8:9].values

# model = LinearRegression()
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'model.joblib')

y_pred = model.predict(X)

for i in range(10):
    print(y[i] , ' => ', y_pred[i])

r2 = r2_score(y, y_pred)
print(f'Coeficiente de Determinação: {r2}')