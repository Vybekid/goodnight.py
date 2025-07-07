import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.title("Hare Krishna Mantra Banner")
screen.bgcolor("#87CEEB") # A nice sky blue background

t = turtle.Turtle()
t.speed(5) # A slightly faster drawing speed
t.hideturtle() # Hide the turtle arrow for a cleaner look

# --- Helper function to move without drawing ---
def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Main Drawing Functions ---

def draw_banner_shape(width, height, corner_radius):
    """Draws a beautiful rounded rectangle for the banner."""
    go_to(-width / 2, height / 2 - corner_radius)
    t.color("#A52A2A", "#FFD700") # Maroon border, Gold fill
    t.pensize(5)
    t.begin_fill()

    # Draw the four rounded corners
    for _ in range(2):
        t.circle(corner_radius, 90) # Top-right corner
        t.forward(height - 2 * corner_radius)
        t.circle(corner_radius, 90) # Bottom-right corner
        t.forward(width - 2 * corner_radius)
        
    t.end_fill()

def draw_tassels(banner_width, banner_height):
    """Draws two cute tassels hanging from the bottom corners."""
    t.pensize(3)
    t.color("#DC143C") # Crimson color for tassels

    # Left Tassel
    go_to(-banner_width / 2 + 20, -banner_height / 2)
    t.setheading(-90)
    t.forward(20)
    t.dot(20) # A simple dot for the tassel puff

    # Right Tassel
    go_to(banner_width / 2 - 20, -banner_height / 2)
    t.setheading(-90)
    t.forward(20)
    t.dot(20)

def write_mantra():
    """Writes the Hare Krishna mantra in the center of the banner."""
    t.color("#4B0082") # A deep Indigo color for the text

    # First line of the mantra
    go_to(0, 15) # Position for the first line
    t.write(
        "Hare Krishna, Hare Krishna, Krishna Krishna, Hare Hare",
        align="center",
        font=("Georgia", 16, "bold")
    )

    # Second line of the mantra
    go_to(0, -25) # Position for the second line
    t.write(
        "Hare Rama, Hare Rama, Rama Rama, Hare Hare",
        align="center",
        font=("Georgia", 16, "bold")
    )


# --- Main Execution ---

# Define banner dimensions
BANNER_WIDTH = 500
BANNER_HEIGHT = 120
CORNER_RADIUS = 20

# Draw all the parts
draw_banner_shape(BANNER_WIDTH, BANNER_HEIGHT, CORNER_RADIUS)
draw_tassels(BANNER_WIDTH, BANNER_HEIGHT)
write_mantra()

# Keep the window open until it's clicked
screen.exitonclick()