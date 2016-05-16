# Product Inventory Class

# manages an inventory of products.
# keeps track of various products and can sum up the inventory value.

class Product(object):

    def __init__(self, price, ID, quantity):
        self.price = price
        self.id = ID
        self.quantity = quantity


class Inventory(object):
    
    def __init__(self, products):   # products arg must be taken as list []
        self.products = products
        self.value = 0

    def print_inv(self):
        for i in range(0, len(self.products)):
            item = self.products[i]
            print (str(i+1)+".", item.id, "$"+str(item.price), "x"+str(item.quantity))

    def add_to_inv(self, item):
        self.products.append(item)

    def inv_sum(self):
        sum_ = 0
        for product in self.products:
            sum_ += product.price * product.quantity
        print ("TOTAL INVENTORY VALUE\n", "[$"+str(sum_)+"]")
