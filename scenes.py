def beach(items):

    if items["charged_phone"] == True:
        print("""You are back where you started your journey. It feels a bit weird to stand at the beach again. 
Maybe here the signal is good enough to have at least enough connection to make a call.
Do you want to check the phone?
1. Yes lets try, there must be a way out.
2. No i think i try it somewhere else""")
        userinput = ""
        userinput = input(">")
        if userinput == "1":
            print("""You turn on the phone to check if there is some connection here. After waiting for a moment you see that there is at least one bar connection.
You press the button for the emergency call and hope its working. You press call and the calling sound appears in your ear.
After some moment you hear a voice speaking to you. You are explaing your situation as good as possible and they tell you to have some patient.
They will send a helicopter to look for you. You feel a huge wave of relief and happiness after you ended the call.
You let yourself fall into the sand and rest for a moment totally carefree now. 
You made it.
Congratulations! Game clear!
おめでとうございますよくできました。""")
            quit()

        elif userinput == "2":
            print("You decided to look somewhere else for a good spot.\nYour options are\n1. Go the left side\n2. Go to the right side")
            userinput = input(">")
            if userinput == "1":
                leftside(items)
            elif userinput == "2":
                rightside(items)
            else:
                print("This is not a valid option.")
        else:
            print("This is not a valid option.")
            
    if items["plastic_bottle"] == True:
        print("\nBeach Startscene\n")
        options = ["1", "2"]
        userinput = ""
        while userinput not in options:
            print("1. Go left\n2. Go right")
            userinput = input(">")
            if userinput == "1":
                leftside(items)
            elif userinput == "2":
                rightside(items)
            else:
                print("This is not a valid option.")
    
    else:
        print("\nBeach Startscene\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 4:
            print("1. Get up and look around\n2. Go left\n3. Go right\n4. Keep laying")
            userinput = input(">")
            if userinput == "1":
                print("""You are trying to get up. Your arm hurts pretty much when you are moving it. 
After you managed to get on your feet. You get a better look of your surroundings. 
As far your eyes can see there is only water. Behind you lies a path that seems to lead into a little jungle. 
While you are look around on the beach, you see a platisc bottle in the sand.
What is your next action?\n""")
            
                print("1. Get the plastic bottle\n2. Go left\n3. Go right")
                userinput = input(">")
                if userinput == "1":
                    items["plastic_bottle"] = True
                    print("You received Plastic Bottle.\nWhat is your next action?\n")
                    print("1. Go left\n2. Go right")
                    userinput = input(">")
                    if userinput == "1":
                        leftside(items)
                    elif userinput =="2":
                        rightside(items)
                    else:
                        print("This is not a valid option.")

                elif userinput == "2":
                    leftside(items)
                elif userinput == "3":
                    rightside(items)
                else:
                    print("This is not a valid option.")

            elif userinput == "2":
                leftside(items)
            elif userinput == "3":
                rightside(items)
            elif userinput == "4":
                print("You feel the sun on your skin and the soft breeze from the wind. If your wound wouldnt hurt then this would be really comfortable and relaxing.\nWhat is your next action?\n")
            else:
                print("This is not a valid option.")

### LEFTSIDE SCENE ####
### LEFTSIDE SCENE ####
### LEFTSIDE SCENE ####

def leftside(items):
    print("\nBeach left side\n")
    options = ["1", "2", "3", "4"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Take the path towards the vegetation")
        userinput = input(">")
        if userinput == "1":
            print("""You take a look around you and you see the beautiful beach and hear the sound of the ocean. The water is crystalclear and you feel like u wanna go swimming.
But the pain in your arm reminds you of your injury. A bit more far away u see some rocks at the beach and in the north it looks like some kind of vegetation.
What is your next step?\n""")

        elif userinput == "2":
            stoned_area(items)
        elif userinput == "3":
            beach(items)
        elif userinput =="4":
            step_into_jungle(items)
        else:
            print("This is not a valid option.")

### STONEDAREA SCENE ####
### STONEDAREA SCENE ####
### STONEDAREA SCENE ####

def stoned_area(items):

    if items["piece_of_wood"] == True:
        print("\nRockybeach\n")
        options = ["1", "2"]
        userinput = ""
        print("Your options are:\n1. Go forward\n2. Go back")
        userinput = input(">")
        if userinput == "1":
            walkin_path_one(items)
        elif userinput == "2":
            leftside(items)
        else:
            print("This is not a valid option.")

    else:
        print("\nRockybeach\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 1:
            print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Explore the rocks")
            userinput = input(">")
            if userinput == "1":
                print("""While you let your eyes wander around. You see then more and more stony the area becomes.
Around twenty meters from you, you see some huge rocks that are nearly as tall as you. If you wanna explore this area.
You need to be careful not to break your legs or anything else.\n""")
            elif userinput == "2":
                walkin_path_one(items)
            elif userinput == "3":
                leftside(items)
            elif userinput == "4":
                print("""You are taking off your shoes to get a better feeling with your feet. You are slowly walkin towards the rocks.
You are carefully climbing on the rocks and trying to hold the balance with ur hands gripping some edge of the rocks. 
As you slowly making your way through the rocks, you notice piece of wood that is laying between two rocks.
What is your next step?\n""")
                  
                print("1. Grab the piece of wood\n2. Go forward\n3. Go back")
                userinput = input(">")
                if userinput == "1":
                    items["piece_of_wood"] = True
                    print("You received Piece of wood.\nWhat is your next action?\n")
                    print("1. Go forward\n2. Go back")
                    userinput = input(">")
                    if userinput == "1":
                        walkin_path_one(items)
                    elif userinput =="2":
                        leftside(items)
                    else:
                        print("This is not a valid option.")
                elif userinput =="2":
                    walkin_path_one(items)
                elif userinput =="3":
                    leftside(items)
                else:
                    print("This is not a valid option.")
            
            else:
                print("This is not a valid option.")

### RIGHTSIDE SCENE ####
### RIGHTSIDE SCENE ####
### RIGHTSIDE SCENE ####

def rightside(items):
    print("\nBeach right side\n")
    options = ["1", "2", "3", "4"]
    userinput = ""
    while userinput not in options or 4 or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back\n4. Sit down")
        userinput = input(">")
        if userinput == "1":
            print("""You take a look around you and you see the beautiful beach and hear the sound of the ocean. The water is crystalclear and you feel like u wanna go swimming.
But the pain in your arm reminds you of your injury. A bit more far away u see some rocks at the beach and in the north it looks like some kind of vegetation.
What is your next step?\n""")
        elif userinput == "2":
            cliff_scene(items)
        elif userinput == "3":
            beach(items)
        elif userinput == "4":
            print("You are sitting down in the sand and make yourself comfortable. Its so nice feeling the sun on your skin. It surely would be nice to spend the day on the beach.\n What is your next step?\n")
        else:
            print("This is not a valid option.")

### CLIFF SCENE ####
### CLIFF SCENE ####
### CLIFF SCENE ####

def cliff_scene(items):

    if items["glass_bottle"] == True:
        print("\nThe Cliffs\n")
        options = ["1", "2"]
        userinput = ""
        print("Your options are:\n1. Go forward\n2. Go back\n")
        userinput = input(">")
        if userinput == "1":
           walkin_path_two(items)
        elif userinput == "2":
           rightside(items)
        else:
            print("This is not a valid option.")

    else:
        print("\nThe Cliffs\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options or 1:
            print("Your options are:\n1. Sit down and look around\n2. Go forward\n3. Climb down\n4. Go back")
            userinput = input(">")
            if userinput == "1":
                print("""You find a comfy spot to sit down and gaze over the scenery that lies infront of you.
You wonder how fast the sandy beach on which you woke up got swapped with this enoumerous cliff that seems to have no end.
You let your eyes go till the edge and realize that its a long way down from the cliff till the water.
You better pay attention to your steps, cause you don't wanna end up as decoration on the ground.
While you let your eyes wander over the cliff, you spot something shiny. As you look closer you moticed that there is something stuck between the rocks.
Probably someone might accidentally dropped something there, which now reflects the sunlight during the daytime.\n""")
            elif userinput == "2":
                walkin_path_two(items)
            elif userinput == "3":
                print("""You decided to climb down the cliff to investiga what the shiny thing is that u spotted. 
First you look around for a path that alloaws you to climb down safely. Around five meters away from you, you see some small way
which seems to lead down the cliff. Carefully you go down, one step after another, always making sure your hands have something to hold on.
As you are getting closer, you see its a bottle probably made of glass. Finally you are close enough to grab the bottle and its indeed a glass bottle.
The bottle is totally empty but maybe it could be of some use anyway at some point. 
What do you wanna do?\n""")
                userinput = ""
                print("Your options are:\n1. Take the bottle with you\n2. Leave it you already have one")
                userinput = input(">")
                if userinput == "1":
                    items["glass_bottle"] = True
                    print("You receive a glass bottle! (<insert zelda sound of receiving an item>)\n What is your next move\n")
                    print("1. Go forward\n2. Go back")
                    userinput = input(">")
                    if userinput == "1":
                        walkin_path_two(items)
                    elif userinput =="2":
                        rightside(items)
                    else:
                        print("This is not a valid option.")
                else:
                    print("You leave the glass bottle where it is\n")

            elif userinput == "4":
                rightside(items)
            else:
                print("This is not a valid option.")

### WALKING PATH ONE SCENE ####
### WALKING PATH ONE SCENE ####
### WALKING PATH ONE SCENE ####

def walkin_path_one(items):
    print("\nWalk along the Beach\n")
    forward = 0
    backward = 1
    options = ["1", "2", "3"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back")
        userinput = input(">")
        if userinput == "1":
            print("""Your eyes are wandering along the beach. As far your eyes can see, you see only water till the horizont. There is nothing much to see here
beside the sand and some shells on the beach. The trees in the jungle are so narrow that there is no path into it. 
Its probably the best to not stay too long in this burning sun.
What is your next step?\n""")
        elif userinput == "2":
            forward = forward +1
            backward = backward +1
        elif userinput == "3":
            forward = forward -1
            backward = backward -1
        else:
            print("This is not a valid option.")

        if backward == 0:
            stoned_area(items)
    
        if forward == 5:
            cliff_scene(items)

### WALKING PATH TWO SCENE ####
### WALKING PATH ONE SCENE ####
### WALKING PATH ONE SCENE ####

def walkin_path_two(items):
    print("\nWalk along the Beach\n")
    forward = 0
    backward = 1
    options = ["1", "2", "3"]
    userinput = ""
    while userinput not in options or 1:
        print("Your options are:\n1. Look around\n2. Go forward\n3. Go back")
        userinput = input(">")
        if userinput == "1":
            print("""Your eyes are wandering along the beach. As far your eyes can see, you see only water till the horizont. There is nothing much to see here
beside the sand and some shells on the beach. The trees in the jungle are so narrow that there is no path into it. 
Its probably the best to not stay too long in this burning sun.
What is your next step?\n""")
        elif userinput == "2":
            forward = forward +1
            backward = backward +1
        elif userinput == "3":
            forward = forward -1
            backward = backward -1
        else:
            print("This is not a valid option.")

        if backward == 0:
            cliff_scene(items)
            
        if forward == 5:
            stoned_area(items)

###### SCENES PART TWO !!!!!!!!!!!!!!!!!!!!!!!
###### SCENES PART TWO !!!!!!!!!!!!!!!!!!!!!!!
###### SCENES PART TWO !!!!!!!!!!!!!!!!!!!!!!!


def step_into_jungle(items):

    if items["injury"] == True and items["galaxy"] == True:
        print("""You are feeling really exhausted and sit down on some tree stump. You are feeling dizzy and its getting harder and harder to keep your eyes open.
YOu let yourself slide to the ground and let your head rest on the grass. The world around you starts to rotating as you lose conciousness.
You died cause of blood loss!
ゲームオーバー """)
        quit()

    elif items["piece_of_wood"] == True and items["coconut"] == True:
         print("\nThe Path to the inside of the island\n")
         options = ["1", "2", "3"]
         userinput = ""
         while userinput not in options or 2:
            print("Your options are:\n1. Continue walkin forward\n2. Drop th piece of wood\n3. Go to the beach\n")
            userinput = input(">")
            if userinput == "1":
                crossroads(items)
            elif userinput == "2":
               items["piece_of_wood"] = False
               print("You dropped the Piece of wood on the ground. Now you feel lighter.\nWhat is your next action?\n")
               print("Your options are:\n1. Continue walkin forward\n2. Go to the beach\n")
               userinput = input(">")
               if userinput == "2":
                    leftside(items)
               elif userinput =="1":
                    crossroads(items)
               else:
                    print("This is not a valid option.")
                    
            elif userinput == "3":
                leftside(items)
            else:
                print("This is not a valid option.")


    elif items["piece_of_wood"] == False and items["coconut"] == False:
        print("\nThe Path to the inside of the island\n")
        options = ["1", "2", "3"]
        userinput = ""
        while userinput not in options:
            print("Your options are:\n1. Continue walkin forward\n2. Go to the beach\n3. Look around")
            userinput = input(">")
            if userinput == "1":
                crossroads(items)
            elif userinput == "2":
                leftside(items)
            elif userinput == "3":
                print("""The scenery changed and instead of the beach with it white sand and the rocks. Your view is now filled with green.
You see some bushes and alot of trees blocking your view. While you look closer you see that some of the trees are actually coconut trees.
Thinkin about coconuts you remember the smell of it and how it gives you always a bad feeling in your stomach.
You notice that one tree even has a coconut on it. You wonder if you should get it, even so You wouldnt eat it for sure.
What will you do?\n""")
                      
                print("1. Climb up the tree and get the coconut\n2. Leave the coconut there.\n")
                userinput = input(">")
                if userinput == "1":
                        items["coconut"] = True
                        print("You received a coconut.\nWhat is your next action?\n")

                        print("1. Go forward\n2. Go back")
                        userinput = input(">")
                        if userinput == "2":
                            leftside(items)
                        elif userinput =="1":
                            crossroads(items)
                        else:
                            print("This is not a valid option.")

                elif userinput == "2":
                        print("You leave the coconut on the tree. Someone else can get it.")
                else:
                        print("This is not a valid option.")       
            else:
                print("This is not a valid option.")


    elif items["piece_of_wood"] == False and items["coconut"] == True:
        print("\nThe Path to the inside of the island\n")
        options = ["1", "2"]
        userinput = ""
        while userinput not in options:
            print("Your options are:\n1. Continue walkin forward\n2. Go to the beach\n")
            userinput = input(">")
            if userinput == "1":
                crossroads(items)
            elif userinput == "2":
                leftside(items)     
            else:
                print("This is not a valid option.")


    if items["piece_of_wood"] == True and items["coconut"] == False:
        print("\nThe Path to the inside of the island\n")
        options = ["1", "2", "3", "4"]
        userinput = ""
        while userinput not in options:
            print("Your options are:\n1. Continue walkin forward\n2. Drop th piece of wood\n3. Go to the beach\n4. Look around")
            userinput = input(">")
            if userinput == "1":
                crossroads(items)
            elif userinput == "2":
               items["piece_of_wood"] = False
               print("You dropped the Piece of wood on the ground. Now you feel lighter.\nWhat is your next action?\n")
               print("Your options are:\n1. Continue walkin forward\n2. Go to the beach\n")
               userinput = input(">")
               if userinput == "2":
                    leftside(items)
               elif userinput =="1":
                    crossroads(items)
               else:
                    print("This is not a valid option.")
                    
            elif userinput == "3":
                leftside(items)
            elif userinput == "4":
                print("""The scenery changed and instead of the beach with it white sand and the rocks. Your view is now filled with green.
You see some bushes and alot of trees blocking your view. While you look closer you see that some of the trees are actually coconut trees.
Thinkin about coconuts you remember the smell of it and how it gives you always a bad feeling in your stomach.
You notice that one tree even has a coconut on it. You wonder if you should get it, even so You wouldnt eat it for sure.
What will you do?\n""")
                      
                print("1. Climb up the tree and get the coconut\n2. Leave the coconut there.\n")
                userinput = input(">")
                if userinput == "1":
                        items["coconut"] = True
                        print("You received a coconut.\nWhat is your next action?\n")

                        print("1. Go forward\n2. Go back")
                        userinput = input(">")
                        if userinput == "2":
                            leftside(items)
                        elif userinput =="1":
                            crossroads(items)
                        else:
                            print("This is not a valid option.")

                elif userinput == "2":
                        print("You leave the coconut on the tree. Someone else can get it.")
                else:
                        print("This is not a valid option.")       

            else:
                print("This is not a valid option.")



### CROSSROADS SCENE ####
### CROSSROADS SCENE ####
### CROSSROADS SCENE ####

def crossroads(items):
     print("\nThe Crossroad\n")
     if items["eatenfood"] == True:
          print("""Just when you left the fireplace you start to feel unwell and you notice some pain in ur stomach that gets more intense.
As the pain gets worse you sit down on the ground and hope it gets better. After some time you are slowly losing consciousness.
The world around you slowly fade into black while you sink to the ground and your head is laying on the floor.
You died!
ゲームオーバー """)
     elif items["filled_bottle"] == True and items["firstaidkit"] == True:     
          options = ["1", "2", "3", "4", "5", "6"]
          userinput = ""
          while userinput not in options:
               print("Your options are:\n1. Continue walkin forward\n2. Take the path to your left\n3. Take the path to your right\n4. Read the Sign\n5. Take care of your injuries\n6. Go back")
               userinput = input(">")
               if userinput == "1":
                    path_one(items)
               elif userinput == "2":
                    fireplace(items)
               elif userinput == "3":
                    path_two(items)
               elif userinput == "4":
                    print("THIS IS A SIGN!!!\n")
               elif userinput == "5":
                    items["injury"] = False
                    items["filled_bottle"] = False
                    items["firstaidkit"] = False
                    print("""First you take the plastic bottle with water and wash the wound properly so you dont get anything in your wound.
Then you use the desinfection liquid. Once you finised you slowly and carefully wrapping the bandage around your arm and fix it at the end. You immedietly feel better already.""")
               elif userinput == "6":
                    step_into_jungle(items)
               else:
                    print("This is not a valid option.")

     else:
          options = ["1", "2", "3", "4", "5"]
          userinput = ""
          while userinput not in options:
               print("Your options are:\n1. Continue walkin forward\n2. Take the path to your left\n3. Take the path to your right\n4. Read the Sign\n5. Go back")
               userinput = input(">")
               if userinput == "1":
                    path_one(items)
               elif userinput == "2":
                    fireplace(items)
               elif userinput == "3":
                    path_two(items)
               elif userinput == "4":
                    print("THIS IS A SIGN!!!")
               elif userinput == "5":
                    step_into_jungle(items)
               else:
                    print("This is not a valid option.")

### FIREPLACE SCENE ###
### FIREPLACE SCENE ###
### FIREPLACE SCENE ###

def fireplace(items):
     print("\nA abandoned fireplace\n")
     if items["glass_bottle"] == True and items["food"] == True:
          print("Now that you have something to eat and something to make fire, you can try to grill the meat. Do you wanna do this?\n1. Yeah lets do this i am hungry\n2. No i am vegetarian and also afraid of food poison")
          userinput = ""
          userinput = input(">")
          if userinput == "1":
               items["eatenfood"] = True
               items["food"] = False
               print("""You search for some branches to prepare the fireplace. After its done you take the meat and prepare it as well.
Then u take the glass bottle and start to create a fire. After you managed this as well. You take a seat and wait till you feel your meat is ready to eat.
Since you don't have a plate or anything to place the meat on, you just eat it from the branch. It actually tastes good and you really enjoy it.
Guess the worry that it was not good anymore was for nothing. After you finised eating you rest a little and then slowly leave the fireplace""")
               crossroads(items)
          elif userinput == "2":
               print("You decided to not cook the meat and leave the fireplace again.")
               crossroads(items)
          else:
               print("This is not a valid option.")

     elif items["glass_bottle"] == True and items["firstaidkit"] == False:
        options = ["1", "2", "3" "4"]
        userinput = ""
        while userinput not in options or 2:
          print("Your options are:\n1. Look around\n2. Sit down for a moment\n3. Use the glass bottle\n4. Go back")
          userinput = input(">")
          if userinput == "1":
               print("""Big trees surrounding the area. It seems that this place was used to make fire and have a nice get together.
You see that thw stones are formed in a circle around the spot in the middle. Inside the circle there is some burned wood and the ashes from the last few times.
Since the trees and the vegetation stand so close to each other. It would be really difficult to find a path forward. But while looking around
you spot some little box laying around. 
Do you wanna take a closer look at it? YES or NO?""")
               
               userinput = input(">")
               if userinput == "YES":
                    print("You walk closer to the box and now its becoming more clear to you. It is a First-Aid kit that someone probably lost here.\nDo you wanna take it?")
                    print("1. Take it with you\n2. Leave it. Why would you need it anyway. Its not like you are injured or anything.")

                    userinput = input(">")
                    if userinput == "1":
                         items["firstaidkit"] = True
                         print("You received a First-Aid Kit!\nAfer obtaining the First-Aid kit you return to the crossroads.\n")
                         crossroads(items)
                    elif userinput == "2":
                         print("You leave it there. Maybe the next person can use it.\n1")
                    else:
                         print("This is not a valid option.")

               elif userinput == "NO":
                    print("Yeah right. You are busy and have better things to do then check out some little box\n")
               else:
                    print("This is not a valid option.")

          elif userinput == "2":
               print("""Time for a little rest. Exploring this island can be pretty tiring right. Even more with the sun shining down on you.
It would be nice for sure if you had something to refresh yourself. But you dont have this luxury here. 
Thanks to the tall trees you can escape the sunlight for a bit.\n""")
          elif userinput == "3":
               print("""You take the glass bottle you found and try different spots to catch the sunlight and reflect to where the ashes is laying on the ground.
It takes some time and adjustments till you find the right angle were it reflects the sunlight perfectly. If you keep this up like this you could make a fire with this for sure.\n""")
          elif userinput == "4":
               crossroads(items)
          else:
               print("This is not a valid option.")


     elif items["glass_bottle"] == False and items["firstaidkit"] == False:
        options = ["1", "2", "3"]
        userinput = ""
        while userinput not in options or 2:
          print("Your options are:\n1. Look around\n2. Sit down for a moment\n3. Go back")
          userinput = input(">")
          if userinput == "1":
               print("""Big trees surrounding the area. It seems that this place was used to make fire and have a nice get together.
You see that alot of stones are formed in a circle in the middle of the spot. Inside the circle there is some burned wood and the ashes from the last few times.
Since the trees and the vegetation stand so close to each other. It would be really difficult to find a path forward. But while looking around
you spot some little box laying around. Do you wanna take a closer look at it? YES or NO?""")
               
               userinput = input(">")
               if userinput == "YES":
                    print("You walk closer to the box and now its becoming more clear to you that it seems to be a First-Aid kit that someone probably lost here.\nDo you wanna take it?")
                    print("1. Take it with you\n2. Leave it. Why would you need it anyway. Its not like you are injured or anything.")

                    userinput = input(">")
                    if userinput == "1":
                         items["firstaidkit"] = True
                         print("You received a First-Aid Kit!\nWhat is your next action?")
                         print("1. Go back")
                         userinput = input(">")
                         if userinput == "1":
                            crossroads(items)
                         else:
                              print("This is not a valid option.")

                    elif userinput == "2":
                         print("You leave it there. Maybe the next person can use it.")
                    else:
                         print("This is not a valid option.")

               elif userinput == "NO":
                    print("Yeah right. You are busy and have better things to do then check out some little box\n")
               else:
                    print("This is not a valid option.")

          elif userinput == "2":
               print("""Time for a little rest. Exploring this island can be pretty tiring right. Even more with the sun shining down on you.
It would be nice for sure if you had something to refresh yourself. But you dont have this luxury here. 
Thanks to the tall trees you can escape the sunlight for a bit.\n""")
          elif userinput == "3":
               crossroads(items)
          else:
               print("This is not a valid option.")


     elif items["glass_bottle"] == True and items["firstaidkit"] == True:
        options = ["1", "2", "3"]
        userinput = ""
        while userinput not in options or 2:
          print("Your options are:\n1. Use the glass bottle\n2. Sit down for a moment\n3. Go back")
          userinput = input(">")
          if userinput == "2":
               print("""Time for a little rest. Exploring this island can be pretty tiring right. Even more with the sun shining down on you.
It would be nice for sure if you had something to refresh yourself. But you dont have this luxury here. 
Thanks to the tall trees you can escape the sunlight for a bit.\n""")
          elif userinput == "1":
               print("""You take the glass bottle you found and try different spots to catch the sunlight and reflect to where the ashes is laying on the ground.
It takes some time and adjustments till you find a position were it reflects the sunlight perfectly. If you keep this up you could make a fire with this for sure.""")
          elif userinput == "3":
               crossroads(items)
          else:
               print("This is not a valid option.")          


     elif items["glass_bottle"] == False and items["firstaidkit"] == True:
        options = ["1", "2"]
        userinput = ""
        while userinput not in options or 1:
          print("Your options are:\n1. Go back\n2. Sit down for a moment")
          userinput = input(">")
          if userinput == "2":
               print("""Time for a little rest. Exploring this island can be pretty tiring right. Even more with the sun shining down on you.
It would be nice for sure if you had something to refresh yourself. But you dont have this luxury here. 
Thanks to the tall trees you can escape the sunlight for a bit.\n""")
          elif userinput == "1":
               crossroads(items)
          else:
               print("This is not a valid option.")          

## WALKING PATH TWO SCENE ###          
## WALKING PATH TWO SCENE ###  
## WALKING PATH TWO SCENE ###       

def path_two(items):
     print("\nThe walk through the wild\n") 
     options = ["1", "2", "3", "4"]
     userinput = ""
     while userinput not in options or 2:
          print("Your options are:\n1. Touch grass\n2. Look around\n3. Keep walking forward\n4. Go back")
          userinput = input(">")
          if userinput == "2":
               print("""\nThe secenery is really beautiful. A small walking path lies in front of you.
Left and right from the path you see all kind of different trees, palms and bushes. From far away you hear the sound of some animals, probably monkeys.
Thanks to the trees its not so hot here anymore and walking feels more relaxing.\n""")
          elif userinput == "1":
               print("""You look on the ground and see the beautiful grass before your eyes. Its so green and fresh.
Your imagine how it would feel to touch it and feel it on your fingertips. 
You hesistate for a moment cause you are unsure if you really wanna do it.\n""")
               print("1. Lets do it, touch the grass!!\n2. Its too dangerous, i wont do it")
               userinput = input(">")
               if userinput == "1":
                    print("The moment you touch the grass with your fingers. You feel like a lightningbolt hits you, you start to feel dizzy and get on your knees.\nYou died\n ゲームオーバー \n")
                    exit()
               elif userinput == "2":
                    print("You decided to resist the urge and wont touch the grass. Maybe its for the better.\n")
               else:
                    print("This is not a valid option.")

          elif userinput == "3":
               statue_place(items)
          elif userinput == "4":
               crossroads(items)
          else:
               print("This is not a valid option.")

### WALKING PATH ONE SCENE ####
### WALKING PATH ONE SCENE ####
### WALKING PATH ONE SCENE ####
    
def path_one(items):
     print("\nThe walk through the wild\n")
     if items["filled_bottle"] == True and items["firstaidkit"] == True:
          options = ["1", "2", "3"]
          userinput = ""
          while userinput not in options or 1:
               print("Your options are:\n1. Take care of your injury\n3. Keep going\n4. Head back")
               userinput = input(">")
               if userinput == "1":
                    items["injury"] = False
                    items["filled_bottle"] = False
                    items["firstaidkit"] = False
                    print("""First you take the plastic bottle with water and wash the wound properly so you dont get anything in your wound.
Then you use the desinfection liquid. Once you finised you slowly and carefully wrapping the bandage around your arm and fix it at the end. You immedietly feel better already.""")
               elif userinput == "2":
                    print("""\nYou are checking the area for a tree that would be easy to climb. After you spotted one you carefully climb up the tree.
Slowly you go higher and higher till you reach a point were you feel the branches wont be able to carry your weight anymore.
But you are already very high up that you can have a good overview. In the north you see there is some kind of building.
Beside this there is a mountain more far north from you. After you finished checking out everything you carefully climb down again.\n""")
               elif userinput == "3":
                    the_house(items)
               elif userinput == "4":
                    crossroads(items)
               else:
                    print("This is not a valid option.")

     else:
          options = ["1", "2", "3", "4"]
          userinput = ""
          while userinput not in options or 1:
               print("Your options are:\n1. Look around\n2. Climb on a tree\n3. Keep going\n4. Head back")
               userinput = input(">")
               if userinput == "1":
                    print("""\nThe path you been walking so far seems to end soon and leading into a broader more spaciousarea.
There are alot of trees, palms and brushwood that is blocking the path and preventing you from go further.
But with some effort you might be able to get through. A other option would be that you try to find a othere path.
WHat will you do?\n""")
               elif userinput == "2":
                    print("""\nYou are checking the area for a tree that would be easy to climb. After you spotted one you carefully climb up the tree.
Slowly you go higher and higher till you reach a point were you feel the branches wont be able to carry your weight anymore.
But you are already very high up that you can have a good overview. In the north you see there is some kind of building.
Beside this there is a mountain more far north from you. After you finished checking out everything you carefully climb down again.\n""")
               elif userinput == "3":
                    the_house(items)
               elif userinput == "4":
                    crossroads(items)
               else:
                    print("This is not a valid option.")

### STATUE PLACE SCENE ####      
### STATUE PLACE SCENE ####
### STATUE PLACE SCENE ####             

def statue_place(items):
     print("\nThen ancient statue\n")
     options = ["1", "2", "3", "4"]
     userinput = ""
     while userinput not in options or 1:
          print("Your options are:\n1. Look around\n2. Go back\n3. Take a look at the statue\n4. Keep going")
          userinput = input(">")
          if userinput == "1":
               print("""\nAs you keep walking the narrow path you see slowly some statues between some of the trees.
As you walk closer, you see there are actually 6 statues that are standing between the trees.
It even looks a bit like they are guarding the path. The statues remind you a bit of the ones you saw in some japanese temples.\n""")
          elif userinput == "2":
               path_two(items)
          elif userinput == "3":
               print("""\nIt looks like its been a quiet some time since someone took care of them the last time. 
Moos started to cover parts of the statues and you can hardly see all the details anymore. You slowly walking from one statue
to another. It seems every statue represents a goddess from the buddism religion. When you get closer to the 4rd statue you see there is some hole inside the chest.
You probably need some item that will trigger some mechanism inside the statue.\n""")
               if items["piece_of_wood"] == True:
                    print("You could try putting the piece of wood in it.\n1. I will try this\n2. No this wont work")
                    userinput = input(">")
                    if userinput == "1":
                         print("You put the piece of wood int the chest of the statue and hear a CLICK. Something falls out of an opening\nYou received a Key!\n")
                         items["doorkey"] = True
                         items["piece_of_wood"] = False
                    elif userinput == "2":
                         print("Better leave things how they are and get going\n")
                    else:
                         print("This is not a valid option.")
               else:
                    print("But it seems you dont have anything that would fit.\n")

          elif userinput == "4":
               path_three(items)
          else:
               print("This is not a valid option.")

### WALKING PATH THREE SCENE ####
### WALKING PATH THREE SCENE ####
### WALKING PATH THREE SCENE ####

def path_three(items):
     print("\nThe walk through the wild\n")
     options = ["1", "2", "3", "4"]
     userinput = ""
     while userinput not in options or 1:
          print("Your options are:\n1. Look around\n2. Keep walking\n3. Try to take water from the river\n4. Go back")
          userinput = input(">")
          if userinput == "1":
               print("""\nAs you still following the narrow path, the statues are already out of sight. You spot some nice place. 
There is a little river passing along side the path. Seems someone worked on the stones here and changed the shape so you can sit comfortable on them.
This would be the perfect time to pull out your bento and eat something...if you would have one with you.
You go closer to the river and sit down. As you look closer you can even see some little fish swimming through it.\n""")
          elif userinput == "2":
               the_house(items)
          elif userinput == "3":
               print("""\nYou sit down at the river and look at the water. It looks so clear and nice that it gives you the feeling its no salt water like at the beach.
In order to test it, you put one hand into the water of the river. The cold water feels refreshing and really good. You pull your hand out and lick the water from your fingers.
To your surprise it doesnt taste salty at all and should be totally fine for drinking.\n""")
               if items["plastic_bottle"] == True:
                    print("Good thing you took the plastic bottle with you. Now you can fill it with the water here.\n1. Take the bottle and fill it\n2. Drink water with your hands instead")
                    userinput = input(">")
                    if userinput == "1":
                         print("You take the plastic bottle and fill it with the fresh water from the river.\n")
                         items["filled_bottle"] = True
                         items["plastic_bottle"] = False
                    elif userinput == "2":
                         print("You bend over and drink water from the river with your hands.\n")
                    else:
                         print("This is not a valid option.")
               else:
                    print("Looks like you have nothing to fill it with the water.\n")
          
          elif userinput == "4":
               statue_place(items)



#### THE HOUSE ####
#### THE HOUSE ####
#### THE HOUSE ####

def the_house(items):
    print("\nThe House\n") 
    options = ["1", "2", "3", "4"]
    userinput = ""
    while userinput not in options or 1:
          print("Your options are:\n1. Look around\n2. Try to open the door\n3. Enter the house\n4. Go back")
          userinput = input(">")
          if userinput == "1":
               print("""You arrived at a single house. It has a gray colour and the shape of a square. It looks like modern architecture with a even and simple surface.
There are 5 stairs you need to climb to get to the entrance. The door looks pretty solid. Nothing you could open just by brute force.\n""")
          elif userinput == "2":
               if items["doorkey"] == True:
                    print("Do you want to try to open the door with the Key you found?\n1. Yes lets give it a go.\n2. No i am scared. I wanna leave this place.")
                    userinput = input(">")
                    if userinput == "1":
                         print("You take the key and try to put it into the keyhole. At first it seems that you cant turn it around after putting in.\nBut after a few tries it works and you hear a clicking sound that tells you the door is unlocked now.\n")
                         items["open_door"] = True
                         items["doorkey"] = False
                         print("Your options are:\n1. Look around\n2. Enter the house\n4. Go back")
                         userinput = input(">")
                         if userinput == "1":
                              print("""You arrived at a single house. It has a gray colour and the shape of a square. It looks like modern architecture with a even and simple surface.
There are 5 stairs you need to climb to get to the entrance. The door looks pretty solid. Nothing you could open just by brute force.\n""")
                         elif userinput == "2":
                              if items["open_door"] == True:
                                   print("You enter the house")
                                   entrance_house(items)
                              elif items["open_door"] == False:
                                   print("The door is looked. You can not enter the house.\n")
                         elif userinput == "3":
                              crossroads(items)
                         else:
                              print("This is not a valid option.")     

                    elif userinput == "2":
                         print("Makes sense. A single house on a island can only be bad news. Better leave this place")
                         crossroads(items)
                    else:
                         print("This is not a valid option.")
               elif items["open_door"] == True:
                    print("The door is already open")
               else:
                    print("You dont have anything to open the door.")
          elif userinput == "3":
               if items["open_door"] == True:
                    print("You enter the house")
                    entrance_house(items)
               elif items["open_door"] == False:
                    print("The door is looked. You can not enter the house.\n")
          elif userinput == "4":
               crossroads(items)
          else:
               print("This is not a valid option.")

#### THE HOUSE ENTRANCE ####
#### THE HOUSE ENTRANCE ####
#### THE HOUSE ENTRANCE ####

def entrance_house(items):
     print("\nThe Entrance\n")
     options = ["1", "2", "3", "4", "5", "6"]
     userinput = ""
     while userinput not in options or 1 or 2 or 3 or 4:
          print("Your options are:\n1. Take of your shoes off\n2. Call\n3. Look around\n4. Look in the mirror\n5. Go to the next room\n6. Leave the house")
          userinput = input(">")
          if userinput == "1":
               print("You take of your shoes and place them in the shoe rack. Now no one could compalin you dont have proper manners.\n")
          elif userinput == "2":
               print("You take a deep breath and call if someone is in the house. To your \"TOTAL\" surprise no one is answering your call.\n")
          elif userinput == "3":
               print("""The entrance of the house is kinda small. Its just enough for you to turn around. 
There is a long mirror on the wall and next to the mirror you could hang your jacket or whatever you were wearing.
You see a long beige coloured jacket hanging. It looks like the one you saw online recently.
There are also two drawers were you could put some little items like keys or cards.\n""")
          elif userinput == "4":
               print("""You take a look in the mirror and see yourself for the first time in a while. 
Your face looks really tired and pale, your hair looks like some intense haircare would be highly appreciated. 
The top you are wearing has gotten a few holes now. Looking in the mirror also reminds you of your wound on your arm.
It looks really bad now and you probably should do something about it soon.\n""")
          elif userinput == "5":
               livingroom_house(items)
          elif userinput == "6":
               the_house(items)

#### THE HOUSE LIVING ROOM ####
#### THE HOUSE LIVING ROOM ####
#### THE HOUSE LIVING ROOM ####

def livingroom_house(items):
     print("\nThe Livingroom\n")
     options = ["1", "2", "3", "4", "5", "6", "7"]
     userinput = ""
     while userinput not in options or 1 or 2 or 3:
          if items["filled_bottle"] == True and items["firstaidkit"] == True:
               print("Your options are:\n1. Look around\n2. Sit on the couch\n3. Open the fridge\n4. Open the cupboard\n5. Go to the next room\n6. Go to the Entrance\n7. Take care of your injuries")
               userinput = input(">")
               if userinput == "1":
                    print("""You enter the room and the first impression you are getting is that you stepped into the living room. 
Before your eyes you see a comfy couch that nearly screams \"Have a seat\". There is also a table in front of the couch and you even have a beautiful chimney.
The room looks really warm and welcoming. There are two lamps on the left and right to the couch and a bookshelf at the opposite side.
This totally doesnt look like a haunted house at all.\n""")
               elif userinput == "2":
                    print("You can't resist and take a seat on the couch. It feels like you are in heaven. Its so soft and comfortable, \nyou let yourself fall to the side and enjoy this comfortable feeling of laying on the couch.\nWhat do you wanna do next?\n")
               elif userinput == "3":
                    print("You open the fridge and take a look whats inside. You didnt really expected something but to your surprise you find some meat in it.\nYou have no idea how long its already in there and if its still good.\nWhat do you wanna do with it?\n1. Take the meat\n2. Leave it")
                    userinput = input(">")
                    if userinput == "1":
                         items["food"] = True
                         print("You take the meat with you. You need to be careful. At these temeratures it might only take a short while till its not good to eat anymore.")
                         livingroom_house(items)
                    elif userinput == "2":     
                         print("You leave the meat in the fridge. You dont want to get food poisoned and on top, its not your house either.")
                         livingroom_house(items)
               elif userinput == "4":
                    print("The cupboard has a lock on it. So as long you dont have the right key for it. You wont be able to open it.\n")
                    if items["cupboardkey"] == True:
                         print("You use your key to open the cupboard. In it you find alot of cups and dishes but also some books and a charging cable.\nWhat do you wanna do?\n1. Take the charging cable\n2. Take a book\n3. Dont take anything at all")
                         userinput = input(">")
                         if userinput == "1":
                              items["charging_cable"] = True
                              print("You received a chargingcable")
                         elif userinput == "2":
                              print("You take a book. Its cover says \" Jojos Bizzar Adventure\". You wonder what kind of story has such a weird title")
                         elif userinput == "3":
                              print("You leave everything in place cause its not your house after all.")
                         else:
                              print("This is not a valid option.")
               elif userinput == "5":
                    bedroom_house(items)
               elif userinput == "6":
                    entrance_house(items)
               elif userinput == "7":
                    items["injury"] = False
                    items["filled_bottle"] = False
                    items["firstaidkit"] = False
                    print("""First you take the plastic bottle with water and wash the wound properly so you dont get anything in your wound.
Then you use the desinfection liquid. Once you finised you slowly and carefully wrapping the bandage around your arm and fix it at the end. You immedietly feel better already.""")
               else:
                    print("This is not a valid option.")

          else:
               options = ["1", "2", "3", "4", "5", "6"]
               userinput = ""
               while userinput not in options or 1 or 2 or 3:
                    print("Your options are:\n1. Look around\n2. Sit on the couch\n3. Open the fridge\n4. Open the cupboard\n5. Go to the next room\n6. Go to the Entrance")
                    userinput = input(">")
                    if userinput == "1":
                         print("""You enter the room and the first impression you are getting is that you stepped into the living room. 
Before your eyes you see a comfy couch that nearly screams \"Have a seat\". There is also a table in front of the couch and you even have a beautiful chimney.
The room looks really warm and welcoming. There are two lamps on the left and right to the couch and a bookshelf at the opposite side.
This totally doesnt look like a haunted house but as if there is living a person there.""")
                    elif userinput == "2":
                         print("You cant resist and take a seat on the couch. It feels like you are in heaven. Its so soft and comfortable, \nyou let yourself fall to the side and enjoy this comfortable feeling of laying on the couch.\nWhat do you wanna do next?")
                    elif userinput == "3":
                         print("You open the fridge and take a look into it. You didnt really expected something but to your surprise you find some meat in it.\n You have no idea how long its already in there and if its still good.\n What do you wanna do with it?\n1. Take the meat\n2. Leave it")
                         userinput = input(">")
                         if userinput == "1":
                              items["food"] = True
                              print("You take the meat with you. You need to be careful. At these temeratures it might only take a short while till its not good to eat anymore.")
                              livingroom_house(items)
                         elif userinput == "2":     
                              print("You leave the meat in the fridge. You dont want to get food poisoned and on top, its not your house either.")
                              livingroom_house(items)
                    elif userinput == "4":
                         print("The cupboard has a lock on it. So as long you dont have the right key for it. You wont be able to open it.\n")
                         if items["cupboardkey"] == True:
                              print("You use your key to open the cupboard. In it you find alot of cups and dishes but also some books and a charging cable.\nWhat do you wanna do?\n1. Take the charging cable\n2. Take a book\n3. Dont take anything at all")
                              userinput = input(">")
                              if userinput == "1":
                                   items["charging_cable"] = True
                                   print("You received a chargingcable")
                              elif userinput == "2":
                                   print("You take a book. Its cover says \" Jojos Bizzar Adventure\". You wonder what kind of story has such a weird title")
                              elif userinput == "3":
                                   print("You leave everything in place cause its not your house after all.")
                              else:
                                   print("This is not a valid option.")
                    elif userinput == "5":
                         bedroom_house(items)
                    elif userinput == "6":
                         entrance_house(items)
                    else:
                         print("This is not a valid option.")

#### THE HOUSE BED ROOM ####
#### THE HOUSE BED ROOM ####
#### THE HOUSE BED ROOM ####

def bedroom_house(items):
     print("\nThe Bedroom\n")
     if items["galaxy"] == True and items["charging_cable"] == True:
          options = ["1", "2", "3", "4", "5", "6"]
          userinput = ""
          while userinput not in options or 1 or 2 or 3 or 4:
               print("Your options are:\n1. Look around\n2. Lay on the bed\n3. Open closet\n4. Try to charge the phone\n5. Go to the next room\n6. Go back to the livingroom")
               userinput = input(">")
               if userinput == "1":
                    print("""The first thing you see when you enter the room is the huge bed in the middle of the room. So without a doubt you just stepped into the bedroom.
On the bed you see a purple pyjama with white outlines and some flower printings on it, laying. 
At the head of the bed there are two little cupboards and on the opposite side you have a huge closet with a mirror on one door. 
Looking at the closet, makes you remember all these bad \"Coming out\" jokes. 
On the wall is a huge picture from two girls embracing each other and the letters \"citrus\" are written below.""")
               elif userinput == "2":
                    print("""Like the couch, the bed looks even more comfortable and welcoming. Since you came all the way here, why not take a short rest in the bed.
The matress is so comfortable and soft. It gives you the feeling like you are floating in the air. Makes it even harder to get up again.""")
               elif userinput == "3":
                    print("""You pull the slide with the mirror to the side and take a look into the closet.
Its filled with lots of clothes. On the right side you have some jackets and blazer hanging that look really cool.
On the side to you left you see alot of tops and t-shirts but also pants and jeans. Looks like the owner of the house is pretty much into fashion.""")
               elif userinput == "4":
                    items["charged_phone"] = True
                    print("""You are plugging in the charging cable in the phone and look around for a socket to charge it. 
After running around in the room you found one between the cupboard and the bed. You plug the cable into the socket and check if its working.
Luckily after a few moments you see the battery symbol on the screen. You wait a few more minutes and turn on the phone. 
Again your lucky cause there is no passcode that locks the phone from using. With the phone now you could call for help to get off this island.
But the display of the phone shows that you have no connection here. Maybe somewhere else?""")
               elif userinput == "5":
                    balcony_house(items)
               elif userinput == "6":
                    livingroom_house(items)
               else:
                    print("This is not a valid option.")

     elif items["filled_bottle"] == True and items["firstaidkit"] == True:
          options = ["1", "2", "3", "4", "5", "6", "7", "8"]
          userinput = ""
          while userinput not in options or 1 or 2 or 3 or 4:
               print("Your options are:\n1. Look around\n2. Lay on the bed\n3. Open closet\n4. Put on the Pjyama\n5. Open the drawer of the cupboard\n6. Go to the next room\n7. Go back to the livingroom\n8. Take care of your injuries")
               userinput = input(">")
               if userinput == "1":
                    print("""The first thing you see when you enter the room is the huge bed in the middle of the room. So without a doubt you just stepped into the bedroom.
On the bed you see a purple pyjama with white outlines and some flower printings on it, laying. 
At the head of the bed there are two little cupboards and on the opposite side you have a huge closet with a mirror on one door. 
Looking at the closet, makes you remember all these bad \"Coming out\" jokes. 
On the wall is a huge picture from two girls embracing each other and the letters \"citrus\" are written below""")
               elif userinput == "2":
                    print("""Like the couch, the bed looks even more comfortable and welcoming. Since you came all the way here, why not take a short rest in the bed.
The matress is so comfortable and soft. It gives you the feeling like you are floating in the air. Makes it even harder to get up again.""")
               elif userinput == "3":
                    print("""You pull the slide with the mirror to the side and take a look into the closet.
Its filled with lots of clothes. On the right side you have some jackets and blazer hanging that look really cool.
On the side to you left you see alot of tops and t-shirts but also pants and jeans. Looks like the owner of the house is pretty much into fashion.""")
               elif userinput == "4":
                    print("There is a pyjama laying next to the bed. You take it and slowly putting it on.\nWhile doing this you noticed something is falling out of the pyjama to the floor. As you look closer, its a little Key.\n You received the cupboardkey!")
                    items["cupboardkey"] = True
               elif userinput == "5":
                    if items["galaxy"] == True:
                         print("There is nothing more interesting here.")
                    else:
                         print("You open the upper drawer of the cupboard. Inside you find a smartphone. While you take a closer look at it, you see its an Samsung Galaxy S6 Edge.\n What will you do?\n1. Take it!\n2. Leave it, its not yours after all")
                         userinput = input(">")
                         if userinput == "1":
                              print("You received a Galaxy S6 Edge. Very Edgy!")
                              items["galaxy"] = True
                         elif userinput == "2":
                              print("You decided to not steal other peoples property. Karma +100!")
                         else:
                              print("This is not a valid option.")
               elif userinput == "6":
                    balcony_house(items)
               elif userinput == "7":
                    livingroom_house(items)
               elif userinput == "8":
                    items["injury"] = False
                    items["filled_bottle"] = False
                    items["firstaidkit"] = False
                    print("""First you take the plastic bottle with water and wash the wound properly so you dont get anything in your wound.
Then you use the desinfection liquid. Once you finised you slowly and carefully wrapping the bandage around your arm and fix it at the end. You immedietly feel better already.""")
               else:
                    print("This is not a valid option.")


     else:
          options = ["1", "2", "3", "4", "5", "6"]
          userinput = ""
          while userinput not in options or 1 or 2 or 3 or 4:
               print("Your options are:\n1. Look around\n2. Lay on the bed\n3. Open closet\n4. Put on the Pjyama\n5. Open the drawer of the cupboard\n6. Go to the next room\n7. Go back to the livingroom")
               userinput = input(">")
               if userinput == "1":
                    print("""The first thing you see when you enter the room is the huge bed in the middle of the room. So without a doubt you just stepped into the bedroom.
On the bed you see a purple pyjama with white outlines and some flower printings on it, laying. 
At the head of the bed there are two little cupboards and on the opposite side you have a huge closet with a mirror on one door. 
Looking at the closet, makes you remember all these bad \"Coming out\" jokes. 
On the wall is a huge picture from two girls embracing each other and the letters \"citrus\" are written below""")
               elif userinput == "2":
                    print("""Like the couch, the bed looks even more comfortable and welcoming. Since you came all the way here, why not take a short rest in the bed.
The matress is so comfortable and soft. It gives you the feeling like you are floating in the air. Makes it even harder to get up again.""")
               elif userinput == "3":
                    print("""You pull the slide with the mirror to the side and take a look into the closet.
Its filled with lots of clothes. ON the right side you have some jackets and blazer hanging that look really cool.
On the side to you left you see alot of tops and t-shirts but also pants and jeans. Looks like the owner of the house is pretty much into fashion.""")
               elif userinput == "4":
                    print("There is a pyjama laying next to the bed. You take it and slowly putting it on.\nWhile doing this you noticed something is falling out of the pyjama to the floor. As you look closer, its a little Key.\nYou received the cupboardkey!")
                    items["cupboardkey"] = True
               elif userinput == "5":
                    if items["galaxy"] == True:
                         print("There is nothing more interesting here.")
                    else:
                         print("You open the upper drawer of the cupboard. Inside you find a smartphone. While you take a closer look at it, you see its an Samsung Galaxy S6 Edge.\nWhat will you do?\n1. Take it!\n2. Leave it, its not yours after all")
                         userinput = input(">")
                         if userinput == "1":
                              print("You received a Galaxy S6 Edge. Very Edgy!")
                              items["galaxy"] = True
                         elif userinput == "2":
                              print("You decided to not steal other peoples property. Karma +100!")
                         else:
                              print("This is not a valid option.")
               elif userinput == "6":
                    balcony_house(items)
               elif userinput == "7":
                    livingroom_house(items)
               else:
                    print("This is not a valid option.")

#### THE HOUSE BALCONY ####
#### THE HOUSE BALCONY ####
#### THE HOUSE BALCONY ####   

def balcony_house(items):
     print("\nThe Balcony\n")
     if items["filled_bottle"] == True and items["firstaidkit"] == True:
          options = ["1", "2", "3", "4", "5"]
          userinput = ""
          while userinput not in options or 1:
               print("Your options are:\n1. Look around\n2. Try to use the phone\n3. Jump off the balcony\n4. Go back to the bedroom\n5. Take care of your injuries")
               userinput = input(">")
               if userinput == "1":
                    print("""\nYou step outside on the balcony. Its not very huge but still very nice. There are two seats made out of wooden.
You take a step forward to the railing. This gives you and nice overview of the island. You notice that the island isnt that big after all.
Maybe the whole island is some kind of private island that belongs to a very rich person who is only here from time to time for some vacation.
Spending time here must be pretty neat, if the circumstances would have been different. \n""")
               elif userinput == "2":
                    if items["galaxy"] == True:
                         print("You take the phone and push the ON button for some seconds. But nothing happens.\n")
                    else:
                         print("Which phone you wanna try to use? You dont have a phone with you.\n")
               elif userinput == "3":
                    print("Why would you do this?")
               elif userinput == "4":
                    bedroom_house(items)
               elif userinput == "5":
                    items["injury"] = False
                    items["filled_bottle"] = False
                    items["firstaidkit"] = False
                    print("""First you take the plastic bottle with water and wash the wound properly so you dont get anything in your wound.
Then you use the desinfection liquid. Once you finised you slowly and carefully wrapping the bandage around your arm and fix it at the end. You immedietly feel better already.""")
               else:
                    print("This is not a valid option.")    

     else:
          options = ["1", "2", "3", "4"]
          userinput = ""
          while userinput not in options or 1:
               print("Your options are:\n1. Look around\n2. Try to use the phone\n3. Jump off the balcony\n4. Go back to the bedroom")
               userinput = input(">")
               if userinput == "1":
                    print("""\nYou step outside on the balcony. Its not very huge but still very nice. There are two seats made out of wooden.
You take a step forward to the railing. This gives you and nice overview of the island. You notice that the island isnt that big after all.
Maybe the whole island is some kind of private island that belongs to a very rich person who is only here from time to time for some vacation.
Spending time here must be pretty neat, if the circumstances would have been different.\n""")
               elif userinput == "2":
                    if items["galaxy"] == True:
                         print("You take the phone and push the ON button for some seconds. But nothing happens.\n")
                    else:
                         print("Which phone you wanna try to use? You dont have a phone with you.")
               elif userinput == "3":
                    print("Why would you do this?")
               elif userinput == "4":
                    bedroom_house(items)
               else:
                    print("This is not a valid option.")