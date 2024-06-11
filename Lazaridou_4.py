# 1η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename:Lazaridou_4.py
# Υποεργασία 4
# Μηχάνημα ροφημάτων

print("Δίνονται οι παρακάτω επιλογές:")
print("\t 1. Καφές: 1.50\u20ac")
print("\t 2. Καφές με γάλα: 1.80\u20ac")
print("\t 3. Σοκολάτα: 2.10\u20ac")
print("\t 4. Σοκολάτα με γάλα: 2.40\u20ac")
print("\t 0. Έξοδος.")
my_choice = int(input("Παρακαλώ εισάγετε την επιλογή σας (1-4) ή πατήστε 0 για έξοδο: "))# Εισαγωγή επιλογής χρήστη
while my_choice not in range(5): # True: Αν my_choice όχι από 0 έως 4
    print("Η επιλογή που εισάγετε δεν είναι έγκυρη")
    my_choice = int(input("Παρακαλώ εισάγετε την επιλογή σας (1-4) ή πατήστε 0 για έξοδο: "))
if my_choice == 0: # Αληθής αν my_choice = 0
    print("Επιλέξατε έξοδο από το πρόγραμμα.")
    exit()
    
prices_list = [1.50,1.80,2.10,2.40] # Λίστα με τις τιμές των ροφημάτων
valid_money = [0.1,0.2,0.50,1,2,5,10] # Λίστα με τα αποδεκτά χρήματα
price = prices_list[my_choice-1] # Η τιμή του επιλεγμένου ροφήματος

sum = 0

while sum < price: # Αληθής όσο τα χρήματα που βάζουμε ειναι λιγότερα από την τιμή
    money_left = (round((price - sum),2)) #Πόσα χρήματα πρέπει να βάλουμε ακόμα
    print("Πρέπει να εισάγετε {:.2f}\u20ac συνολικά".format(money_left))
    payment = float(input("Πόσα εισάγετε; ")) #Πόσα χρήματα βάζουμε
    while payment not in valid_money: #Αληθής αν το ποσό που εισάγουμε δεν ανήκει στα αποδεκτά χρήματα
        print("ΣΦΑΛΜΑ. Εισαγωγή μη έγκυρου ποσού.")
        print("Παρακαλώ εισάγετε μια έγκυρη τιμή: 0.1, 0.2, 0.5, 1, 2, 5, 10")
        print("Πρέπει να εισάγετε {:.2f}\u20ac συνολικά".format(money_left))
        payment = float(input("Πόσα εισάγετε; "))
    sum += payment #Αθροιστής χρημάτων
    
change = (sum*100) - (price*100) #  Ρέστα
print("Επιστροφή: {:.2f}".format(sum - price))

while change > 0 : #Αληθής όσο η μεταβλητή change >0
    print("Παρακαλώ πάρτε:")
    for i in valid_money[4::-1]: # Βρόγχος επανάληψης 
        number_of_coins = change //(i*100)
        if (number_of_coins >= 1): #Αληθής όταν το πλήθος των κερμάτων είναι από ένα και πάνω 
            print(i,"\u20ac X",int(number_of_coins))
            change = change % (i*100) 
            
end_string ="Ολοκληρώθηκε η εκτέλεση του προγράμματος"
print('\n{:^70}'.format(end_string))
