
export function signInHandler()
{
    const form = document.getElementById("signInForm");
    if (!form) return; // Prevent errors if form is not loaded

    form.addEventListener("submit", function (event)
	{
        event.preventDefault(); // Prevent page reload

        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        let errorMessage = document.getElementById("error-message");

        //TODO need to send the data to the backend and check
        //if it's valid data
    });
}
