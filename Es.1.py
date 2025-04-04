# Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di 
# dato che riceve in entrata. Deve poter stampare una lista singola o tutte.  Si deve ripetere X 
# volte definite all'inizio dall'utente



# Liste vuote che conterrano i tipi di dato
num = []
stri = []
boolean = []

# Controllore per ciclo
control = True
while control:
    user_input = input('Inserisci un intero, una stringa o un booleano: (€ per uscire, = per stampare le liste)\n')
    
    # Condizioni:
    if user_input == '€': # Esce
        print('Ciao!')
        break
    elif user_input == '=': # Stampa i valori
        print(num)
        print(stri)
        print(boolean)
    elif user_input.isdigit(): # Controlla se è un intero e lo aggiunge alla lista numeri
        num.append(int(user_input)) # Converte il tipo
        print(f'{user_input} aggiunto alla lista')
        continue
    elif user_input == 'True' or user_input == 'False': # Se input True o False
        boolean.append(user_input == 'True') # Aggiunge booleano, nelle parentesi condizione per aggiungere False, o restituisce sempre True)
        print(f'{user_input} aggiunto alla lista')
        continue
    else:
        stri.append(user_input)
        print(f'{user_input} aggiunto alla lista')
        continue

        
    
    