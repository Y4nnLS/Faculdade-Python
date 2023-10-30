import joblib

model = joblib.load('C:\Programação\Python\Faculdade\Exercícios Aula19\model.joblib')

y_pred = model.predict([[-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252]])
print(y_pred)