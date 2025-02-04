
export async function fetchUser(username, password) {
    try {
        const response = await fetch("/api/users/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
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
