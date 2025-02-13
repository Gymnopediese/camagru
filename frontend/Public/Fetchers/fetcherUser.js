
export async function fetchUserLogin(credential, password) {
    try {
        const response = await fetch("/api/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ credential, password }),
        });

        const data = await response.json();

        if (!response.ok) {
            console.log(data)
            throw new Error(data.message || "Invalid credentials");
        }

        return data;
    } catch (error) {
        return { error: error.message };
    }
}

export async function fetchUserRegister(username, email, password) {
    try {
        const response = await fetch("api/auth/signup", {
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
