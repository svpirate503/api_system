document.addEventListener("DOMContentLoaded",function(){





    document.getElementById('form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        formData.append('csrfmiddlewaretoken', csrfToken);

        fetch('http://127.0.0.1:8000/api/submit/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
             alert(data.success);
             } else {
            alert('Error: ' + JSON.stringify(data)); // Muestra el objeto completo en caso de error
             }
            document.getElementById('form').reset();
        })
        .catch(error => console.error('Error:', error));
    });
})