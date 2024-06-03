// Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyCB2w7nDJ2jiU2C_CSLhwG2FHOtEzymAG4",
    authDomain: "fir-dec23.firebaseapp.com",
    databaseURL: "https://fir-dec23-default-rtdb.firebaseio.com",
    projectId: "fir-dec23",
    storageBucket: "fir-dec23.appspot.com",
    messagingSenderId: "209807234342",
    appId: "1:209807234342:web:45951d762242f8aff41de7",
    measurementId: "G-GK24R5KV78"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference to the Firebase Realtime Database
var database1 = firebase.database().ref('Slots1_5');
var database2 = firebase.database().ref('slots6_10');

function ubahWarna(element, status) {
    if (status === 'tersedia') {
        element.classList.remove('slot-terisi');
        element.classList.add('slot-tersedia');
    } else {
        element.classList.remove('slot-tersedia');
        element.classList.add('slot-terisi');
    }
}

// Listen for changes in the database for slots 1-5
database1.on('value', (snapshot) => {
    const slots = snapshot.val();
    for (const slotId in slots) {
        const slotElement = document.querySelector(`img[data-slot-id="${slotId}"]`);
        if (slotElement) {
            ubahWarna(slotElement, slots[slotId]);
        }
    }
});

// Listen for changes in the database for slots 6-10
database2.on('value', (snapshot) => {
    const slots = snapshot.val();
    for (const slotId in slots) {
        const slotElement = document.querySelector(`img[data-slot-id="${slotId}"]`);
        if (slotElement) {
            ubahWarna(slotElement, slots[slotId]);
        }
    }
});

// Add event listener to toggle fullscreen mode
document.querySelector(".toggle").addEventListener("click", function (event) {
    if (document.fullscreenElement) {
        // If there is a fullscreen element, exit full screen.
        document.exitFullscreen();
        return;
    }
    // Make the .element div fullscreen.
    document.querySelector(".element").requestFullscreen();
});
