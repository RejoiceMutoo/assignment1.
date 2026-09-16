class BankAccount:

  def __init__(self, owner, initial_balance=0.0):
    self.owner = owner
    # Private attribute using double underscores
    self.__balance = initial_balance if initial_balance >= 0 else 0.0

  def deposit(self, amount):
    """Deposit money if the amount is positive."""
    if amount > 0:
      self.__balance += amount
      print(f"Deposited: ${amount:.2f}")
    else:
      print("Deposit amount must be positive.")

  def withdraw(self, amount):
    """Withdraw money if there are sufficient funds and amount is valid."""
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"Withdrawn: ${amount:.2f}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
    """Display the current account balance."""
    print(f"Account Balance for {self.owner}: ${self.__balance:.2f}")
    return self.__balance


# --- Demonstration ---
# Create an account
my_account = BankAccount("Alice", 100.0)

# Display initial balance
my_account.display_balance()

# Deposit and withdraw using controlled methods
my_account.deposit(50.0)
my_account.withdraw(30.0)

# Attempting to modify or access __balance directly from outside will fail
try:
  print(my_account.__balance)
except AttributeError as e:
  print(f"\nDirect access blocked: {e}")

# Python uses name mangling, so it can technically be accessed via _BankAccount__balance,
# but encapsulation relies on convention and controlled methods to protect data integrity.
