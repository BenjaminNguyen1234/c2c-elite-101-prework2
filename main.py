import random

userage = 2
userbirthday = ""
endless = True
posstopics = ["Weather", "Age", "Family", "Misc", "End"]
print(posstopics)
response = ""
favgame = ""
favsports = ""
favcolor = ""
favshow = ""

weather_responses = [
    "Hows the weather?", "It's pretty nice outside",
    "Tell me how it is out there"
]
neg_res = ["Bad", "Terrible", "Horrible", "Awful"]
good_res = ["Great", "Good", "Nice", "Amazing", "Terrific", "Awesome"]


def weatherfunc():

    if random.choice(weather_responses) == weather_responses[0]:
        response = input(weather_responses[0])
        if response.capitalize() in good_res:
            print("Awesome")
        else:
            print("Aww, too bad")
    elif random.choice(weather_responses) == weather_responses[1]:
        response = input(weather_responses[1] + " ")
        print(
            "Is it really? I couldn't tell, I'm just a program inside your browser."
        )
    elif random.choice(weather_responses) == weather_responses[2]:
        response = input(weather_responses[2] + " ")
        if response.capitalize() in good_res:
            print("I hope it stays that way!")
        else:
            print("Aww, too bad")


def agefunc():
    global userage
    userage = int(input("How old are you?"))
    if int(userage) >= 18:
        print("Wow, an adult? Amazing!")
    else:
        print("Still growing!")
    return userage

    print(userbirthday)


def birthday(age):
    global userbirthday
    usermonth = input("What month is your birthday?")
    userday = input("What day is your birthday?")
    useryear = 2022 - age
    userbirthday = f"Your birthday is {usermonth}, {userday}, {useryear}"
    print(userbirthday)


def familyfunc():
    siblings = int(input("How many siblings do you have?"))
    if siblings > 10:
        print("Wow you have an extraordinary amount of siblings")
    elif siblings > 5:
        print("You have a lot of siblings")
    elif siblings > 3:
        print("You have a nice amount of siblings")
    elif siblings > 1:
        print("You guys must be close!")
    elif siblings == 1:
        print("You only have one sibling, you must be lucky!")
    elif siblings == 0:
        print("You have no siblings, you must be lonely ")


def miscfunc():
    miscstuff = ["Games", "Color", "Sport", "Show"]
    global favgame, favcolor, favsports, favshow
    if random.choice(miscstuff) == "Games":
        favgame = input("What is your favorite game? :")
    elif random.choice(miscstuff) == "Color":
        favcolor = input("What is your favorite color? :")
    elif random.choice(miscstuff) == "Sport":
        favsports = input("What is your favorite sport? : ")
    elif random.choice(miscstuff) == "Show":
        favshow = input("What is your favorite show? : ")


while endless == True:
    choice = input("What would you like to talk about? : ").capitalize()
    if choice == posstopics[0]:
        weatherfunc()
    elif choice == posstopics[1]:
        agefunc()
        if userbirthday == "":

            birthday(userage)
        elif input(
                "You already have a birthday saved, would you like to edit it?"
        ).capitalize() == "Yes":
            birthday()
        else:
            print(userbirthday)
    elif choice == posstopics[2]:
        familyfunc()
    elif choice == posstopics[3]:
        miscfunc()
        print(
            f"Your current favorite things are : {favgame}, {favcolor}, {favsports}, {favshow}"
        )
    elif choice == posstopics[4]:
        break
    else:
        print("Not a valid option, please select again")
        print(posstopics)

print("finished talking")