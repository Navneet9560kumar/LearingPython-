def pure_chai(cups):
    return cups * 10  

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups 

def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)  

print(pour_chai(3))



chai_type  =["Light","tofu","fofo","kadak"]

strong_chai = list(filter(lambda chai:chai=="tofu", chai_type))

print(strong_chai)