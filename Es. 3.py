# Andare a creare una funzioni che si occupi di salvare i dati dell'utente, andare a creare una funzione che si occupi di fare il login dell'utente, 
# Andare a creare un funzioni che modifichi i dati dell'utente solo se questi sono già stati creati  / salvati e solo dopo il login.  
# Andare a creare un menu che concateni le tre funzioni precedenti e permetta di ripetere il ciclo a più utenti diversi.

users = []

# FUnzione per registrazione
def register():
    while True: # Ciclo per richiedere username in caso esistente
        username = input('Inserisci l\'username: \n')
        for user in users:
            if user[0] == username:
                print('Nome utente già in uso')
                continue
        
        password = input()
                
                
# Codice non teminato