import heapq


class SeatManager:
    def __init__(self, n):    
        self.seats = list(range(1, n + 1))

    def reserve(self):
        reserved_seat = heapq.heappop(self.seats)
        return reserved_seat

    def unreserve(self, seat_number):
        heapq.heappush(self.seats, seat_number) # Add the seat back to available seats.
