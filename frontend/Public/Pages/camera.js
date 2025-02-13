
export default function camera() {
  return `
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg flex flex-col items-center space-y-4">

        <h2 class="text-2xl font-semibold text-gray-800">Camera Page</h2>

        <!-- Camera Preview (Canvas) -->
        <div class="relative border-4 border-gray-300 rounded-lg overflow-hidden">
          <canvas id="canvas" class="rounded-lg w-[640px] h-[480px]"></canvas>
        </div>

        <!-- Controls -->
        <div class="flex flex-wrap justify-center gap-3 w-full mt-4">
          <button id="startButton" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">Start Camera</button>
          <button id="captureButton" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">Take Picture</button>
          <button id="stopButton" class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">Stop Camera</button>
          <input type="file" id="uploadInput" accept="image/*" class="hidden">
          <button id="uploadButton" class="bg-purple-500 text-white px-4 py-2 rounded-lg hover:bg-purple-600 transition">Import Picture</button>
        </div>
      </div>
    </div>
  `;
}
