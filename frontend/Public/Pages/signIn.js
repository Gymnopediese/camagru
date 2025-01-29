
export default function signIn() {
    return `
        <div class="flex items-center justify-center min-h-screen">
            <div class="bg-white p-8 rounded-lg shadow-lg w-96">
                <h2 class="text-2xl font-semibold text-center text-gray-800">Sign In</h2>

                <form id="signInForm" class="mt-4">
                    <!-- Email Input -->
                    <label for="email" class="block text-gray-700">Email:</label>
                    <input type="email" id="email" name="email" placeholder="Enter your email"
                        class="w-full p-2 border border-gray-300 rounded-lg mt-1 focus:ring-2 focus:ring-blue-500">

                    <!-- Password Input -->
                    <label for="password" class="block text-gray-700 mt-4">Password:</label>
                    <input type="password" id="password" name="password" placeholder="Enter your password"
                        class="w-full p-2 border border-gray-300 rounded-lg mt-1 focus:ring-2 focus:ring-blue-500">

                    <!-- Submit Button -->
                    <button type="submit"
                        class="w-full bg-blue-500 text-white p-2 mt-4 rounded-lg hover:bg-blue-600 transition duration-300">
                        Sign In
                    </button>

                </form>

                <!-- Error Message -->
                <p id="error-message" class="text-red-500 text-sm mt-2 text-center hidden">Invalid email or password.</p>
            </div>
        </div>
    `;
}
