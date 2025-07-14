# set is unique
one = {"top","rop","gop"}
tow = {"close","open","top"}

all_number = one | tow

print(f"sab batao : {all_number}")

al_number = one & tow


print(f"common batao : {al_number}")


only_in_all = one - tow
print(f"only wala part : {only_in_all}")