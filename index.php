<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
    <link rel="stylesheet" href="/asset/css/style.css">
</head>
<body>
    <div class="navbar">
        <div class="nav-con">
            <div class="logo">
                <h1>S T O N K</h1>
            </div>
            <div class="menu">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#section_2">Member</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="/stock_prediction/">Graph</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="section_1">
        <div class="graph-container">
            <canvas id="stockCanvas"></canvas>
        </div>
        <div class="particle">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
        <div class="stock-predict">
            <a href="/test/"><button class="btn">Stock Prediction</button></a>
        </div>
    </div>
    <div class="section_2" id="section_2">
        <div class="Member">
            <h1>Member</h1>
        </div>
        <div class="flip-con">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="flip-con">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <p class="title">FLIP CARD</p>
                        <p>Hover Me</p>
                    </div>
                    <div class="flip-card-back">
                        <p class="title">BACK</p>
                        <p>Leave Me</p>
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
    <script src="asset/javascript/app.js"></script>
    <script src="asset/javascript/jquery.js"></script>
    <script src="asset/javascript/slick.min.js"></script>
    <script>
        $('.carousel-view').slick({
        dots: false,
        infinite: true,
        speed: 800, // Slower transition for smoother movement
        autoplay: true,
        autoplaySpeed: 1500,
        slidesToShow: 3,
        slidesToScroll: 1,
        cssEase: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)', // Custom easing for smoother motion
        responsive: [
        {
        breakpoint: 1500,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
        }
        },
        {
        breakpoint: 1000,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1
        }
        }
        ]
        });
    </script>
</body>
</html>