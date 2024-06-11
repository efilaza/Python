# 3η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_4.py
# Υποεργασία 4
# Κληρονομικότητα και Πολυμορφισμός

class Package():
    def __init__(self, description, destination):
        #Contructor κλάσης
        self.description = description
        self.destination = destination

    def cost(self):
        #Μέθοδος υπολογισμού κόστους
        if self.destination == 'Αθήνα':
            return 1
        elif self.destination == 'Θεσσαλονίκη':
            return 2
        else:
            return 0

    def __str__(self):
        # Εκτύπωση πληροφοριών δέματος
        return f"{self.description}: Προορισμός: {self.destination}, "


 ###### Κλάση Parcel
class Parcel(Package):
    def __init__(self,description,destination,weight):
        #Constructor
        # Overload super-constructor
        Package.__init__(self,description,destination)
        self.weight = weight

    def cost(self):
        # υπερφόρτωση μεθόδου cost υπερκλάσης
        lst = self.weight.split(" ")
        weight = "".join([x for x in lst[1] if not  x.isalpha()])
        return Package.cost(self) + 0.5 * float(weight)

    def __str__(self,invoice = False):
        # υπερφόρτωση μεθόδου  __ str__ υπερκλάσης
        if invoice == False:
            return f" {Package.__str__(self)} Βάρος: {self.weight}."
        else:
            return f"{self.__str__()}, Κόστος: {self.cost():.2f}€"

#### Κλάση Envelope
class Envelope(Package):


    def __init__(self,description,destination,priority):
        # Constructor
        # Overload super-constructor
        Package.__init__(self, description, destination)
        self.priority = priority

    def cost(self):
        # υπερφόρτωση μεθόδου cost υπερκλάσης
        if "1" in self.priority:
            return Package.cost(self) +  0.2*1
        elif "2" in self.priority == 2:
            return Package.cost(self)  +  0.2 * 2
        elif "3" in self.priority:
            return Package.cost(self) + 0.2 * 3

    def __str__(self,invoice = False):
        # υπερφόρτωση μεθόδου  __ str__ υπερκλάσης
        if invoice == False:
            return f" {Package.__str__(self)} Προτεραιότητα:{self.priority}"
        else:
            return f"{self.__str__()}, Κόστος: {self.cost():.2f}€"

#### Κλάση Bulky_Item
class Bulky_Item(Package):
    def __init__(self, description, destination,length,width,height):
        # Constructor
        # Overload super-constructor
        Package.__init__(self, description, destination)
        self.length = length
        self.width = width
        self.height = height

    def cost(self):
        # υπερφόρτωση μεθόδου cost υπερκλάσης
        lst = self.length.split(" ")
        length = float("".join([x for x in lst[2] if not x.isalpha()]))
        lst = self.width.split(" ")
        width = float("".join([x for x in lst[2] if not x.isalpha()]))
        lst = self.height.split(" ")
        heigth = float("".join([x for x in lst[2] if not x.isalpha()]))

        cost = length * width * heigth * 20.0
        return Package.cost(self) + cost

    def __str__(self,invoice = False):
        # υπερφόρτωση μεθόδου  __ str__ υπερκλάσης
        if invoice == False:
            return f" {Package.__str__(self)} Διαστάσεις :{self.length} x {self.width} x {self.height}."
        else:
            return f"{self.__str__()}, Κόστος: {self.cost():.2f}€ "



items = '''Πακέτο1 (Αθήνα, 20kg),
Πακέτο2 (Θεσσαλονίκη, 10kg),
Πακέτο3 (Αθήνα, 30kg),
Πακέτο4 (Αθήνα, 4.5kg),
Φάκελος1 (Θεσσαλονίκη, προτεραιότητα 1),
Φάκελος2 (Θεσσαλονίκη, προτεραιότητα 3),
ΟγκώδεςΑντικείμενο1 (Αθήνα, μήκος 0.7μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο2 (Θεσσαλονίκη, μήκος 1μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο3 (Αθήνα, μήκος 2μ, πλάτος 0.7μ, ύψος 0.7μ),
'''


def filter(txt):
    return txt.replace("(", ",").replace(")", "").split(",")


packages = []
for item in items.split("\n"):
    if 'Πακέτο' in item:
        p = filter(item)
        packages.append(Parcel(*p[:3]))
    elif 'Φάκελος' in item:
        p = filter(item)
        packages.append(Envelope(*p[:3]))
    elif 'ΟγκώδεςΑντικείμενο' in item:
        packages.append(Bulky_Item(*filter(item)[:5]))


## εκτυπώσεις
print('Δελτίο αποστολής')
for p in packages:
    print(p)
print(70 * "_" + "\n\n")

print('Τιμολόγιο')
for p in packages:
    print(p.__str__(invoice=True))
print(f"ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {sum([p.cost() for p in packages]):.2f}€")
print(40 * "_" + "\n\n")
