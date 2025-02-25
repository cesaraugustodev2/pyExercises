class Wallet:
    """
    A class to represent a wallet.

    Attributes
    ----------
    refund_count : int
        A class variable to count the number of refunds.
    balance : float
        The current balance of the wallet.

    Methods
    -------
    add_funds(amount: float):
        Adds the specified amount to the wallet balance.
    remove_funds(amount: float):
        Removes the specified amount from the wallet balance if sufficient funds are available.
    get_balance():
        Returns the current balance of the wallet.
    add_refund():
        Increments the global refund count.
    check_refund():
        Prints the global refund count.
    """
    refund_count = 0  # Variável de classe para contar reembolsos

    def __init__(self):
        """Initializes the wallet with a balance of 0."""
        self.balance = 0
        self.refund_ammont = 0
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
            self.wallet.add_refund()
            print(f"{self.price} was removed from wallet")
            print(f"Wallet total: U$$ {self.wallet.get_balance():.2f}")
        else:
            print("Wallet empty, can't process refund")         

purse=Wallet()

lotr = Book("Lord of the Rings", "J.R.R. Tolkien", 1954, 24.99)
lotr.new_order(2)
lotr.new_order(1)
lotr.new_order(-1)
lotr.check_wallet()
lotr.refund()
lotr.refund()
lotr.refund()



purse.check_refund()


