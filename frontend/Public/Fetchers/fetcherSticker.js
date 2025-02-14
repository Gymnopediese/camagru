
export async function fetchStickerList() {
    try {
        const token = localStorage.getItem('token'); // Assuming token is stored in localStorage

        const response = await fetch("api/images/stickers", {
            method: "GET",
            headers: {
                "accept": "application/json",
                ...(token && { "Authorization": `Bearer ${token}` })
            },
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Error getting list stickers");
        }

        return data;

    } catch (error) {
        console.error("Upload error:", error);
        return { error: error.message };
    }
}

export async function fetchSticker(url) {
    try {
        const token = localStorage.getItem('token'); // Assuming token is stored in localStorage

        const response = await fetch(`api/images/${url}`, {
            method: "GET",
            headers: {
                "accept": "application/json",
                ...(token && { "Authorization": `Bearer ${token}` })
            },
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Error getting sticker");
        }

        return data;

    } catch (error) {
        console.error("Upload error:", error);
        return { error: error.message };
    }
}
