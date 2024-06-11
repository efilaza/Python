# 2η Γραπτή Εργασία Θ.Ε ΠΛΗΠΡΟ
# Filename: Lazaridou_4.py
# Υποεργασία 4
# Λεξικά, Δομημένος Προγραμματισμός


zen_txt = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# ερώτημα (α)
def capitalize_keep_only_en_chars(word):

    # βοηθητική συνάρτηση που επιστρέφει μόνο αγγλικούς κεφαλαίους χαρακτήρες
    # της συμβολοσειράς εισόδου word

    new_word = ''.join(ch for ch in word if ch.isalpha() and ch.isascii()).upper()
    return new_word


# ερώτημα (β)
def tokenize(txt):
    # συνάρτηση που "σπάει" το κείμενο txt σε λέξεις απορρίπτοντας
    # χαρακτήρες που δεν είναι γράμματα του αγγλικού αλφαβήτου,
    # επιστρέφει λίστα με λέξεις με κεφαλαία γράμματα
    word_list = []
    lst = txt.splitlines()
    for line in lst:
        for word in line.split(' '):
            new_word = capitalize_keep_only_en_chars(word)
            word_list.append(new_word)
    return word_list


# ερώτημα (γ)
def char_frequencies(word_list):
    # συνάρτηση που επιστρέφει ένα λεξικό με το πλήθος εμφάνισης
    # κάθε χαρακτήρα στη λίστα συμβολοσειρών word_list
    dict = {}
    for word in word_list:
        for char in word:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict


# ερώτημα (δ)
def word_frequencies(word_list):
    # συνάρτηση που επιστρέφει λεξικό με το πλήθος εμφάνισης κάθε λέξης
    # στη λίστα συμβολοσειρών word_list
    dict = {}
    for word in word_list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


def check_input(hint, start = float('-inf')):
    """Βοηθητική συνάρτηση για τον έλεγχο της εισόδου του χρήστη
    Attributes:
    string hint: Μήνυμα εισόδου προς τον χρήστη
    int start: Κατώτερη τιμή, Default τιμή = μείον άπειρο"""

    while True:  # αμυντικός προγραμματισμός
        try:
            user = int(input(f"{hint}: "))
            if user <= start :  # Αν user < start προβάλλετε το κατάλληλο μήνυμα
                print(f"O αριθμός πρέπει να είναι μεγαλύτερος από {start}.")
            else:
                break
        except ValueError:
            print("Δεν δώσατε ακέραιο αριθμό. Προσπαθήστε ξανά.")
    return user

# ερώτημα (ε)
### Κυρίως πρόγραμμα ###
choice = 0
while choice not in range(1, 4):
    print("Παρακαλώ επιλέξτε το κείμενο που θέλετε ανάλυση.")
    print("1 - 'Zen of Python', by Tim Peters.")
    print("2 - 'War and Peace', by Leon Tolstoy.")
    print("3 - Exit")
    try:
        choice = int(input("Επιλογή: "))
    except ValueError:
        print("Η επιλογή που δώσατε δεν είναι αποδεκτή!")
    except Exception as e:
        print(f"Σφάλμα: {e}")
    if choice == 1:
        words = tokenize(zen_txt)
        break
    elif choice == 2:
        try:
            with open("War_and_Peace.txt", encoding="utf-8") as f:
                file = f.read()
        except FileNotFoundError:
            print("File not Found")
        words = tokenize(file)
        break
    elif choice == 3:
        print("Επιλέξατε έξοδο από το πρόγραμμα.")
        exit()

# ερώτημα (ε1)
print("*" * 30)
print("Συχνότητα εμφάνισης γραμμάτων: ")
char_dict = char_frequencies(words)
total_chars = sum(char_dict.values())
for char in sorted(char_dict.keys()):
    percent = (char_dict[char] * 100) / total_chars
    print(f'{char} : {(char_dict[char] / total_chars) * 100 : .2f} %')

# ερώτημα (ε2)

words_dict = word_frequencies(words)
print("\nΠοιό είναι το ελάχιστο μήκος λέξεων που επιθυμείτε? ")
length = check_input("Παρακαλώ δώστε την επιλογή σας ",0)

print(f"\nΛέξεις με πάνω από {length} γράμματα: ")
i = 1
while True:
    for key in sorted(words_dict, key=words_dict.get, reverse=True):
        if len(key) > length:
            print(f'{i} {key} {words_dict[key]}')
            frequency = words_dict[key]
            words_dict.pop(key) #βγάζει από το λεξικό την συγκεκριμένη λέξη
            i += 1
        if i == 11: #οταν ο μετρητής γίνει 11  αναζητά τις υπόλοιπες λέξεις με ίδια συχνότητα(value)
            for word, freq in words_dict.items():
                if freq == frequency and len(word) > length:  # από το λεξικό words_dic θα τυπώσει όσες λέξεις έχουν μείνει που να έχουν τιμή ίση
                    print(f'{i} {word} {freq}')  # με τις τιμές που έχει το λεξικό dict.
                    i += 1
            break
    break

end_string = "Ολοκληρώθηκε η εκτέλεση του προγράμματος"
print(f'{end_string:.^90}')
