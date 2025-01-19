from place import Place
from player import Player
from item import Item

class Game():
    def __init__(self):
        main_room = Place("Lobby", 10)
        self.current_place = main_room
        self.current_player = None
        self.game_finished = False

    def setup(self):
        # Setup the game with places and items
        front_garden = Place("Front garden", 20)
        home = Place("Home", 10)
        downstairs_hallway = Place("Downstairs Hallway", 10)
        living_room = Place("Living room", 12)
        stairs = Place("Stairs", 4)
        bedroom = Place("Bedroom", 5)
        bathroom = Place("Bathroom", 4, True)  # Bathroom is locked
        attic = Place("Attic", 5)
        master_bedroom = Place("Master Bedroom", 15, True)
        kitchen = Place("Kitchen", 10)
        garden = Place("Garden", 15)
        shed = Place("Shed", 3)

        # Connecting places
        home.add_next_place(front_garden)
        front_garden.add_next_place(home)

        home.add_next_place(downstairs_hallway)
        downstairs_hallway.add_next_place(home)

        downstairs_hallway.add_next_place(living_room)
        living_room.add_next_place(downstairs_hallway)

        downstairs_hallway.add_next_place(stairs)
        stairs.add_next_place(downstairs_hallway)

        downstairs_hallway.add_next_place(kitchen)
        kitchen.add_next_place(downstairs_hallway)

        kitchen.add_next_place(garden)
        garden.add_next_place(kitchen)

        garden.add_next_place(shed)
        shed.add_next_place(garden)

        stairs.add_next_place(bedroom)
        bedroom.add_next_place(stairs)

        stairs.add_next_place(master_bedroom)
        master_bedroom.add_next_place(stairs)

        stairs.add_next_place(bathroom)
        bathroom.add_next_place(stairs)

        master_bedroom.add_next_place(attic)
        attic.add_next_place(master_bedroom)

        # Items
        hammer = Item("Hammer", "tool")
        pen = Item("Pen", "tool")
        key_bedroom = Item("Bedroom Key", "key")
        key_masterbedroom = Item("Master Bedroom Key", "key")
        apple = Item("Apple", "food")
        axe = Item("Axe", "tool")

        home.add_item(hammer)
        bedroom.add_item(key_bedroom)
        garden.add_item(key_masterbedroom)

        kitchen.add_item(apple)
        bathroom.add_item(axe)

        self.current_place = home

    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        name = input("Enter player name: ")
        player1 = Player(name)
        self.current_player = player1  # Add this line to assign player1 to current_player

        while not self.game_finished:
            print(f"\nYou are currently in {self.current_place.name}.")
            print("What would you like to do?")
            opt = input(""" 
    1. Go to a place
    2. Pick up item
    3. Check inventory
    4. Quit game
    5. Remove an item from inventory
    Enter your choice: """)

            if opt == "1":
                print("Available places to go:")
                self.current_place.show_next_places()
                self.current_place.choose_next_place(self)
                print(f"You moved to {self.current_place.name}.")
            elif opt == "2":
                if len(self.current_place.items) > 0:
                    print("\nItems available in this place:")
                    index = 1
                    for item in self.current_place.items:
                        print(f"{index}. {item.name}")
                        index += 1

                    choice = input("Which item would you like to pick up? (Enter the number): ")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(self.current_place.items):
                            item = self.current_place.items.pop(choice - 1)
                            player1.add_item(item)
                            print(f"You picked up {item.name}.")
                        else:
                            print("Invalid choice. Please try again.")
                    else:
                        print("Please enter a valid number.")
                else:
                    print("No items to pick up here.")
            elif opt == "3":
                print("Your inventory contains:")
                if player1.inventory:
                    for item in player1.inventory:
                        print(f"- {item.name} ({item.type})")
                else:
                    print("Your inventory is empty.")
            elif opt == "4":
                print("Thanks for playing!")
                self.game_finished = True
            elif opt == "5":
                if player1.inventory:
                    print("\nYour inventory contains:")
                    for i in range(len(player1.inventory)):
                        item = player1.inventory[i]
                        print(f"{i + 1}. {item.name} ({item.type})")

                    choice = input("Which item would you like to remove? (Enter the number): ")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(player1.inventory):
                            removed_item = player1.inventory.pop(choice - 1)
                            print(f"You removed {removed_item.name} from your inventory.")
                        else:
                            print("Invalid choice. Please try again.")
                    else:
                        print("Please enter a valid number.")
                else:
                    print("Your inventory is empty. Nothing to remove.")
            else:
                print("Invalid option. Please try again.")




game1 = Game()
game1.setup()
game1.start()
