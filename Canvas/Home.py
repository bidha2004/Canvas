import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("House Drawing")
window.geometry("700x600")

# Create Canvas
canvas = tk.Canvas(window, width=700, height=600, bg="skyblue")
canvas.pack()

# Sun
canvas.create_oval(550, 50, 620, 120, fill="yellow", outline="orange")

# Ground
canvas.create_rectangle(0, 450, 700, 600, fill="green", outline="green")

# House body
canvas.create_rectangle(
    200, 250, 500, 450,
    fill="lightyellow",
    outline="black",
    width=3
)

# Roof
canvas.create_polygon(
    160, 250,
    350, 100,
    540, 250,
    fill="red",
    outline="black",
    width=3
)

# Door
canvas.create_rectangle(
    320, 350, 390, 450,
    fill="brown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    370, 395, 380, 405,
    fill="yellow",
    outline="black"
)

# Left window
canvas.create_rectangle(
    230, 290, 290, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window
canvas.create_rectangle(
    410, 290, 470, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Window crosses
canvas.create_line(260, 290, 260, 350, fill="black", width=2)
canvas.create_line(230, 320, 290, 320, fill="black", width=2)

canvas.create_line(440, 290, 440, 350, fill="black", width=2)
canvas.create_line(410, 320, 470, 320, fill="black", width=2)

# Tree trunk
canvas.create_rectangle(
    80, 350, 120, 450,
    fill="brown",
    outline="black"
)

# Tree leaves
canvas.create_oval(
    40, 280, 160, 380,
    fill="darkgreen",
    outline="black"
)

canvas.create_oval(
    70, 240, 150, 330,
    fill="green",
    outline="black"
)

# Text
canvas.create_text(
    350, 520,
    text="My House",
    font=("Arial", 24, "bold"),
    fill="black"
)

# Cloud
canvas.create_oval(80, 80, 160, 130, fill="white", outline="white")
canvas.create_oval(120, 60, 200, 130, fill="white", outline="white")
canvas.create_oval(160, 80, 240, 130, fill="white", outline="white")
canvas.create_rectangle(100, 90, 210, 130, fill="white", outline="white")

# Small Dog House

# Dog house body
canvas.create_rectangle(
    560, 405, 630, 450,
    fill="orange",
    outline="black",
    width=2
)

# Dog house roof
canvas.create_polygon(
    550, 405,
    595, 365,
    640, 405,
    fill="red",
    outline="black",
    width=2
)

# Dog house entrance
canvas.create_oval(
    580, 415, 610, 450,
    fill="black",
    outline="black"
)

# Dog house label
canvas.create_text(
    595, 470,
    text="Dog House",
    font=("Arial", 10, "bold"),
    fill="black"
)


# Run the application
window.mainloop()
