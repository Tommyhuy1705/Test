#INHERITANCE
from Python_study.item import Item

class Phone(Item): #--> Class phone inherit from Item
    def __init__(self, name: str, price: float, quantity: float, broken_phones = 0):
        #Call to super function to have access to all attributes/ methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"
        
        #assign yo self object 
        self.broken_phones = broken_phones

phone1 = Phone('Ip14', 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone('Ip15', 700, 5, 1)

print(Phone.all)
print(Item.all)
#--> deu in ra item(...) --> do __rerp__ chua phan class name