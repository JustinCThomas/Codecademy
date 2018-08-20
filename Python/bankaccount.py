class BankAccount(object):
  balance = 0
  
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "This account belongs to %s. The current account balance is $%.2f." % (self.name, self.balance)
  
  def show_balance(self):
     print("The current account balance is $%.2f" % ( self.balance))
      
  def deposit(self, amount):
    if amount <= 0:
      print("You can only deposit amounts greater than $0.00")
      return
    else:
      print("Depositing $%.2f into the account" % amount)
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount > self.balance:
      print("You can withdraw at MOST: $%.2f" % self.balance)
      return
    else:
      print("You are withdrawing $%.2f from the account." % amount)
      self.balance -= amount
      self.show_balance()
      
  
my_account = BankAccount("George")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)

