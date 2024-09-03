from typing import Union
from fastapi import FastAPI
from fishmlserv.model.manager import get_model_path
from sklearn.neighbors import KNeighborsClassifier
import fire
import pickle
import os

app = FastAPI()

#def get_model_path():
 #   f = os.path.abspath(__file__)
  #  dir_name = os.path.dirname(f)
   # model_path = os.path.join(dir_name, "model.pkl")
    #return model_path

def fish(length: float, weight: float):
    """
    물고기의 길이(l)와 무게(w) 값을 기반으로 해당 물고기의 종류를 예측

    Args:
        l (float) : 물고기의 길이
        w (float) : 물고기의 무게

    Returns:
        str : 예측된 물고기의 종류("도미" or "빙어")를 반환

    how to use:
    1.
    2.
    3.

    """
    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    if prediction[0] == 1:
        return "도미"
    else:
        return "빙어"

#def main():
 #   fire.Fire(fish)

#if __name__ == "__main__":
 #   main()
