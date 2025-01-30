
import homePage from "./Pages/homePage.js";
import register from "./Pages/register.js";
import logIn	from "./Pages/logIn.js";
import { registerHandler } from "./Scripts/registerHandler.js";

export default async function pageRouting() {
	const path = window.location.pathname;
	let contentDiv = document.getElementById("content");

	switch(path) {
		case "/":
			contentDiv.innerHTML = homePage();
			break ;
		case "/register":
			contentDiv.innerHTML = register();
			registerHandler();
			break ;
		case "/logIn":
			contentDiv.innerHTML = logIn();
			break ;
		default :
			contentDiv.innerHTML = `<h1 class="text-2xl text-red-600">Default Page</h1>`;
	}
}

// Handle navigation clicks dynamically
document.addEventListener("DOMContentLoaded", () => {
	document.querySelectorAll("[data-link]").forEach(link => {
		link.addEventListener("click", event => {
			event.preventDefault(); // Prevent full page reload
            const newPath = link.getAttribute("href");
            window.history.pushState({}, "", newPath); // Update browser URL without reloading
            pageRouting(); // Call function to update content dynamically
        });
    });
});

pageRouting();
