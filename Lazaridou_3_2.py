# 3η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_2.py
# Υποεργασία 2
# Κλάσεις και Αντικείμενο

class Student():
    def __init__(self, arithmos_mitroou, name, vathmos):
        # Costructor κλάσης
        self.name = name
        self.am = str(arithmos_mitroou)
        self.vathmos = float(vathmos)

    def __str__(self):
        return f"[{self.am:5s}] {self.name:20s}    {self.vathmos:.1f}"


# --------------------------
class Control():
    theStudents = {}  # μεταβλητή επιπέδου κλάσης, χρήση: Control.theStudents

    def __init__(self):
        # Constructor Κλάσης
        self.run()

    def add_student(self):
        # Προσθήκη αντικειμένου Student

        while True:
            try:
                data = input("Δώσε στοιχεία φοιτητή ΑΜ,ΟΝΟΜΑ,ΒΑΘΜΟΣ (enter για τέλος): ")
                data = tuple(data.split(","))
                am, name, grade = data
                try:
                    grade = float(grade)
                except ValueError:
                    print("Ο βαθμός που δώσετε δεν είναι σωστός.")
                if am.isdigit() and name.isalpha() and 1 <= grade <= 10:
                    break
                else:
                    print('Τα στοιχεία που δώσατε δεν είναι ορθά.')
            except ValueError:
                print("Οι τιμές πρέπει να χωρίζονται με κόμμα.")

        if am in Control.theStudents:
            print(f"Ο φοιτητής με αριθμό μητρώου {am} υπάρχει ήδη.")
            answers = ["Y", "N", "Υ", "Ν"]  # Αγγλικοί και ελληνικοί χαρακτήρες.
            while True:
                try:
                    reply = input(f"Θα θέλατε να αλλάξετε τα στοιχεία του φοιτητή (Y/N):")
                    if reply.upper() in answers:
                        break
                    else:
                        print("Παρακαλώ επιλέξτε Y/N.")
                except ValueError:
                    print("Σφάλμα εισόδου.")
            if reply.upper() == "N" or reply.upper() == "Ν":
                return

            else:
                s = Student(am, name, grade)
                Control.theStudents[am] = s
                print(f"Επιτυχής αντιγραφή φοιτητή, συνολικό πλήθος {len(Control.theStudents)}")
        else:
            s = Student(am, name, grade)
            Control.theStudents[am] = s
            print(f"Προστέθηκε ένας φοιτητής, συνολικό πλήθος {len(Control.theStudents)}")

    def delete_student(self):
        # Διαγραφή αντικειμένου
        while True:
            try:
                am = input("Δώστε ΑΜ φοιτητή προς διαγραφή: ")
                if am not in Control.theStudents:
                    print('Ο ΑΜ που δώσατε δεν αντιστοιχεί σε κάποιο φοιτητή.\nΠροσπαθήστε ξανά.')
                else:
                    break
            except ValueError:
                print("Σφάλμα τιμής. Προσπαθήστε ξανά.")
        del Control.theStudents[am]
        print("O φοιτητής διαγράφηκε.")

    def show_students(self):
        # Προβολή ταξινομημένου λεξικού φοιτητών
        for key in sorted(Control.theStudents):
            print(f"{Control.theStudents[key]}")

    def run(self):
        # Menu διαχείρισης προγράμματος
        while True:
            print('Προσθήκη φοιτητή (+), διαγραφή φοιτητή (x), εμφάνιση φοιτητών (?), <enter> για έξοδο')
            reply = input("...")
            if not reply: break
            if reply == "+":
                self.add_student()
            elif reply == "x":
                self.delete_student()
            elif reply == "?":
                self.show_students()


# --------------------------
if __name__ == "__main__":
    Control()
