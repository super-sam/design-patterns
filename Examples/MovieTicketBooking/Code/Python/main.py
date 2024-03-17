from enum import Enum
from datetime import datetime, timedelta
from typing import List
import os
from flask import Flask, request, jsonify

class SeatStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2
    RESERVED = 3

class PaymentStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    DECLINED = 3
    REFUNDED = 4

class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    DENIED = 4
    REFUNDED = 5

class Seat:
    def __init__(self, seat_no: str):
        self.__seat_no = seat_no
        self.__status = SeatStatus.AVAILABLE

    def is_available(self) -> bool:
        return self.__status == SeatStatus.AVAILABLE

    def set_status(self, status: SeatStatus):
        self.__status: SeatStatus = status

    def set_rate(self, rate: float):
        self.__rate: float = rate
    
    def __str__(self) -> str:
        return f"Seat No: {self.__seat_no}, Status: {self.__status}, Rate: {self.__rate}"
    
    def __repr__(self) -> str:
        return f"Seat No: {self.__seat_no}, Status: {self.__status}, Rate: {self.__rate}"

class Gold(Seat):
    def __init__(self, seat_no: str, rate: float):
        super().__init__(seat_no)
        self.set_rate(rate)


class Silver(Seat):
    def __init__(self, seat_no: str, rate: float):
        super().__init__(seat_no)
        self.set_rate(rate)


class Platinum(Seat):
    def __init__(self, seat_no: str, rate: float):
        super().__init__(seat_no)
        self.set_rate(rate)


class ShowTime:
    def __init__(self, show_id: str, start_time: datetime, date: datetime, duration: int):
        self.show_id = show_id
        self.start_time = start_time
        self.date = date
        self.duration = duration
        self.seats = []

    def get_available_seats(self) -> List[Seat]:
        return [seat for seat in self.seats if seat.is_available()]
    
    def add_seats(self, seats: List[Seat]):
        self.seats.extend([seat for seat in seats])
    
    def book_seat(self, seat: Seat) -> bool:
        """
        Book a seat with multithread locks with atomicity and timeout of 15 seconds
        """
        pass


class Hall:
    def __init__(self, hall_id: int):
        self.hall_id = hall_id
        self.shows: List[ShowTime] = []
    
    def add_show(self, show: ShowTime):
        self.shows.append(show)

class Cinema:
    def __init__(self, cinema_id: int, halls: List[Hall], city: str):
        self.cinema_id = cinema_id
        self.halls = halls
        self.city = city

class City:
    def __init__(self, name: str, state: str, pincode: int, cinemas: List[Cinema]):
        self.name = name
        self.state = state
        self.pincode = pincode
        self.cinemas = cinemas

class Movie:
    def __init__(self, title: str, genre: str, release_date: datetime, language: str, duration: int):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.language = language
        self.duration = duration
        self.shows: List[ShowTime] = []
    
    def add_show(self, show: ShowTime):
        self.shows.append(show)
    
    def get_shows(self) -> List[ShowTime]:
        return self.shows

class MovieTicket:
    def __init__(self, ticket_id: int, movie: Movie, show_time: ShowTime, seats: List[Seat]):
        self.ticket_id = ticket_id
        self.movie = movie
        self.show_time = show_time
        self.seats = seats

class Payment:
    def __init__(self, amount: float, status: PaymentStatus, timestamp: datetime):
        self.amount = amount
        self.status = status
        self.timestamp = timestamp

    def make_payment(self) -> bool:
        pass

class CreditCard(Payment):
    def __init__(self, amount: float, status: PaymentStatus, timestamp: datetime, name_on_card: str, card_number: str, code: int, billing_address: str):
        super().__init__(amount, status, timestamp)
        self.name_on_card = name_on_card
        self.card_number = card_number
        self.code = code
        self.billing_address = billing_address

    def make_payment(self) -> bool:
        pass

class Cash(Payment):
    def __init__(self, amount: float, status: PaymentStatus, timestamp: datetime):
        super().__init__(amount, status, timestamp)

    def make_payment(self) -> bool:
        pass

class Person:
    def __init__(self, name: str, address: str, email: str, phone: str):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

class Customer(Person):
    def __init__(self, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)
        self.bookings: List['Booking'] = []

    def create_booking(self, booking: 'Booking') -> bool:
        pass

    def update_booking(self, booking: 'Booking') -> bool:
        pass

    def cancel_booking(self, booking: 'Booking') -> bool:
        pass

    def add_booking(self, booking: 'Booking'):
        self.bookings.append(booking)
    
    def get_bookings(self) -> List['Booking']:
        return self.bookings

class TicketAgent(Person):
    def __init__(self, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)

    def create_booking(self, booking: 'Booking') -> bool:
        pass

class Admin(Person):
    def __init__(self, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)

class Booking:
    def __init__(self, booking_id: str, amount: str, total_seats: int, status: BookingStatus, payment: Payment, tickets: MovieTicket, show: ShowTime):
        self.booking_id = booking_id
        self.amount = amount
        self.total_seats = total_seats
        self.status = status
        self.payment = payment
        self.tickets = tickets
        self.show = show

    
def create_app():
    app = Flask(__name__)
    # Create a new city
    city = City("Bangalore", "Karnataka", 560001, [])

    # Create a new cinema
    cinema = Cinema(1, [], "Bangalore")

    # Create a new hall
    hall = Hall(1)

    # Create a new show time
    show = ShowTime("1", datetime.now(), datetime.now(), 120)
    # Create another show time after 2 hours 30 minutes from current time
    show2 = ShowTime("2", datetime.now() + timedelta(hours=2, minutes=30), datetime.now(), 120)

    # Create a new movie
    movie = Movie("The Shawshank Redemption", "Drama", datetime.now(), "English", 120)


    # Create a new customer
    customer = Customer("John Doe", "Bangalore", "supratim.smantray@gmail.com", "1234567890")

    # Create a new ticket agent
    agent = TicketAgent("Jane Doe", "Bangalore", "supratim.smantray@gmail.com", "1234567890")

    # Create a new admin
    admin = Admin("Admin", "Bangalore", "", "")

    movie.add_show(show=show)
    movie.add_show(show=show2)
    seats = [Gold("G1", 100), Silver("S1", 200), Platinum("P1", 300)]
    show.add_seats(seats)

    @app.route("/book", methods=["GET"])
    def book():
        available_seats = movie.get_shows()[0].get_available_seats()
        if len(available_seats) == 0:
            return jsonify({"message": "No seats available for the show"}), 400
        return jsonify({"message": "Seats available for the show"}), 200
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)