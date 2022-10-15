# не понимаю, как исправить ошибку - массив из книг оказывается общим
# для всех библиотек, хотя задаётся как переменная экземпляра, а не класса

import collections


class Book:
    def __init__(self, name, author, year: int):
        self.name = name
        self.author = author
        self.year = year
        

class Library:
    def __init__(self, name, books = []):
        self.name = name
        self.books = books

    def addbook(self, other):
        self.books.append(other.name + other.author)
        name = self.name
        books = self.books
        return Library(name, books)

    def __add__(self, other) -> 'Library':
        return self.addbook(other)

    def compare(self, other):
        return len(self.books) > len(other.books)

    def __gt__(self, other) -> bool:
        return self.compare(other)

    def similar(self, other):
        return collections.Counter(self.books) == collections.Counter(other.books)

    def __eq__(self, other) -> bool:
        return self.similar(other)

    def __str__(self) -> str:
        return f'{self.name} (число книг: {len(self.books)})'
    
    def __repr__(self) -> str:
        return f'Library(name="{self.name}")'
