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
const transitionDuration = 100; // 2 seconds in milliseconds
const framesForTransition = transitionDuration / animationSpeed; // Total frames for transition

function drawLine() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const gradient = ctx.createLinearGradient(0, canvas.height, 0, 0);
    gradient.addColorStop(1, 'rgba(34,180,255, 0.7)');
    gradient.addColorStop(0, 'rgba(29, 30, 34,1)');

    ctx.beginPath();
    for (let index = 0; index < progress && index < dataPoints.length; index++) {
        const x = (index / (dataPoints.length - 1)) * canvas.width;
        const y = canvas.height - dataPoints[index];

        // Calculate opacity for the current point based on progress
        const opacity = Math.min(1, index / framesForTransition); // Opacity transitions from 0 to 1

        // Set the stroke style with the calculated opacity
        ctx.strokeStyle = `rgba(255,255,255, ${opacity})`; // Line color with dynamic opacity

        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }

    ctx.lineTo(canvas.width, canvas.height);
    ctx.lineTo(0, canvas.height);
    ctx.closePath();

    // Set the glow effect for the stroke
    ctx.shadowColor = 'rgba(255, 255, 255, 0.4)'; // White glow
    ctx.shadowBlur = 20; // Adjust blur level for the glow effect
    ctx.shadowOffsetX = 0; // No horizontal offset
    ctx.shadowOffsetY = 0; // No vertical offset

    // Fill the area with the gradient
    ctx.fillStyle = gradient;
    ctx.fill();

    // Draw the glowing stroke on top of the filled area
    ctx.lineWidth = 2;
    ctx.stroke();

    // Reset shadow for subsequent drawings (if any)
    ctx.shadowColor = 'transparent'; // Reset shadow to avoid affecting other drawings
    ctx.shadowBlur = 0;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 0;
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

    // Increment progress more quickly for faster line generation
    if (progress < dataPoints.length) {
        progress += 0.2; // Increase the increment for faster drawing (previously 0.1)
    } else {
        progress = dataPoints.length;
    }

    drawLine();

    // Use requestAnimationFrame for smoother animation
    requestAnimationFrame(animate);
}


// Start the animation
animate();

