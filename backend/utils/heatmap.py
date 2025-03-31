import cv2
import numpy as np

# If applied to an image, it will highlight highly visible regions in red/yellow and less noticeable areas in blue.
def generate_saliency_heatmap(image):
    """
    Generates a heatmap highlighting salient regions in an image.

    Parameters:
    - image (np.ndarray): Input image (BGR format).

    Returns:
    - heatmap (np.ndarray): Colored heatmap of saliency.
    - overlay (np.ndarray): Original image with heatmap overlay.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the saliency map
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    success, saliency_map = saliency.computeSaliency(gray)

    if not success:
        return None, None

    # Convert saliency map to 255 scale
    saliency_map = (saliency_map * 255).astype(np.uint8)

    # Apply a colormap to create a heatmap
    heatmap = cv2.applyColorMap(saliency_map, cv2.COLORMAP_JET)

    # Blend heatmap with original image for visualization
    overlay = cv2.addWeighted(image, 0.6, heatmap, 0.4, 0)

    return heatmap, overlay