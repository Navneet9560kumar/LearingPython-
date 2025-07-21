def local_chai():
      yield "Masala Chai"
      yield "Ginger chai"



def imported_chai():
      yield "Matcha"
      yield "Oolong"


def full_menu():
      yield from local_chai()
      yield from imported_chai()


for chai in full_menu():
      print(chai)


def chai_stall():
      try: 
            while True:
               order = yield "Wating for chai order"
      except:
            print("Stall clode,No more chai")


stall = chai_stall()
print(next(stall))
stall.close()  
                  