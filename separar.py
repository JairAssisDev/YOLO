import os
import shutil
from os import listdir
from sklearn.model_selection import train_test_split


diretorios = os.listdir("dataset/train")

if os.path.exists("dataset/train/val"):
    print(diretorios)
    diretorios.remove(diretorios[diretorios.index("val")])
    print(diretorios)

for i in diretorios:
    total_img = os.listdir("dataset/train/"+i)
    if os.path.exists("dataset/val") == False:
        os.mkdir("dataset/val")
    #print(f"{len(total_img)} de {i}")
    if os.path.exists("dataset/val/"+i)==False:
        os.mkdir("dataset/val/"+i)

for i in diretorios:
    mover_para = "dataset/val/" + i
    total_img = os.listdir("dataset/train/"+i)
    #print(f"{len(total_img)} de {i}")
    if os.listdir(mover_para) == []:
        train, test = train_test_split(total_img, test_size=0.2, random_state=42)
    else:
        print("diretorios já nâo esta vazio")
        continue
    for j in test:
        if os.path.exists(f"dataset/val/{i}/{j}") == False:
            shutil.move(f"dataset/train/{i}/{j}",mover_para)
        else:
            print("imagem já esta no conjunto de val")


