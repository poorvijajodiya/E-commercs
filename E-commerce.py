class Customer:
	def __init__(self,name,email):
		self.name = name
		self.email=email
		self.purchase = []
	def purchase_product(self,product,inventory):
		inventory_dict = inventory.inventory
		if product in inventory_dict:
			if inventory_dict[product]>0:
				self.purchase.append(product)
				inventory_dict[product] -= 1
			else:
				print("Out of stock")
		else:
			print("We don't have that product")
	def print_purchase(self):
		print("The customer has purchased")
		for item in self.purchase:
			print(item.name)
		
class Product:
	def __init__(self,name,price):
		self.name = name
		self.price = price
		
		
class Inventory:
	def __init__(self):
		self.inventory = {}
		
	def add_prod(self,product,quantity):
		if product not in self.inventory:
			self.inventory[product] =quantity
		else:
			self.inventory[product] +=quantity
	
	def print_inventory(self):
		for key,value in self.inventory.items():
			print(key.name+":"+str(value))
			print()
			
customer = Customer("Joe","Joe@gmail.com")
watch = Product("watch","344")
laptop = Product("laptop","543")
inventory = Inventory()
inventory.add_prod(watch,344)
inventory.add_prod(laptop,543)
inventory.print_inventory()
customer.purchase_product(watch,inventory)
customer.purchase_product(laptop,inventory)
inventory.print_inventory()
customer.print_purchase()