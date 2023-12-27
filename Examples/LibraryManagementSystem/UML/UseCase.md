# Use Case Diagram
## System
Library
## Actors
### Primary
    - Member
    - Librarian
### Secondary
    - System
## UseCase
### Librarian
- Add Book
- Remove Book
- Edit Book
- Register new account
- Cancel Membership
- Register/Update account
- Login/Logout
- Issue Book
- Remove reservation
- Renew book
- Reserve Book
- View account

### Member
- Search catalog
- Cancel membership
- Register/Update account
- Login/Logout
- Checkout book
- Remove reservation
- Renew book
- Reserve Book
- View Account
- Return book

### System
- Overdue notification
- Reservation Available notification
- Reservation canceled notification


## Relation

### Associations
| Librarian | Member | System |
|--|--|--|
| Add book | Search Catalog | Overdue Notidcation
|Remove Book|||
|Edit Book|||


