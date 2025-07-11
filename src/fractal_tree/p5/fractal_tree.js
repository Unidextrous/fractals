/**
 * fractal_tree.js
 * 
 * Renders an interactive fractal tree using the p5.js library.
 * A slider controls the branching angle in real-time, letting the user
 * explore different tree shapes generated via recursive geometry.
 */
var angle;    // Branching angle in radians
var slider;   // Angle control slider

function setup() { 
  createCanvas(500, 500);

  // Create a slider from 0 to 2π radians with default PI/4
  slider = createSlider(0, 2 * PI, PI / 4, 0.01);
  slider.position(10, height); // Position it just below the canvas
} 

function draw() { 
  background(220);

  // Get the angle from the slider
  angle = slider.value();

  // Start drawing from the bottom center
  translate(width/2, height);

  // Initial trunk length
  branch(100);
  
}

/**
 * Recursively draws a tree branch, splitting left and right.
 * 
 * @param {number} len - The length of the current branch
 */
function branch(len) {
  // Draw the main trunk segment
	line(0, 0, 0, -len);
  translate(0, -len);

  // Stop recursion at minimum length
  if (len > 10) {
    // Right branch
    push();
    rotate(angle);
    branch(len * 0.75) // Recursive right branch
    pop();

    // Left branch
    push();
    rotate(-angle);
    branch(len * 0.75); // Recursive left branch
    pop();  
  }
}