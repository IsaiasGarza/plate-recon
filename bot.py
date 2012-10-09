import urllib
import urllib2
import webbrowser
from os import remove

PLACA = 'JJH8311'
url = "http://www2.repuve.gob.mx:8080/ciudadania/servletconsulta"
data = urllib.urlencode({'placa': PLACA, 'pageSource':'index.jsp' })
results = urllib2.urlopen(url,data)
with open("pre.html", "w") as f:
    f.write(results.read())
with open("results.html", "w") as out:
    for line in open("pre.html"):
        line = line.replace('<img  src="/ciudadania/jcaptcha" alt="Captcha">', '<img  src="http://www2.repuve.gob.mx:8080/ciudadania/jcaptcha" alt="Captcha">')
        line = line.replace('<img src="/ciudadania/common/img/Buscar.gif" width="86" height="28" border="0" alt="">','<img src="http://www2.repuve.gob.mx:8080/ciudadania/common/img/Buscar.gif" width="86" height="28" border="0" alt="">')
        line = line.replace('<script type="text/javascript" src="/ciudadania/common/js/ciudadania.js"></script>','<script type="text/javascript" src="http://www2.repuve.gob.mx:8080/ciudadania/common/js/ciudadania.js"></script>')
        line = line.replace('<img src="/ciudadania/common/img/cerrar.gif" width="86" height="28" border="0" alt="">', '<img src="http://www2.repuve.gob.mx:8080/ciudadania/common/img/cerrar.gif" width="86" height="28" border="0" alt="">')
        line = line.replace('<img src="/ciudadania/common/img/ayuda.jpg" border="0" alt="Ayuda">','<img src="http://www2.repuve.gob.mx:8080/ciudadania/common/img/ayuda.jpg" border="0" alt="Ayuda">')
        out.write(line)
remove("./pre.html")
webbrowser.open("results.html")