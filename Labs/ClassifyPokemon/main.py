from matplotlib import colors
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def remove_clutter(data:str, x:list, y:list) -> None:
        temp_coor = []
        temp = ""

        for line in data:
            temp = line
            temp = temp.replace("(","")
            temp = temp.replace(")","")
            temp = temp.replace(",","")
            temp_coor = temp.split()
            x.append(float(temp_coor[0]))
            y.append(float(temp_coor[1]))

def plot_data(data:str,color:str):
    remove_clutter(data)
    plt.scatter


with open("Labs/ClassifyPokemon/files/pichu.txt", "r") as f_pichu, open("Labs/ClassifyPokemon/files/pikachu.txt", "r") as f_pikachu:

    pichu_data = f_pichu.readlines()
    pikachu_data = f_pikachu.readlines()
    pichu_data.pop(0)
    pikachu_data.pop(0)
    pikachu_x = []
    pikachu_y = []
    pichu_x = []
    pichu_y = []
    
    
    remove_clutter(pichu_data, pichu_x, pichu_y)
    remove_clutter(pikachu_data, pikachu_x, pikachu_y)

    plt.scatter(pichu_x, pichu_y, c="r" )
    plt.scatter(pikachu_x, pikachu_y, c="b")
    plt.show()
    plt.legend()
