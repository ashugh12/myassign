figma.showUI(__html__, { width: 400, height: 400 });

figma.ui.onmessage = async (msg) => {
    if (msg.type === "analyze-design") {
        const selection = figma.currentPage.selection;

        if (selection.length === 0) {
            figma.ui.postMessage({ type: "error", message: "No image selected." });
            return;
        }

        const node = selection[0];
        if (node.type !== "FRAME" && node.type !== "RECTANGLE" && node.type !== "IMAGE") {
            figma.ui.postMessage({ type: "error", message: "Please select an image or frame." });
            return;
        }

        try {
            // Export the selected node as PNG
            const imageBytes = await node.exportAsync({ format: "PNG" });
            const blob = new Blob([imageBytes], { type: "image/png" });

            // Send to Flask server
            const formData = new FormData();
            formData.append("image", blob, "design.png");

            const response = await fetch("http://127.0.0.1:5000/analyze", {
                method: "POST",
                body: formData
            });

            const data = await response.json();
            
            if (data.error) {
                figma.ui.postMessage({ type: "error", message: data.error });
            } else {
                figma.ui.postMessage({ type: "analysis-complete", results: data.results });
            }
        } catch (error) {
            console.error("❌ Analysis failed:", error);
            figma.ui.postMessage({ type: "error", message: "Analysis failed." });
        }
    }
};
