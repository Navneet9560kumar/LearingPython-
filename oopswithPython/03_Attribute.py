class go:
      temperature ="hot"
      strength ="Strong"


cutting = go()
print(cutting.temperature)

cutting.temperature = "Mild"
print("After changing", cutting.temperature)

del cutting.temperature
print(cutting.temperature)


# Attribute shadowing tab hoti hai jab child class (subclass) me ek attribute (variable) define kiya jata hai same name se jo already parent class (superclass) me exist karta hai.

# Yani child class ka attribute parent ke attribute ko "shadow" ya "hide" kar deta hai.

