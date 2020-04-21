weight = input("Please enter your Weight: ")
weight_unit = input("(L)bs or (K)g: ")

if weight_unit.lower() == "l":
    print(f"You are {float(weight) / 0.45} kilos")
elif weight_unit.lower() == "k":
    print(f"You are {float(weight) * 0.45} pounds")
else:
    print("Please enter unit between L or K")
