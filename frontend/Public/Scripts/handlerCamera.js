export function handlerCamera() {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let videoStream = null;

    const startButton = document.getElementById("startButton");
    const captureButton = document.getElementById("captureButton");
    const stopButton = document.getElementById("stopButton");
    const uploadInput = document.getElementById("uploadInput");
    const uploadButton = document.getElementById("uploadButton");

    // Start Camera
    startButton.addEventListener("click", async () => {
        try {
            videoStream = await navigator.mediaDevices.getUserMedia({ video: true });

            const video = document.createElement("video");
            video.srcObject = videoStream;
            video.play();

            // Draw video stream on canvas in real time
            function drawFrame() {
                if (!videoStream.active) return;
                ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                requestAnimationFrame(drawFrame);
            }

            drawFrame();
        } catch (err) {
            console.error("Error accessing camera:", err);
        }
    });

    // Capture Image
    captureButton.addEventListener("click", () => {
        // Captures the current frame (already on canvas)
        console.log("Picture taken!");
    });

    // Stop Camera
    stopButton.addEventListener("click", () => {
        if (videoStream) {
            videoStream.getTracks().forEach(track => track.stop());
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas
        }
    });

    // Upload Image
    uploadButton.addEventListener("click", () => uploadInput.click());

    uploadInput.addEventListener("change", (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                const img = new Image();
                img.onload = () => {
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
}

