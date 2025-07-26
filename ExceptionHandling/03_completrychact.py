def server_go(flavor):
      try:
            print(f"Prepaing{flavor} chai....")
            if(flavor == "unknow"):
                  raise ValueError("We dont know that flour")
      except ValueError as e:
            print("error",e)
      else:
            print(f"{flavor} chai is served")
      finally:
            print("Next customer please")



server_go("masala")
server_go("unkown")