def goo_customure():
      print("Wellcome waht tpye of thing u like ")
      order = yield
      while True:
            print(f"preparing: {order}")
            order = yield

stall = goo_customure()
next(stall);

stall.send("Masal bro")
stall.send("tera bro")