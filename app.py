from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import base64

app = Flask(__name__)

def process_image(image_data):
    try:
        # print("Image Data:", image_data)
        # Decode base64 image data
        # image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Failed to decode image")

        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Invert the grayscale image
        inverted_gray_image = 255 - gray_image

        # Create a blurred version of the inverted grayscale image
        blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

        # Blend grayscale image with blurred image to create pencil sketch
        pencil_sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

        # Encode pencil sketch image to base64
        _, img_encoded = cv2.imencode('.jpg', pencil_sketch)
        pencil_sketch_base64 = base64.b64encode(img_encoded).decode('utf-8')

        return pencil_sketch_base64
    except Exception as e:
        print("Error processing image:", e)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'})

        image_file = request.files['image']
        image_data = image_file.read()

        # Process the uploaded image
        pencil_sketch = process_image(image_data)

        if pencil_sketch is None:
            return jsonify({'error': 'Failed to process image'})

        return jsonify({'pencil_sketch': pencil_sketch})
    except Exception as e:
        print("Error uploading image:", e)
        return jsonify({'error': 'Failed to process image'})

if __name__ == '__main__':
    app.run(debug=True)




