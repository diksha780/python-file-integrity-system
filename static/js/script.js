document.addEventListener("DOMContentLoaded", function () {
  // Get the file input and the button
  const fileInput = document.getElementById("file");
  const submitButton = document.querySelector("form button");
  const feedback = document.createElement("p");

  // Insert feedback element into the DOM after the form
  document.querySelector("form").appendChild(feedback);

  // Display the selected file name when a file is chosen
  fileInput.addEventListener("change", function (event) {
    const fileName = event.target.files[0]
      ? event.target.files[0].name
      : "No file chosen";
    feedback.textContent = `Selected file: ${fileName}`;
  });

  // Handle the form submission
  document.querySelector("form").addEventListener("submit", function (event) {
    // Prevent the form from submitting immediately
    event.preventDefault();

    // Show feedback to the user (e.g., "Uploading..." message)
    submitButton.disabled = true;
    feedback.textContent = "Uploading...";

    // Simulate form submission (for demonstration purposes)
    setTimeout(function () {
      // After the upload is done, update the feedback
      feedback.textContent = "File uploaded successfully!";

      // Re-enable the submit button
      submitButton.disabled = false;

      // Optionally, reset the form after submission
      fileInput.value = ""; // Clear the file input
    }, 2000); // Simulated upload time (2 seconds)
  });
});

// function func1() {
//   //   let a = document.getElementById("div1");
//   //   a.innerHTML = "Helo";
//   alert("Hello");
// }
