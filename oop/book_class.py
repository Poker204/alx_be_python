class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance with title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method that is called when a Book instance is deleted.
        It prints the message: "Deleting (title of the book)".
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method to return a user-friendly string description of the book.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation method to return a string that would recreate the Book instance.
        Format: "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
