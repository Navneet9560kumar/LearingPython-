class Chaicup:
      size = 150

      def descrile(self):
            return f"A {self.size}ml chai cup"
      

cup= Chaicup()
print(cup.descrile())
print(Chaicup.descrile())

cup_two = Chaicup()
print(cup_two.descrile())  
print(Chaicup.descrile(cup))

cup_two = Chaicup()
cup_two.size =100
print(Chaicup.descrile(cup_two))