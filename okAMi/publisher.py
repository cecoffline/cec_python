class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, n_o_page):
        super().__init__(name, title, author)
        self.price = price
        self.n_o_page = n_o_page

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Pages:", self.n_o_page)

pub_name = input("Enter publisher name: ")
book_title = input("Enter book title: ")
book_author = input("Enter author name: ")
price = float(input("Enter price: "))
pages = int(input("Enter number of pages: "))

p = Python(pub_name, book_title, book_author, price, pages)

print("\n--- BOOK DETAILS ---")
p.display()
