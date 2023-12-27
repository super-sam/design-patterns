# User is an abstract class
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, isbn, title, subject, publisher, language, number_of_pages, book_format):
        self.__isbn = isbn
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pages
        self.__book_format = book_format
        self.__authors = []


class BookItem(Book):
    def __init__(self, id, is_reference_only, borrowed, due_date, price, status, date_of_purchase, publication_date, placed_at):
        self.__id = id
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__status = status
        self.__date_of_purchase = date_of_purchase
        self.__publication_date = publication_date
        self.__placed_at = placed_at

    def checkout(self, member_id):
        None
    def set_added_by(self, librarian):
        None
    def set_added_by(self, librarian):
        None


class Rack:
    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier
        self.__book_items = []
    def add_book_item(self, book_item):
        None