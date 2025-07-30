
// Admission form submission
document.getElementById('admissionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('formMessage').textContent = 
        "Application submitted successfully! You will receive an email confirmation. (Note: No backend connected)";
    this.reset();
});

// Application status checker
document.getElementById('statusForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const appNo = document.getElementById('appNo').value;
    if(appNo.trim() === "" || appNo.length < 6) {
        document.getElementById('statusMessage').textContent = 
            "Please enter a valid application number.";
    } else {
        document.getElementById('statusMessage').textContent = 
            "Status for Application #" + appNo + ": Under Review.";
    }
    this.reset();
});

