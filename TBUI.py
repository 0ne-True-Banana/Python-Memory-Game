import sys
import random
import time
import os

print ("THE HERO OF CODE")
def start():
    user_input = input ("Type 'Y' to start ")
    
    if user_input == ("Y"):
        print("Starting.....")
        time.sleep(4)
        print ("This is the story of a land deep in Cyberspace.")
        time.sleep(3)
        print ("The story tells of a hero, not your usual one, but one a quest for power.....")
        time.sleep(3)
        print("in the office")
        time.sleep(3)
        print("Anticlimactic I know")
    elif user_input == ("N"):
         print("Bye Bye!, I don't know why u opened the game if you weren't gonna play it. :(")
         sys.exit(0)

start()
time.sleep(5)

# Input Tutorial
print ("Let's start with a tutorial \n")
time.sleep(3)
print ("This game is a text based game.")
time.sleep(3)
print ("This means that the game is not graphical. Moreover, it relies on your text.")
time.sleep(3)
print ("It will majorly test your memory skills")
time.sleep(3)
print ("Let's start with an example,")

user_tutorial = input ("Yes or No? p.s type Yes ")

if user_tutorial == ("Yes"):
        print ("Great! Now you're getting the hang of it.")
        print (" Now we can get to the actual game.")
else:
        print("All you had to do was to type 'Yes'")
        print ("It's not that hard")

name = input("What is your name? ")

print ("Chapter 1: Getting Up and At It")
print ("Objective: Check Your Email")
print ("You are in your room a dark but clean place.")

def stand_up():
    return input("Type stand or sleep ")

wake_up = 7.0

while wake_up <= 7.10:
    user_choice = stand_up()

    if user_choice == "stand":
        print("As you emerge from your bed, your computer chimes and notifies you of the time,", wake_up)
        break

    elif user_choice == "sleep":
        print("You choose to sleep")
        wake_up += 0.01
        wake_up = round (wake_up, 3)
        print("Time:", wake_up)

if wake_up >= 7.10:
    print("You choose to get up and stop being lazy")

print ("You stand up, and need to check your email to see the salary of your job offer.")
print ("You walk to you desk and sit in front of your computer. You remember your password, 079022")
print (" You are met with the starting screen of your computer.")

while True:
    password_input = input ("Password: ")
     
    if password_input == "079022":
        print ("The box that previously held the password bar now holds a rolling icon")
        print ("The computer opens up and you are met by your email.")
        break

    else:
        print ("The computer notifies you that the password is incorrect")


print ("There are five tabs: Inbox, Promotions, Starred, and Bin")
print ("Your job offer should be located in the INBOX tab")

while True:
    email_input= input("Which tab do you enter? ")
    
    if email_input == "Inbox":
        print ("You scroll through the tab and find your job offer")
        break
    
    else:
        print (" You scroll through the tab but you cannot find your job offer")

print ("Your job offer reads:")
print ("Synchronix Org.")
print ("We live in the present, but we form the future")
print ("Your job application to Synchronix Org. has been accepted")
print ("Salary: 20,000 bits per week")
print ("Accept or Decline?")
print ("You click accept on the company's job offer.")
print ("You head into the showers and your automated shower chimes.")
print ("'Your Office Wear will be delivered in 5 Mins")
print (" You emerge from the showers,")

def wait():
    return input ("Do you wish to sleep or sit to wait for your wear? ")

original_time = 8.51

while original_time < 8.56:
    user_choice = wait ()
    
    if user_choice == "sit":
        print ("You choose to sit down and wait for the wear.")
        original_time += 0.01
        original_time = round(original_time, 3)
        print ("The time is,", original_time, "A.M")
    elif user_choice == "sleep":
        print ("You choose to sleep")
        original_time += 0.05
        original_time = round(original_time, 3)
        print ("You wake up and the time is", original_time , "A.M")
        break
    else:
        print ("Please choose to sit or sleep.")

        
print ("Your wear arrives and you put it on.")
print ("As you walk down the street, you realize, deep down, that your adventure has just begun.")
print()
print (" Chapter 2: The Office")

day = 1
Office_Time = 2.00
work_value = 1


    
print ("Day", day)
print ("You arrive at your office unit and sit down at your desk.")
print ("Time: 2:00")
print ("The chair feels comfortable and smooth as the AI in the chair system re-adjusts to your specifications")
print (" An office robot gives you directions to different places")
print ("Lounge")
print ("Manager's Office")
print ("Conveyors")
print ("Server Room")
print ("The robot hands you a wristwatch and speeds off")
print ("The watch reads, 'PLEASE REPORT TO THE MANAGER'S OFFICE FOR BREIFING BEFORE 2:15")

def direction():
    return input("Where do you go to? ")

