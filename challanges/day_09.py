import time
while True:

      try:
            Second = int (input("⏲️Enter a time in seconds: "))
            if Second <1:
                  print("Please enter a positive number greater than 0.")
                  continue
            break
      except ValueError:
            print("Invalid input, please enter a number.")
print(" \n⏲️ Timer Started... ")
for remaining in range(Second, 0, -1):
      mins, secs = divmod(remaining, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")
      time.sleep(1)


print("\n⏲️ Time up! Take a break or move on to next task. ")