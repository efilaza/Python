# 2η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_2.py
# Υποεργασία 2
# Πλειάδες, Δομημένος Προγραμματισμός


from math import sin, cos, sqrt, atan2, radians

# ερώτημα (α)
airport_data = """
Alexandroupoli	40.855869°N 25.956264°E
Athens 37.936389°N 23.947222°E
Chania	35.531667°N 24.149722°E
Chios	38.343056°N 26.140556°E
Corfu 39.601944°N 19.911667°E
Heraklion	35.339722°N 25.180278°E
Kalamata	37.068333°N 22.025556°E
Kavala 40.913333°N 24.619167°E
Kefalonia	38.12°N 20.500278°E
Kos	36.793336°N 27.091667°E
Lemnos	39.917072°N 25.236308°E
Mytilene	39.0567°N 26.5994°E
Paros	37.020833°N 25.113056°E
Rhodes	36.405419°N 28.086192°E
Samos	37.6891°N 26.9116°E
Thessaloniki 40.519722°N 22.970833°E
Zakynthos 37.750833°N 20.884167°E"""


# ερώτημα (α)
def process_airports(data):
    # συνάρτηση που διαβάζει τα στοιχεία αεροδρομίων και γεμίζει τη λίστα airports
    airports_list = [airport for airport in (x.strip() for x in data.splitlines()) if airport]
    # το x.strip() είναι για να αφαιρέσει τα άδεια string
    airports = []
    for airport in airports_list:
        if '\t' in airport:
            airport = airport.replace('\t', ' ')  # αντικατάσταση του χαρακτήρα '\t' με κενό
        name, lat, lon = airport.split(' ')  # unpacking
        lat = lat.replace('°N', '')  # αφαίρεση των συμβόλων '°N' και '°E'
        lon = lon.replace('°E', '')
        airports.append((name, float(lat), float(lon)))  # προσθήκη της πλειάδας(name, lat,lon)  στην λίστα airports
    return airports


def distance(lat1, lon1, lat2, lon2):
    # υπολογισμός της απόστασης μεταξύ των γεωγραφικών συντεταγμένων lon1, lat1 και
    # των γεωγραφικών συντεταγμένων lon2, lat2 χρησιμοποιώντας τον τύπο Haversine
    # https://en.wikipedia.org/wiki/Haversine_formula

    R = 6373.0  # ακτίνα της γης σε km
    lat1, lon1 = radians(lat1), radians(lon1)
    lat2, lon2 = radians(lat2), radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


# ερώτημα (β)
def menu():
    # συνάρτηση που παρουσιάζει το μενού επιλογών και χειρίζεται τις
    # απαντήσεις του χρήστη
    while True:
        try:
            print("\nΕπιλέξτε δύο αεροδρόμια i,j για υπολογισμό της απόστασής τους ή 'min' για ελάχιστη απόσταση ή πατήστε 'Enter' για έξοδο: ")
            for count, airport_name in enumerate(process_airports(airport_data), start=1):
                print(count, airport_name[0], end=', ')
                if count % 8 == 0: print("")
            # έλεγχος εισόδου
            string = input("\nΕπιλογή: ")
            if string == 'min' or string == "":
                return string
            else:
                i, j = string.split(',')
                i = int(i)
                j = int(j)
                if i == j:
                    print("Δώσατε την ίδια τιμή! \nΠροσπαθήστε ξανά. ")
                elif (1 > i or i > 17) or (1 > j or j > 17):
                    print("Πρέπει να δώσετε μια τιμή από 1 έως 17.")
                else:
                    return i, j
        except ValueError:
            print("Δεν δώσατε αποδεκτή επιλογή.")
        except Exception as e:
            print(f"Σφάλμα: {e}")


# ερώτημα (γ)
def min_distance(a_list):
    # συνάρτηση που υπολογίζει την ελάχιστη απόσταση μεταξύ των αεροδρομίων της λίστας airports
    min_dis = 6373.0  # # ακτίνα της γης σε km
    for item1 in a_list:
        a1, b1, c1 = item1
        for item2 in a_list:
            if item1 == item2:
                continue
            a2, b2, c2 = item2
            if distance(b1, c1, b2, c2) < min_dis:
                min_dis = distance(b1, c1, b2, c2)
                airport1 = a1
                airport2 = a2
    print(f"\nΗ ελάχιστη απόσταση είναι μεταξύ των αεροδρομίων {airport1} - {airport2}: ({min_dis:.2f}km) ")


# ερώτημα (δ)
### κυρίως πρόγραμμα ###

airports = (process_airports(airport_data))

## επαναληπτική κλήση μενού και διαχείριση απάντησης χρήστη
while True:
    user = menu()

    if isinstance(user, str):  # αν η είσοδος του χρήστη είναι string
        if user == 'min':  # αν είναι η λέξη 'min'
            min_distance(airports)
            print("_" * 90)
        else:  # αν είναι το <enter>
            end_string = "Ολοκληρώθηκε η εκτέλεση του προγράμματος"
            print(f'{end_string:.^90}')
            exit()
    if isinstance(user, tuple):  # αν η είσοδος του χρήστη είναι tuple
        name1, lat1, lon1 = airports[user[0] - 1]
        name2, lat2, lon2 = airports[user[1] - 1]
        dis = distance(lat1, lon1, lat2, lon2)
        print(f"\nΗ απόσταση μεταξύ των αεροδρομίων {name1} και {name2} είναι {dis:.2f}km\n")
        print("_" * 90)
