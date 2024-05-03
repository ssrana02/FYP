document.getElementById('urlForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the URL from the input field
    var url = document.getElementById('url').value;

    // Send a POST request to the Flask server
    fetch('/predict', {  // Changed endpoint to /predict
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        alert(data.result); // Display result from Flask server
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

