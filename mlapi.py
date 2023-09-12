from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow import keras
import pandas as pd
import h5py

app = FastAPI()


# Model definition
class ScoreItem(BaseModel):
    Gender: int  # 1 - Man. 0 - Woman
    Age: int
    AnnualSalary: float
    CreditCardDebt: float
    NetWorth: float


file_model = h5py.File('./keras_car_prediction_trained_model.h5', mode='r')
model = keras.models.load_model(file_model)


@app.post('/')
async def card_purchase_prediction(item: ScoreItem):
    dollarSymbol = "$"
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    y_predict = model.predict(df)
    return {"Expected Purchase Amount": dollarSymbol + str(round(float(y_predict[:, 0]), 2))}
