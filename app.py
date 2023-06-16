import cv2
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Ashvin's API!"

@app.route('/resize', methods=['POST'])
def resize_image():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    resized_img = cv2.resize(img, (28, 28))
    _, img_encoded = cv2.imencode('.jpg', resized_img)
    resized_image_data = img_encoded.tobytes()
    return resized_image_data, 200

@app.route('/size', methods=['POST'])
def image_size():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img_size = img.shape
    return jsonify({'image_size': img_size})

@app.route('/array', methods=['POST'])
def image_array():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return jsonify({'image_array': img.tolist()})

@app.route('/border', methods=['POST'])
def image_with_border():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    bordered_image = cv2.copyMakeBorder(img, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    _, img_encoded = cv2.imencode('.jpg', bordered_image)
    bordered_image_data = img_encoded.tobytes()
    return bordered_image_data, 200

if __name__ == '__main__':
    app.run(debug=True)

