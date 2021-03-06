
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import unittest
import platform

PATH = str(pathlib.Path().resolve())
OPTIONS = webdriver.ChromeOptions()
OPTIONS.headless = True
plataforma = platform.system()
if plataforma == "Windows":
    DRIVER = webdriver.Chrome(executable_path=PATH+"/test/chromedriver.exe",options=OPTIONS)
else:
    DRIVER = webdriver.Chrome(executable_path=PATH+"/test/chromedriver",options=OPTIONS)

URL_APP ="https://generador-diplomas-innosoft-2.herokuapp.com"

class SeleniumTest(unittest.TestCase):

    def test_generate(self):
        
        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba&name=Alejandro&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=generadordiplomasinnosoft@gmail.com")

        self.assertEqual('{"status":"Diploma generado correctamente.Mail enviado a \'generadordiplomasinnosoft@gmail.com\'"}', DRIVER.find_element_by_tag_name('pre').text)


    def test_generate_error_mail(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=Alejandro&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=kikii")

        self.assertTrue("Correo: " in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_mail_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=Alejandro&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=")

        self.assertTrue("Correo: " in DRIVER.find_element_by_tag_name('pre').text)


    def test_generate_error_nombre(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=!!!!&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=generadordiplomasinnosoft@gmail.com")

        self.assertTrue("Nombre: " in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_nombre_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=generadordiplomasinnosoft@gmail.com")

        self.assertTrue("Nombre: " in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_diploma_generar_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=&nombreDiploma=holaprueba1&name=Alejandro&course=Comité%20de%20Programa&score=2&date=2020-02-02&mailto=generadordiplomasinnosoft@gmail.com")

        self.assertTrue("Diploma a Generar: " in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_curso_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba&name=Alejandro&course=&score=2&date=2020-02-02&mailto=fernandoclarosb@gmail.com")

        self.assertTrue("Curso: " in DRIVER.find_element_by_tag_name('pre').text)


    def test_generate_error_puntuacion_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba&name=Alejandro&course=primero&score=&date=2020-02-02&mailto=fernandoclarosb@gmail.com")

        self.assertTrue("no puede estar" in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_fecha(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba&name=Alejandro&course=2&score=2&date=soss&mailto=fernandoclarosb@gmail.com")

        self.assertTrue("Fecha: " in DRIVER.find_element_by_tag_name('pre').text)

    def test_generate_error_fecha_vacio(self):

        DRIVER.get(URL_APP+"/diploma?diplomaGenerar=wasd&nombreDiploma=prueba&name=Alejandro&course=2&score=2&date=&mailto=fernandoclarosb@gmail.com")

        self.assertTrue("no puede estar" in DRIVER.find_element_by_tag_name('pre').text)


if __name__ == "main":
    unittest.main()
