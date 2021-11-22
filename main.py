import pdfkit 
import pathlib
from jinja2 import Environment, FileSystemLoader

diploma_a_generar ="diploma_ctf.html"
nombre_diploma="nuevo_pdf4.pdf"

env = Environment(loader=FileSystemLoader("egc-generador_diplomas/plantillas"))
template=env.get_template(diploma_a_generar)
usuario ={
    
'name' : 'Sergio Rojas',
'course':'laravel',
'score' : 5,
'date':'10/10/1998'
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

path = pathlib.Path().resolve() 
path_wkhtmltopdf = str(path)+ "\egc-generador_diplomas\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
print("Generando diploma de la plantilla '" +diploma_a_generar+"'")
pdfkit.from_string(html,nombre_diploma,options=options,configuration=config)
print("Diploma generado correctamente")
