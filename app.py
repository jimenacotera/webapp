#for the following code to run, Flask, Pillow, pytesseract, tesseract, and picamera have to be installed.
from flask import Flask, render_template
try:
    from PIL import Image
except ImportError:
    import Image
#import pytesseract

#from picamera import PiCamera
import time


app = Flask(__name__)

#what is called every time the page is reloaded; will render a new template of the html page
@app.route("/")
def index():
    return render_template("index.html")


#code that is called when the button is pressed
@app.route("/capture", methods=['POST'])
def capture():
    '''
    with PiCamera() as camera:
        camera.start_preview()

        time.sleep(8)
        camera.capture('test.jpeg')
    name = pytesseract.image_to_string(Image.open('test.jpeg'))

    return(name)
'''
    val = 'dinosaur'
    return(val)


#this app is run in your computer's localhost:8000
app.run(port=8000, debug=True, host="0.0.0.0")
