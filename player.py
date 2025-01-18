class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_limit = 50
        self.inventory = []
        self.balance = 10
        # add more atributes as needed

    def calculate_inventory_size(self):
        x = 0
        for counter in self.inventory:
            x += counter
        return x
    
    def add_item(self, item_instance):
        if self.calculate_inventory_size() < self.inventory_limit:
            self.inventory.append(item_instance)
            print("\n"f"{item_instance.name} has been added to your inventory.")
        else:
            print("\nYour inventory is full!")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        # add more code here

    # add more methods as needed
