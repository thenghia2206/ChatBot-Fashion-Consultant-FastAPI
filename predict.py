from tensorflow import keras
import pandas as pd
import numpy as np

def predict(wid,age,hei):
    model = keras.models.load_model('model_cnn')
    data = [[ wid , age , hei]]
    model_predict = model.predict(data)
    max = np.argmax(model_predict,axis=1)
    x = max
    if x == 0:
        return "XS"
    elif x==1:
        return "S"
    elif x ==2:
        return "M"
    elif x == 3:
        return "L"
    elif x ==4:
        return "XL"
    elif x ==5:
        return "XXL"