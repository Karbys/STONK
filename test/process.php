<?php
// Start session if using session variables for messages
session_start();

// Get inputs from the form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $ticker = escapeshellarg($_POST["ticker"]);
    $years = escapeshellarg($_POST["years"]);

    // Run the Python script with the provided inputs
    $command = "python ../app.py $ticker $years";
    $output = shell_exec($command . " 2>&1");

    // Optional: Store output in a session variable for feedback on index.php
    $_SESSION["output_message"] = $output ? $output : "Error running the script.";
    
    // Redirect back to index.php
    header("Location: index.php");
    exit();
}
?>
