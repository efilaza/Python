# 2η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_1.py
# Υποεργασία 1
# Λίστες, Δομημένος Προγραμματισμός

import random


def generate_random_floats(n, m, seed=0):
    """συνάρτηση που επιστρέφει λίστα n τυχαίων αριθμών στη διάστημα
    -m, m με σπόρο γεννήτριας ψευδοτυχαίων αριθμών seed (προαιρετικό όρισμα)
    Attributes:
    int n: πλήθος τυχαίων αριθμών
    int m: ευρος τυχαίων αριθμών
    int seed: γεννήτρια τυχαίων αριθμών (Default τιμή : 0)
    """

    random_float_list = []
    if seed == 0:
        random.seed()  # Κλήση της συνάρτησης random.seed() με την  system.time
    else:
        random.seed(seed)
    for _ in range(n):
        random_float_list.append(random.uniform(-m, m))
    return random_float_list


def find_max_gap(a_list):
    """ συνάρτηση  που δέχεται λίστα πραγματικών αριθμών και επιστρέφει τη
     μέγιστη απόσταση μεταξύ τους
     Attributes:
    list a_list:λίστα πραγματικών αριθμών """

    a_list.sort()
    max_gap = 0
    for i in range(len(a_list)):
        if a_list[i] - a_list[i - 1] > max_gap:
            max_gap = a_list[i] - a_list[i - 1]
    return max_gap


def present_list(a_list):
    """Βοηθητική συνάρτηση που τυπώνει τα στοιχεία μιας λίστας
    Αttributes:
    list a_list:λίστα πραγματικών αριθμών"""

    print(f"Η τυχαία λίστα είναι: {(' , '.join(str(i) for i in a_list))}")


def check_input(hint, start = float('-inf')):
    """Βοηθητική συνάρτηση για τον έλεγχο της εισόδου του χρήστη
    Attributes:
    string hint: Μήνυμα εισόδου προς τον χρήστη
    int start: Κατώτερη τιμή, Default τιμή = μείον άπειρο"""

    while True:  # αμυντικός προγραμματισμός
        try:
            user = int(input(f"{hint}: "))
            if user < start:  # Αν user < start προβάλλετε το κατάλληλο μήνυμα
                print(f"O αριθμός πρέπει να είναι μεγαλύτερος από {start}.")
            else:
                break
        except ValueError:
            print("Δεν δώσατε ακέραιο αριθμό. Προσπαθήστε ξανά.")
    return user


### κυρίως πρόγραμμα ###

# Είσοδος αριθμών από τον χρήστη με έλεγχο της εισόδου μέσω της συνάρτησης check_input
n = check_input("Δώστε το πλήθος τυχαίων αριθμών", 1)
m = check_input("Δώστε το εύρος των  τυχαίων αριθμών", 0)
seed = check_input("Δώστε την γεννήτρια των τυχαίων αριθμών")

# δημιουργία λίστας τυχαίων αριθμών
float_list = generate_random_floats(n, m, seed)

# παρουσίαση της λίστας
print("*" * 11 * (len(float_list)))
present_list(float_list)

# υπολογισμός μέγιστης απόστασης
print(f'Η μέγιστη διαφορά ανάμεσα σε δύο διαδοχικές τιμές της λίστας είναι: {find_max_gap(float_list):.3f}')
print("*" * 11 * (len(float_list)))

end_string = "Ολοκληρώθηκε η εκτέλεση του προγράμματος"
print(f'{end_string:.^90}')



