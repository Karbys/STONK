const canvas = document.getElementById('stockCanvas');
const ctx = canvas.getContext('2d');

// Set canvas dimensions
canvas.width = 1920;
canvas.height = 1080;

// Increase the number of data points for a smoother line
let dataPoints = Array.from({ length: 12 }, () => Math.floor(Math.random() * canvas.height));

// Set the desired speed of the animation (in milliseconds)
const animationSpeed = 10; // Frame delay for smoother animation
const smoothFactor = 0.1; // Smaller value for smoother transitions
let progress = 0;

// Set the total transition duration for opacity
const transitionDuration = 200; // 2 seconds in milliseconds
const framesForTransition = transitionDuration / animationSpeed; // Total frames for transition

function drawLine() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const gradient = ctx.createLinearGradient(0, canvas.height, 0, 0);
    gradient.addColorStop(0, 'rgba(0, 31, 29, 0.8)');
    gradient.addColorStop(1, 'rgba(0, 63, 58, 0.6)');

    ctx.beginPath();
    for (let index = 0; index < progress && index < dataPoints.length; index++) {
        const x = (index / (dataPoints.length - 1)) * canvas.width;
        const y = canvas.height - dataPoints[index];

        // Calculate opacity for the current point based on progress
        const opacity = Math.min(1, index / framesForTransition); // Opacity transitions from 0 to 1

        // Set the stroke style with the calculated opacity
        ctx.strokeStyle = `rgba(0, 255, 153, ${opacity})`; // Line color with dynamic opacity

        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }

    ctx.lineTo(canvas.width, canvas.height);
    ctx.lineTo(0, canvas.height);
    ctx.closePath();

    ctx.fillStyle = gradient;
    ctx.fill();

    // Draw the line on top of the filled area
    ctx.lineWidth = 2;
    ctx.stroke();
}

function generateNewTargets() {
    return dataPoints.map(point => {
        const variance = Math.random() * 10 - 5;
        return Math.min(Math.max(point + variance, 0), canvas.height);
    });
}

function animate() {
    const targetPoints = generateNewTargets();

    // Smoothly transition each point towards its new target
    dataPoints = dataPoints.map((point, index) => {
        return point + (targetPoints[index] - point) * smoothFactor;
    });

    // Increment progress
    if (progress < dataPoints.length) {
        progress += 0.1; // Smaller increment for smoother progress
    } else {
        progress = dataPoints.length;
    }

    drawLine();

    // Use requestAnimationFrame for smoother animation
    requestAnimationFrame(animate);
}

// Start the animation
animate();
