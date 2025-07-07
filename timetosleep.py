import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.title("Krishna with an Arrow (Corrected)")
screen.bgcolor("#E0FFFF") # A light cyan background

t = turtle.Turtle()
t.speed(3) # Set drawing speed
t.pensize(3) # Set the thickness of the line

# A helper function to move the turtle without drawing
def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Drawing Functions (Corrected) ---

def draw_head_and_hair():
    # This function was mostly okay
    go_to(0, 0)
    t.color("#6495ED") # Cornflower Blue for Krishna's skin
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    go_to(0, 80)
    t.color("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def draw_peacock_feather():
    # This function was also fine
    go_to(15, 95)
    t.setheading(120)
    t.color("green")
    t.begin_fill()
    t.forward(60)
    t.right(90)
    t.circle(10, 180)
    t.right(90)
    t.forward(60)
    t.end_fill()
    
    go_to(35, 125)
    t.color("blue")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
def draw_body_and_dhoti():
    # FIXED: Torso now connects head to the dhoti's waist
    go_to(0, -40) # Start from the bottom of the head
    t.setheading(-90)
    t.color("black")
    t.pensize(5) # A thicker line for the torso
    t.forward(40) # Torso ends at the waist (y=-80)
    t.pensize(3)

    # FIXED: Dhoti now drawn neatly below the torso
    go_to(35, -80) # Start at the right waist
    t.color("black", "gold")
    t.begin_fill()
    t.goto(-35, -80) # Go to the left waist
    t.goto(0, -130)  # Go to the bottom point of the dhoti
    t.goto(35, -80)  # Connect back to the start
    t.end_fill()

def draw_arms_and_arrow():
    # FIXED: Arm now connects to the body and holds the arrow
    
    # Right arm reaching across the body
    go_to(20, -60) # Start from the right shoulder
    t.setheading(180) # Point left
    t.color("#6495ED")
    t.forward(60) # Arm reaches position (-40, -60) to hold the arrow
    
    # A simple left arm for balance
    go_to(-20, -60) # Start from left shoulder
    t.setheading(-90)
    t.forward(30)

    # Arrow (drawn so the hand is holding it)
    go_to(-100, -60) # Start of the arrow's tail
    t.color("saddlebrown")
    t.pensize(5)
    t.setheading(0) # Point straight to the right
    t.forward(150) # Draw the arrow shaft
    
    # Arrowhead
    t.begin_fill()
    t.right(150)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()
    
    t.pensize(3) # Reset pensize

def draw_legs():
    # FIXED: Legs now connect to the bottom of the dhoti
    # The dhoti ends at y=-130.
    
    # First leg
    go_to(-10, -130) # Start from the left side of the dhoti's tip
    t.color("#6495ED")
    t.setheading(-90)
    t.forward(50)
    
    # Second leg
    go_to(10, -130) # Start from the right side of the dhoti's tip
    t.forward(50)

# --- Main Drawing Execution ---
draw_head_and_hair()
draw_peacock_feather()
draw_body_and_dhoti()
draw_arms_and_arrow()
draw_legs()

# Hide the turtle cursor and finish
t.hideturtle()
screen.exitonclick()