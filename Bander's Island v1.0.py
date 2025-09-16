strangeness = 0 #reset vars (later check if some vars are redundant)
sticks = 0
stones = 0
shelter = 0
shelterval = 0
water = 5
food = 5
day = 0
time = 0
tools = 0
toolval = 0
fire = 0
hurt = 0
hard = 0
ruinedthefun = 0
gameend = 0
sjused = 0
foodgather = 0
hurtcheck = 0
sheltercheck = 0
trueend = 0
firecheck = 0
ans = ''
import random
import time as clock
ans = input('Activate strangeness? Y/N ')  #diff and strangeness
if ans in ['Y', 'y']:
    print("You have activated strangeness. This may or may not have an effect.")
    strangeness = 1
ans = input('"Would you like to play on normal or hard mode? N/H ')
if ans in ['H', 'h']:
    print("You have activated hard mode. Healing wounds is disabled.")
    hard = 1
def ask(): #Ask for next command
    global ans
    global water
    global food
    if water <= 0 and food <= 0:
        print('You died of starvation and thirst. Try harder next time.')
    elif water <= 0:
        print('You died of thirst. Try harder next time.')
    elif food <= 0:
        print('You died of starvation. Try harder next time.')
    else:
        ans = input("Type a command: ")
        if ans in ["gather", "Gather", "G", "g"]:
            gather()
        elif ans in ["inventory", "Inventory", "I", "i"]:
            inventory()
        elif ans in ["sleep", "Sleep", "S", "s"]:
            sleep()
        elif ans in ["Hunt", "hunt", "HT", "ht"]:
            hunt()
        elif ans in ['Body Check', 'body check', 'BC', 'bc']:
            bodycheck()
        elif ans in ['Craft Tools', 'craft tools', 'CT', 'ct']:
            crafttools()
        elif ans in ['Build Shelter', 'build shelter', 'BS', 'bs']:
            buildshelter()
        elif ans in ['Build Raft', 'build raft', 'BR', 'br']:
            buildraft()
        elif ans in ['Build Campfire', 'build campfire', 'BCF', 'bcf']:
            buildcampfire()
        elif ans in ['Add to Campfire', 'add to campfire', 'ATC', 'atc']:
            addtocampfire()
        elif ans in ['Heal', 'heal', 'H', 'h']:
            heal()
        elif ans in ['Ruin the Fun', 'ruin the fun', 'RTF', 'rtf']:
            ruinthefun()
        elif ans in ['Search Junk', 'search junk', 'SJ', 'sj']:
            searchjunk()
        elif ans in ['Reinforce Shelter', 'reinforce shelter', 'RS', 'rs']:
            reinforceshelter()
        else:
            print("Invalid command.")
            ask()
def gather(): #Gather command
    global time
    global hurt
    global stones
    global sticks
    global water
    global tools
    global toolval
    if time < 4:
        time += 1
        if tools == 1:
            stonegather = random.randint(2, 5)
            stickgather = random.randint(2, 5)
            watergather = random.randint(2, 5)
        else:
            stonegather = random.randint(1, 4)
            stickgather = random.randint(1, 4)
            watergather = random.randint(0, 2)
        hurtcheck = random.randint(1, 5)
        if hurtcheck == 5:
            hurt += random.randint(1, 2)
        if hurt > 0:
            stickgather -= 1
            stonegather -= 1
            watergather -= 1
        if watergather < 0:
            watergather = 0
        stones += stonegather
        sticks += stickgather
        water += watergather
        if toolval == 0 and tools == 1 and hurtcheck == 5:
            print("You gathered", stickgather, "sticks,", stonegather, "stones and", watergather, "water. Your tools broke and you hurt yourself.")
            tools = 0
        elif toolval == 0 and tools == 1:
            print("You gathered", stickgather, "sticks,", stonegather, "stones and", watergather, "water. Your tools broke.")
            tools = 0
        elif hurtcheck == 5:
            print("You gathered", stickgather, "sticks,", stonegather, "stones and", watergather, "water. You hurt yourself.")
        else:
            print("You gathered", stickgather, "sticks,", stonegather, "stones and", watergather, "water.")
        ask()
    else:
        print("You are tired, you must sleep.")
        ask()
def inventory(): #Inventory command
    global shelter
    global tools
    global toolval
    global fire
    global sticks
    global stones
    global shelterval
    if shelter == 1 and tools == 1:
        print("You have", sticks, "sticks and", stones, "stones. You have a shelter and tools.")
    elif shelter == 1:
        print("You have", sticks, "sticks and", stones, "stones. You have a shelter.")
    elif tools == 1:
        print("You have", sticks, "sticks and", stones, "stones. You have tools.")
    else:
        print("You have", sticks, "sticks and", stones, "stones.")
    if fire > 0:
        print("Campfire value is", str(fire) + ".")
    if tools > 0:
        print("You have", toolval, "uses on your tools.")
    if shelter > 0:
        print("Your shelter is guaranteed to be safe for", shelterval, "days.")
    ask()
