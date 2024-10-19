# from item import Item
#Getters and Setters
# item1 = Item('TV', 750, 0)
# item1.name = 'Television'

# print(item1.read_only_name)

# item1.read_only_name = 'BBB'
# item1.name = 'OtherItem'
# print(item1.name)

#Abstract
# item1 = Item('MyItem', 750, 6)
# item1.send_email()

# from phone import Phone
# item1 = Phone('Ip14prm', 1000, 3)
# item1.send_email()


#Change all value --> Refactor --> doi 1 chu cung 1 luc


class Hero:
    # all = []
    damage = 10000
    # def __init__(self, name: str, weapon: str, color: str):
    #     self.name = name
    #     self.weapon = weapon
    #     self.color = color
        #self.damage = damage

        # Hero.all.append(self)
    def __init__(self, ho, ten):
        self.ho = ho 
        self.ten = ten
        # self.email = ho + ten + '@gmail.com'
    @property #change method to thuoc tinh --> no ()
    def ho_ten(self):
        return'{}{}'.format(self.ho, self.ten)
    @property
    def email(self):
        return self.ho + self.ten + '@gmail.com'
    @ho_ten.setter
    def ho_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.name = ten_moi
    @ho_ten.deleter
    def ho_ten(self):
        self.ho = None
        self.ten = None
        print('Deleted')

#Special method
    # def __str__(self):
    #     return f"{self.__class__.__name__}, {self.name}, {self.weapon}, {self.color}"
    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.weapon}, {self.color}"
    #--> hai method same, if both --> uu tien str then rerp, str just give value, repr give all value 

    def __len__(self):
        return len(self.name)
    @staticmethod #--> the same as nothing --> co cung duoc khong cung duoc
    def say_hello(self):
        return 'Hello, I am ' + self.name
    
    @classmethod #--> tao method de bao toan tinh dung dan cua du lieu --> optimization
    def damage_update(cls, update_damage):
        cls.damage = update_damage
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        name, weapon, color = new_lst
        return cls(name, weapon, color)
    

hero3 = Hero('Tran', 'Tommy')

hero3.ho_ten = 'Nguyen Tommy' #--> error --> setter
# hero3.ho = 'Nguyen'
# hero3.ten = 'Huy'

# print(hero3.ho)
# print(hero3.ten)
# print(hero3.email()) #--> ho ten change but email not change --> write email method
# print(hero3.email) #after user @property
# print(hero3.ho_ten())
print(hero3.ho_ten)
del hero3.ho_ten
print(hero3.ho_ten)

# info_str = "Tommy - sword - navy"
# hero2 = Hero.from_string(info_str)

# print(hero2.__dict__)

# hero1 = Hero('Super Hero', 'Gun','Red')

# print('Hero 1 name is: ', hero1.name)
# print('Hero 1 weapon is: ', hero1.weapon)
# print('Hero 1 color is: ', hero1.color)
# print('Hero 1 damage is: ', hero1.damage)
# print(hero1.say_hello())

# Hero.damage = 9000 #--> change all damage value
# hero1.damage = 9000 #--> change hero1 damage value
# print(hero1.damage)
# print(Hero.damage)

# print(Hero.damage)
# Hero.damage_update(15000)#== hero1.damage_update(15000)
# print(Hero.damage)

# class Superhero(Hero):
#     def __init__(self, name: str, weapon: str, color: str):
#         super().__init__(name, weapon, color)#inherit all functions in father class


# Superhero1 = Superhero('TM', 'Gun', 'Blue')
# print(Superhero1.damage)
# # print(Superhero1.__dict__)
# print(Superhero1.all)
# print(Superhero1.__len__())# 2 --> #len name above in len function