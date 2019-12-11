#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  _cache = {}
  batches = None

  if len(recipe.items()) != len(ingredients.items()):
    return 0

  for k, v in ingredients.items():
    _cache[k] = math.floor(v / recipe[k])

  for _k, _v in _cache.items():
    if batches == None:
      batches = _v
    elif _v < batches:
      batches = _v

  return batches
      
print(recipe_batches({ 'milk': 2 }, { 'milk': 200}))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))