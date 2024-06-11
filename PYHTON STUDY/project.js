

let generatedOtp = '';

function sendOtp() {
    // Generate a random 6-digit OTP
    generatedOtp = Math.floor(100000 + Math.random() * 900000).toString();
    // Display the OTP input field and enable the Verify OTP button
    document.getElementById("otp-verification").style.display = 'block';
    // Play OTP sound
    document.getElementById("otp-sound").play();
    // Simulate sending OTP by displaying an alert (in real use, send via SMS)
    alert("OTP sent to your phone number: " + generatedOtp);
}

function verifyOtp() {
    const enteredOtp = document.getElementById("otpInput").value;
    if (enteredOtp === generatedOtp) {
        // Hide OTP section and display patient details form
        document.getElementById('otp-section').style.display = 'none';
        document.getElementById('patient-details-section').style.display = 'block';
    } else {
        alert("Incorrect OTP. Please try again.");
    }
}

document.getElementById('patient-details-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const disease = document.getElementById('disease').value.toLowerCase();

    if (disease === 'diabetics' || disease === 'diabetes') {
        document.getElementById('patient-details-section').style.display = 'none';
        document.getElementById('diabetes-info').style.display = 'block';
        startDiabetesNotifications();
    } else {
        alert('Details submitted successfully');
        startGeneralNotifications();
    }
});

function startDiabetesNotifications() {
    setInterval(() => {
        // Play diabetes reminder sound
        document.getElementById("diabetes-reminder-sound").play();
        alert('Diabetes Reminder: Please check your blood sugar levels and maintain a healthy diet.');
    }, 20000); // Sends notification every hour (3600000 milliseconds)
    setInterval(() => {
        // Play general reminder sound
        document.getElementById("general-reminder-sound").play();
        alert('General Reminder: Please take care of your health and stay hydrated.');
    }, 5000);
}



// Adding a fade-in effect using CSS class
const fadeInEffect = `
.fade-in {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
`;

// Append the fade-in effect style to the document
const style = document.createElement('style');
style.innerHTML = fadeInEffect;
document.head.appendChild(style);