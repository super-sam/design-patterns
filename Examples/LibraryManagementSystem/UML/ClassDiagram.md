# Class Diagram
Contents
- [Classes](#classes)
- [Enumerations](#enumerations)
- [Custom Datatypes](#custom-datatype)
- [Relations](#relation-between-the-classes)
    - [Association](#association)
        - [One Way](#one-way)
        - [Two Way](#two-way)
    - [Composition](#composition)
    - [Aggregation](#aggregation)


## Classes
### Books
**Requirements 3, 4**

```mermaid
classDiagram

class Book{
    <<Abstract>>
    - ISBN: string
    - title: string
    - subject: string
    - publicationDate: date
    - language: string
    - pages: int
    - format: BookFormat
    - authors: Author
}
class BookItem{
    - isReferenceOnly: bool
    - borrowed: date
    - dueDate: date
    - price: double
    - status: BookStatus
    - dateOfPurchase: date
    - placedAt: Rack
    + checkout(string memberid): bool
}

Book <|-- BookItem: Extends

```

```mermaid

classDiagram
note "Requirements 2"
class Rack{
    -number: int
    - locationIdentifier: string
}
```
### Person & Author
```mermaid
classDiagram
class Person{
    - name: string
    - address: Address
    - email: string
    - phone: string
}
class Author{
    - books: list
}
Person <|-- Author: Extends
```

### Users: Librarian & Members
**Requirements: 5, 11**
```mermaid
classDiagram

class User{
    <<Abstract>>
    - id: string
    - password: string
    - status: AccountStatus
    - person: Person
    + resetPassword() bool
}
class Member{
 - dateOfMembership: date
 - totalBooksCheckedout: int
 + getTotalBooksCheckout() int
 + reserveBookItem(BookItem bookItem) bool
 + incrementCheckoutBookItem() void
 + returnBookItem(BookItem bookItem) bool
 + renewBookItem(BookItem bookItem) bool
 + checkForFine(string bookItemId) void
}
class Librarian{
    + addBookItem(BookItem bookItem) bool
    + blockMember(Member member) bool
    + unBlockMember(Member member) bool 
}

User <|-- Member: extends
User <|-- Librarian: extends
```

### Library Card
```mermaid
classDiagram

class LibraryCard{
    - cardNumber: string
    - issueDate: date
    - active: bool
    + isActive(): bool
}
```

### Book Reservation
```mermaid
classDiagram

class BookReservation{
    - itemId: string
    - creationDate: date
    - status: ReservationStatus
    - memberId: string

    + getStatus(): BookReservation
    + fetchReservationDetails(BookItem book) BookReservation
}

```

### Book Lending
```mermaid
classDiagram

class BookLending{
    - itemId: string
    - creationDate: date
    - dueDate: date
    - returnDate: date
    - memberId: string

    + lendBook(BookItem book, string memberId) void
    + fetchLendingDetails(BookItem book) BookLending
    + getReturnDate() date
}

```

### Notification
**Requirements**
- 12

```mermaid
classDiagram
class Notification{
    <<Abstract>>
    - notificationId: string
    - created: date
    - content: string
    + sendNotification() bool

}

class PostalNotification{
    - address: Address
}

class EmailNotification{
    - email: string
}

Notification <|-- PostalNotification: Extends
Notification <|-- EmailNotification: Extends
```

### Search & Catalog

```mermaid
classDiagram
class Search{
    <<interface>>
    + searchByTitle(string title)
    + searchByAuthor(string author)
    + searchBySubject(string subject)
    + searchByPubDate(date publishDate)
}
class Catalog{
    - bookTitles: List~string~
    - bookAuthors: List~Author~
    - bookSubjects: List~string~
    - bookPublicationDates: List~date~

    + searchByTitle(string query)
    + searchByAuthor(string query)
    + searchBySubject(string query)
    + searchByPubDate(string query)
}
Search <|-- Catalog: Implements
```

### Library
```mermaid
classDiagram
class Library{
    - name: string
    - address: Address
    + getAddress() Address
}
```

## Enumerations
```mermaid
classDiagram
class BookFormat{
    Hardcover
    Paperback
    AudioBook
    Ebook
    Newspaper
    Magazine
    Journal
}

class AccountStatus{
    Active
    Closed
    Canceled
    Blacklisted
    None
}

class ReservationStatus{
    Waiting
    Pending
    Canceled
    None
}

class BookStatus {
    Available
    Reserved
    Loaned
    Lost
}

```

## Custom Datatype
```mermaid
classDiagram
class Address{
    - street: string
    - city: string
    - state: string
    - pincode: string
    - country: string
}

```

## Relation between the classes
### Association
#### One-Way
```mermaid
classDiagram
direction LR
class User{
    <<Abstract>>

}
User --> BookReservation
User --> BookItem
BookReservation --> BookItem
BookItem <-- BookLending
```

#### Two-Way
```mermaid
classDiagram
direction LR
class User{
    <<Abstract>>

}
class Notification{
    <<Abstract>>

}

class Book{
    <<Abstract>>
}

Librarian -- BookItem
BookItem -- Rack

Notification -- BookLending
Notification -- BookReservation
BookLending -- User
BookLending -- BookReservation

Book -- Author
```

### Composition
```mermaid
classDiagram

LibraryCard --* User
BookItem --* Library

```
### Aggregation
```mermaid
classDiagram
Book --o Catalog
```

### Inheritance
