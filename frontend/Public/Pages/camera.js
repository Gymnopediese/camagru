
export default function camera() {
  return `
    <div class="flex justify-center items-center min-h-screen bg-gray-100">

      <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-7xl flex gap-8">

        <!-- Left: Camera Section -->
        <div class="flex flex-col items-center w-3/4">
          <h2 class="text-3xl font-semibold text-gray-800 mb-4">Camera</h2>

          <div class="relative border-4 border-gray-400 rounded-lg overflow-hidden">
            <canvas id="canvas" class="rounded-lg w-[900px] h-[700px]"></canvas>
            <img id="sticker" class="absolute hidden cursor-grab" draggable="true">
          </div>

          <!-- Title & Description -->
          <div class="w-full mt-4">
            <input id="imageTitle" type="text" placeholder="Title" class="w-full p-3 border rounded-lg">
            <textarea id="imageDescription" placeholder="Description" class="w-full p-3 border rounded-lg mt-2"></textarea>
          </div>

          <!-- Controls -->
          <div class="flex gap-4 mt-4">
            <button id="startButton" class="bg-green-500 text-white px-5 py-3 rounded-lg hover:bg-green-600 transition">Start Camera</button>
            <button id="captureButton" class="bg-blue-500 text-white px-5 py-3 rounded-lg hover:bg-blue-600 transition">Take Picture</button>
            <button id="stopButton" class="bg-red-500 text-white px-5 py-3 rounded-lg hover:bg-red-600 transition">Stop Camera</button>

            <!-- Upload Image Button -->
            <input type="file" id="uploadInput" accept="image/*" class="hidden">
            <button id="uploadButton" class="bg-purple-500 text-white px-4 py-2 rounded-lg hover:bg-purple-600 transition">Upload Image</button>
          </div>
        </div>

        <!-- Right: Sticker Selection -->
        <div class="flex flex-col items-center w-1/4">
          <h3 class="text-xl font-medium text-gray-700 mb-3">Choose a Sticker:</h3>
          <div id="stickerSelection" class="grid grid-cols-2 gap-3 p-3 overflow-y-auto max-h-[600px] border border-gray-300 rounded-lg w-full">
            <!-- Stickers will be dynamically inserted here -->
          </div>
        </div>

      </div>
    </div>
  `;
}
