# 2η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_3.py
# Υποεργασία 3
# Σύνολα, Δομημένος Προγραμματισμός


employees = """Γιώργος Γεωργίου,m,eng,project1 project3 
 Μαρία Ρήγα,f,eng,project2 
 Κατερίνα Σελή,f,secr,project1 project2 
 Νίκος Πάλης,m,tech,project2 
 Λίνα Πενταγιά,f,eng,project1 
 Ρένα Ντορ,f,secr,project3 project2 
 Τζον Κλης,m,tech,project1 project2 
 Λάκης Λαζός,m,eng,project2 
 Μαρίνα Μαρή,f,eng,project3 
 Ζήσης Χελάς,m,tech,project1 project2"""

# αρχικοποίηση των συνόλων
m = set()
f = set()
eng = set()
tech = set()
secr = set()
p1 = set()
p2 = set()
p3 = set()


def load_sets(employees_string):
    global m, f, eng, tech, secr, p1, p2, p3
    # φόρτωμα των στοιχείων του πίνακα εργαζομένων στα σύνολα
    lst = (employees_string.splitlines())
    employees = []  # αρχικοποίηση κενής λίστας
    for item in lst:
        employ_list = item.strip().split(',')
        employees.append(employ_list)
    m = {employee[0] for employee in employees if employee[1] == 'm'}  # τοποθετεί το όνομα για κάθε εργαζόμενο από την λίστα employees εαν το δεύτερο στοιχείο του είναι "m"
    f = {employee[0] for employee in employees if employee[1] == 'f'}
    eng = {employee[0] for employee in employees if employee[2] == 'eng'}
    tech = {employee[0] for employee in employees if employee[2] == 'tech'}
    secr = {employee[0] for employee in employees if employee[2] == 'secr'}
    p1 = {employee[0] for employee in employees if 'project1' in employee[3]}
    p2 = {employee[0] for employee in employees if 'project2' in employee[3]}
    p3 = {employee[0] for employee in employees if 'project3' in employee[3]}


# εκτύπωση set
def show_set(hint, s):
    # βοηθητική συνάρτηση εκτύπωσης συνόλου s με εξήγηση hint
    print(f'{hint}: {s}')


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ
# οι άνδρες που δουλεύουν στο project1
def men_project1():
    show_set('Οι άνδρες που δουλεύουν στο project1', m & p1)


# όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3
def project1_not_project2_not_project3():
    show_set('Όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3', p1 - p2 - p3)


# οι γυναίκες μηχανικοί
def f_eng():
    show_set('Οι γυναίκες μηχανικοί', f & eng)


# όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2
def tech_p1_p2():
    show_set('Όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2', tech & (p1 | p2))


# οι άνδρες μηχανικοί που δεν δουλεύουν στο project2
def m_eng_not_p2():
    show_set('Oι άνδρες μηχανικοί που δεν δουλεύουν στο project2', m - p2)


#### κυρίως πρόγραμμα ####
# αρχικά σύνολα
load_sets(employees)
### κλήση συναρτήσεων
print("_" * 90)
print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ".center(90))
men_project1()
project1_not_project2_not_project3()
f_eng()
tech_p1_p2()
m_eng_not_p2()
end_string = "Ολοκληρώθηκε η εκτέλεση του προγράμματος"
print(f'\n{end_string:.^90}')
