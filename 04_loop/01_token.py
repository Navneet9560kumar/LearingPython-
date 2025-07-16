# for token in range(1,11):
#       print(f"Serving the Token : #{token}")

for batch in range(1,5):
      print(f"Preparing chai for batch #{batch}")


def  multiplication_table(number):
      table=[]
      for i in range(1, 11):
            result = number * i
            table.append(f"{number} X {i} = {result}")
            return table