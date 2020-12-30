K = ''
weight = int(input("what is your weight? "))
unit = input("(k)g or (l)bs? ")

if unit.upper() == K:
    new_weight = weight/0.45
    print(f"weight is {new_weight} pounds")
else:
    new_weight = weight * 0.45
    print(f"weight is {new_weight} kilos")
