astv_type = ["family", "cooperate", "global"]

family_subtype = ["simplex", "duplex"]
family_price = [[1600, 15], [2400, 27]]

cooperate_subtype = ["complex", "superlative"]
cooperate_price = [[3500, 35], [4700, 43]]

global_subtype = ["mini", "maxi"]
global_price = [[7800, 89], [9400, 130]]


def username(name):
    return "Hi " + name + ", " + "Welcome to ASTV! \n\n\n"


print(username(input("Enter your name: ").capitalize()))

for item in astv_type:
    print(item.capitalize())

def select_astv(type):
    subtype = ""
    print("\nYou have selected " + type)
    if type == "family":
        for item in family_subtype:
            print(item.capitalize())
        subtype = input("\nEnter plan: ")
        if subtype == "simplex":
            return f"Price is: {family_price[0][0]}\nChannels: {family_price[0][1]}"
        else:
            return f"Price is: {family_price[1][0]}\nChannels: {family_price[1][1]}"
    elif type == "cooperate":
        for item in cooperate_subtype:
            print(item)
        subtype = input("\nEnter plan: ")
        if subtype == "complex":
            return f"Price is: {cooperate_price[0][0]}\nChannels: {cooperate_price[0][1]}"
        else:
            return f"Price is: {cooperate_price[1][0]}\nChannels:  {cooperate_price[1][1]}"
    else:
        subtype = input(global_subtype).capitalize()
        if subtype == "mini":
            return f"Price is: {global_price[0][0]}\nChannels: {global_price[0][1]}"
        else:
            return f"Price is: {global_price[1][0]}\nChannels: {global_price[1][1]}"


print(select_astv(input("\nEnter a package: ")))