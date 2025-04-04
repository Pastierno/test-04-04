# Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, 
# l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, 
# alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito.

# Inizializzo lista vuota
stri = []

# Variabile per avere sempre l'indice dell'ultima stringa inserita
index = len(stri) - 1
# Controllroe ciclo while
contr = True
while contr:
    user_input = input('Inserimento stringhe, (premi 0 per stampare la lista e € per uscire): \n'
                       '\nInserisci una stringa, la prima verrà salvata \n'
                       'le successive, se maggiori della precedente, verranno salvate \n'
                       'oppure verranno aggiunte ala stessa : \n')
    
    if stri == []:
        stri.append(user_input)
        print(f'\nLista inizializzata, la stringa {user_input} aggiunta alla lista!\n')
    elif user_input == '0':
        print(stri)
    elif user_input == '€':
        print('Ciao!')
        break
        
    elif len(user_input) > len(stri[-1]): # Nel caso in cui la lunghezza della stringa inserita sia maggiore dell'ultima presente nella lista
        stri.append(user_input)
        print(f'\nLa stringa {user_input} è maggiore dell\'ultima stringa inserita, aggiunta alla lista!\n')
        
    elif len(user_input) < len(stri[-1]): # Nel caso stringa inserita minore della lunghezza dell'ultima
        new_string = (stri[-1] + user_input)
        stri.pop()
        stri.append(new_string)
        print(f'\nLa stringa {user_input} è più corta, aggiunta alla precedente!\n')
    else:
        print('Ciao!')
