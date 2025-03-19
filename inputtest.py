num1 = float(input("Pick the first number. "))
num2 = float(input("Pick the second number. "))
op = str(input("Choose an operator. (plus, minus, times, divide, modulus, exponent) "))
if op == "plus":
    print(num1 + num2)
elif op == "minus":
    print(num1 - num2)
elif op == "times":
    print(num1 * num2)
elif op == "divide":
    print(num1 / num2)
elif op == "modulus":
    print(num1 % num2)
elif op == "exponent":
    print(num1 ** num2)
else:
    print("Invalid answer.")
prem2223 = ["Man City", "Arsenal", "Man United", "Newcastle", "Newcastle", "Brighton", "Villa", "Spurs", "Brentford", "Fulham", "Palace", "Chelsea", "Wolves", "West Ham", "Bournemouth", "Forest", "Everton", "Leicester", "Leeds", "Southampton"]
place = int(input("Which place in the 2022-23 Premier League would you like to know? "))
if place > 0 and place < 21:
    print(prem2223[place-1])
else:
    print("Invalid answer.")
buyshield = input("Would you like to buy a shield for 50 gold?\n1. Buy it\n2. Dont buy it ")
if buyshield == "1":
    print("You have bought the shield for 50 gold.")
elif buyshield == "2":
    print("You decide not to buy the shield.")
else:
    print("Invalid answer.")
prem2324 = ["Man City", "Arsenal", "Liverpool", "Villa", "Spurs", "Chelsea", "Newcastle", "Man United", "West Ham", "Palace", "Brighton", "Bournemouth", "Fulham", "Wolves", "Everton", "Brentford", "Forest", "Luton", "Burnley", "Sheffield"]
place = int(input("Which place in the 2023-24 Premier League would you like to know? "))
if place > 0 and place < 21:
    print(prem2324[place-1])
else:
    print("Invalid answer.")