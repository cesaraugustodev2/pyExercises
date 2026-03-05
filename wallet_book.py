class Wallet:
    refund_count = 0

    def __init__(self):
        self.balance = 0.0

    def add_funds(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print("Amount to add must be positive.")

    def remove_funds(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def get_balance(self) -> float:
        return self.balance

    @classmethod
    def add_refund(cls):
        cls.refund_count += 1

    @classmethod
    def check_refund(cls):
        print(f"Total refunds: {cls.refund_count}")


class Book:
    def __init__(self, title: str, author: str, year: int, price: float):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.wallet = Wallet()

    def new_order(self, qty: int):
        total_price = self.price * qty
        self.wallet.add_funds(total_price)
        print(f"Order placed: {qty} copies of '{self.title}'. Total: R$ {total_price:.2f}")

    def check_wallet(self):
        print(f"Current wallet balance for '{self.title}': R$ {self.wallet.get_balance():.2f}")

    def refund(self):
        if self.wallet.remove_funds(self.price):
            Wallet.add_refund()
            print(f"Refund processed for '{self.title}'.")
        else:
            print(f"Refund failed for '{self.title}': Insufficient funds in wallet.")


if __name__ == "__main__":
    # Example usage:
    my_book = Book("Python Basics", "John Doe", 2023, 50.0)
    my_book.new_order(2)
    my_book.check_wallet()
    my_book.refund()
    my_book.check_wallet()
    Wallet.check_refund()
