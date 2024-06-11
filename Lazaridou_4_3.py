import sqlite3  # Χρήση της βιβλιοθήκης sqlite3

file = 'library.db'
try:
    connection = sqlite3.connect(file)
except FileNotFoundError:
    print("Το αρχείο δεν βρέθηκε")
    exit()
except sqlite3.Error as e:
    print("Σφάλμα εισαγωγής στοιχείων.")
    exit()

cursor = connection.cursor()

def print_tuple(tup):
    for i in range(len(tup)):
        print(f'{tup[i]:^10}',end = '\t')
    print()

def show_records(table):  # Συνάρτηση προβολής των εγγραφών του πίνακα table
    # Ερώτημα (query) για την προβολή των εγγραφών ενός πίνακα
    try:
        sql = f"SELECT * from {table}"
        # Υποερώτημα α
        cursor.execute((sql))
        names = [description[0] for description in cursor.description]
        if table == 'students':
            for name in names:
                print(f"{name:^10} ",end = '\t')
            print()
            print("_" * 33)
            for record in cursor.fetchall():
                print_tuple(record)
            print()
        elif table == 'books':
            for name in names:
                print(f" {name:^18}",end="")
            print()
            print("_" * 70)
            for record in cursor.fetchall():
                print_tuple(record)
            print()
        elif table == 'lending':
            print(f'{names[0]:^10}  {names[1]:^10}  {names[2]:^10} \t\t\t{names[3]:^10} {names[4]:^10}')
            print("_" * 70)
            for record in cursor.fetchall():
                print_tuple(record)
            print()
    except sqlite3.Error as e:
        print(e)
def insert_student(name, surname):  # Συνάρτηση εισαγωγής φοιτητή
    try:
        sql = "INSERT INTO students(name,surname) VALUES (?,?)"  # Ερώτημα (query) για την εισαγωγή του ονόματος (name) και επώνυμου (surname) του νέου μαθητή στον πίνακα students
        # Υποερώτημα β
        cursor.execute((sql),(name,surname))
        connection.commit()
    except sqlite3.Error as e:
        print("Σφάλμα εισαγωγής",e)

def delete_student(code):  # Συνάρτηση διαγραφής φοιτητή
    try:
        sql = "DELETE FROM students WHERE id==(?)"  # Ερώτημα (query) για τη διαγραφή του μαθητή βάση του κωδικού του από τον πίνακα students
        # Υποερώτημα γ
        cursor.execute((sql), (code,))
        if cursor.rowcount == 0:
            print("Ο μαθητής δεν βρέθηκε")
        connection.commit()
    except sqlite3.Error as e:
        print("Σφάλμα διαγραφής",ε)
# Κυρίως πρόγραμμα

# Συμβολοσειρά με τις επιλογές του μενού
library_menu = '''Επιλογές συστήματος:  
1) Προβολή μαθητών
2) Προβολή βιβλίων
3) Προβολή δανεισμών 
4) Καταχώρηση μαθητή
5) Διαγραφή μαθητή
6) Έξοδος
Η επιλογή σας: '''

# Κεντρικό μενού της εφαρμογής
while True:
    entry = input(library_menu)  # Εισαγωγή επιλογής μενού
    if entry == '1':
        show_records('students')  # Χρήση της συνάρτησης show_records για τον πίνακα students
    elif entry == '2':
        show_records('books')  # Χρήση της συνάρτησης show_records για τον πίνακα books
    elif entry == '3':
        show_records('lending')  # Χρήση της συνάρτησης show_records για τον πίνακα lending
    elif entry == '4':
        on = input("Καταχώρησε το όνομα του μαθητή: \n")
        ep = input("Καταχώρησε το επώνυμο του μαθητή: \n")
        insert_student(on, ep)  # Χρήση της συνάρτησης insert_student
    elif entry == '5':
        student_code = input("Καταχώρησε τον κωδικό του μαθητή προς διαγραφή: \n")
        delete_student(student_code)  # Χρήση της συνάρτησης delete_student
    elif entry == '6':
        connection.close()
        break
    else:
        print(
            "Λανθασμένη επιλογή. Παρακαλώ επιλέξετε 1 έως 6 \n")  # Μήνυμα λάθους σε περίπτωση λανθασμένης επιλογής menu
