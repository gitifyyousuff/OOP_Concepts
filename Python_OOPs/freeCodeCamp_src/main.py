# import csv

# class Item:
#     pay_rate = 0.8 # pay after 20% of discount
#     all = []
#     def __init__(self,name:str,prc:float,qnty) :
#         #run validations to the received args
#         assert prc >= 0, f'prc {prc} is not greater than or equal to 0'
#         assert qnty >= 0
#         # print(f'Instance created:{name}')
#         #assign to self object
#         self.name = name
#         self.prc = prc
#         self.qnty = qnty

#         #action to execute
#         Item.all.append(self)

#     def calc(self):
#         return self.prc*self.qnty

#     def apply_discnt(self):
#         self.prc =  self.prc*self.pay_rate

   
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.prc},{self.qnty})"
    
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open(r'D:\Python_OOPs\freeCodeCamp_src\Items.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)   
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 prc = float(item.get('prc')),
#                 qnty = int(item.get('qnty'))
#             )
#     @staticmethod
#     def is_integer(num):
#         #we will count the floats that are point zero
#         #for eg:5.0
#         if isinstance(num,float):#isinstance is python build-in fucntion
#             #count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num,int):
#             return True
#         else:
#             return False


# Item.instantiate_from_csv()
# print(Item.is_integer(7.0))

# item1 = Item("phone",100,1)
# item1.nm = 'phone'
# item1.prc = 100
# item1.qnty = 5
# print(item1.calc(item1.prc,item1.qnty))
# item1.apply_discnt()
# print(item1.prc)


# item2 = Item('Laptop',300,7)
# item2.pay_rate = 0.7
# item2.apply_discnt()
# print(item2.prc)
# item2.nm = 'Laptop'
# item2.prc = 80
# item2.qnty = 5
# print(item2.calc(item2.prc,item2.qnty))

# print(item1.calc())
# print(item1.name)
# print(item2.name)
# print(item1.prc)
# print(item2.prc)
# print(item1.qnty)
# print(item2.qnty)
# print(Item.pay_rate)
# print(item1.pay_rate)

# print(Item.__dict__) #all the attributes on class level
# print(item1.__dict__) #all the attributes on instance level

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)




#Class Inheritance
# class Phone(Item):
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
#         # Call to super function to have access to all attributes / methods
#         super().__init__(
#             name, price, quantity
#         )

#         # Run validations to the received arguments
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

#         # Assign to self object
#         self.broken_phones = broken_phones

# phone1 = Phone("jscPhonev10", 500, 5, 1)

# print(phone1.broken_phones)
# print(Item.all)
# print(Phone.all)
# phone1 = Phone("jscPhonev10", 500, 5)
# print(phone1.calc())
# phone2 = Phone("jscPhonev30", 700, 5)
# phone2.broken_phones = 1
# print(phone2)

# from items import Item


# item1 = Item("MyItem", 750)

# # Setting an Attribute
# item1.name = "OtherItem"

# item1.apply_increment(0.2)
# # item1.pay_rate =0.8
# item1.apply_discount()
# # Getting an Attribute
# print(item1.price)

# from phone import Phone

# p1 = Phone('nokia',100,4)
# p1.apply_discount()
# print(p1.price)

from keyboard import Keyboard
from phone import Phone
# from items import Item

p1 = Keyboard('nokia',100,4)
p2 = Phone('Htc',100,7)
'''polymorphism property starts - since pay rate is different for 
phone and keyboard. Accordingly apply_discount() method 
provides result wrt pay rate of Keyboard and Phone class'''
p1.apply_discount()
p2.apply_discount()
#polymorphism property ends
print(p1.price)
print(p2.price)
print(p2.calculate_total_price())
print(p1.all)
print(p2.all)
# Item.instantiate_from_csv()