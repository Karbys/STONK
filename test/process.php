<?php
session_start();

// Get inputs from the form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $ticker = escapeshellarg($_POST["ticker"]);
    $years = escapeshellarg($_POST["years"]);

    // Checkboxes: Set default value to "0" if not checked
    $stock_open = isset($_POST["stock_open"]) ? "1" : "0";
    $stock_close = isset($_POST["stock_close"]) ? "1" : "0";

    // Run the Python script with the provided inputs
    $command = "python ../app.py $ticker $years $stock_open $stock_close";
    $output = shell_exec($command . " 2>&1");

    // Save output for debugging or displaying on the web page
    $_SESSION["output_message"] = $output ? $output : "Error running the script.";
    header("Location: index.php");
    exit();
}
?>
