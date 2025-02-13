
export default function camera() {
  return `
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg flex flex-col items-center space-y-4">

        <h2 class="text-2xl font-semibold text-gray-800">Camera Page</h2>

        <!-- Camera Preview (Canvas) -->
        <div class="relative border-4 border-gray-300 rounded-lg overflow-hidden">
          <canvas id="canvas" class="rounded-lg w-[640px] h-[480px]"></canvas>
        </div>

        <!-- Title & Description Inputs -->
        <input id="imageTitle" type="text" placeholder="Title" class="w-full p-2 border rounded-lg">
        <textarea id="imageDescription" placeholder="Description" class="w-full p-2 border rounded-lg"></textarea>

        <!-- Controls -->
        <div class="flex flex-wrap justify-center gap-3 w-full mt-4">
          <button id="startButton" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">Start Camera</button>
          <button id="captureButton" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">Take Picture</button>
          <button id="stopButton" class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">Stop Camera</button>
        </div>
      </div>
    </div>
  `;
}

