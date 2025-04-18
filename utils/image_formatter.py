import base64
import cv2
import numpy as np
from io import BytesIO


def decode_base64_image(encoded_str):
   
    if ',' in encoded_str:
        encoded_str = encoded_str.split(',')[1]
        
    try:
        image_bytes = base64.b64decode(encoded_str)
        image_np = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        print(f"Error decoding base64 image: {e}")
        return None

def encode_image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    base64_str= base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_str}"

