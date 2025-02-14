import { fetchPublication } from "../Fetchers/fetcherPost.js";
import { fetchStickerList } from "../Fetchers/fetcherSticker.js";

export function handlerCamera() {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let videoStream = null;
    let videoElement = null;

    const startButton = document.getElementById("startButton");
    const captureButton = document.getElementById("captureButton");
    const stopButton = document.getElementById("stopButton");
    const uploadButton = document.getElementById("uploadButton");
    const uploadInput = document.getElementById("uploadInput");

    const stickerSelection = document.getElementById("stickerSelection");
    let selectedSticker = null; // Will hold the sticker image after being clicked
    let stickerPosition = { x: 450, y: 350 }; // Starting at center

    let isDragging = false; // Flag to track if a sticker is being dragged
    let offsetX = 0;
    let offsetY = 0;

    const titleInput = document.getElementById("imageTitle");
    const descriptionInput = document.getElementById("imageDescription");

    // Function to load stickers from the backend and display them
    async function loadStickers() {
        const stickesListResponse = await fetchStickerList();

        if (stickesListResponse.error) {
            alert("Error loading Stickers");
            return;
        }
        const stickerList = stickesListResponse.stickers; // create array of stickers
        stickerSelection.innerHTML = ""; // clear previous stickers

        // Loop through the stickers list and display each one
        stickerList.forEach((stickerPath) => {
            const stickerImage = document.createElement("img");

            // Replace / with #
            const formattedPath = stickerPath.replace(/\//g, '%23');

            stickerImage.src = `api/images/${formattedPath}`;
            stickerImage.classList.add("w-20", "h-20", "cursor-pointer", "border", "border-gray-300", "rounded-lg", "p-1");

            // When a sticker is clicked, store it in localStorage
            stickerImage.addEventListener("click", () => {
                const sticker = new Image();
                sticker.src = `api/images/${formattedPath}`; // Path of the sticker

                // Store the sticker image in localStorage
                sticker.onload = () => {
                    localStorage.setItem("selectedSticker", sticker.src); // Save the image path in localStorage
                    selectedSticker = sticker;
                    stickerPosition = {
                        x: canvas.width / 2 - 50 / 2, // Centering the sticker with fixed size 50x50
                        y: canvas.height / 2 - 50 / 2
                    };
                    drawCanvas(); // Redraw canvas with the selected sticker
                };
            });

            stickerSelection.appendChild(stickerImage);
        });
    }

    // Function to draw the canvas (video feed + sticker)
    function drawCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas before drawing

        // Draw the uploaded image if it's stored in localStorage
        const backgroundImage = localStorage.getItem("backgroundImage");
        if (backgroundImage) {
            const img = new Image();
            img.onload = function () {
                // Draw the uploaded image onto the canvas
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                // Draw the sticker on top of the uploaded image
                drawSticker();
            };
            img.src = backgroundImage;
        }

        // If the video stream is active, draw the video feed
        if (videoStream) {
            ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height); // Draw video feed as background
        }

        // Draw the sticker if it's set
        drawSticker();
    }

    // Function to draw the sticker with fixed size 50x50px
    function drawSticker() {
        if (selectedSticker) {
            ctx.drawImage(selectedSticker, stickerPosition.x, stickerPosition.y, 50, 50); // Draw the sticker on top of the background
        }
    }

    // Start Camera
    startButton.addEventListener("click", async () => {
        try {
            videoStream = await navigator.mediaDevices.getUserMedia({ video: true });

            videoElement = document.createElement("video");
            videoElement.srcObject = videoStream;
            videoElement.play();

            // Update the canvas at a regular interval to draw the video feed
            function drawFrame() {
                if (!videoStream.active) return;
                drawCanvas(); // Redraw the canvas each time the video frame updates
                requestAnimationFrame(drawFrame); // Continue drawing frames
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

            // Upload to backend with the new prototype
            const stickerFromStorage = localStorage.getItem("selectedSticker");
            console.log(stickerFromStorage);

            const response = await fetchPublication(title, description, blob, stickerPosition, stickerFromStorage);

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

    // Handle image upload from file input
    uploadButton.addEventListener("click", () => {
        uploadInput.click(); // Trigger file input when upload button is clicked
    });

    uploadInput.addEventListener("change", async (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                const img = new Image();
                img.onload = function () {
                    // Clear the canvas before drawing the new image
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    // Draw the uploaded image onto the canvas
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                    // Save the uploaded image in localStorage as background
                    localStorage.setItem("backgroundImage", e.target.result);
                };
                img.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    });


    // Update the position of the sticker with mouse movement
    canvas.addEventListener("mousemove", (e) => {
        if (selectedSticker && isDragging) {
            // Update the sticker's position based on mouse movement
            stickerPosition.x = e.offsetX - offsetX;
            stickerPosition.y = e.offsetY - offsetY;
            drawCanvas(); // Redraw the canvas after moving the sticker
        }
    });

    // When mouse is clicked, start dragging
    canvas.addEventListener("mousedown", (e) => {
        if (selectedSticker) {
            const mouseX = e.offsetX;
            const mouseY = e.offsetY;

            // Check if the mouse is on the sticker
            if (mouseX > stickerPosition.x && mouseX < stickerPosition.x + 50 && mouseY > stickerPosition.y && mouseY < stickerPosition.y + 50) {
                isDragging = true;
                offsetX = mouseX - stickerPosition.x;
                offsetY = mouseY - stickerPosition.y;
            }
        }
    });

    // When mouse is released, stop dragging
    canvas.addEventListener("mouseup", () => {
        isDragging = false;
    });

    loadStickers();
}

