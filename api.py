
# app.py
from flask import Flask, request, jsonify
import pathlib
import os.path
import re
from main import Diploma
from mail_sender import sendMail
from flask_talisman import Talisman
from datetime import datetime

app = Flask(__name__)
Talisman(app,force_https=False)
#PATHPLANTILLAS = CURRENTPATH+"/plantillas"
MAILFROM ="diplomaapiinnosoft@gmail.com"


@app.route('/diploma', methods=['GET'])
def respond():
        CURRENTPATH = str(pathlib.Path().resolve())
        PATHPLANTILLAS = CURRENTPATH+"/plantillas"
        MAILFROM ="diplomaapiinnosoft@gmail.com"

        
        # Retrieve the name from url parameter
        diplomaGenerar = str(request.args.get("diplomaGenerar", None))
        nombreDiploma = str(request.args.get("nombreDiploma", None))
        name = str(request.args.get("name", None))
        course = str(request.args.get("course", None))
        score = str(request.args.get("score", None))
        date = str(request.args.get("date", None))
        mailto = str(request.args.get("mailto", None))
        
        args = dict()
        args['diplomaGenerar'] = diplomaGenerar
        args['nombreDiploma'] = nombreDiploma
        args['name'] = name
        args['course'] = course
        args['score'] = score
        args['date'] = date
        args['mailto'] = mailto
        
        correcto = validar(args)

        if len(correcto) > 0:

            return {'No se ha podido completar el generado y envio de diploma por los siguientes motivos:':correcto
            
            
            }, 500 
        

        # ----------- Si se quiere usar el directorio de plantillas de la api ------------
        #diploma_a_generar = str(args['diplomaGenerar'])+".html"

        #if not os.path.exists(PATHPLANTILLAS+"/"+diploma_a_generar):
        #    return {'Diploma Incorrecto':"El diploma '"+diploma_a_generar+"' no existe"}, 500 

        # ----------- Si se quiere dar la plantilla como parámetro de la petición ------------
        diploma_a_generar = str(diplomaGenerar)
        # -----------
        
        diploma = Diploma(diploma_a_generar,str(nombreDiploma)+".pdf",name
        ,course,score,date) 
       
       

        

        if diploma.generate():
            
            sendMail( 
            "diplomaapiinnosoft@gmail.com",
            [mailto],
            "Certificación " + course,
            "Mail generado automaticamente",
            [CURRENTPATH+"/"+nombreDiploma+".pdf"]
            )            
            return {'status':"Diploma generado correctamente.Mail enviado a '"+mailto+"'"
            
            
            }, 200  # return data with 200 OK
        else:
            return {'status':"Fallo del servidor al generar diploma"
            
            
            }, 500 

def validar(args): 
    correcto = []
    nombreDiploma = str(args['nombreDiploma'])
    print(nombreDiploma)
    if nombreDiploma == '':
        correcto.append('Nombre del Diploma: El nombre del diploma no puede estar vacío')

    nombre = str(args['name'])
    if nombre == '':
        correcto.append('Nombre: El nombre no puede estar vacío')

    elif not all(x.isalpha() or x.isspace() for x in nombre):
        correcto.append('Nombre: El nombre tiene que contener solo caracteres alfabéticos')
        


    mailto = str(args['mailto'])
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    if(re.match(expresion_regular, mailto) is None):
        print(mailto)
        print(re.match(expresion_regular, mailto) is None)
        correcto.append('Correo: El formato del correo electrónico es incorrecto. Tiene que seguir el patron xxxx@xxx.xx')

    if mailto == '':
        correcto.append('Correo: El correo no puede estar vacío')



    course = str(args['course'])
    if course == '':
        correcto.append('Curso: El curso realizado no puede estar vacío')

    
    diploma = str(args['diplomaGenerar'])

    if diploma == '':
        correcto.append('Diploma a Generar: La plantilla del diploma a generar no puede estar vacía')
    elif not diploma.find('%3C%21DOCTYPE+html%3E+%3Chtml%3E+%3Chead%3E+%3C'):
        correcto.append('Diploma a Generar: La plantilla del diploma a generar es incorrecta')

    score = str(args['score'])
    print(score)
    if score == '':
        correcto.append('Puntuación: La puntuación no puede estar vacía')


    date = str(args['date'])
    print(date)
    try:
        fecha = datetime.strptime(date, '%Y-%m-%d')
        print(fecha)
    except ValueError:
        correcto.append('Fecha: El formato es inválido. El formato es el siguiente: YYYY-MM-DD')
    
    if date == '':
        correcto.append('Nombre: La fecha no puede estar vacía')
    
    

    return correcto
  

@app.route('/')
def index():
    return  {'status':"Fallo del servidor al generar diploma"
            
            
            }, 200 

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)