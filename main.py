from place import Place
from player import Player
from item import Item

class Game():
    def __init__(self):
        main_room = Place("Lobby",10)
        self.current_place = main_room 
        
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        front_garden = Place("Front garden", 20)
        home = Place('Home', 10)
        downstairs_hallway = Place("Downstairs Hallway", 10)
        living_room = Place("Living room", 12)
        stairs = Place("Stairs", 4)
        bedroom = Place('Bedroom', 5)
        bathroom = Place('Bathroom', 4, True) # bathroom is locked
        attic = Place("Attic",5)
        master_bedroom = Place("Master bedroom", 15, True)
        kitchen = Place("Kitchen", 10)
        garden = Place('Garden', 15)
        shed = Place('Shed', 3)
        upstairs = Place("Upstairs", 5)
        cave = Place('Cave', 50)
    

        home.add_next_place(front_garden)
        home.add_next_place(downstairs_hallway)
        front_garden.add_next_place(home)
        downstairs_hallway.add_next_place(living_room)
        downstairs_hallway.add_next_place(stairs)
        downstairs_hallway.add_next_place(kitchen)
        kitchen.add_next_place(garden)
        garden.add_next_place(shed)
        stairs.add_next_place(bedroom)
        stairs.add_next_place(master_bedroom)
        stairs.add_next_place(bathroom)
        master_bedroom.add_next_place(attic)
   
        # etc. 
        
        # items
        hammer = Item('Hammer',"tool")
        pen = Item('Pen',"tool")

        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        name = input("Enter player name: ")
        player1 = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
etc.      
""")
        if opt == "1":
            self.current_place.choose_next_place(self)
                

            
            pass
        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass
            
game1 = Game()
game1.setup()
game1.start()