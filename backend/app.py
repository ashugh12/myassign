import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
from PIL import Image
import io
from flask_cors import CORS  # ✅ Import CORS
from models.predict_saliency import predict_saliency

from utils.encodeTobase64 import encode_image_to_base64
from utils.heatmap import generate_saliency_heatmap


app = Flask(__name__)
CORS(app)  # ✅ Enable CORS



@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image = Image.open(file.stream).convert("RGB")
    image_np = np.array(image)
    image_cv2 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    saliency_map, marked_image = predict_saliency(image_cv2)
    # Example 1: Segment using a bounding box
    # mask, segmented_image = segment_with_sam(image_cv2, box=[50, 100, 200, 250])


    if saliency_map is None:
        return jsonify({"error": "Saliency computation failed"}), 500

    # Convert to Base64

    saliency_base64=encode_image_to_base64(saliency_map)

    marked_base64=encode_image_to_base64(marked_image)

    print("✅ Saliency map and marked image generated!")  # Debugging
    print("Saliency Base64 Length:", len(saliency_base64))  # Debugging
    print("Marked Image Base64 Length:", len(marked_base64))  # Debugging

    heatmap, overlay = generate_saliency_heatmap(image_cv2)

    heatmap_base64= encode_image_to_base64(heatmap)
    overlay_base64= encode_image_to_base64(overlay)

    return jsonify({
        "saliency_map": saliency_base64,
        "marked_image": marked_base64,
        "heat_map": heatmap_base64,
        "overlay_image": overlay_base64
    })




if __name__ == "__main__":
    app.run(debug=True)
