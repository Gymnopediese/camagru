
import signIn from ".Pages/sign_in.js"

export default async function pageRouting()
{
	const path = window.location.pathname;
	let contentDiv = document.getElementById("content");

	switch(path)
	{
		case "/":
			contentDiv.innerHTML = homePage();
			break ;
	}
}
