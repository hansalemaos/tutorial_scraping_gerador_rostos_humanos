import os
import random
import time

import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv
import requests

gender = ["male", "female"]
age = ["12-18", "19-25", "26-35", "35-50", "50"]
etni = ["asian", "black", "white", "indian", "middle_eastern", "latino_hispanic"]

while True:
    try:
        t = int(time.time())
        g1 = random.choice(gender)
        a1 = random.choice(age)
        e1 = random.choice(etni)
        params = {"time": t, "gender": g1, "age": a1, "etnic": e1}
        pasta_para_salvar = "c:\\rostosquenaoexistem"
        pasta_para_rosto = os.path.join(pasta_para_salvar, f"{g1}_{a1}_{e1}")
        os.makedirs(pasta_para_rosto, exist_ok=True)
        with requests.get(
            "https://this-person-does-not-exist.com/new", params=params
        ) as q:
            if q.status_code == 200:
                print(q.json())
                with requests.get(
                    "https://this-person-does-not-exist.com" + q.json()["src"]
                ) as bi:
                    nome_arquivo = os.path.join(pasta_para_rosto, q.json()["name"])

                    img = open_image_in_cv(bi.content)
                    img = img[65 : 1024 - 65, 65 : 1024 - 65]
                    cv2.imwrite(nome_arquivo, img)
    except Exception as fe:
        print(fe)
        continue
    time.sleep(1)
