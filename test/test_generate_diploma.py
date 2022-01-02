import unittest
from main import Diploma

class TestGenerateDiploma(unittest.TestCase):
    def test_generate(self):

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

        diplo1=Diploma(html,"prueba 1.pdf","Alejandro Ruiz","Comité de Programa","2","XI Edición Innosoft 2021")
        diplo2= diplo1.generate()
        diplo_esperado="""<!DOCTYPE html>
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
            <p style="font-size: 2.4em;margin:0px" class="bold">Alejandro Ruiz</p>
            <br>
            <br>

            <p style="margin:0px;">Por formar parte de:</p>
            <h2 style="max-width: 600px;margin:25px auto;font-size: 3em;" class="bold">Comité de Programa</h2>

            <br>
            <br>
            <br>
            <br>

            <p style="font-size: 2.4em;margin:0px;">Nombrado el mejor comité de la edición:</p>
            <p style="font-size: 1.5em;" class="bold">XI Edición Innosoft 2021</p>


        </div>
    </div>
</body>
</html>"""
        self.maxDiff=None

        self.assertEquals(diplo2, diplo_esperado)


if __name__ == "__main__":
    unittest.main()
