# Saliency Prediction API

This Flask-based API processes images to generate saliency maps, marked images, heatmaps, and overlay images using computer vision techniques.

## Features
- Accepts image uploads for processing.
- Generates saliency maps using `predict_saliency`.
- Generates heatmaps and overlay images using `generate_saliency_heatmap`.
- Returns processed images in Base64 format for easy integration.
- Supports Cross-Origin Resource Sharing (CORS) for frontend compatibility.

## Installation
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the Flask application:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/predict`.

## API Endpoint
### `POST /predict`
#### Request
- **Form Data**: `image` (file)

#### Response (JSON)
```json
{
  "saliency_map": "<Base64_encoded_image>",
  "marked_image": "<Base64_encoded_image>",
  "heat_map": "<Base64_encoded_image>",
  "overlay_image": "<Base64_encoded_image>"
}
```

## Dependencies
- Flask
- Flask-CORS
- OpenCV
- NumPy
- Pillow


## My understandin
I have used the Computer Vision technique uses the  OpenCv Saliency Detection Model(it mix of ML + CV)

Advantage of this model:
- Lightweight
- Analyze frequency domain of an image to detect visually important regions
- Work without deeplearning, purely on the mathematical approach(we can use the DeepGaze use the sliency but could learn from the data)
- This model help to generates the heatmap and salient points for the attention prediction


## What I did
I have created the backend processing for this. I don't know whether I should make it available on the figma as plugin. But I thougth that thing need to be structured manner. 

On the honest ground, I have own this completely. 

Saliency is lightweight which can work fast. 

 ##  About the picture
- 1️⃣ Saliency Map 🧠🔍

A grayscale heatmap highlighting the most attention-grabbing areas in an image.

Generated using the Static Saliency Spectral Residual model, which detects visually important regions without deep learning.

- 2️⃣ Marked Image (with Points) 🎯

The original image with red markers indicating the top salient points.

These points represent regions that are most likely to attract user attention.

- 3️⃣ Heatmap of Image 🌡️🎨

A color-coded representation of saliency, where warmer colors (red/yellow) indicate high attention areas and cooler colors (blue) indicate low attention areas.

Helps visualize how human attention might be distributed across the image.

- 4️⃣ Overlay of Image 🖼️

The saliency heatmap blended with the original image.

Provides an intuitive view of how visual focus interacts with the overall composition.