def sleep(): #Sleep command
    global time
    global day
    global water
    global food
    global shelter
    global shelterval
    global fire
    global hard
    global hurt
    global sjused
    if fire > 0 and shelter == 1:
        shelterlost = 0
        foodlost = 0
        waterlost = 0
        if shelterval > 0:
            shelterval -= 1
        else:
            shelterlost = random.randint(1, 10)
        fire -= 1
        time = 0
        day += 1
        if hard == 0:
            if hurt > 0:
                hurt -= 1
        if shelterlost > 10:
            print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", day, ". Your shelter was destroyed in a storm.")
            shelter = 0
            sjused = 0
            ask()
        else:
            print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", str(day) + ".")
            sjused = 0
            ask()
    elif fire > 0:
        fire -= 1
        foodlost = random.randint(0, -1)
        waterlost = random.randint(0, -1)
        if hurt == 1:
            foodlost -= 1
            waterlost -= 1
        food += foodlost
        water += waterlost
        time = 0
        day += 1
        if hard == 0:
            if hurt > 0:
                hurt -= 1
        print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", str(day) + ".")
        sjused = 0
        ask()
    elif shelter == 1:
        foodlost = random.randint(0, -1)
        waterlost = random.randint(0, -1)
        if shelterval > 0:
            shelterval -= 1
        else:
            shelterlost = random.randint(1, 10)
        if hurt == 1:
            foodlost -= 1
            waterlost -= 1
        food += foodlost
        water += waterlost
        time = 0
        day += 1
        if hard == 0:
            if hurt > 0:
                hurt -= 1
        if shelterlost > 10:
            print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", str(day) + ". Your shelter was destroyed in a storm.")
            shelter = 0
            sjused = 0
            ask()
        else:
            print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", str(day) + ".")
            sjused = 0
            ask()
    else:
        foodlost = random.randint(-2, -1)
        waterlost = random.randint(-2, -1)
        if hard == 0:
            if hurt > 0:
                hurt -= 1
        food += foodlost
        water += waterlost
        time = 0
        day += 1
        print("You lost", abs(foodlost), "food and", abs(waterlost), "water. Today is day", str(day) + ".")
        sjused = 0
        ask()
def hunt(): #Hunt command
    global food
    global water
    global time
    global hurt
    global tools
    global toolval
    global hurtcheck
    global foodgather
    if time < 4:
        time += 1
        hurtcheck = random.randint(1,4)
        if tools == 1:
            foodgather = random.randint(1,3)
            toolval -= 1
        else:
            foodgather = random.randint(1,2)
        if hurtcheck == 4:
            hurt += random.randint(1,2)
        if hurt > 0:
            foodgather -= 1
        if foodgather < 0:
            foodgather = 0
        food += foodgather
        if hurtcheck == 4 and toolval == 0 and tools == 1:
            print('You gained', foodgather ,'food, your tools broke and you got hurt.')
            tools = 0
            ask()
        elif toolval == 0 and tools == 1:
            print('You gained', foodgather, 'food, your tools broke.')
            tools = 0
            ask()
        elif hurtcheck == 4:
            print('You gained', foodgather, 'food, you got hurt.')
            ask()
        else:
            print('You gained', foodgather, 'food.')
            ask()
    else:
        print('You are tired, you must sleep.')
        ask()
def bodycheck(): #Body Check command
    global food
    global water
    global hurt
    global time
    if hurt > 0:
        print('You have', food, 'food and', water,  'water, and you have', hurt, 'wounds. You have used', time, 'out of 4 actions today.')
        ask()
    else:
        print('You have', food, 'food and', water, 'water. You have used', time, 'out of 4 actions today.')
        ask()
def crafttools(): #Craft Tools command
    global time
    global sticks
    global stones
    global toolval
    global tools
    if time < 4:
        if sticks > 3 and stones > 3:
            time += 1
            stones -= 4
            sticks -= 4
            toolval += random.randint(10,15)
            tools = 1
            print('You built tools. You have gained', toolval, 'uses for your tools.')
            ask()
        else:
            print('Insufficient resources.')
            ask()
    else:
        print('You are tired, you need sleep.')
        ask()
def buildshelter(): #Build Shelter command (fix re-building shelter)
    global time
    global sticks
    global stones
    global shelter
    global sheltercheck
    if time < 4:
        if sticks > 6 and stones > 6:
            sticks -= 7
            stones -= 7
            sheltercheck = random.randint(1,5)
            if not sheltercheck == 5:
                shelter = 1
                time += 1
                print('You built a shelter.')
                ask()
            else:
                print('The shelter you built caved in. You have lost 7 sticks and 7 stones.')
                ask()
        else:
            print('Insufficient resources.')
            ask()
    else:
        print('You are tired, you need sleep.')
        ask()
