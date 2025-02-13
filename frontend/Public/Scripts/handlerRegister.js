
import { fetchUserRegister } from "../Fetchers/fetcherUser.js";

export function handlerRegister() {
    const form = document.getElementById("formRegister");
    if (!form) return; // Prevent errors if form is not loaded

    const passwordInput = document.getElementById("password");
    const errorMessage = document.getElementById("password-error");

    function validatePassword(password) {
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return passwordRegex.test(password);
    }

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent page reload

        const email = document.getElementById("email").value;
        const password = passwordInput.value;
        const username = document.getElementById("username").value;

        // Password Validation Before Sending Request
        if (!validatePassword(password)) {
            errorMessage.textContent = "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character.";
            errorMessage.classList.remove("hidden");
            return; // Stop submission if password is invalid
        } else {
            errorMessage.classList.add("hidden");
        }

        // Proceed with Registration if Password is Valid
        const result = await fetchUserRegister(username, email, password);

        if (result.error) {
            errorMessage.textContent = result.error;
            errorMessage.classList.remove("hidden");
        } else {
            alert("Registration successful!");
            window.location.href = "/";
        }
    });
}

