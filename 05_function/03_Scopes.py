def server_chai():
      chai_type = "meri "
      print(f"Inside function {chai_type}")

chai_type = "Lemon"
server_chai()
print(f"outside function: {chai_type}")



def chai_counter():
      chai_order = "Lemon"

      def print_order():
            chai_order = "Ginger"
            print("Inner", chai_order)
      print_order()
 