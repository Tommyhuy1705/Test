import csv

class Item:
    pay_rate = 0.8 #The pay rate after discount 20%
    all = []
    #pay_ rate co phan cap lon hon cac def
    #magic methods
    def __init__(self, name: str, price: float, quantity: float):
        #Run validation to the received arguments
        #use assert as a statement not a function --> check the value --> print AssertError
        assert price >= 0,f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        
        #assign yo self object 
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)
        #--> pick objects to the list all


        # print('I am created!')# --> print 2 lan vi co 2 function item
        # I am created!
        # I am created!
        # print(f"An instance created: {name} + cost about {price}")
    
    @property
    #Property Decorator = Read - only attribute
    def name(self):
        return self.__name
    #--> if no setter --> name just be read not set
    @name.setter
    def name(self, value):
        #Here you can do anything to get and set
        #print("You are the best")
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value # allow to get set new value for name



    def calculate_total_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate#explain for item 1
        self.price = self.price * self.pay_rate#explain for item 2

    #CSV : comma separated values
    # @classmethod
    # def instantiate_from_csv(cls):
    #     with open('items.csv', 'r') as f:
    #         reader = csv.DictReader(f)
    #         items = list(reader)

    #     for item in items:
    #         #print(item)
    #         Item(
    #             name = item.get('name'),
    #             price = float(item.get('price')),
    #             quantity =int(item.get('quantity')),
    #         )

    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        #For i.3: 5.0, 10.0
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    
    #__repr__: kiem soat cach the hien cua objects
    def __repr__(self):
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    #--> no se phan ten lop va in ra   

#__ de chuyen doi phuong thuc thanh private
    def __connect(self, smpt_server):
        pass
    def __prepare_body(self):
        return f"""
        Hello someone.
        We have {self.name} {self.quantity} times.
        Regards, Tommy
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    # @property
    # def read_only_name(self):
    #     return 'AAA'
 
# print(Item.is_integer(7.0))#True
# print(Item.is_integer(7.5))#False

# Item.instantiate_from_csv()
# print(Item.all)
# item1 = Item('Phone', 500, 50)
# item1.apply_discount()#item 1 still read pay_rate from Item
# print(item1.price)

# item2 = Item('Laptop', 1000, 100)
# item2.pay_rate = 0.7# item 2 find the pay_rate in instance level
# item2.apply_discount()
# print(item2.price)

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)
#print(Item.all) #--> 5 elements


# for instance in Item.all:
#     print(instance.name)

# print(item1.name, item1.price, item1.quantity)
# print(item2.name, item2.price, item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

#Tinh phan cap cac lop
# print(Item.pay_rate)#0.8
# print(item1.pay_rate)#0.8 --> because item 1 can not access to their value like price,... so it wants to extract value from class

#Check the attributes
# print(Item.__dict__)#All the attributes for Class level
# print(item1.__dict__)#All the attributes for Instance level