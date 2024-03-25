if(clickLabel == 'Quote Auto'){
    fetch('http://127.0.0.1:5000/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch data from server');
            }
            return response.text();
        })
        .then(data => {
        // Handle the response from the server
            console.log('Response from server:', data);
// You can process the data here as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
    targetPanel = 'c:TGSI_Rater_Auto'
}