# Class Diagram

## Seat
```mermaid
classDiagram
class Seat{
    <<Abstract>>
    - seat_no: str
    - status: SeatStatus

    + is_available() bool
    + set_status() void
    + set_rate() void
}

class Gold{
    - rate: double
    + set_seat() void
    + set_status void
}
class Silver{
    - rate: double
    + set_seat() void
    + set_status void
}
class Platinum{
    - rate: double
    + set_seat() void
    + set_status void
}

Seat <|-- Silver: Extends
Seat <|-- Platinum: Extends
Seat <|-- Gold: Extends
```

## Show Time
```mermaid
classDiagram
class ShowTime{
    - show_id: str
    - start_time: datetime
    - date: datetime
    - duration: int
    - seats: List~Seat~

    + get_avaialble_seats() List~Seat~

}
```
## Hall
```mermaid
classDiagram
class Hall{
    - hall_id: int
    - shows: List~ShowTime~
}
```

## Cinemas
```mermaid
classDiagram
class Cinema{
    - cinema_id: int
    - halls: List<Hall>
    - city: str
}
```

## City
```mermaid
classDiagram
class City{
    - name: str
    - state: str
    - pincode: int
    - cinemas: List~Cinema~
}
```

## Movie
```mermaid
classDiagram
class Movie{
    - title: string
    - genere: string
    - release_date: datetime
    - language: string
    - duration: int
    - shows: List~ShowTime~
}

```
## Movie Ticket

```mermaid
classDiagram
class MovieTicket{
    - ticket_id: int
    - movie: Movie
    - show_time: ShowTime
    - seats: List~Seat~
}
```

## Payment
```mermaid
classDiagram
class Payment{
    <<Abstract>>
    - amount: double
    - status: PaymentStatus
    - timestamp: datetime
    + make_payment() bool
}

class CreditCard{
    - name_on_card: str
    - card_number: str
    - code: int
    - billing_address: Address
    + make_payment() bool
}

class Cash{
    + make_payment() bool
}

Payment <|-- CreditCard: Extends
Payment <|-- Cash: Extends
```
## Person
```mermaid
classDiagram
class Person{
    - name: str
    - address: Address
    - email: str
    - phone: str
}
class Customer{
    - bookings: List~Booking~
    + create_booking(booking): bool
    + update_booking(booking): bool
    + cancel_booking(booking): bool
}
class TicketAgent{
    + create_booking(booking): bool
}
class Admin

Person <|-- Customer: Extends
Person <|-- TicketAgent: Extends
Person <|-- Admin: Extends
```

## Booking
```mermaid
classDiagram
class Booking{
    - booking_id: str
    - amount: str
    - total_seats: int
    - status: BookingStatus
    - payment: Payment
    - tickets: MovieTicket
    - show: ShowTime
}
```

## Enums
```mermaid
classDiagram
class BookingStatus{
    <<enum>>
    Pending
    Confirmed
    Cancelled
    Denied
    Refunded
}

class SeatStatus{
    <<enum>>
    Avaialble
    Booked
    Reserved
}

class PaymentStatus{
    <<enum>>
    Pending
    Confirmed
    Declined
    Refunded
}
```

## Relationship

### Association
```mermaid
classDiagram

City --> Cinema: has
Customer -- Booking
Booking -- Payment
Booking --> Seat
Booking --> ShowTime
Movie --> MovieTicket
MovieTicket --> Seat
ShowTime --> Seat
```

### Composition
```mermaid
classDiagram
Cinema *-- Hall: Composed Of
Hall *-- ShowTime

```

### Aggregation
```mermaid
classDiagram
Movie --o Catalog: Contains
```

### Generalisation
```mermaid
classDiagram
Catalog --|> Search
```









