<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Plot with Plotly</title>
</head>
<body>
    <h1>Interactive Plot from Python</h1>
    <a href="../">Back</a>

    <!-- Form to collect user inputs for the stock ticker and prediction period -->
    <form action="process.php" method="post">
        <label for="ticker">Enter stock ticker (e.g., AAPL, GOOGL): </label>
        <input type="text" id="ticker" name="ticker" required>
        <br>
        <label for="years">Enter years of prediction (1 to 4): </label>
        <input type="number" id="years" name="years" min="1" max="4" required>
        <br>
        <button type="submit">Submit</button>
    </form>

    <?php
    // session_start();
    // if (isset($_SESSION["output_message"])) {
    //     echo "<p>{$_SESSION["output_message"]}</p>";
    //     unset($_SESSION["output_message"]);
    // }
    ?>

    <!-- Display the plots -->
    <h2>Raw Data Plot</h2>
    <iframe src="../asset/graph/raw_data_plot.html" width="50%" height="620px" style="border: none;"></iframe>
    <h2>Forecast Plot</h2>
    <iframe src="../asset/graph/forecast_plot.html" width="50%" height="620px" style="border: none;"></iframe>
</body>
</html>
