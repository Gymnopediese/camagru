
import { fetchUser } from "../Fetchers/fetcherUser.js";

export function handlerLogin() {
    const form = document.getElementById("formLogin");
    if (!form) return;

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const   userName = document.getElementById("userName").value;
        const   password = document.getElementById("password").value;

        const result = await fetchUser(userName, password);

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
