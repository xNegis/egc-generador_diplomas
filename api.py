
# app.py
from flask import Flask, request, jsonify, reqparse
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

        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('diplomaGenerar', required=True)  
        parser.add_argument('nombreDiploma', required=True)
        parser.add_argument('name', required=True)  
        parser.add_argument('course', required=True)
        parser.add_argument('score', required=True)
        parser.add_argument('date', required=True)
        parser.add_argument('mailto', required=True)
        
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        
        mailto = str(args['mailto'])

        # ----------- Si se quiere usar el directorio de plantillas de la api ------------
        #diploma_a_generar = str(args['diplomaGenerar'])+".html"

        #if not os.path.exists(PATHPLANTILLAS+"/"+diploma_a_generar):
        #    return {'Diploma Incorrecto':"El diploma '"+diploma_a_generar+"' no existe"}, 500 

        # ----------- Si se quiere dar la plantilla como parámetro de la petición ------------
        diploma_a_generar = str(args['diplomaGenerar'])
        # -----------
        
        diploma = Diploma(diploma_a_generar,str(args['nombreDiploma'])+".pdf",args['name']
        ,args['course'],args['score'],args['date']) 
       
       

        

        if diploma.generate():
            
            sendMail( 
            "diplomaapiinnosoft@gmail.com",
            [mailto],
            "Certificación " + args['course'],
            "Mail generado automaticamente",
            [CURRENTPATH+"/"+args['nombreDiploma']+".pdf"]
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