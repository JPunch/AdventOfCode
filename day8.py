'''Advent of code 2019 day8'''

import numpy as np

with open("inputday8.txt", "r") as f:
    f_read = f.read()
len(f_read)

def create_layer(input):
    layers = [input[x:x+150] for x in range(0, len(input), 150)]
    counts = [x.count("0") for x in layers]
    ans = layers[counts.index(min(counts))]
    return ans.count("1") * ans.count("2")

def create_image(input):
    image = [2] * 150
    layers = [input[ x : x + 150] for x in range(0, len(input), 150)]
    for i in range(150):
        for layer in layers:
            if layer[i] == "1":
                image[i] = 1
                break
            elif layer[i] == "0":
                image[i] = 0
                break
    image = [image[x : x + 25] for x in range(0, len(image), 25)]
    return np.matrix(image)
                

if __name__ == "__main__":
    # print(create_layer(f_read))
    print(create_image(f_read))