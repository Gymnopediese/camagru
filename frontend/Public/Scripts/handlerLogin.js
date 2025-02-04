
import { fetchUser } from "../Fetchers/fetcherUser.js";

export function handlerLogin() {
    const form = document.getElementById("formLogin");
    if (!form) return;

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const   username = document.getElementById("username").value;
        const   password = document.getElementById("password").value;

        console.log("coucou")
        const result = await fetchUser(username, password);

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
