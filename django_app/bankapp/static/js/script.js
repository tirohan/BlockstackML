$(document).ready(function () {
    // Listen for form submission
    $("form").on("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the form data
        var formData = $(this).serialize();

        // Send a POST request to the server for prediction
        $.ajax({
            type: "POST",
            url: "/bankapp/predict/", // Update the URL to the correct endpoint
            data: formData,
            success: function (data) {
                // Update the result on the web page
                $(".result").text("Prediction: " + data.prediction);
            },
            error: function (error) {
                // Handle any errors here
                $(".result").text("Error: " + error.responseJSON.message);
            },
        });
    });
});