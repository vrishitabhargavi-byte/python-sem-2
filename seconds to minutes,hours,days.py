class Time:
  def read(self,seconds):
    self.seconds=seconds
  def to_convert(self):
    self.minutes=self.seconds//60
    self.hours=self.seconds//3600
    self.days=self.seconds//84600
  def display(self):
    print("Hours:",self.hours)
    print("Minutes:",self.minutes)
    print("Days:",self.days)
t=Time()
t.read(86400)
t.to_convert()
t.display()