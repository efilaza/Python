# 3η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_1.py
# Υποεργασία 1
# Εισαγωγή στον Αντικειμενοστρεφή Προγραμματισμό

class Stack():

    def  __init__(self):
        # Ερώτημα (α) Costructor
        self.stuck = []
    
    def push(self,item):
        # Eρώτημα (β) Προσθήκη αντικειμένου
        if item not in self.stuck:
            self.stuck.append(item)
            return True
        else:
            print("Το αντικείμενο υπάρχει ήδη στην στοίβα.")
            return False
    
    def pop(self):
        # Ερώτημα (γ) Διαγραφή αντικειμένου
        if len(self.stuck) == 0:
            print("Δεν υπάρχει αντικείμενο στη στοίβα προς απομάκρυνση.")
        else:
            last = self.stuck[-1]
            self.stuck.pop()
            print(f"Το στοιχείο {last} απωθήθηκε από τη στοίβα.")
       
    def  __str__(self):
        # Ερώτημα (δ) Εκτύπωση στοίβας
        return '->\t' + "\n\t".join(reversed(self.stuck))


class Control():
    s = Stack() # Δημιουργία στοίβας και ανάθεσή της στη μεταβλητή s
    while True:
        # Menu επιλογών και κλήση των αντίστοιχων μεθόδων επί του
        # στιγμιότυπου s
        r = input('+item για ώθηση, - για απώθηση, ? για παρουσίαση, x για έξοδο:')
        if r[0] == 'x': break
        if r[0] == '+' and len(r.strip()) > 1: s.push(r.strip()[1:])
        if r[0] == '-' : s.pop()
        if r[0] == '?' : print(s)

c = Control()
