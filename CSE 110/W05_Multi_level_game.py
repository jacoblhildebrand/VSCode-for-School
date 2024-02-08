import time

def prompt(message):
    print(message)
    time.sleep(1.5)  #  delay for dramatic effect

def level_1():
    prompt("You find yourself standing at the entrance of a dark and eerie cave. "
           "The air is damp, and the only sounds you hear are your own footsteps echoing off the walls. "
           "You notice two paths leading deeper into the cave: one to the LEFT and one to the RIGHT. "
           "Which path will you choose?")

    choice = input("LEFT or RIGHT? ").lower()
    if choice == "left":
        prompt("You cautiously make your way down the left path, feeling the cold stone walls on either side of you. "
               "Suddenly, you hear a faint dripping sound ahead and the air is getting more and more humid. ")
        level_2_left()
    elif choice == "right":
        prompt("You decide to take the right path, which seems to slope downward. "
               "As you venture further, you hear a low growling noise echoing from the darkness ahead as the foliage gets thicker. ")
        level_2_right()
    else:
        prompt("Invalid choice! Please type LEFT or RIGHT.")
        level_1()

def level_2_left():
    prompt("Do you want to CONTINUE forward or TURN back?")
    choice = input("CONTINUE or TURN? ").lower()
    if choice == "continue":
         level_3_swamp()
    elif choice == "turn":
        
        pass
    else:
        prompt("Invalid choice! Please type CONTINUE or TURN.")
        level_2_left()

def level_2_right():
    prompt("Do you want to KEEP going or RETREAT?")
    choice = input("KEEP or RETREAT? ").lower()
    if choice == "keep":
        level_3_forest()   
    elif choice == "retreat":
        
        pass
    else:
        prompt("Invalid choice! Please type KEEP or RETREAT.")
        level_2_right()

def level_3_forest():
    prompt("You push your way through the thick foliage of the forest, feeling the branches scratch against your skin. "
           "After a while, you come across a clearing with a small pond. Suddenly, you hear rustling in the bushes nearby.")
    prompt("Do you want to INVESTIGATE or IGNORE it?")
    choice = input("INVESTIGATE or IGNORE? ").lower()
    if choice == "investigate":
        level_4_investigate()
        
    elif choice == "ignore":
        level_4_ignore()
        
    else:
        prompt("Invalid choice! Please type INVESTIGATE or IGNORE.")
        level_3_forest()

def level_3_swamp():
    prompt("You decide to brave the soggy terrain of the swamp, carefully avoiding the murky waters. "
           "As you trudge along, you catch a glimpse of something shiny half-buried in the mud.")
    prompt("Do you want to EXAMINE it closer or KEEP moving?")
    choice = input("EXAMINE or KEEP? ").lower()
    if choice == "examine":
        level_4_examine()
        
    elif choice == "keep":
        level_4_keep()
        
    else:
        prompt("Invalid choice! Please type EXAMINE or KEEP.")
        level_3_swamp()

def level_4_examine():
    prompt("You want to examine the shiny object a little closer. As you reach down and pull it out, you find it to be a "
           "small dagger. It has intricate carvings along the length of the blade that appear to be a foreign language of some sort."
           "You put it in your bag and move deeper through the swamp. You see a small cottage at the end of the path that appears abondoned.")
    prompt("Do you want to CHECK the cottage or MOVE on?")
    choice = input("CHECK or MOVE? ").lower()
    if choice == "check":

        pass
    elif choice == "move":

        pass
    else:
        prompt("Invalid choice! please type CHECK or KEEP.")
        level_4_examine()

def level_4_keep():
    prompt("You leave the shiny object where it is and keep moving forward. As you brush by a large bush you startle what appears to be "
           "a large dog. It growls as it eyes you warily with the hair on the scruff of it's neck standing up.")
    prompt("Do you want to try to APPROACH the dog or steer CLEAR of it?")
    choice = input("APPROACH or CLEAR? ").lower()
    if choice == "approach":

        pass
    elif choice == "clear":

        pass
    else:
        prompt("Invalid choice! Please type APPROACH or CLEAR.")
        level_4_keep()

def level_4_investigate():
    prompt("You take a step forward to investiage the rustling bush further, but as you set your foot down, you snap a large brach "
           "laying on the ground. The sound startles a large rabbit hiding behind the tree next to you. As the rabbit runs away, "
           "a large shadow darts after it and from the ensuing sounds you deduct the the rabbit has become the predators dinner.")
    prompt("Do you want to LOOK and see what it was or WALK on? ")
    choice = input("LOOK or WALK? ").lower()
    if choice == "look":

        pass
    elif choice == "walk":

        pass
    else:
        prompt("Invalid choice! Please type LOOK or WALK. ")
        level_4_investigate()
        
def level_4_ignore():
    prompt("You decide to ignore the sound and continue on your path. You haven't taken more than five steps when an adolescent wolf appears in fornt of you. "
           "with a low growl it lunges forward and knocks you down to the ground and you find yourself staring into the cold gray eyes of the wolf. "
           "As you contemplate what options you have left you come up with two. ")
    prompt("Do you want to FIGHT the wolf or attempt to CALM and tame it?")
    choice = input("FIGHT or CALM? ").lower()
    if choice == "fight":

        pass  
    elif choice == "calm":
        
        pass
    else:
        prompt("Invalid choice! Please type FIGHT or CALM.")
        level_4_ignore()

# start the game
prompt("Welcome to the text-based adventure game!")
level_1()