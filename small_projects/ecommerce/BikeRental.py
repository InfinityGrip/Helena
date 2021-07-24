import datetime

class BikeRental:
    def __init__(self, stock=0):
        """construction class that instantiates bike rental shop."""

        self.stock = stock

    def displaystock(self):
        """display bikes currently available for rent in shop."""

        print(f"curently have {self.stock} bikes available.")

        return self.stock

    def rentBikeOnHour(self, n):
        """rents a bike by the hour."""
        pay = 5

        if n <= 0: # checks the input
            print(f"Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print(f"we can't fufill the demand for {n} bikes, maybe try a smaller quantity or try later!")

            return None
        else:
            now = datetime.datetime.now()
            print(f"you are renting {n} bike(s) on an hourly basis.\n"
                  f"your charge will be ${pay} for each bike per hour.\n")

            self.stock -= n
            return now

    def rentBikeOnDaily(self, n):

        """rent bikes on daily basis"""
        pay = 20

        if n <= 0:
            print("number of bikes must be positive")
            return None
        elif n > self.stock:
            print(f"We only have {self.stock} available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"you rented {n} bikes on {now.hour}."
                  f"you will be charged ${pay} for each bike weekly.")
            self.stock -= n

            return now

    def rentBikeOnWeek(self, n):
        """
        rent bikes on weekly basis.
        :param n:
        :return now:
        """

        pay = 60
        if n <= 0:
            print(f"Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print(f"we currently have {self.stock} bikes available")
            return None
        else:
            now = datetime.datetime.now()

            print(f"you have rented {n} bike(s) on a weekly basis."
                  f"you will be charged ${pay} per bike for every week.")

            self.stock -= n

            return now

    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replenish the inventory
        3. Retun a bill
        :param request:
        :return:
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            if (3 <= numOfBikes <= 5):
                print("you are eligible for family rental promotion of 30% discount.")
                bill = bill * 0.7

                return bill


        else:
            print("please rent with us!!")
            return None