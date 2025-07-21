def infinte_goo():
      count =1
      while True:
            yield f"Refil #{count}"
            count +=1

refill = infinte_goo()

for _ in range(85):
      print(next(refill))