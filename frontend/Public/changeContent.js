
// import pages
import homePage from "./Pages/homePage.js";
import register from "./Pages/register.js";
import login	from "./Pages/login.js";
import camera   from "./Pages/camera.js";

// import scripts
import { handlerRegister }  from "./Scripts/handlerRegister.js";
import { handlerLogin }     from "./Scripts/handlerLogin.js";
import { handlerCamera }    from "./Scripts/handlerCamera.js";

function updateNavButton() {
    const token = localStorage.getItem("token");
    const navButton = document.getElementById("nav-buttons");

    if (!navButton) return;

    navButton.innerHTML = "";

    if (token) {
        // User is logged in
        navButton.innerHTML = `
            <li><a href="/" class="route text-white px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg" data-link>Home</a></li>
            <li><a href="/camera" class="route text-white px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg" data-link>Camera</a></li>
            <li><button id="logout" class="text-white px-4 py-2 bg-red-500 hover:bg-red-600 rounded-lg">Disconnect</button></li>
        `;

        // Attach logout event
        document.getElementById("logout").addEventListener("click", () => {
            localStorage.removeItem("token");  // Remove token
            updateNavButton();  // Refresh button state
            pageRouting(); // Ensure content updates after logout
        });
    } else {
        // User is NOT logged in
        navButton.innerHTML = `
            <li><a href="/login" class="route text-white px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg" data-link>Login</a></li>
            <li><a href="/register" class="route text-white px-4 py-2 bg-blue-500 hover:bg-blue-600 rounded-lg" data-link>Sign In</a></li>
        `;
    }
}

export default async function pageRouting() {
	const path = window.location.pathname;
	let contentDiv = document.getElementById("content");
    const token = localStorage.getItem("token")

	switch(path) {
		case "/":
			contentDiv.innerHTML = homePage();
			break ;
		case "/register":
			contentDiv.innerHTML = register();
			handlerRegister();
			break ;
		case "/login":
			contentDiv.innerHTML = login();
			handlerLogin();
			break ;
        case "/camera":
            if (!token) {
                // If user is not logged in, redirect to login page
                window.history.pushState({}, "", "/login");
                contentDiv.innerHTML = login(); // Load the login page
                handlerLogin(); // Initialize login handler
                break
            }
            contentDiv.innerHTML = camera();
            handlerCamera();
            break ;
		default :
			contentDiv.innerHTML = `<h1 class="text-2xl text-red-600">Default Page</h1>`;
	}

	updateNavButton(); // Update the nav bar if user is log in or not
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
