import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.title("Hare Krishna Scroll Banner (Corrected)")
screen.bgcolor("#87CEEB") # Sky blue background

t = turtle.Turtle()
t.speed(9) # Speed up drawing
t.hideturtle()

# --- Helper function to move without drawing ---
def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Drawing Functions for the Scroll ---

def draw_scroll_ends(width, roll_radius):
    """Draws the two 'rolled up' ends of the scroll on the sides."""
    t.pensize(5)
    t.color("#A52A2A", "#DAA520") # Maroon border, Goldenrod fill (darker yellow)

    go_to(-width / 2, 0)
    t.begin_fill()
    t.circle(-roll_radius)
    t.end_fill()

    go_to(width / 2, 0)
    t.begin_fill()
    t.circle(-roll_radius)
    t.end_fill()

def draw_main_banner(width, height):
    """Draws the central flat part of the scroll."""
    go_to(-width / 2, -height / 2)
    t.color("#A52A2A", "#FFD700") # Maroon border, Gold fill (brighter yellow)
    t.pensize(5)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        
    t.end_fill()

def draw_tassels(width, height):
    """Draws tassels hanging from the bottom of the banner."""
    t.pensize(3)
    t.color("#DC143C")

    go_to(-width / 2 + 40, -height / 2)
    t.setheading(-90)
    t.forward(25)
    t.dot(20)

    go_to(width / 2 - 40, -height / 2)
    t.setheading(-90)
    t.forward(25)
    t.dot(20)

# --- RECTIFIED FUNCTION TO FIT THE TEXT ---
def write_mantra(height):
    """
    Writes the mantra by breaking it into four lines to ensure it
    fits perfectly inside the banner.
    """
    t.color("#4B0082") # Deep Indigo for text
    # A slightly smaller font to ensure it fits well
    font_style = ("Georgia", 14, "bold")

    # Define the four lines of the mantra
    line1 = "Hare Krishna, Hare Krishna,"
    line2 = "Krishna Krishna, Hare Hare"
    line3 = "Hare Rama, Hare Rama,"
    line4 = "Rama Rama, Hare Hare"

    # Calculate vertical positions for four lines to be centered
    go_to(0, height * 0.30)
    t.write(line1, align="center", font=font_style)
    
    go_to(0, height * 0.05)
    t.write(line2, align="center", font=font_style)

    go_to(0, -height * 0.25)
    t.write(line3, align="center", font=font_style)

    go_to(0, -height * 0.50)
    t.write(line4, align="center", font=font_style)


# --- Main Execution ---

# Define scroll dimensions
SCROLL_WIDTH = 450 # Width of the flat part
SCROLL_HEIGHT = 150 # Made it a bit taller for better text spacing
ROLL_RADIUS = SCROLL_HEIGHT / 2 + 10

# --- Drawing Order Matters ---
# 1. Draw the rolls first, so they appear 'behind'.
draw_scroll_ends(SCROLL_WIDTH, ROLL_RADIUS)

# 2. Draw the main banner on top of the rolls.
draw_main_banner(SCROLL_WIDTH, SCROLL_HEIGHT)

# 3. Add the details onto the banner.
draw_tassels(SCROLL_WIDTH, SCROLL_HEIGHT)
write_mantra(SCROLL_HEIGHT)

# Keep the window open until it's clicked
screen.exitonclick()