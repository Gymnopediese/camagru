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
                        x: canvas.width / 2 - selectedSticker.width / 2,
                        y: canvas.height / 2 - selectedSticker.height / 2
                    };
                    drawCanvas(); // Redraw canvas with the selected sticker
                };
            });

            stickerSelection.appendChild(stickerImage);
        });
    }

    // Function to draw the canvas
    function drawCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas before drawing

        // Draw video if available
        if (videoStream && videoStream.active) {
            ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
        }

        // Draw the background image (if uploaded)
        const backgroundImage = localStorage.getItem("backgroundImage");
        if (backgroundImage) {
            const img = new Image();
            img.src = backgroundImage;

            img.onload = function () {
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height); // Draw the background image
                drawSticker(); // After the background image is drawn, draw the sticker on top
            };
        } else {
            // If no background image is in localStorage, draw an empty canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        // Draw the sticker if it's set
        drawSticker();
    }

    // Function to draw the sticker
    function drawSticker() {
        if (selectedSticker) {
            ctx.drawImage(selectedSticker, stickerPosition.x, stickerPosition.y, 35, 35);
        }
    }

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

            // Upload to backend with the new prototype
            const stickerFromStorage = localStorage.getItem("selectedSticker");

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

    // Enable dragging of the sticker
    canvas.addEventListener("mousedown", (e) => {
        if (!selectedSticker) return;

        const mouseX = e.offsetX;
        const mouseY = e.offsetY;

        // Check if the mouse is over the sticker
        if (mouseX >= stickerPosition.x && mouseX <= stickerPosition.x + selectedSticker.width &&
            mouseY >= stickerPosition.y && mouseY <= stickerPosition.y + selectedSticker.height) {
            isDragging = true;
            offsetX = mouseX - stickerPosition.x;
            offsetY = mouseY - stickerPosition.y;
        }
    });

    canvas.addEventListener("mousemove", (e) => {
        if (isDragging) {
            const mouseX = e.offsetX;
            const mouseY = e.offsetY;

            // Update the sticker's position while dragging
            stickerPosition.x = mouseX - offsetX;
            stickerPosition.y = mouseY - offsetY;

            drawCanvas(); // Redraw the canvas to update the sticker position
        }
    });

    canvas.addEventListener("mouseup", () => {
        isDragging = false;
    });

    loadStickers();
}

