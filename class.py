class Wallet:
    def __init__(self):
        self.balance = 0

    def add_funds(self, amount: float):
        self.balance += amount

    def remove_funds(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
        
class Book:
    def __init__(self, title: str, author: str, year: int, price: float):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.wallet = Wallet()
        print(f"\n{self.title} by {self.author} was created with retail price: U$$ {self.price}\n")
        
    def new_order(self, qty: int):
        try:
            if qty <= 0:
                raise ValueError
            print("**New Order**")
            total = self.price * qty
            self.wallet.add_funds(total)
            print(f"{qty} {'copy' if qty == 1 else 'copies'} of {self.title} was sold!")
            print(f"{total} was added to wallet\n")
        except ValueError:
            print("New Order Error: Value must be positive\n")
          
    def check_wallet(self):
        print("**Opening wallet**")
        print(f"Wallet Total U$$ {self.wallet.get_balance():.2f}\n")

    def refund(self):
        print(f"Refund of {self.title} requested")
        if self.wallet.remove_funds(self.price):
            print(f"{self.price} was removed from wallet")
            print(f"Wallet total: U$$ {self.wallet.get_balance():.2f}")
        else:
            print("Wallet empty, can't process refund")         

lotr = Book("Lord of the Rings", "J.R.R. Tolkien", 1954, 24.99)
lotr.new_order(2)
lotr.new_order(1)
lotr.new_order(-1)
lotr.check_wallet()
lotr.refund()
