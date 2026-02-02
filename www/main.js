// // GG1 Voice Assistant - Cross-browser version with WAV recording
// const startBtn = document.getElementById('start-btn');
// const responseDiv = document.getElementById('response');

// let audioContext;
// let recorder;
// let isRecording = false;

// // Check if browser supports Web Audio API
// if (!window.AudioContext && !window.webkitAudioContext) {
//     alert('Your browser does not support the Web Audio API. Please use a modern browser.');
// } else {
//     startBtn.addEventListener('click', toggleRecording);
// }

// async function toggleRecording() {
//     if (!isRecording) {
//         await startRecording();
//     } else {
//         stopRecording();
//     }
// }

// async function startRecording() {
//     try {
//         const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
//         audioContext = new (window.AudioContext || window.webkitAudioContext)();

//         const input = audioContext.createMediaStreamSource(stream);
//         recorder = new Recorder(input, { numChannels: 1 });

//         recorder.record();
//         isRecording = true;

//         startBtn.innerHTML = '<i class="fas fa-stop"></i> Stop Recording';
//         startBtn.classList.remove('btn-primary');
//         startBtn.classList.add('btn-danger');
//         responseDiv.style.display = 'none';

//     } catch (error) {
//         console.error('Error starting recording:', error);
//         alert('Could not access microphone. Please check permissions.');
//     }
// }

// function stopRecording() {
//     if (recorder && isRecording) {
//         recorder.stop();
//         isRecording = false;

//         startBtn.innerHTML = '<i class="fas fa-microphone"></i> Start Recording';
//         startBtn.classList.remove('btn-danger');
//         startBtn.classList.add('btn-primary');

//         recorder.exportWAV(async (blob) => {
//             await processAudio(blob);
//             recorder.clear();
//         });
//     }
// }

// async function processAudio(audioBlob) {
//     try {
//         const formData = new FormData();
//         formData.append('audio', audioBlob, 'recording.wav');

//         const response = await fetch('http://localhost:5000/process_audio', {
//             method: 'POST',
//             body: formData
//         });

//         const result = await response.json();

//         if (result.success) {
//             displayResponse(result.response);
//             speakResponse(result.response);
//         } else {
//             displayResponse('Sorry, I couldn\'t process that audio. ' + result.error);
//         }

//     } catch (error) {
//         console.error('Error processing audio:', error);
//         displayResponse('Sorry, there was an error processing your request.');
//     }
// }

// function displayResponse(text) {
//     responseDiv.innerHTML = `<p>${text}</p>`;
//     responseDiv.style.display = 'block';
// }

// function speakResponse(text) {
//     if ('speechSynthesis' in window) {
//         const utterance = new SpeechSynthesisUtterance(text);
//         utterance.rate = 0.9;
//         utterance.pitch = 1;
//         utterance.volume = 0.8;

//         // Optional: Choose a voice
//         const voices = speechSynthesis.getVoices();
//         const englishVoice = voices.find(voice => voice.lang.startsWith('en'));
//         if (englishVoice) {
//             utterance.voice = englishVoice;
//         }

//         speechSynthesis.speak(utterance);
//     } else {
//         console.warn('Speech synthesis not supported');
//     }
// }

// // Load voices when available
// if ('speechSynthesis' in window) {
//     speechSynthesis.onvoiceschanged = function() {
//         // Voices loaded
//     };
// }

// // Simple Recorder.js implementation for WAV recording
// class Recorder {
//     constructor(source, cfg = {}) {
//         this.config = {
//             numChannels: cfg.numChannels || 2,
//             ...cfg
//         };
//         this.recording = false;
//         this.buffers = [];
//         this.init(source);
//     }

//     init(source) {
//         const { numChannels } = this.config;
//         this.context = source.context;
//         this.node = (this.context.createScriptProcessor || this.context.createJavaScriptNode).call(
//             this.context,
//             4096,
//             numChannels,
//             numChannels
//         );

//         this.node.onaudioprocess = (e) => {
//             if (!this.recording) return;
//             const buffer = [];
//             for (let channel = 0; channel < numChannels; channel++) {
//                 buffer.push(new Float32Array(e.inputBuffer.getChannelData(channel)));
//             }
//             this.buffers.push(buffer);
//         };

//         source.connect(this.node);
//         this.node.connect(this.context.destination);
//     }

//     record() {
//         this.recording = true;
//     }

//     stop() {
//         this.recording = false;
//     }

//     clear() {
//         this.buffers = [];
//     }

//     exportWAV(callback) {
//         const { numChannels, sampleRate = this.context.sampleRate } = this.config;
//         const buffers = this.buffers;
//         const length = buffers.length * buffers[0][0].length;
//         const arrayBuffer = new ArrayBuffer(44 + length * numChannels * 2);
//         const view = new DataView(arrayBuffer);

//         const writeString = (offset, string) => {
//             for (let i = 0; i < string.length; i++) {
//                 view.setUint8(offset + i, string.charCodeAt(i));
//             }
//         };

//         // WAV header
//         writeString(0, 'RIFF');
//         view.setUint32(4, 36 + length * numChannels * 2, true);
//         writeString(8, 'WAVE');
//         writeString(12, 'fmt ');
//         view.setUint32(16, 16, true);
//         view.setUint16(20, 1, true);
//         view.setUint16(22, numChannels, true);
//         view.setUint32(24, sampleRate, true);
//         view.setUint32(28, sampleRate * numChannels * 2, true);
//         view.setUint16(32, numChannels * 2, true);
//         view.setUint16(34, 16, true);
//         writeString(36, 'data');
//         view.setUint32(40, length * numChannels * 2, true);

//         // PCM data
//         let offset = 44;
//         for (let i = 0; i < buffers.length; i++) {
//             for (let channel = 0; channel < numChannels; channel++) {
//                 const buffer = buffers[i][channel];
//                 for (let j = 0; j < buffer.length; j++) {
//                     const sample = Math.max(-1, Math.min(1, buffer[j]));
//                     view.setInt16(offset, sample * 0x7FFF, true);
//                     offset += 2;
//                 }
//             }
//         }

//         const blob = new Blob([view], { type: 'audio/wav' });
//         callback(blob);
//     }
// }

$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: 'ios9',
        amplitude: 1,
        speed: 0.3,
        // frequency: 2,
        autostart: true,
    });

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutDown",
            sync: true,
        },
    });

});