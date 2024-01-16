"""
Jacob Hildebrand
Lsn23-adventure_game
3/2/23
"""

print("You are in a room. Do you go through the DOOR or the WINDOW?")
choice1 = input("> ")
if choice1.lower() == "door":
    print("You see a hallway with two doors. Do you choose the LEFT or the RIGHT door?")
    choice2a = input("> ")
    if choice2a.lower() == "left":
        print("You enter a room with a locked chest. Do you try to PICK the lock or SMASH the chest?")
        choice3a = input("> ")
        if choice3a.lower() == "pick":
            print("You successfully pick the lock and find a treasure inside. Congratulations, you win!")
        elif choice3a.lower() == "smash":
            print("You smash the chest and find nothing inside. You lose!")
        else:
            print("Invalid choice. You lose!")
    elif choice2a.lower() == "right":
        print("You enter a room with a sleeping dragon. Do you try to SNEAK past it or FIGHT it?")
        choice3b = input("> ")
        if choice3b.lower() == "sneak":
            print("You successfully sneak past the dragon and find a treasure. Congratulations, you win!")
        elif choice3b.lower() == "fight":
            print("You fight the dragon but it overpowers you. You lose!")
        else:
            print("Invalid choice. You lose!")
    else:
        print("Invalid choice. You lose!")
elif choice1.lower() == "window":
    print("You find yourself on the roof. Do you CLIMB DOWN using a rope or JUMP off?")
    choice2b = input("> ")
    if choice2b.lower() == "climb down":
        print("You find yourself in an alley. Do you turn LEFT or RIGHT?")
        choice3c = input("> ")
        if choice3c.lower() == "left":
            print("You find a shortcut and make it home safely. Congratulations, you win!")
        elif choice3c.lower() == "right":
            print("You encounter a mugger and lose all your belongings. You lose!")
        else:
            print("Invalid choice. You lose!")
    elif choice2b.lower() == "jump":
        print("You find yourself in a river. Do you SWIM to the shore or follow the river DOWNSTREAM?")
        choice3d = input("> ") 
        if choice3d.lower() == "swim":
            print("You successfully swim to the shore and find a treasure. Congratulations, you win!")
        elif choice3d.lower() == "downstream":
            print("You follow the river downstream and get lost in the wilderness. You lose!")
        else:
            print("Invalid choice. You lose!")
else:
    print("Invalid choice. You lose!")
