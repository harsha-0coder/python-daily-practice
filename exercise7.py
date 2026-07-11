# E-Commerce

class Product:
    def __init__(self,name, price, stock):
        self.name = name
        self.price = price
        self.quantity = stock

    def buy(self,quantity):
        if quantity > self.quantity:
            print(f"{self.name} is not available in {quantity} ")
            return
        else:
           self.quantity -= quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"the {self.name} is available in the number of {self.quantity}")

    def show(self):
        print("==============Product Details==================")
        print(f"Product Name       : {self.name}\n"
              f"Price              :  {self.price}\n"
              f"Quantity Available : {self.quantity}")
        

if __name__ == "__main__":
    products =[]
    number = int(input("Enter the number of Product\n"))
    if number < 0:
        print("invalid number")
        
    else:

        for i in range(number):
            name = input("Enter Product name\n").lower()
            price = int(input("Enter Price\n"))
            stock = int(input("Enter Available Quantity\n"))
            product = Product(name,price,stock)
            products.append(product)
        

        for i in products:
           product.show()

        choice = input("want to buy? (yes/no)\n").lower()
        if choice == "yes":
            nu = input("Enter Product name\n").lower()
            for nu in products:
                if nu in products:
                   qua = int(input("Enter the quantity\n"))
                   product.buy(qua)
                   print("Thank you for purchasing")

                else:
                   print("Product is not available")
        for i in products:
           product.show()

    
    
    
