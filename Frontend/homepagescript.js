

document.getElementById('urlForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    var urlInput = document.getElementById('urlInput').value;
    var resultContainer = document.getElementById('resultContainer');
    
    // Placeholder code for displaying result
    var resultMessage = document.createElement('p');
    resultMessage.textContent = 'Detection result for ' + urlInput + ': Malicious';
    resultContainer.innerHTML = ''; // Clear previous results
    resultContainer.appendChild(resultMessage);
});
