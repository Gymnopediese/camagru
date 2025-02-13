
import { fetchUserLogin } from "../Fetchers/fetcherUser.js";

export function handlerLogin() {
    const form = document.getElementById("formLogin");
    if (!form) return;

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const   credential = document.getElementById("credential").value;
        const   password = document.getElementById("password").value;

        const result = await fetchUserLogin(credential, password);

        if (result.error) {
            console.log(result.error)
        } else {
            localStorage.setItem("token", result.token); // store the token from backend
            alert("Login successful!");
            window.location.href = "/";
        }
    });
}
