import random

class RailwayReservation:
    def __init__(self):
        self.users = {}
        self.trains = {}
        self.bookings = {}

    def generate_pnr(self):
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))

    def create_account(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        return username in self.users and self.users[username] == password

    def add_train(self, train_name, source, destination):
        self.trains[train_name] = {
            'source': source,
            'destination': destination
        }

    def make_reservation(self, username, train_name, passenger_details):
        if train_name not in self.trains:
            return None

        pnr = self.generate_pnr()
        self.bookings[pnr] = {
            'username': username,
            'train_name': train_name,
            'passenger_details': passenger_details
        }
        return pnr

    def get_booking_details(self, pnr):
        return self.bookings.get(pnr, None)

if __name__ == "__main__":
    reservation_system = RailwayReservation()

    while True:
        print("\nRailway Reservation System")
        print("1. Create Account")
        print("2. Login")
        print("3. Add Train")
        print("4. Make Reservation")
        print("5. Get Booking Details")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if reservation_system.create_account(username, password):
                print("Account created successfully!")
            else:
                print("Username already exists. Please choose a different username.")
        
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if reservation_system.login(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password.")
        
        elif choice == 3:
            train_name = input("Enter train name: ")
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            reservation_system.add_train(train_name, source, destination)
            print("Train added successfully!")

        elif choice == 4:
            username = input("Enter your username: ")
            if username not in reservation_system.users:
                print("User not found. Please create an account first.")
                continue
            
            train_name = input("Enter train name: ")
            passenger_count = int(input("Enter number of passengers: "))
            passenger_details = []
            for _ in range(passenger_count):
                passenger_name = input("Enter passenger name: ")
                passenger_age = int(input("Enter passenger age: "))
                passenger_details.append({'name': passenger_name, 'age': passenger_age})
            
            pnr = reservation_system.make_reservation(username, train_name, passenger_details)
            if pnr:
                print(f"Reservation successful! Your PNR is: {pnr}")
            else:
                print("Invalid train name. Please add the train first.")
        
        elif choice == 5:
            pnr = input("Enter PNR: ")
            booking_details = reservation_system.get_booking_details(pnr)
            if booking_details:
                print("Booking Details:")
                print(f"Username: {booking_details['username']}")
                print(f"Train Name: {booking_details['train_name']}")
                print("Passenger Details:")
                for passenger in booking_details['passenger_details']:
                    print(f"Name: {passenger['name']}, Age: {passenger['age']}")
            else:
                print("Invalid PNR. Booking not found.")
        
        elif choice == 6:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
