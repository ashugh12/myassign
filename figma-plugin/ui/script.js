document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const fileInput = document.getElementById("imageUpload");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Failed to analyze image");

        const data = await response.json();

        // Display saliency map
        document.getElementById("saliencyImage").src = "data:image/png;base64," + data.saliency_map;
        document.getElementById("saliencyImage").style.display = "block";

        // Display marked image with points
        document.getElementById("markedImage").src = "data:image/png;base64," + data.marked_image;
        document.getElementById("markedImage").style.display = "block";

        // Display heat map
        document.getElementById("heatMapImage").src = "data:image/png;base64," + data.heat_map;
        document.getElementById("heatMapImage").style.display = "block";


        // Display overlay image
        document.getElementById("overlayImage").src = "data:image/png;base64," + data.overlay_image;
        document.getElementById("overlayImage").style.display = "block";
        
        console.log("✅ Image analyzed successfully!");

    } catch (error) {
        alert("Error processing image!");
        console.error(error);
    }
});

const saliencyImg = document.getElementById("saliencyImage");
const markedImg = document.getElementById("markedImage");
const heatMapImg = document.getElementById("heatMapImage");
const overlayImg = document.getElementById("overlayImage");

saliencyImg.src = `data:image/png;base64,${data.saliency_map}`;
saliencyImg.style.display = "block";

markedImg.src = `data:image/png;base64,${data.marked_image}`;
markedImg.style.display = "block";

heatMapImg.src = `data:image/png;base64,${data.heat_map}`;
heatMapImg.style.display = "block";

overlayImg.src = `data:image/png;base64,${data.overlay_image}`;
overlayImg.style.display = "block";

console.log("✅ Saliency and Marked Images Set!");

document.getElementById("closeBtn").addEventListener("click", () => {
    parent.postMessage({ pluginMessage: { type: "close" } }, "*");
});
