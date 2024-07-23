# Movie-Ticket-Booking-System
This is one of my Python Program, using OOPs concept.
I simulate a Multiplex Ticket Booking System using Object-Oriented Programming (OOP) principles. The system should allow customers to book movie tickets sequentially if available.

Class: Multiplex and Hall

Design a class named Multiplex with the following features:

    Number of Halls
    Address
Design a class named Hall with the following features:

    movie_name
    total_tickets
    __list_available_seat_number
    ticket_price
    
Methods:

    __init__(self): Initialize the class instances.
    calculate_ticket_price(self, movie_name, number_of_tickets): Calculate the total price for the
    specified number of tickets and movies.
    check_seat_availability(self, movie_name, number_of_tickets): Check if the specified number of
    tickets are available for the given movie.
    get_seat_numbers(self): Get the list of seat numbers.
    book_ticket(self, movie_name, number_of_tickets): Book tickets for a given movie and number
    of tickets.
    cancel_ticket (self, seat_number)
