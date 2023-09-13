def cakes(recipe, available):
    return min([int(available[ingredient]/recipe[ingredient]) if ingredient in available else 0 for ingredient in recipe])