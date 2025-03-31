import cv2
import base64
import numpy as np

def encode_image_to_base64(image):
    """
    Converts an OpenCV image to a Base64 string.

    Parameters:
    - image (np.ndarray): Image to convert.

    Returns:
    - base64_str (str): Base64 encoded image.
    """
    # Ensure image is in correct format
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Invalid image provided for encoding.")

    # Convert to PNG format
    _, buffer = cv2.imencode('.png', image)
    
    # Encode to Base64
    base64_str = base64.b64encode(buffer).decode('utf-8')
    
    return base64_str