def buildraft(): #Build Raft command
    global sticks
    global stones
    global food
    global water
    global tools
    global time
    global strangeness
    global trueend
    global ruinedthefun
    global gameend
    global day
    global hard
    if sticks >= 30 and stones >= 30 and food >= 10 and tools == 1 and water >= 10:
        if time < 1:
            sticks -= 30
            stones -= 30
            time += 4
            water -= 10
            food -= 10
            if ruinedthefun == 0 and strangeness == 1 and hard == 1:
                print('You survived in', day, 'days but something doesn\'t feel right, like a part of you that you had in the beginning is misssing.')
                gameend = 1
                clock.sleep(4)
                print('Why do you feel this way? You wonder why for the rest of your life.')
                clock.sleep(4)
                print('You wash up on an island inhabited by Americans and they take you in. You live a good life.')
                clock.sleep(4)
                trueend = 1
                print('You have achieved the true ending. Great work.')
            else:
                print('You survived in', day, 'days.')
                gameend = 1
        else:
            print('It needs to be a new day for you to build a raft.')
            ask()
    else:
        print('Insufficient resources.')
        ask()
def buildcampfire(): #Build campfire command (make this cost an action perhaps, unsure though)
    global fire
    global sticks
    global firecheck
    if fire == 0:
        if sticks > 3:
            sticks -= 4
            firecheck = random.randint(1,3)
            if not firecheck == 3:
                fire = 1
                print('You built a campfire.')
                ask()
            else:
                print('You couldn\'t start the fire. You have lost 4 sticks.')
                ask()
        else:
            print('Insufficient resources.')
            ask()
    else:
        print('You already have a campfire.')
        ask()
def addtocampfire(): #Add to Campfire command
    global sticks
    global fire
    if fire > 0:
        if sticks > 1:
            sticks -= 2
            fire += 1
            print('Campfire value is now',  str(fire) + '.')
            ask()
        else:
            print('Insufficient resources.')
            ask()
    else:
        print('You don\'t have a campfire.')
        ask()
def heal(): #Heal command
    global hard
    global hurt
    global water
    if hard == 0:
        if hurt > 0:
            if water > 1:
                hurt = 0
                water -= 2
                print('You heal your wounds.')
                ask()
            else:
                print('Insufficient resources.')
                ask()
        else:
            print('You don\'t have any wounds.')
            ask()
    else:
        print('You can\'t heal in hard mode, your wounds are permanent.')
        ask()
def ruinthefun(): #Ruin the Fun command
    global fire
    global day
    global shelter
    global sticks
    global stones
    global water
    global food
    global tools
    global toolval
    global shelterval
    global ruinedthefun
    fire = 99999
    day = 0
    shelter = 1
    sticks = 999
    stones = 999
    water = 999
    food = 999
    tools = 1
    toolval = 9999
    shelterval = 99999
    ruinedthefun = 1
    print('But why though?')
    ask()
def searchjunk(): #Search Junk command (make this consume a tool use)
    global time
    global sjused
    global stones
    global sticks
    global water
    global food
    global hurt
    global tools
    global toolval 
    if time < 4:
        if sjused == 0:
            time += 1
            if tools == 1:
                stonegather = random.randint(1,5)
                stickgather = random.randint(1,5)
                watergather = random.randint(2,4)
                foodgather = random.randint(1,3)
            else:
                stonegather = random.randint(0,4)
                stickgather = random.randint(0,4)
                watergather = random.randint(0,3)
                foodgather = random.randint(0,2)
            hurtcheck = random.randint(1,5)
            if hurtcheck == 5:
                hurt += random.randint(1,2)
            if hurt > 0:
                stickgather -= random.randint(1,2)
                stonegather -= random.randint(1,2)
                watergather -= random.randint(0,2)
                foodgather -= random.randint(0,2)
            if stickgather < 0:
                stickgather = 0
            if stonegather < 0:
                stonegather = 0
            if watergather < 0:
                watergather = 0
            if foodgather < 0:
                foodgather = 0
            stones += stonegather
            sticks += stickgather
            water += watergather
            food += foodgather
            if toolval == 0 and tools == 1 and hurtcheck == 5:
                print('You found', stickgather,  'sticks,', stonegather, 'stones,', watergather, 'water and', foodgather, 'food in the ocean, your tools broke and you hurt yourself.')
                tools = 0
            elif toolval == 0 and tools == 1:
                print('You found', stickgather, 'sticks,', stonegather, 'stones,', watergather, 'water and', foodgather, 'food in the ocean, your tools broke.')
                tools = 0
            elif hurtcheck == 5:
                print('You found', stickgather, 'sticks,', stonegather, 'stones,', watergather, 'water and', foodgather, 'food in the ocean, you hurt yourself.')
            else:
                print('You found', stickgather, 'sticks,', stonegather, 'stones,', watergather, 'water and', foodgather, 'food in the ocean.')
            sjused == 1
            ask()
        else:
            print('There is no more junk in the ocean.')
            ask()
    else:
        print('You are tired, you must sleep.')
        ask()
def reinforceshelter(): #Reinforce Shelter command
    global time
    global shelter
    global stones
    global shelterval
    time += 1
    if shelter == 1:
        if stones > 3:
            stones -= 4
            shelterval += 1
            print('Your shelter will now be protected for', shelterval, 'days.')
            ask()
        else:
            print('Insufficient resources.')
            ask()
    else:
        print('You don\'t have a shelter.')
        ask()
print('You are stranded on a deserted island. What will you do?')
ask()