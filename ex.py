class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_tuple = (id, movie_name, time)
        self.__show_list.append(show_tuple)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            return "Invalid show ID"
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                return f"Invalid seat: ({row}, {col})"
            
            if self.__seats[id][row][col] == 1:
                return f"Seat ({row}, {col}) is already booked"
        
        # If all checks pass, book the seats
        for row, col in seat_list:
            self.__seats[id][row][col] = 1
        
        return "Seats booked successfully!"

    def view_show_list(self):
        show_info = "Shows running:\n"
        for show in self.__show_list:
            show_info += f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}\n"
        return show_info

    def view_available_seats(self, id):
        if id not in self.__seats:
            return "Invalid show ID"
        
        seats_info = f"Available seats for show {id}:\n"
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0:
                    seats_info += f"({i}, {j}) "
            seats_info += "\n"
        return seats_info

# Replica system for the counter
def main():
    hall = Hall(5, 5, 1)
    
    while True:
        print("\n1. View all shows")
        print("2. View available seats")
        print("3. Book tickets")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(hall.view_show_list())
        
        elif choice == '2':
            id = input("Enter show ID: ")
            result = hall.view_available_seats(id)
            print(result)
        
        elif choice == '3':
            id = input("Enter show ID: ")
            num_seats = int(input("Enter number of seats to book: "))
            seat_list = []
            for _ in range(num_seats):
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                seat_list.append((row, col))
            
            result = hall.book_seats(id, seat_list)
            print(result)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()