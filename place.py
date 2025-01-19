class Place():
    def __init__(self, given_name, given_size, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.size = given_size
        self.locked = locked
        self.next_places = []
        self.items = []
        # add more atributes as needed

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        (self.items).append(item_instance)

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            # remember that next_places is a list of Place instances hence why we can use place.name
            print(place.name)

    def number_of_next_places(self):
        return len(self.next_places)

    def choose_next_place_1(self, game):
        print("hello")

    def choose_next_place(self, game):
        print("\nHere is where you can go: ")
        index = 1
        for place in self.next_places:
            print(f"{index}. {place.name}")
            index += 1

        choice = input("\nWhere would you like to go? (Enter a number): ")
        if choice.isdigit():
            option = int(choice) - 1
            if 0 <= option < len(self.next_places):
                next_place = self.next_places[option]

                if next_place.locked:  # Check if the place is locked
                    print(f"\n{next_place.name} is locked. You need a key to enter.")

                    has_key = False
                    for item in game.current_player.inventory:
                        if item.type == "key" and item.name == "Bedroom Key":  # Check for specific key
                            has_key = True
                            print("You have the Bedroom Key in your inventory!")
                            use_key = input(f"Do you want to use the key to unlock {next_place.name}? (yes/no): ").strip().lower()
                            if use_key == "yes":
                                next_place.locked = False  # Unlock the place
                                print(f"{next_place.name} is now unlocked. You can enter!")
                                game.current_place = next_place
                            else:
                                print("You chose not to unlock the room.")
                            break

                    if not has_key:
                        print("You do not have the correct key in your inventory.")
                else:
                    game.current_place = next_place  # Move to the unlocked place
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Please enter a valid number.")