while Office_Time <= 2.15:
    user_choice = direction()

    if user_choice == "Lounge":
        Office_Time += 0.05
        Office_Time = round(Office_Time, 3)
        print("You visit the lounge, filled with many different people and snacks")
        print("Your watch still reads, 'PLEASE REPORT TO THE MANAGER'S OFFICE BEFORE 2:15'")
        print(Office_Time)

    elif user_choice == "Conveyors":
        Office_Time += 0.05
        Office_Time = round(Office_Time, 3)
        print("You visit the conveyors, a place brimming with different machines, all working to make the company's products.")
        print("Your watch still reads, 'PLEASE REPORT TO THE MANAGER'S OFFICE BEFORE 2:15'")
        print(Office_Time)

    elif user_choice == "Server Room":
        Office_Time += 0.05
        Office_Time = round(Office_Time, 3)
        print("You visit the server room but a robot stops you as you do not have access yet")
        print("Your watch still reads, 'PLEASE REPORT TO THE MANAGER'S OFFICE BEFORE 2:15'")
        print(Office_Time)

    elif user_choice == "Manager's Office":
        Office_Time += 0.05
        Office_Time = round(Office_Time, 3)
        print("You visit the Manager's office and open the door with a passcode embedded in your wristwatch")
        print("The manager urges you into the chair")
        break

if Office_Time >= 2.15:
    print("The manager bursts out of his room and screams, 'WHERE IS THE INTERN!'")
    print("The manager kicks you out of the office and your time there ends")
    print("Hint: Next time, try to follow instructions")
    sys.exit(0)
 
print ("As you sit down in the chair, the manager's prescence looms over you.")
print ("He brings out a pen and proceeds to rotate it through his fingers")
print ("HAHA! You should've seen your face!")
print ("Anyways, let's get down to business.")
print ("You were hired by this company because of your exceptional skills in technology")
print ("In fact, we want to commend you for your stellar application")
print("The boss looks at your application and is shocked at your performance")
print ("Well, well, well, We got a nerd here.")
print ("Your performance was adequate, but you definitely need to hit the gym more.")
print (" The boss takes you back to your desk, where he introduces you to the different functions of your computer.")

print("The boss asks you to open your WORK FILE")
print("You open the computer and find different files:")
print("Work")
print("Meals")
print("Packages")
print("Security Services")

def file_open():
    return input("Which file do you click on? ")

while True:
    user_choice = file_open()

    if user_choice == "Work":
        print("The boss looks at you with approval")
        print("Great! At least you can listen to instructions")
        break
    elif user_choice in ["Meals", "Packages", "Security Services"]:
        print("The boss looks at you with a sight of disapproval")
        print("Listen, don't waste my time. Open the Work File")
    else:
        print("Choose an option")

print ("The boss gives you a task and asks you to begin you work as he walks away.")
print ("")
print ("Hours pass by as you endlessy move your fingers across the keyboard")
print ("This sensation is what is known as the work flow.")
print ("From me to you, this isnt something you need to be worried about")
def end_day():
    print("6 HOURS LATER")
    print ("You close from work.")
    print("You arrive at your apartment.")
end_day()

day +1
print("Day" ,day)
print ("You head to the office and sit down at your desk")
# Office status tutorial
print("To increase your office status, you need to do work.")
print("When you do work, it increases your office value, but as you rise up, the work becomes harder")
print("Don't worry though, as the work becomes harder, the value you go up by also increases")
office_value = 1


def get_work():
    return work_value

get_work()
if get_work() == 1:
    def first_work():
        while True:
            random_least = 1
            random_most = 10
            random_amount = 3
            work1 = random.sample(range(random_least, random_most),random_amount)
            print(work1)
            print("Memorize these quickly!, You have 30 seconds.")
            time.sleep(30)
            os.system('cls' if os.name == 'nt' else 'clear')
            work_input= input("What were the numbers? ")

            work_input_list = [int(x) for x in work_input.split()]
            if work_input_list == work1:
                print("Nice Job!")
                break
            else:
                print("Ouch!, Try again!")
    first_work()

def completed_tutorial():
    work_value +1
    print ("Congratulations!")
    time.sleep(2)
    print("You have completed the tutorial")
    time.sleep(2)
    print ("Now here comes the fun part")
    time.sleep(5)
    print ("You have, one goal in this office")
    time.sleep(1)
    print ("To get to the boss's level")
    time.sleep(1)
    print("Word on the street is, he's gonna retire")
    time.sleep(2)
    print("This is your BIG chance!")
    time.sleep(3)
    print("Shoot for the skies.... ", name)
    print("TUTORIAL COMPLETE")
    work_value +1
    print ("Work Value:" ,work_value)

completed_tutorial()
def start():
    while work_value <= 20:
        if work_value == 1:
            def new_work():
                while work_value < 10:
                    print("Great, time for a fresh start!")
                    time.sleep(2)
                    print ("And with a fresh start comes new work!")
                    time.sleep(2)
                    print ("Get ready to work your butt off, " ,name)
                    print ("5")
                    time.sleep(1)
                    print("4")
                    time.sleep(1)
                    print("3")
                    time.sleep(1)
                    print ("2")
                    time.sleep(1)
                    print("1")
                    time.sleep(1)
                    print("Work!")
                    random_least = 1
                    random_most = 30
                    random_amount = 5
                    work1 = random.sample(range(random_least, random_most),random_amount)
                    print(work1)
                    print("Memorize these quickly!, You have 20 seconds.")
                    time.sleep(20)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    work_input= input("What were the numbers? ")
                    new_work_list = [int(x) for x in work_input.split()]

                    if work_input == new_work_list:
                        print("Nice Job! Now do it again.")
                        work_value +1
                        new_work()
                    else:
                        print("Ouch!, Try again!")
                
            new_work()

start()