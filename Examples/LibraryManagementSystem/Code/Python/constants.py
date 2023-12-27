from enum import Enum, auto

class BookFormat(Enum):
    HARDCOVER = auto()
    PAPERBACK = auto()
    AUDIOBOOK = auto()
    EBOOK = auto()
    NEWSPAPER = auto()
    MAGAZINE = auto()
    JOURNAL = auto()

class AccountStatus(Enum):
    ACTIVE = auto()
    CLOSED = auto()
    CANCELED = auto()
    BLACKLISTED = auto()
    NONESTATUS = auto()

class ReservationStatus(Enum):
    WAITING = auto()
    PENDING = auto()
    CANCELED = auto()
    NONESTATUS = auto()

class BookStatus(Enum):
    AVAILABLE = auto()
    RESERVED = auto()
    LOANED = auto()
    LOST = auto()