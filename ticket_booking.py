class Hall:
    def __init__(self, movie_name, total_tickets, ticket_price):
        self.movie_name = movie_name
        self.total_tickets = total_tickets
        self.ticket_price = ticket_price
        self.available_seats = list(range(1, total_tickets + 1))
   
    def calculate_ticket_price(self, number_of_tickets):
        return number_of_tickets * self.ticket_price
   
    def check_seat_availability(self, number_of_tickets):
        return len(self.available_seats) >= number_of_tickets
   
    def get_seat_numbers(self):
        return self.available_seats
   
    def book_ticket(self, number_of_tickets):
        if self.check_seat_availability(number_of_tickets):
            booked_seats = self.available_seats[:number_of_tickets]
            self.available_seats = self.available_seats[number_of_tickets:]
            return booked_seats
        else:
            return []

    def cancel_ticket(self, seat_numbers):
        self.available_seats.extend(seat_numbers)
        self.available_seats.sort()





class Multiplex:
    def __init__(self, number_of_halls, address):
        self.number_of_halls = number_of_halls
        self.address = address
        self.halls = []

    def add_hall(self, hall):
        self.halls.append(hall)

    def find_hall_by_movie_name(self, movie_name):
        for hall in self.halls:
            if hall.movie_name == movie_name:
                return hall
        return None






if __name__ == "__main__":
    # MULTIPLEX WITH 3 HALLS
    multiplex = Multiplex(number_of_halls=2, address="Kalyani CENTER PARK")

    # Add halls to the multiplex
    hall1 = Hall(movie_name="Movie1", total_tickets=50, ticket_price=10)
    hall2 = Hall(movie_name="Movie2", total_tickets=60, ticket_price=12)
    hall3 = Hall(movie_name="Movie3", total_tickets=40, ticket_price=8)
    multiplex.add_hall(hall1)
    multiplex.add_hall(hall2)
    multiplex.add_hall(hall3)

    while True:
        print("\n..........................MOVIE TICKET BOOKING SYSTEM...........................")
        print("1. Book Tickets")
        print("2. Cancel your Ticket")
        print("3. Exit from page")
        choice = input("Enter your choice: ")

        if choice == "1":
            movie_name = input("Enter movie name: ")
            hall = multiplex.find_hall_by_movie_name(movie_name)
            if hall:
                number_of_tickets = int(input("Enter the number of tickets to book: "))
                if hall.check_seat_availability(number_of_tickets):
                    booked_seats = hall.book_ticket(number_of_tickets)
                    if booked_seats:
                        total_price = hall.calculate_ticket_price(number_of_tickets)
                        print(f"Tickets booked successfully! Your seat numbers are: {booked_seats}")
                        print(f"Total Price: ${total_price}")
                    else:
                        print("Sorry, requested number of tickets are not available.")
                else:
                    print("Sorry, requested number of tickets are not available.")
            else:
                print("Movie not found in the multiplex.")

        elif choice == "2":
            movie_name = input("Enter movie name: ")
            hall = multiplex.find_hall_by_movie_name(movie_name)
            if hall:
                seat_numbers_str = input("Enter the seat numbers to cancel (comma-separated): ")
                seat_numbers = [int(seat) for seat in seat_numbers_str.split(",")]
                hall.cancel_ticket(seat_numbers)
                print("Tickets canceled successfully.")
            else:
                print("Movie not found in the multiplex.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")