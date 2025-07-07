import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.title("Krishna with an Arrow")
screen.bgcolor("#E0FFFF") # A light cyan background

t = turtle.Turtle()
t.speed(3) # Set drawing speed (1=slowest, 10=fast, 0=instant)
t.pensize(3) # Set the thickness of the line

# A helper function to move the turtle without drawing
def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Drawing Functions ---

def draw_head_and_hair():
    # Go to position for the head
    go_to(0, 0)
    
    # Draw face (a simple circle)
    t.color("#6495ED") # Cornflower Blue for Krishna's skin
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    # Draw hair bun
    go_to(0, 80) # Position for the bun on top of the head
    t.color("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def draw_peacock_feather():
    # Position for the feather
    go_to(15, 95)
    t.setheading(120) # Point the turtle upwards and left
    
    # Draw the main feather shape
    t.color("green")
    t.begin_fill()
    t.forward(60)
    t.right(90)
    t.circle(10, 180) # Create a rounded tip
    t.right(90)
    t.forward(60)
    t.end_fill()
    
    # Draw the blue "eye" of the feather
    go_to(35, 125)
    t.color("blue")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
def draw_body_and_dhoti():
    # Position for the body (neck)
    go_to(0, 0)
    t.setheading(-90) # Point down
    
    # Torso
    t.color("black", "#6495ED") # Black outline, blue fill
    t.begin_fill()
    t.forward(80)
    
    # Dhoti (yellow garment)
    t.color("black", "gold") # Black outline, gold fill
    t.right(90)
    t.forward(40)
    t.left(120)
    t.forward(80)
    t.left(120)
    t.forward(80)
    t.left(120)
    t.forward(40)
    t.end_fill()

def draw_arms_and_arrow():
    # Right arm (holding the arrow)
    go_to(-10, -30)
    t.setheading(200) # Point arm forward
    t.color("#6495ED")
    t.circle(50, 100) # A curved arm

    # The Arrow
    go_to(-120, -60) # Start position of the arrow
    t.color("saddlebrown") # Brown color for the arrow
    t.setheading(0) # Point straight to the right
    t.pensize(5)
    t.forward(150) # Draw the arrow shaft
    
    # Arrowhead (a simple triangle)
    t.begin_fill()
    t.right(150)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()
    
    t.pensize(3) # Reset pensize

def draw_legs():
    # First leg
    go_to(-20, -135)
    t.color("#6495ED")
    t.setheading(-90)
    t.forward(50)
    
    # Second leg
    go_to(20, -135)
    t.forward(50)

# --- Main Drawing Execution ---
draw_head_and_hair()
draw_peacock_feather()
draw_body_and_dhoti()
draw_arms_and_arrow()
draw_legs()

# Hide the turtle cursor and finish
t.hideturtle()
screen.exitonclick() # Click on the screen to close the window