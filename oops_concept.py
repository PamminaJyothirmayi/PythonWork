#Classes: Classes can be used to bundle related attributes and methods.
class className:
    attributes
    methods



#Special Method: In Python, a special method __init__ is used to assign values to attributes.

class Mobile:
    def __init__(self, model):
        self.model = model







#Instance of Class: Syntax for creating an instance of class looks similar to function call. An instance of class is an Object.

class Mobile:
    def __init__(self, model):
        self.model = model

mobile_obj = Mobile("iPhone 12 Pro")






#Class Object: An object is simply a collection of attributes and methods that act on those data.

class Mobile:
    def __init__(self, model):
        self.model = model
    def make_call(self,number):
        return "calling..{}".format(number)




#Attributes of an Object: Attributes can be set or accessed using . (dot) character.

class Mobile:
    def __init__(self, model):
        self.model = model

obj = Mobile("iPhone 12 Pro")
print(obj.model) # iPhone 12 Pro





#Accessing in Other Methods: We can also access and update attributes in other methods.

class Mobile:
    def __init__(self, model):
        self.model = model

    def get_model(self):
        print(self.model) # iPhone 12 Pro

obj_1 = Mobile("iPhone 12 Pro")
obj_1.get_model()




#Updating Attributes: It is recommended to update attributes through methods.

class Mobile:
    def __init__(self, model):
        self.model = model

    def update_model(self, model):
        self.model = model

obj_1 = Mobile("iPhone 12")
obj_1.update_model("iPhone 12 Pro")
print(obj_1.model) # iPhone 12 Pro



#Accessing Instance Attributes: Instance attributes can only be accessed using instance of class.
class Cart:
  def __init__(self):
      self.items = {'book': 3}
  def display_items(self):
      print(self.items)  # {'book': 3}

a = Cart()
a.display_items()




#Accessing Class Attributes:

class Cart:
   flat_discount = 0
   min_bill = 100
   def __init__(self):
       self.items = {}

print(Cart.min_bill) # 100




#Updating Class Attribute:

class Cart:
   flat_discount = 0
   min_bill = 100
   def print_min_bill(self):
       print(Cart.min_bill) # 200
a = Cart()
b = Cart()
Cart.min_bill = 200
b.print_min_bill() 




#Instance Methods: Instance methods can access all attributes of the instance and have self as a parameter.

class Cart:
   def __init__(self):
       self.items = {}
   def add_item(self, item_name,quantity):
       self.items[item_name] = quantity
   def display_items(self):
       print(self.items) # {'book': 3}

a = Cart()
a.add_item("book", 3)
a.display_items()



#Class Methods: Methods which need access to class attributes but not instance attributes are marked as Class Methods. 
#For class methods, we send cls as a parameter indicating we are passing the class.

class Cart:
   flat_discount = 0
   @classmethod
   def update_flat_discount(cls, new_flat_discount):
       cls.flat_discount = new_flat_discount

Cart.update_flat_discount(25)
print(Cart.flat_discount) # 25





#Static Method: Usually, static methods are used to create utility functions which make more sense to be part of the class.
#@staticmethod decorator marks the method below it as a static method.

class Cart:
   @staticmethod
   def greet():
       print("Have a Great Shopping") # Have a Great Shopping
 
Cart.greet()












#Inheritance

class Product:
    def __init__(self, name):
        self.name = name

    def display_product_details(self):
        print("Product: {}".format(self.name)) # Product: TV
   
       
class ElectronicItem(Product):
    pass

e = ElectronicItem("TV")
e.display_product_details()




#Super Class & Sub Class:

class Product:
   def __init__(self, name):
       self.name = name
   def display_product_details(self):
       print("Product: {}".format(self.name)) # Product: TV

class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

e = ElectronicItem("TV")
e.display_product_details()





#Calling Super Class Method: 
class Product:
    def __init__(self, name):
       self.name = name
    def display_product_details(self):
       print("Product: {}".format(self.name)) # Product: TV

class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months
   
    def display_electronic_product_details(self):
        self.display_product_details()

e = ElectronicItem("TV")
e.display_electronic_product_details()






#Composition
class Product:
    def __init__(self, name):
       self.name = name
       self.deal_price = deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name)) # Product: Milk
           
    def get_deal_price(self):
        return self.deal_price

class GroceryItem(Product):
    pass
   
class Order:
    def __init__(self):
         self.items_in_cart = []
     
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            
milk = GroceryItem("Milk")
order.add_item(milk, 2)
order.display_order_details()




#Overriding Methods:

class Product:
    def __init__(self, name):
        self.name = name

    def display_product_details(self): 
        print("Superclass Method")

class ElectronicItem(Product):
    def display_product_details(self): # same method name as superclass
        print("Subclass Method")
 
e = ElectronicItem("Laptop")
e.display_product_details()
# Output is:Subclass Method




#Accessing Super Class’s Method: 
class Product:
  def __init__(self, name):
      self.name = name
   
  def display_product_details(self):
      print("Product: {}".format(self.name)) # Product: Laptop

class ElectronicItem(Product):
   
  def display_product_details(self):
      super().display_product_details()    
      print("Warranty {} months".format(self.warranty_in_months)) # Warranty 10 months
    
  def set_warranty(self, warranty_in_months):
      self.warranty_in_months = warranty_in_months

e = ElectronicItem("Laptop")
e.set_warranty(10)
e.display_product_details()




#MultiLevel Inheritance: We can also inherit from a subclass. This is called MultiLevel Inheritance.

class Product:
    pass

class ElectronicItem(Product):
    pass

class Laptop(ElectronicItem):
    pass


#Inheritance & Composition:
#Inheritance	            Composition	
#Car is a vehicle	        Car has a Tyre
#Truck is a vehicle	      Order has a product








