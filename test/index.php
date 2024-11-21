<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Plot with Plotly</title>
    <link rel="stylesheet" href="../asset/css/test.css">
</head>
<body>
    <div class="header">
        <h1>Interactive Plot from Python</h1>
        <div class="button">
            <a href="../">Back</a>
        </div>
    </div>
    <!-- Form to collect user inputs for the stock ticker and prediction period -->
    <div class="form-con">
        <form action="process.php" method="post">
            <div class="ticker-con">
                <label for="ticker">Enter stock ticker (e.g., AAPL, GOOGL): </label>
                <br>
                <input type="text" id="ticker" name="ticker" required>
            </div>
            <div class="year-con">
                <label for="years">Enter years of prediction (1 to 4): </label>
                <br>
                <input type="range" id="years" name="years" min="1" max="4" class="slider" required>
            </div>
            <div class="checkbox-con">
                <label>Select data to display:</label><br>
                <input type="checkbox" id="stock_open" name="stock_open" value="1">
                <label for="stock_open">Stock Open</label><br>
                <input type="checkbox" id="stock_close" name="stock_close" value="1">
                <label for="stock_close">Stock Close</label>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>

    <!-- Display the plots -->
    <h2>Raw Data Plot</h2>
    <iframe src="../asset/graph/raw_data_plot.html" width="50%" height="620px" style="border: none;"></iframe>
    <h2>Forecast Plot</h2>
    <iframe src="../asset/graph/forecast_plot.html" width="50%" height="620px" style="border: none;"></iframe>
</body>
</html>
