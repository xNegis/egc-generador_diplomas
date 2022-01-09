
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

class SeleniumTest(unittest.TestCase):
    def test_generate(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)

        driver.get("https://generador-diplomas-innosoft.herokuapp.com/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=Alejandro Ruiz&course=Comité de Programa&score=2&date=XI Edición Innosoft 2021&mailto=fernandoclarosb@gmail.com")

        self.assertEqual('{"status":"Diploma generado correctamente.Mail enviado a 'fernandoclarosb@gmail.com'"}', driver.find_element_by_tag_name('pre').text)
        driver.quit()
    

    def test_generate_error_mail(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)

        driver.get("https://generador-diplomas-innosoft.herokuapp.com/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=Alejandro Ruiz&course=Comité de Programa&score=2&date=XI Edición Innosoft 2021&mailto=kikii")

        self.assertEqual("Internal Server Error", driver.find_element_by_tag_name('h1').text)
        driver.quit()

    def test_generate_error_mail(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)

        driver.get("https://generador-diplomas-innosoft.herokuapp.com/diploma?diplomaGenerar=wasd&nombreDiploma=prueba1&name=Alejandro Ruiz&course=Comité de Programa&score=2&date=XI Edición Innosoft 2021&mailto=kikii")

        self.assertEqual("Internal Server Error", driver.find_element_by_tag_name('h1').text)
        driver.quit()

if name == "main":
    unittest.main()