from abc import ABC, abstractmethod
from Examples.LibraryManagementSystem.Code.Python.constants import AccountStatus
import customdata
import constants

from datetime import datetime

class User(ABC):
    def __init__(self, id, password, person: customdata.Person, card=None, status=constants.AccountStatus.ACTIVE) -> None:
        self.__id = id
        self.__password = password
        self.__person = person
        self.__status = status
        self.__card = card
    
    @abstractmethod
    def reset_password(self):
        pass

class Librarian(User):
    def __init__(self, id, password, person: customdata.Person, status=constants.AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
    
    def add_book_item(self, book_item):
        book_item.set_added_by(self)
    
    def block_member(self, member):
        None
    
    def unblock_member(self, member):
        None
    
    def reset_password(self):
        pass

class Member(User):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)
    self.__date_of_membership = datetime.date.today()
    self.__total_books_checked_out = 0

  def reserve_book_item(self, book_item):
    None

  def increment_total_books_checked_out(self):
    None

  def checkout_book_item(self, book_item):
    None

  def check_for_fine(self, book_item_barcode):
    None

  def return_book_item(self, book_item):
    None

  def renew_book_item(self, book_item):
    None
    
  def reset_password(self):
    pass