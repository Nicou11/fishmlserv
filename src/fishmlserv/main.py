from typing import Union
from fastapi import FastAPI
from src.fishmlserv.model.manager import get_model_path
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기 종류 판별기
    ```
    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)
    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    From fish model
    ```
    """
    ### 모델 불러오기
    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])
    
    #if kn.predict([[30, 600]])[0] == 1:
     #   print('도미')
    #else:
     #   print('빙어')
    #prediction = fish_model.predict([[length, weight]])

    #fish_class = "몰라"
    if prediction[0] == 1:
        fish_class = "도미"
    else:
      fish_class = "빙어"

    return {
                "생선": fish_class,
            }

@app.get("/model_path")
def fish2(length: float, weight: float):
    with open(model, "rb") as p:
        fish_model = pickle.load(p)
    prediction = fish_model.predict([[length, weight]])

    if prediction[0] == 1:
        fish_class = "도미"
    else:
       fish_class = "빙어"
