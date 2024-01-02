from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Load the pre-trained model
loaded_data = pickle.load(open("content/gld_data.pkl", "rb"))


class Item(BaseModel):
    SPX: float
    USO: float
    SLV: float
    EUR_USD: float


@app.post("/predict", response_model=dict)
def predict(item: Item):
    try:
        features = np.array([item.SPX, item.USO, item.SLV, item.EUR_USD]).reshape(1, -1)
        prediction = loaded_data.predict(features)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
