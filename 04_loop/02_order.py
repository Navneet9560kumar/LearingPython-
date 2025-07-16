# # order =["Navneet","Aman","aadi"]

# # for name in order:
# #       print(f"order ready for {name}")


# menu = ["maggi","lemon","Spiced","mint"]

# for idx, item in enumerate(menu, start=1):
#       print(f"{idx}: {item} chai")


name = ["Hitesh","Merra","Sam","Ail"]
bills= [50,70,100,55]

for name,amount in zip(name, bills):
      print(f"{name} paid {amount} rupees")