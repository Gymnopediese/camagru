
export async function fetchUser(userName, password) {
    try {
        const response = await fetch("/api/usres/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ userName, password }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Invalid credentials");
        }

        return data; // Returns { token: "...", user: { ... } }
    } catch (error) {
        return { error: error.message };
    }
}
