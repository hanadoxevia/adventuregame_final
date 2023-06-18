from scenes import *

items = {"plastic_bottle": False, "piece_of_wood": False, "glass_bottle": False, "coconut": False, "firstaidkit": False, "doorkey": False, "food": False, "galaxy": False, "injury": True, "cupboardkey": False, "filled_bottle": False, "eatenfood": False, "charging_cable": False, "charged_phone": False, "open_door": False}

def main():
    print("Welcome to the Survival Game!\nサバイバルゲームへようこそ")
    print("First of all, lets start with entering your name.")
    name = input("My name is ")
    print("\nVery well, " +name+ " let your journey begin.\n")

    print("Beach Startscene\n")
    print("""You wake up and you cant remember where you are or how you got there.
You try to remember what happened but the moment you try, your head starts hurting really bad.
You look around and you notice that you are on a beach. According to the sun its probably early afternoon.
When you take a look at yourself, you noticed that your clothes are damaged and you are injured 
on your left arm and blood keeps dripping out of the wound.\nWhat are you going to do?\n""")      

    beach(items)

if __name__ == "__main__":
    main()