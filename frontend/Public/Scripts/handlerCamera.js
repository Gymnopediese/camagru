
import { fetchPublication } from "../Fetchers/fetcherPost.js";

export function handlerCamera() {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let videoStream = null;
    let videoElement = null;

    const startButton = document.getElementById("startButton");
    const captureButton = document.getElementById("captureButton");
    const stopButton = document.getElementById("stopButton");

    const titleInput = document.getElementById("imageTitle");
    const descriptionInput = document.getElementById("imageDescription");

    // Start Camera
    startButton.addEventListener("click", async () => {
        try {
            videoStream = await navigator.mediaDevices.getUserMedia({ video: true });

            videoElement = document.createElement("video");
            videoElement.srcObject = videoStream;
            videoElement.play();

            function drawFrame() {
                if (!videoStream.active) return;
                ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
                requestAnimationFrame(drawFrame);
            }

            drawFrame();
        } catch (err) {
            console.error("Error accessing camera:", err);
        }
    });

    // Capture Image & Upload
    captureButton.addEventListener("click", async () => {
        if (!videoStream) {
            alert("Please start the camera first.");
            return;
        }

        const title = titleInput.value.trim();
        const description = descriptionInput.value.trim();

        if (!title || !description) {
            alert("Please enter a title and description.");
            return;
        }

        // Convert canvas content to a Blob
        canvas.toBlob(async (blob) => {
            if (!blob) {
                alert("Error capturing image.");
                return;
            }

            // Upload to backend
            const response = await fetchPublication(title, description, blob);

            if (response.error) {
                alert("Upload failed: " + response.error);
            } else {
                alert("Image uploaded successfully!");
            }
        }, "image/png");
    });

    // Stop Camera
    stopButton.addEventListener("click", () => {
        if (videoStream) {
            videoStream.getTracks().forEach(track => track.stop());
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    });
}

