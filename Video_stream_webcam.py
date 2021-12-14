from flask import Flask,render_template,url_for,Response
import cv2
# from camera import Camera

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # reading the camera frame
        # ret is a bool type with True or False as the output
        ret,frame = camera.read()
        if not ret:
            print("Not able to read")
            break
        else:
            #imencode , it encode an image into an memory buffer
            # """cv2.imencode() function is to convert(encode) the image format into streaming data and assign it to memory cache
            # It is mainly used for compressing image data format to facilitate network transmission"""
            return_value , buffer = cv2.imencode(ext= ".jpg",img= frame)
            if not return_value:
                print(return_value," = return value")
                break
            else:
                frame = buffer.tobytes()
        # return frame -> these will return only the last frame
        
        # yield keyword let's the execution to continue and keeps on generating frame until alive or running
            yield(b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
            
   

@app.route(rule = "/")
def cam():
    return render_template("cam.html")

@app.route(rule = '/video')
def video():
    # A media type (also known as a Multipurpose Internet Mail Extensions or MIME type) is a standard that indicates the nature and format of a document, file, or assortment of bytes
    return Response(generate_frames(),mimetype = "multipart/x-mixed-replace; boundary = frame")



if __name__ == "__main__":
    app.run(debug = True)
