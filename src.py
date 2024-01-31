import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land.")
    time.sleep(1)
    print("Your goal is to reach the treasure at the end of the journey.")
    time.sleep(1)
    print("Let the adventure begin!")

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter your choice (1-{}): ".format(len(options))))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_scenario():
    print("\nYou enter a dark and mysterious forest.")
    time.sleep(1)
    print("You encounter a fork in the path.")

    choice = make_choice("Which path do you choose?", ["Go left", "Go right"])

    if choice == 1:
        print("You follow the left path and discover a hidden cave.")
        time.sleep(1)
        print("Inside the cave, you find a magical sword.")
    else:
        print("You take the right path and encounter a pack of wolves.")
        time.sleep(1)
        print("You narrowly escape by climbing a tree.")

def desert_scenario():
    print("\nYou enter a vast and scorching desert.")
    time.sleep(1)
    print("You see a mirage in the distance.")

    choice = make_choice("What do you do?", ["Investigate the mirage", "Continue walking"])

    if choice == 1:
        print("You approach the mirage and discover an oasis.")
        time.sleep(1)
        print("You quench your thirst and find a map to the treasure.")
    else:
        print("You ignore the mirage and continue walking under the relentless sun.")

def main():
    introduction()

    choice = make_choice("You come to a crossroads. Which path do you take?", ["Forest", "Desert"])

    if choice == 1:
        forest_scenario()
    else:
        desert_scenario()

    print("\nCongratulations! You've completed the adventure and found the treasure.")

if __name__ == "__main__":
    main()




HAA YE KRLOO PEHLEEE!!!!!
