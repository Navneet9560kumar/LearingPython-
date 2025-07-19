favourite_chais = [
      "Masala Chai", "Green Tea", "Masala Chai",
      "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = { chai for chai in favourite_chais}



print(unique_chai)


recipes ={
      "Masal Chai" :["ginger","cardamon", "clove"],
      "Ealichi chai":["cardamon", "milk"],
      "Spicy Chai":["ginger","black pepper","clove"]

}

unique_chai = {ingredient for ingredients in recipes.values() for ingredient in ingredients}


print(unique_chai)