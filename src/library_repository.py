from abc import ABC, abstractmethod


class LibraryRepository(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int): pass

    @abstractmethod
    def remove_book(self, title: str) -> bool: pass

    @abstractmethod
    def get_all_books(self) -> list: pass


class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self.books = {}

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = {"author": author, "year": year}

    def remove_book(self, title: str) -> bool:
        return self.books.pop(title, None) is not None

    def get_all_books(self) -> list:
        return [{"title": title, "author": data["author"], "year": data["year"]} for title, data in self.books.items()]