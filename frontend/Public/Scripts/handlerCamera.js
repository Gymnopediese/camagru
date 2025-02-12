
export function handlerCamera() {
    const startButton = document.getElementById("startButton");
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    if (!startButton) return;

    startButton.addEventListener("click", function () {
        // Start camera when the user clicks the "Start Camera" button
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                // Attach the stream to the video element
                video.srcObject = stream;

                // Start drawing the video to canvas
                function drawToCanvas() {
                    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                    requestAnimationFrame(drawToCanvas); // Continuously call this function
                }

                drawToCanvas(); // Start drawing video frames to canvas
            })
            .catch(function (error) {
                console.error("Error accessing camera: ", error);
            });
    });
}

