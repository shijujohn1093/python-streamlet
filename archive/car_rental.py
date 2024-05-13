# car_rental.py
import datetime

class CarRental:
    def __init__(self, stock=10):
        self.stock = stock
        self.rentalTime = None
        self.rentalBasis = None
        self.carsRented = 0

    def display_stock(self):
        print(f"Total cars available for rent: {self.stock}")
        return self.stock
    

    def rent_for(self, n, frequency):
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry, only {self.stock} cars available to rent.")
            return None
        else:
            self.rentalTime = datetime.datetime.now()
            self.rentalBasis = frequency
            self.carsRented = n
            self.stock -= n
            print(f"You have rented {n} car(s) on an {frequency} basis today at {self.rentalTime}.")
            return self.rentalTime
        
    def rent_hourly(self, n):
        self.rent_for(self, n,'hourly')

    def rent_daily(self, n):
        self.rent_for(self, n,'daily')
        # Similar to rent_hourly, change the basis to 'daily'

    def rent_weekly(self, n):
        self.rent_for(self, n,'weekly')
        # Similar to rent_hourly, change the basis to 'weekly'

    def return_car(self, request):
        rentalTime, rentalBasis, numOfCars = request
        if not all([rentalTime, rentalBasis, numOfCars]):
            print("Rental details are missing.")
            return None

        bill = 0
        now = datetime.datetime.now()
        rentalPeriod = now - rentalTime

        # Calculate bill based on the rental basis (hourly/daily/weekly)

        self.stock += numOfCars
        print(f"Thanks for returning your car(s). Hope you enjoyed our service!")
        print(f"Total bill: ${bill}")
        return bill


class Customer:
    def __init__(self):
        self.rental = None
        self.rent_type = None
        self.rentalTime = None
        self.numOfCars = 0

    def request_car(self, rental_system, num_cars, rental_type):
        """Request a number of cars for rent from the rental system based on a rental type."""
        if rental_type not in ['hourly', 'daily', 'weekly']:
            print("Invalid rental type. Please choose hourly, daily, or weekly.")
            return

        if num_cars <= 0:
            print("Number of cars must be greater than zero.")
            return

        if rental_system.stock < num_cars:
            print(f"Sorry, only {rental_system.stock} cars available to rent.")
            return

        self.rent_type = rental_type
        self.numOfCars = num_cars

        # Perform the rental operation based on the rental type
        if rental_type == 'hourly':
            self.rentalTime = rental_system.rent_hourly(num_cars)
        elif rental_type == 'daily':
            self.rentalTime = rental_system.rent_daily(num_cars)
        elif rental_type == 'weekly':
            self.rentalTime = rental_system.rent_weekly(num_cars)

        if self.rentalTime:
            print(f"You have successfully rented {num_cars} car(s) on a {rental_type} basis.")

    def return_car(self, rental_system):
        """Return the cars and handle billing through the rental system."""
        if not self.rentalTime:
            print("You have no cars to return. Please rent a car first.")
            return

        request = (self.rentalTime, self.rent_type, self.numOfCars)
        bill = rental_system.return_car(request)
        if bill:
            print(f"Thank you for returning your car(s). Your total bill is ${bill:.2f}.")
        # Reset the customer state
        self.rental = None
        self.rent_type = None
        self.rentalTime = None
        self.numOfCars = 0
