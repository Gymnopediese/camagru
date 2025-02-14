
export async function fetchPublication(title, description, imageFile, pos, stickerPath) {
    try {
        const token = localStorage.getItem('token'); // Assuming token is stored in localStorage
        const formData = new FormData();
        formData.append("image", imageFile);

        const url = `api/publications/?title=${encodeURIComponent(title)}&description=${encodeURIComponent(description)}&posX=${encodeURIComponent(pos.x)}&posY=${encodeURIComponent(pos.y)}&stickerPath=${encodeURIComponent(stickerPath)}`;

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "accept": "application/json",
                ...(token && { "Authorization": `Bearer ${token}` })
            },
            body: formData,
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Error uploading image");
        }

        return data;

    } catch (error) {
        console.error("Upload error:", error);
        return { error: error.message };
    }
}

