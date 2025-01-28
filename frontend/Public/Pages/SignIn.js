// This function is called after the sign_in.js script is loaded dynamically
function renderSignInPage() {
  const app = document.getElementById('app');  // The main content container
  
  // Define the HTML content for the sign-in page
  const signInHTML = `
  <h1>coucou</h1>
  `;
  
  // Insert the sign-in form into the main content area
  app.innerHTML = signInHTML;
}

