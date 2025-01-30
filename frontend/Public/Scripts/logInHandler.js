
export function handleLogin() {
    const form = document.getElementById("LogInForm");
    if (!form) return;

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        let identifier = document.getElementById("identifier").value;
        let password = document.getElementById("password").value;
        let errorMessage = document.getElementById("error-message");

        const result = await logInFetcher(identifier, password);

        if (result.error) {
            errorMessage.textContent = result.error;
            errorMessage.classList.remove("hidden");
        } else {
            localStorage.setItem("authToken", result.token);
            alert("Login successful!");
            window.location.href = "/";
        }
    });
}
