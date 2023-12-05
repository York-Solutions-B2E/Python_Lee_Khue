
from item import Item 

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):  #these are attributes
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # run validations to the received arguments
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than zero"

        #assign to self object
        self.broken_phones = broken_phones