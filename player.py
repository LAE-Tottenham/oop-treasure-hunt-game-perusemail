class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_limit = 50
        self.inventory = []
        self.balance = 10
        # add more atributes as needed

    def add_item(self, item):
        if self.calculate_inventory_size() < self.inventory_limit:
            self.inventory.append(item)
            print(f"{item.name} has been added to your inventory.")
        else:
            print("Your inventory is full! You can't add more items.")
    
    def calculate_inventory_size(self):
        # Instead of adding up items, return the length of the inventory list
        return len(self.inventory)

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        # add more code here

    # add more methods as needed
