class Convertor:
  def to_inches(self,inches):
    self.inches=inches
  def to_feet(self):
    self.feet=self.inches/12
  def display(self):
    print("Inches:",self.inches)
    print("Feet:",self.feet)
c=Convertor()
c.to_inches(65)
c.to_feet()
c.display()