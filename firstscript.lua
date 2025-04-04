cash = 4000
print(os.date("%d/%m/%Y") .. ": Your balance is $" .. cash .. ".")
print("Go to work? (y/n)")
getinput = io.read()
if getinput == "y" then
    print("You went to work and earned $1000")
    cash = cash + 1000
else
    print("You stayed home and did nothing")
end
print("Your balance is now $" .. cash)
print("You go to sleep and wake up on the next day.The week feels monotonous.")
for i = 1, 5 do
    print("Day " .. i .. ": You're still at work and awaiting your biweekly payday.")
end
print("You get paid $2000.")
cash = cash + 2000
print("Your balance is now $" .. cash)
function travel()
    print("You decide to travel to a new city.")
    print("You spend $2000 on the trip.")
    cash = cash - 2000
    print("Your balance is now $" .. cash, ".")
end
print("You have a choice to make: do travel or invest? (t/i)")
getinput = io.read()
if getinput == "t" then
    travel()
elseif getinput == "i" then
    print("You decide to invest in stocks.")
    print("You spend $1000 on the investment.")
    cash = cash - 1000
    print("Your balance is now $" .. cash, ".")
else
    print("Invalid choice. Please choose 't' for travel or 'i' for invest.")
end