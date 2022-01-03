
# app.py
from flask import Flask, request, jsonify
import pathlib
import os.path
from main import Diploma
from mail_sender import sendMail
from flask_talisman import Talisman


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
        
        
        
        

        # ----------- Si se quiere usar el directorio de plantillas de la api ------------
        #diploma_a_generar = str(args['diplomaGenerar'])+".html"

        #if not os.path.exists(PATHPLANTILLAS+"/"+diploma_a_generar):
        #    return {'Diploma Incorrecto':"El diploma '"+diploma_a_generar+"' no existe"}, 500 

        # ----------- Si se quiere dar la plantilla como parámetro de la petición ------------
        diploma_a_generar = str(diplomaGenerar)
        # -----------
        
        diploma = Diploma(diploma_a_generar,str(diplomaGenerar)+".pdf",name
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
        

@app.route('/')
def index():
    return  {'status':"Fallo del servidor al generar diploma"
            
            
            }, 200 

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)