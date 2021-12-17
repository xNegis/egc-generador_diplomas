from flask import Flask
from flask_restful import Resource, Api, reqparse
from main import Diploma
import pathlib
import os.path
from mail_sender import sendMail
app = Flask(__name__)
api = Api(app)

CURRENTPATH = str(pathlib.Path().resolve())
PATHPLANTILLAS = CURRENTPATH+"/plantillas"
MAILFROM ="diplomaapiinnosoft@gmail.com"

class DiplomaAPI(Resource):
    def get(self):
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

        diploma_a_generar = str(args['diplomaGenerar'])+".html"

        if not os.path.exists(PATHPLANTILLAS+"/"+diploma_a_generar):
            return {'Diploma Incorrecto':"El diploma '"+diploma_a_generar+"' no existe"}, 500 

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
        

api.add_resource(DiplomaAPI, '/diploma')  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
