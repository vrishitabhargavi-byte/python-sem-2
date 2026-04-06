class Product:
  def set_details(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock
  def update_price(self, change):
    self.price = self.price + change
  def update_stock(self, quantity):
    self.stock = self.stock + quantity
  def display(self):
    print("Product Name:", self.name)
    print("Price:", self.price)
    print("Stock:", self.stock)
    print("Stock cost is",self.stock*self.price)
p = Product()
p.set_details("Laptop", 50000, 10)
p.update_price(-5000)
p.update_stock(5)
p.display()