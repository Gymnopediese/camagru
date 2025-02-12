
export default function camera() {
  return `
        <div class="flex items-center justify-center min-h-screen">
            <div class="bg-white p-8 rounded-lg shadow-lg w-96">
                <h2 class="text-2xl font-semibold text-center text-gray-800 mb-4">Camera Page</h2>

                <!-- Video Element -->
                <video id="video" class="mx-auto mb-4 rounded-lg" width="640" height="480" autoplay></video>

                <!-- Canvas Element -->
                <canvas id="canvas" class="mx-auto rounded-lg border-2" width="640" height="480"></canvas>

                <button id="startButton" class="w-full bg-blue-500 text-white p-2 mt-4 rounded-lg hover:bg-blue-600 transition duration-300">Start Camera</button>
            </div>
        </div>
    `;
}

