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
        x= 0
        for place in self.next_places:
            x= x+1
        return 1
    
    def choose_next_place(self, game):
        x = self.number_of_next_places()
        if x ==1:
            for counter in self.next_places:
                print(counter.name)
            game.current_place = (self.next_places[0])
        elif x >1:
            for counter in self.next_places:
                print(counter)
            option = int(input("Where would you like to go? (options 1,2...)"))
            option = option -1
            game.current_place = self.next_places[option]
        print(game.current_place.name)
        
        

    # add more methods as needed
