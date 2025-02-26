class Book:
    def __init__(self, title:str, author:str,year:int,publisher:str,price:float):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.price = price


    def display(self):
        print(f"{self.title} by {self.author}\npublished by {self.publisher} in {self.year}\nRetail Price: U$$ {self.price}")

b1=Book("The Alchemist","Paulo Coelho",1988,"HarperCollins",25.99)
b1.display()
b2=Book("The Da Vinci Code","Dan Brown",2003,"Doubleday",19.99)   
b2.display()