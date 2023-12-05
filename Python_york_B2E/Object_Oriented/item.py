import csv

class Item: 
    all = []
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):  #these are attributes
        # run validations to the received arguments
        assert price >=0,  f"Price {price} is not greater than zero"
        assert quantity >=0, f"Price {quantity} is not greater than zero"

        #assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to excute
        Item.all.append(self)
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Object_Oriented/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that point zero i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.__class__.__name__}', {self.price}, {self.quantity})"
    