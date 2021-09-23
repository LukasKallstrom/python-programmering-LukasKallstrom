from matplotlib import colors
import matplotlib.pyplot as plt
import math

def remove_clutter(data:str, x_list:list, y_list:list) -> None:
        temp_coor = []
        temp = ""

        for line in data:
            temp = line
            temp = temp.replace("(","")
            temp = temp.replace(")","")
            temp = temp.replace(",","")
            temp_coor = temp.split()
            x_list.append(float(temp_coor[0]))
            y_list.append(float(temp_coor[1]))

def plot_data(data:str, color:str):
    remove_clutter(data)
    plt.scatter


with open("Labs/ClassifyPokemon/files/pichu.txt", "r") as f_pichu, open("Labs/ClassifyPokemon/files/pikachu.txt", "r") as f_pikachu, open("Labs/ClassifyPokemon/files/test_points.txt", "r") as f_testpoints:

    pichu_data = f_pichu.readlines()
    pikachu_data = f_pikachu.readlines()
    test_points = f_testpoints.readlines()
    pichu_data.pop(0)
    pikachu_data.pop(0)
    pikachu_x = []
    pikachu_y = []
    pichu_x = []
    pichu_y = []
    test_points_x = []
    test_points_y = []
    
    
    remove_clutter(pichu_data, pichu_x, pichu_y)
    remove_clutter(pikachu_data, pikachu_x, pikachu_y)
    remove_clutter(test_points, test_points_x, test_points_y)

    plt.scatter(pichu_x, pichu_y, c="r" )
    plt.scatter(pikachu_x, pikachu_y, c="b")
    #plt.show()
    #plt.legend()

    point = (25, 35)
    
    avrg_pichu = 0
    avrg_pikachu = 0
    
    distances_pichu = []
    distances_pikachu = []
    
    for i in range(50):
        distances_pichu.append(math.sqrt((pichu_x[i] - point[0])**2 + (pichu_y[i] - point[1])**2))
    for i in range(50):
        distances_pikachu.append(math.sqrt((pikachu_x[i] - point[0])**2 + (pikachu_y[i] - point[1])**2))
    distances_pichu.sort()
    distances_pikachu.sort()

    avrg_pichu = sum(distances_pichu[0:5]) / len(distances_pichu[0:5])
    avrg_pikachu = sum(distances_pikachu[0:5]) / len(distances_pikachu[0:5])

    print(f"Pichu shortest distances: {distances_pichu[0:5]}")
    print(f"Pikachu shortest distances: {distances_pikachu[0:5]}")
    print(f"Pichu avarage: {avrg_pichu}")
    print(f"Pikachu avarage: {avrg_pikachu}")

    if avrg_pichu < avrg_pikachu:
        print(f"Data point belongs to Pichu")
    else:
        print(f"Data point belongs to Pikachu")


    