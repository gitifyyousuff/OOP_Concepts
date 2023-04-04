class Item:
    def __init__(self,name,price,qnty) :
        self.name = name
        self.price = price
        self.qnty = qnty
    
    def calc(self,count):
        # self.count = count
        return self.price * count
    
item1 = Item('phone',400,5)
print(item1.qnty)