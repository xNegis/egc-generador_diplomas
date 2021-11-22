from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
from main import Diploma
import pathlib
from mail_sender import sendMail
app = Flask(__name__)
api = Api(app)


class DiplomaAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('diplomaGenerar', required=True)  
        parser.add_argument('nombreDiploma', required=True)
        parser.add_argument('name', required=True)  
        parser.add_argument('course', required=True)
        parser.add_argument('score', required=True)
        parser.add_argument('date', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        diploma = Diploma(str(args['diplomaGenerar'])+".html",str(args['nombreDiploma'])+".pdf",args['name']
        ,args['course'],args['score'],args['date']) 
       



        if diploma.generate():
            
            path = str(pathlib.Path().resolve())
            sendMail( 
            "diplomaapiinnosoft@gmail.com",
            ["diplomaapiinnosoft@gmail.com"],
            "Certificación" + args['course'],
            "Mail generado automaticamente",
            [path+"\\"+args['nombreDiploma']+".pdf"]
            )            
            return {'status':"Diploma generado correctamente.Mail Enviado"
            
            
            }, 200  # return data with 200 OK
        else:
            return {'status':"Fallo del servidor al generar diploma"
            
            
            }, 500 
        

api.add_resource(DiplomaAPI, '/diploma')  


if __name__ == '__main__':
    app.run()  # run our Flask app