
export async function fetchUserLogin(username, password) {
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

        return data;
    } catch (error) {
        return { error: error.message };
    }
}

export async function fetchUserRegister(username, email, password) {
    try {
        const response = await fetch("api/users/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({username, email, password }),
        });

        const data = await response.json()

        if (!response.ok) {
            throw new Error(data.message || "Invalid credentials");
        }

        return data;
    } catch (error) {
        return { error: error.message };
    }
}
