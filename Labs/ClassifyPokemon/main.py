import matplotlib.pyplot as plt
with open("ClassifyPokemon/files/pichu.txt", "r") as f_pichu, open("ClassifyPokemon/files/pikachu.txt", "r") as f_pikachu:

    pichu_data = f_pichu.readlines()
    pikachu_data = f_pikachu.readlines()
    pichu_data.pop(0)
    pikachu_data.pop(0)
    plt.show()

