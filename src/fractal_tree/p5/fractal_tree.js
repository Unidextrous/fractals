var angle
var slider

function setup() { 
  createCanvas(500, 500);
  slider = createSlider(0, 2 * PI, PI / 4, 0.01)
  slider.position(10, height);
} 

function draw() { 
  background(220);
  angle = slider.value();
  translate(width/2, height);
  branch(100);
  
}

function branch(len) {
	line(0, 0, 0, -len);
  translate(0, -len);
  if (len > 10) {
  push();
  rotate(angle);
  branch(len * 0.75)
  pop();
  push();
  rotate(-angle);
  branch(len * 0.75)
  pop();  
  }
}