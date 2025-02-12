
import { fetchUserLogin } from "../Fetchers/fetcherUser.js";

export function handlerLogin() {
    const form = document.getElementById("formLogin");
    if (!form) return;

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const   username = document.getElementById("username").value;
        const   password = document.getElementById("password").value;

        const result = await fetchUserLogin(username, password);

        if (result.error) {
            errorMessage.textContent = result.error;
            errorMessage.classList.remove("hidden");
        } else {
            localStorage.setItem("token", result.token); // store the token from backend
            alert("Login successful!");
            window.location.href = "/";
        }
    });
}
