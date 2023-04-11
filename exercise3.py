2# AVOURIS SPYRIDON 321/2017001
# Άσκηση 3

# Αποθήκευση αριθμών πίνακα με τη μορφή string
triliza = {'00': ' ', '01': ' ', '02': ' ', '03': ' ', '04': ' ',
           '10': ' ', '11': ' ', '12': ' ', '13': ' ', '14': ' ',
           '20': ' ', '21': ' ', '22': ' ', '23': ' ', '24': ' ',
           '30': ' ', '31': ' ', '32': ' ', '33': ' ', '34': ' ',
           '40': ' ', '41': ' ', '42': ' ', '43': ' ', '44': ' ', }

# Δήλωση δισδιάστατου πίνακα
grammes, stiles = (5, 5)
board_keys = [[0]*grammes]*stiles

for key in triliza:
    board_keys.append(key)

# Ορισμός αναδρομικής συνάρτησης για την ανανέωση των στοιχείων 
# του πίνακα κάθε φορά που πάιζει ο κάθε παίχτης
def printTriliza(board):
    print(board['00'] + '|' + board['01'] + '|' +
          board['02'] + '|' + board['03'] + '|' + board['04'])
    print('-+-+-+-+-')
    print(board['10'] + '|' + board['11'] + '|' +
          board['12'] + '|' + board['13'] + '|' + board['14'])
    print('-+-+-+-+-')
    print(board['20'] + '|' + board['21'] + '|' +
          board['22'] + '|' + board['23'] + '|' + board['24'])
    print('-+-+-+-+-')
    print(board['30'] + '|' + board['31'] + '|' +
          board['32'] + '|' + board['33'] + '|' + board['34'])
    print('-+-+-+-+-')
    print(board['40'] + '|' + board['41'] + '|' +
          board['42'] + '|' + board['43'] + '|' + board['44'])


# Ορισμός κύριας συνάρτησης με τις βασικές λειτουργίες του παιχνιδιού
def startGame():

    # Πρώτος ξεκινάει ο χρήστης με το Χ
    turn = 'X'
    counter = 0
    # Το πρόγραμμα θα τρέχει έως ότου νικήσει κάποιος παίχτης ή 
    # συμπληρωθούν όλα τα κελιά 
    for i in range(26):
        printTriliza(triliza)
        move = input("It's your turn, " + turn +
              ". Enter the position of the cell you want to move: ")

        if triliza[move] == ' ':
            triliza[move] = turn
            counter += 1
        else:
            print("That cell is already filled.")
            continue

        # Έλεγχος κάθε παίχτη για το αν κέρδισε μετά από 5 κινήσεις 
        if counter >= 5:
            
            if triliza['00'] == triliza['01'] == triliza['02'] == triliza['03'] == triliza['04'] != ' ':  
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['10'] == triliza['11'] == triliza['12'] == triliza['13'] == triliza['14'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['20'] == triliza['21'] == triliza['22'] == triliza['23'] == triliza['24'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['30'] == triliza['31'] == triliza['32'] == triliza['33'] == triliza['34'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['40'] == triliza['41'] == triliza['42'] == triliza['43'] == triliza['44'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['00'] == triliza['10'] == triliza['20'] == triliza['30'] == triliza['40'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['01'] == triliza['11'] == triliza['21'] == triliza['31'] == triliza['41'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['02'] == triliza['12'] == triliza['22'] == triliza['32'] == triliza['42'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif triliza['03'] == triliza['13'] == triliza['23'] == triliza['33'] == triliza['43'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            
            elif triliza['04'] == triliza['14'] == triliza['24'] == triliza['34'] == triliza['44'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif triliza['00'] == triliza['11'] == triliza['22'] == triliza['33'] == triliza['44'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif triliza['04'] == triliza['13'] == triliza['22'] == triliza['31'] == triliza['40'] != ' ':
                printTriliza(triliza)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break

        # Εάν έχει καλυφθεί το εμβαδόν της τρίλιζας, δηλαδή 25, δεν κέρδισε κανένας από τους 2 πάιχτες.
        if counter == 25:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Αλλαγή μεταβλητής που δείχνει τον κάθε παίχτη, μετά απο κάθε γύρο.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

# Δήλωση συνάρτησης για την έναρξη του παιχνιδιού
if __name__ == "__main__":
    startGame()
