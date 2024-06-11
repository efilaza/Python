# 3η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_4.py
# Υποεργασία 3
# Μέθοδοι οριζόμενες από τον χρήστη

from math import sin, cos, sqrt, atan2, radians
import re

data = '''ATH	Athens	37.936389°N 23.947222°E
JTR	Santorini	36.402937°N 23.947222°E
KLX	Kalamata	37.068333°N 22.025556°E
RHO	Rhodes	36.405419°N 28.086192°E
SKG	Thessaloniki	40.519722°N 22.970833°E'''


class Airport():
    '''κλάση αεροδρομίων'''
    airport_dict = {}  # λεξικό που περιέχει ως τιμές τα αντικείμενα της κλάσης

    @staticmethod
    def load_airports():
        for line in data.split('\n'):
            Airport(*line.strip().split("\t"))


    @staticmethod
    def available_airports():
        airport_list = "Διαθέσιμα αεροδρόμια: "
        for air in Airport.airport_dict:
            airport_list += f"{air}, "
        return airport_list.rstrip(", ")

    def __init__(self, code, name, coordinates):
        self.code = code
        self.name = name
        self.coordinates_str = coordinates
        self.coordinates = [float(x[:-2]) for x in coordinates.split()]
        Airport.airport_dict[code] = self

    def __str__(self):
        return f"{self.code}  {self.name}  {self.coordinates_str}"

    def get_distance(self, other):
        '''μέθοδος που υπολογίζει την απόσταση από ένα άλλο αεροδρόμιο'''
        # based on haversine formula https://en.wikipedia.org/wiki/Haversine_formula#cite_note-Gade2010-9
        R = 6373.0  # approximate radius of earth in km
        lat1, lon1 = radians(self.coordinates[0]), radians(self.coordinates[1])
        lat2, lon2 = radians(other.coordinates[0]), radians(other.coordinates[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = R * c
        return d


class Trip():
    # '''Κλάση Ταξιδιού, εκτυπώνει τις αποστάσεις των επί μέρους πτήσεων'''

    def __init__(self, itinerary):
        #Constructor
        self.itinerary = itinerary
        self.airports = itinerary.split('-')
        self.total_distance = 0

    def __str__(self):
        '''επιστρέφει συμβολοσειρά με τη συνολική διαδρομή και τις αποστάσεις των πτήσεων'''
        # ερώτημα (α)
        st = "Υπολογισμός αποστάσεων πτήσης\n"
        for i in range(len(self.airports) - 1):
            st += f'<{Airport.airport_dict[self.airports[i]].name}, ' \
                  f'{Airport.airport_dict[self.airports[i + 1]].name}>  '
            st += f'{Airport.airport_dict[self.airports[i]].get_distance(Airport.airport_dict[self.airports[i + 1]]):.2f} \n'
        st += f"Συνολική απόσταση   {self.total_distance_calc():.2f}"
        return st

    def total_distance_calc(self):
        #Συνάρτηση υπολογισμού της συνολικής απόστασης
        # του συγκεκριμένου ταξιδιού.
        total = 0
        for i in range(len(self.airports) - 1):
            total += Airport.airport_dict[self.airports[i]].get_distance(Airport.airport_dict[self.airports[i + 1]])
        return total


class Menu():
    def __init__(self):
        #Constuctor
        Airport.load_airports()
        while True:
            print("Παρακαλώ εισάγετε δρομολόγιο ως ακολουθία κωδικών αεροδρομίων, πχ. KLX-ATH-RHO-ATH")
            print(Airport.available_airports())
            itinerary = input(">>")
            if not itinerary: break #Εάν το δρομολόγιο είναι κενό -> έξοδος

            ## ερώτημα (β)
            #else:
            while True:
                airports = Airport.airport_dict.keys()
                if  '-' not in itinerary or len([air for air in  itinerary.split('-') if air not in airports]) != 0 :
                        print("Λανθασμένη είσοδος")
                        print("Παρακαλώ εισάγετε δρομολόγιο ως ακολουθία κωδικών αεροδρομίων, πχ. KLX-ATH-RHO-ATH")
                        print(Airport.available_airports())
                        itinerary = input(">>")
                        if not itinerary: exit() # Εάν το δρομολόγιο είναι κενό -> έξοδος

                else:
                    break

            trip = Trip(itinerary)
            print(trip)


if __name__ == "__main__": Menu()
