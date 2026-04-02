
with open("jedzenie.txt", "a") as file:
    file.write(input("Jakie jest Twoje ulubione danie?\n") + "\n")

with open("jedzenie.txt", "r") as file:
    zawartosc = file.read()
    print("Twoje ulubione dania to:")
    print(zawartosc)