class Book():
    def __init__(self,title:str,author:str,year:int,price:float):
        self.title=title
        self.author=author
        self.year=year
        self.price=price
        self.wallet=0
        print(f"\n{self.title} by {self.author} was created with retail price: U$$ {self.price}\n")
        
    def new_order(self,qty:int):
        try:
            if qty<=0:
             raise ValueError
            print("**New Order**")
            print(f"{qty} {'copy' if qty==1 else 'copies'} of {self.title} was sold!\n{self.price*qty} was added to wallet\n")
            self.wallet+=self.price*qty
        except ValueError:
             print("New Order Error Value must be positive\n")
          
    def check_wallet(self):
     print("**Opening wallet**")
     print(f"Wallet Total U$$ {self.wallet}\n")
    def refund(self):
     print(f"Refund of {self.title} requested")
     try:
         if self.wallet<=0:
             raise ValueError
         self.wallet-=self.price
         print(f"{self.price} was removed from wallet")
         print(f"Wallet total: U$$ {self.wallet:.2f}")
     except ValueError:
        print(f"Wallet empty can´t proccess refund")
         

lotr = Book("Lord of the Rings", "J.R.R. Tolkien", 1954, 24.99)
lotr.new_order(2)
lotr.new_order(1)
lotr.new_order(-1)
lotr.check_wallet()
lotr.refund()
