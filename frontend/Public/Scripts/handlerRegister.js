
export function handlerRegister()
{
    const form = document.getElementById("formRegister");
    if (!form) return; // Prevent errors if form is not loaded

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent page reload

        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        let pseudo = document.getElementById("pseudo").value
        let errorMessage = document.getElementById("error-message");

        //TODO need to send the data to the backend and check
        //if it's valid data
        // to create a user i need to go send [userName, email, pswd] to /api/users (post)
    });
}
