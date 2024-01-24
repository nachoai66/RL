#Cargamos el modelo que previamente hemos desplegado 
pickled_model = pickle.load(open('model.pkl', 'rb'))
#Date cuenta de que el modelo lo estas deserializando 
#Ahora puedes volver a invocar los métodos propios del modelo generado.
'''
  Ejemplos de métodos, son:
    - predict
    - ......
'''

pickled_model.predict(X_test)
