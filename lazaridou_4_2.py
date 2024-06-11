import pandas as pd  # Χρήση της βιβλιοθήκης pandas
import matplotlib.pyplot as plt  # Χρήση της βιβλιοθήκης matplotlib.pyplot
import openpyxl


def printMeteoData(file, city):
    '''Ανάγνωση μετεωρολογικών δεδομένων, για μια πόλη, και εκτύπωσή τους'''
    # Υποερώτημα α
    # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
    df = pd.read_excel(file, sheet_name=city)
    # Εκτύπωση του dataframe με τα στοιχεία της πόλης
    print(df)


def printMeteoStats(file, metric, city):
    '''Ανάγνωση μετεωρολογικών δεδομένων, για μια πόλη, και εκτύπωση βασικών στατιστικών στοιχείων μιας μετρικής'''
    # Υποερώτημα β
    # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
    df = pd.read_excel(file, sheet_name=city)
    # Υπολογισμός και εκτύπωση μέσης τιμής και οριακών τιμών της μετρικής
    mesos_oros = df[metric].mean()
    elaxisto = df[metric].min()
    megisto = df[metric].max()
    print("-" * 25)
    print(f'Ο μέσος όρος των ενδείξεων "{metric}" για την πόλη {city} είναι: {mesos_oros:.2f}')
    print(f'Η ελάχιστη τιμή των ενδείξεων "{metric}" για την πόλη {city} είναι: {elaxisto:.2f}')
    print(f'Η μέγιστη τιμή των ενδείξεων "{metric}" για την πόλη {city} είναι: {megisto:.2f}')
    print("-" * 25)


def plotMeteoData(file, x_axis, metric, *list_of_cities):
    '''Ανάγνωση μετεωρολογικών δεδομένων και εμφάνιση συγκριτικού γραφήματος μιας μετρικής'''

    # Υποερώτημα γ
    # Επανάληψη για όλες τις πόλεις
    for list in list_of_cities:
        for city in list:
            # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
            df = pd.read_excel(file, sheet_name=city)
            # Δημιουργία γραφήματος με τα δεδομένα της μετρικής για την πόλη των τριών πόλεων
            plt.plot(df['Μήνας'], df['Υγρασία'], label=city)

    # Προσθήκη τίτλου, ετικετών αξόνων και υπομνήματος
    plt.title(f'Συγκριτικά δεδομένα υγρασίας')
    plt.xlabel('Μήνας')
    plt.ylabel('Υγρασία')
    plt.legend(fontsize=10)

    # Εμφάνιση του γραφήματος
    plt.show()
    plt.set_dpi(100)


# Κυρίως πρόγραμμα

# Ορισμός του αρχείου με τα δεδομένα προς ανάγνωση
excel_file = 'weatherdata.xlsx'

# Υποερώτημα δ

# Εκτύπωση, με την printMeteoData, των στοιχείων για την Αθήνα
printMeteoData(excel_file, 'Αθήνα')

# Εκτύπωση, με την  printMeteoStats, βασικών στατιστικών τιμών θερμοκρασίας
# για τη Θεσσαλονίκη

printMeteoStats(excel_file, 'Θερμοκρασία', 'Θεσσαλονίκη')
printMeteoStats(excel_file, 'Άνεμος', 'Θεσσαλονίκη')
printMeteoStats(excel_file, 'Υγρασία', 'Θεσσαλονίκη')
printMeteoStats(excel_file, 'Ορατότητα', 'Θεσσαλονίκη')

# Δημιουργία συγκριτικού διαγράμματος για την υγρασία στις τρεις πόλεις

plotMeteoData(excel_file, 'Μήνας', 'Υγρασία', ['Αθήνα', 'Θεσσαλονίκη', 'Πάτρα'])
