def too_go():
      yield "cup1 : mera bro "
      yield "cup2 : tera bro "
      yield "cup3 : sabak bro "

stall = too_go()

# for cup in stall:
#       print(cup)


def get_too_go_list():
      return["cup 1","cup 2", "cup 3"]

#generator function

def get():
      yield "Cup 1"
      yield "Cup 2"
      yield "Cup 3"

chai =get()
print (next(chai))