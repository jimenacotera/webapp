
from flask import Flask, render_template
try:
    from PIL import Image
except ImportError:
    import Image
#import pytesseract

#from picamera import PiCamera
import time


app = Flask(__name__)


@app.route("/")
def index():
    value = 'starter'
    print(value)
    return render_template("index.html", val = value)

@app.route("/capture", methods=['POST'])
def capture():
    '''
    with PiCamera() as camera:
        camera.start_preview()

        time.sleep(7)
        camera.capture('test.jpeg')
    name = pytesseract.image_to_string(Image.open('test.jpeg'))

    return(name)
'''
    val = 'cherry'
    return(val)



app.run(port=8000, debug=True, host="0.0.0.0")
