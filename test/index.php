<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Plot with Plotly</title>
    <link rel="stylesheet" href="../asset/css/test.css">
</head>
<body>
    <div class="navbar">
        <div class="nav-con">
            <div class="logo">
                <h1>S T O N K</h1>
            </div>
            <div class="menu">
                <ul>
                    <li><a href="../">Home</a></li>
                    <li><a href="../#section_2">Member</a></li>
                    <li><a href="../#about-con">About</a></li>
                    <li><a href="/test/">Graph</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="header">
            <h1>Interactive Plot from Python</h1>
        </div>
        <!-- Form to collect user inputs for the stock ticker and prediction period -->
        <div class="form-con">
            <form action="process.php" method="post">
                <div class="ticker-con">
                    <!-- <label for="ticker">Enter stock ticker (e.g., AAPL) </label> -->
                    <br>
                    <input type="text" id="ticker" name="ticker" placeholder="Enter stock ticker(e.g., AAPL)" required>
                </div>
                <div class="year-con">
                    <!-- <label for="years">Year (1 to 4)</label> -->
                    <br>
                    <!-- <input type="range" id="years" name="years" min="1" max="4" class="slider" value="1"required> -->
                    <span id="rangeValue">0</span>
                    <Input class="range" type="range" id="years" name="years" value="1" min="1" max="4" onChange="rangeSlide(this.value)" onmousemove="rangeSlide(this.value)" required></Input>
                </div>

                <!-- <div class="checkbox-con">
                    <label>Select data to display:</label><br>
                    <input type="checkbox" id="stock_open" name="stock_open" value="1" checked>
                    <label for="stock_open">Stock Open</label><br>
                    <input type="checkbox" id="stock_close" name="stock_close" value="1" checked>
                    <label for="stock_close">Stock Close</label>
                </div> -->

                <!-- <div class="customCheckBoxHolder">
                    <input class="customCheckBoxInput" id="stock_open" name="stock_open" type="checkbox" value="1" checked>
                    <label class="customCheckBoxWrapper" for="stock_open">
                        <div class="customCheckBox">
                            <div class="inner">Stock Open</div>
                        </div>
                    </label>

                    <input class="customCheckBoxInput" id="stock_close" name="stock_close" type="checkbox" value="1" checked>
                    <label class="customCheckBoxWrapper" for="stock_close">
                        <div class="customCheckBox">
                            <div class="inner">Stock Close</div>
                        </div>
                    </label>
                </div> -->

                <button type="submit">Submit</button>
            </form>
        </div>

        <!-- Display the plots -->
        <div class="frame-con">
            <div class="frame-item">
                <h2>Stock Data</h2>
                <iframe src="../asset/graph/raw_data_plot.html" width="100%" height="620px" style="border: none;"></iframe>
            </div>
            <div class="frame-item">
                <h2>Forecast Plot</h2>
                <iframe src="../asset/graph/forecast_plot.html" width="100%" height="620px" style="border: none;"></iframe>
            </div>
        </div>

        <div class="button">
            <a href="../">Back</a>
        </div>

        <div class="stars">
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
            <div class="star"></div>
        </div>
    </div>

    <script type="text/javascript">
        function rangeSlide(value) {
            document.getElementById('rangeValue').innerHTML = "Year " + value;
        }
    </script>
</body>
</html>
