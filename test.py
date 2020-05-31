import os
from os.path import join


def read_and_transform(filename):
    cook_book = {}
    recipe = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                # print(recipe)
                cook_book[recipe[0]] = recipe[1:]
                recipe.clear()
            else:
                recipe.append(line)
        print(cook_book)

    for ingredients in cook_book.values():
        ingredients.pop(0)
        for ingredient in ingredients:
            print(ingredient)


read_and_transform()