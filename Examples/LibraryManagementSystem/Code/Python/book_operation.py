class BookReservation:
    def __init__(self, creation_date, status, item_id, member_id) -> None:
        self.__creation_date = creation_date
        self.__status = status
        self.__item_id = item_id
        self.__member_id = member_id

    def fetch_reservation_details(self, book_item_id):
        pass

class BookLending:
    def __init__(self, creation_date, due_date, book_item_id, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_id = book_item_id
        self.__member_id = member_id
        self.__book_reservation = None
        self.__user = None

    def lend_book(self, item_id, member_id):
        None

    def fetch_lending_details(self, item_id):
        None

class Fine:
    def __init__(self, creation_date, book_item_id, member_id):
        self.__creation_date = creation_date
        self.__book_item_id = book_item_id
        self.member_id = member_id

    def collect_fine(self, member_id, days):
        None


