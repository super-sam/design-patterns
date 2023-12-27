# Library Management System
Design Patterns Used
- Factory design pattern
- Delegation design pattern
- Observer design pattern

## Requirements
1. The system should be able to store info about
    - books
    - members of library
    - log of book borroed
2. Every book should have 
    - uid
    - meta (rack_number) to help locate the book
3. Every book should have info:
    - ISBN
    - Author
    - Title
    - Subject
    - Publication Date
4. Can have multiple copies of book. Each copy is book item
5. User Types:
    - librarian
    - members
6. Each user must have library card with UID
7. One member can issue max 10 books
8. The menece can issue a book for max 15 days
9. Each book item can only be reserved by a single member
10. Record 
    - who issused which book item
    - when was a book item issued
11. Renew the reserved book
12. Send notification if book isn't returned within duedate
13. Check for availability of the book
14. Search book by
    - title
    - author
    - subject
    - publication data
   
