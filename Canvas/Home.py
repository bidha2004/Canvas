import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("House Drawing")
window.geometry("700x600")

# Create Canvas
canvas = tk.Canvas(window, width=700, height=600, bg="skyblue")
canvas.pack()


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

# Run the application
window.mainloop()