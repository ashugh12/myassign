import cv2
import numpy as np

def get_salient_points(saliency_map, num_regions=5):
    # Normalize the saliency map
    saliency_map = cv2.normalize(saliency_map, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Adaptive thresholding for better contour detection
    _, binary_map = cv2.threshold(saliency_map, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort by contour area to get the most significant ones
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:num_regions]

    # Extract bounding box coordinates
    salient_regions = [cv2.boundingRect(cnt) for cnt in contours]

    return salient_regions


def mark_points_on_image(image, keypoints, size=15):
    marked_image = image.copy()

    for (x, y, w, h) in keypoints:
        half_size = size // 2

        # Draw a bounding box instead of a small square
        cv2.rectangle(marked_image, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

    return marked_image