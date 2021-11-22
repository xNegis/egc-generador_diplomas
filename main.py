import pdfkit 
import pathlib
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("plantillas"))
template=env.get_template("diploma_ctf.html")
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
path_wkhtmltopdf = str(path)+ "\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_string(html,'nuevo_pdf4.pdf',options=options,configuration=config)