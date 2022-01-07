import pdfkit 
import pathlib
import platform
from jinja2 import Template#, Environment, FileSystemLoader


class Diploma:
  def __init__(self, _diploma_a_generar, _nombre_diploma,_nombre_alumno,_course,_score,_date):
    self.diploma_a_generar=_diploma_a_generar
    self.nombre_diploma=_nombre_diploma
    self.nombre_alumno=_nombre_alumno
    self.course = _course
    self.score = _score
    self.date = _date
  
  def generate(self):
    # ----------- Si se quiere usar el directorio de plantillas de la api ------------
    #env = Environment(loader=FileSystemLoader("./plantillas"))
    #template=env.get_template(self.diploma_a_generar)

    # ----------- Si se quiere dar la plantilla como parámetro de la petición ------------
    template = Template(self.diploma_a_generar)
    # ----------- 

    usuario ={
        
    'name' : self.nombre_alumno,
    'course':self.course,
    'score' : self.score,
    'date':self.date
    }

    html=template.render(usuario)

    options = {
    'page-size':'A5',
    'margin-top':'0.1in',
    'margin-right':'0.1in',
    'margin-bottom':'0.1in',
    'margin-left':'0.1in',
    'encoding': "UTF-8",
    }

    # path = pathlib.Path().resolve() 
    # plataforma = platform.system()
    # if plataforma == "Windows":
    #   path_wkhtmltopdf = str(path)+ "\wkhtmltopdf.exe"
    # elif plataforma == "Linux":
    #   path_wkhtmltopdf = str(path) + "\wkhtmltox_0.12.6-1.focal_amd64.deb"
      
    #config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    print("Generando diploma de la plantilla ...")
    pdfkit.from_string(html,self.nombre_diploma,options=options)
    print("Diploma generado correctamente")
    return html

#----Html de la plantilla a usar----
html = """<!DOCTYPE html>
<html>

<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
    html,body{height: 70%;}
    body{
        background-image: url("https://www.detoxpobyt.sk/wp-content/uploads/2017/07/response.jpg");
        /* https://www.insperity.com/wp-content/uploads/organization_structure1200x600.png */
        background-size: cover;
        background-repeat: no-repeat;
        font-family: 'Poppins';
        font-weight: 300;
        height: 100%;
        text-align: center;
        color: #2a7a31;
        text-shadow: 3px 3px 4px #000000;
    }
    .bold{
        font-weight: 300;
    }
</style>
</head>

<body>
    <div style= "padding-top: 80px;">
        <div>
            <h1 class="bold">DIPLOMA AL MEJOR COMITÉ</h1>
            <p style="margin-bottom: 0px;margin-top: 25px;" class="light">Da la enhorabuena a:</p>
            <p style="font-size: 2.4em;margin:0px" class="bold">{{name}}</p>
            <br>
            <br>

            <p style="margin:0px;">Por formar parte de:</p>
            <h2 style="max-width: 600px;margin:25px auto;font-size: 3em;" class="bold">{{course}}</h2>

            <br>
            <br>
            <br>
            <br>

            <p style="font-size: 2.4em;margin:0px;">Nombrado el mejor comité de la edición:</p>
            <p style="font-size: 1.5em;" class="bold">{{date}}</p>


        </div>
    </div>
</body>
</html>"""
diploma = Diploma(html,"prueba 1.pdf","Alejandro Ruiz","Comité de Programa","2","XI Edición Innosoft 2021")
diploma.generate()

