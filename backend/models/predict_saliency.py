import cv2
import numpy as np

from utils.image_processing import get_salient_points, mark_points_on_image

def predict_saliency(image):
    """
    Detects saliency regions using OpenCV.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute Spectral Residual Saliency Map
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    success, saliency_map = saliency.computeSaliency(gray)

    if not success:
        return None, None

    # Convert saliency map to 255 scale
    saliency_map = cv2.convertScaleAbs(saliency_map, alpha=255)
    saliency_map = cv2.GaussianBlur(saliency_map, (5, 5), 0)  # Reduce noise

    # Compute Fine-Grained Saliency and blend with SpectralResidual
    fine_saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    success, fine_map = fine_saliency.computeSaliency(gray)
    
    if success:
        fine_map = cv2.convertScaleAbs(fine_map, alpha=255)
        saliency_map = cv2.addWeighted(saliency_map, 0.7, fine_map, 0.3, 0)

    # Find top salient regions
    keypoints = get_salient_points(saliency_map, 5)

    # Overlay the points on the image
    marked_image = mark_points_on_image(image, keypoints)

    return saliency_map, marked_image
