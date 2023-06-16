import requests
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Helper function to display an image
def display_image(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Base URL of your API running on localhost
base_url = 'http://localhost:5000'

# Read the image
image_path = input("Enter path of image you want to use: ")
image = cv2.imread(image_path)

user_input = int(input('''Type a number: 1,2,3,4 for the 4 different tasks: 
1. Resize
2. Obtain size
3. Image as List
4. 3-pixel black border
'''))
if (user_input == 1):
    files = {'image': open(image_path, 'rb')}
    resize_url = base_url + '/resize'
    response = requests.post(resize_url, files=files)
    resized_image_data = np.frombuffer(response.content, np.uint8)
    resized_image = cv2.imdecode(resized_image_data, cv2.IMREAD_COLOR)
    display_image(resized_image)

elif (user_input == 2):
    files = {'image': open(image_path, 'rb')}
    size_url = base_url + '/size'
    response = requests.post(size_url, files=files)
    image_size = response.json()['image_size']
    print('Image Size:', image_size)

elif (user_input == 3):
    files = {'image': open(image_path, 'rb')}
    array_url = base_url + '/array'
    response = requests.post(array_url, files=files)
    image_array = response.json()['image_array']
    print('Image Array:', image_array)

elif (user_input == 4):
    files = {'image': open(image_path, 'rb')}
    border_url = base_url + '/border'
    response = requests.post(border_url, files=files)
    bordered_image_data = np.frombuffer(response.content, np.uint8)
    bordered_image = cv2.imdecode(bordered_image_data, cv2.IMREAD_COLOR)
    display_image(bordered_image)