class Star_Cinema:
    hall_list=[]
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.row=row
        self.cols=cols
        self.hall_no=hall_no
        super().entry_hall(self)

    def entry_show(self,id,movie_name,time):
        tuple=(id,movie_name,time)
        self.show_list.append(tuple)

        seat = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seat

    def book_seats(self,id,)


    
