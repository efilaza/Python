import numpy as np # Χρήση της βιβλιοθήκης numpy
import time as tm # Χρήση της βιβλιοθήκης time

def internalProduct(v1,v2):
    '''Τυπική υλοποίηση εσωτερικού γινομένου διανυσμάτων.'''
    # Υποερώτημα α
    #
    # Υπολογισμός του γινομένου των v1 και v2 με την τυπική 
    # υλοποίηση
    s = 0
    for i in range(len(v1)):
        s += (v1[i] * v2[i])
    return s

def internalProduct_np(v1,v2):
    # Υποερώτημα β
    #
    # Υπολογισμός του γινομένου των v1 και v2 με κλήση της dot() της numpy
    product = np.dot(v1,v2)
    return product


def timeit(mode, rep,v1,v2):
    '''Χρονομέτρηση επαναληπτικού υπολογισμού εσωτερικού γινομένου με την τυπική υλοποίηση'''
    # Αποθήκευση στην μεταβλητή start του χρόνο έναρξης του επαναληπτικού 
    # υπολογισμού με την τυπική υλοποίηση του πολλαπλασιασμού διανυσμάτων

    func = internalProduct if mode == 'τυπιμή υλοποίηση' else internalProduct_np
    start_time = tm.perf_counter()

    # Υποερώτημα γ

    # Επανάληψη πολλές φορές, ώστε η ακρίβεια του ρολογιού να μην επηρεάζει 
    # το αποτέλεσμα
    for _ in range(rep):
        # Κλήση της συνάρτησης, για τον υπολογισμό του γινομένου των v1 και v2
        result =func(v1,v2)

    # Εμφάνιση του αποτελέσματος
    print(f"Το εσωτερικό γινόμενο των δύο διανυσμάτων είναι: {result}")


    # Αποθήκευση στην μεταβλητή finish_time του χρόνου ολοκλήρωσης του 
    # υπολογισμού
    finish_time = tm.perf_counter()
    # Επιστροφή χρονικού διαστήματος 
    return finish_time-start_time

# Κυρίως πρόγραμμα

# Aρχικοποίηση παραμέτρων
random_num_range = 100 # το εύρος των παραγόμενων τυχαίων αριθμών
vector_size = 10000 # το πλήθος των στοιχείων ενός διανύσματος
repetitions = 5000 # ο αριθμός επαναλήψεων του υπολογισμού
# Αρχικοποίηση δύο διανυσμάτων, v1 και v2, με τυχαίους αριθμούς 
v1 = np.random.randint(random_num_range,size=vector_size)
v2 = np.random.randint(random_num_range,size=vector_size)
internalProduct(v1,v2)
internalProduct_np(v1,v2)
# Υποερώτημα δ

# Υπολογισμός και εμφάνιση χρόνων αναμονής
print("Τυπική υλοποίηση")
typical_mode = timeit('τυπική υλοποίηση',repetitions,v1,v2)
print(f"Ο χρόνος επεξεργασίας είναι: {typical_mode}")
print("\nΥλοποίηση με χρήση της numpy")
numpy_mode = timeit('numpy',repetitions,v1,v2)

print(f"Ο χρόνος επεξεργασίας είναι: {numpy_mode}")

# Υπολογισμός και εμφάνιση του λόγου των χρόνων εκτέλεσης
print(f'O λόγος του χρόνου εκτέλεσης της τυπικής υλοποίησης προς την μέθοδο numpy είναι {typical_mode/numpy_mode}')