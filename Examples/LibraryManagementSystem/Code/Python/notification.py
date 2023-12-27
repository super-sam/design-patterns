# User is an abstract class
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, notification_id, creation_date, content):
        self.__notification_id = notification_id
        self.__creation_date = creation_date
        self.__content = content
        self.__book_lending = None
        self.__book_reservation = None

    def send_notification(self):
        None

class PostalNotification(Notification):
    def __init__(self, notification_id, creation_date, content, address):
        super().__init__(notification_id, creation_date, content)
        self.__address = address

class EmailNotification(Notification):
    def __init__(self, notification_id, creation_date, content, email):
        super().__init__(notification_id, creation_date, content)
        self.__email = email