import tkinter as tk

root = tk.Tk()
root.title("My New House")

canvas = tk.Canvas(root, width=500, height=450, bg="lightcyan")
canvas.pack()

# Ground
canvas.create_rectangle(0, 380, 500, 450, fill="olivedrab", outline="")

# Path leading to the door
canvas.create_polygon(225, 380, 275, 380, 310, 450, 190, 450, fill="lightgray", outline="gray")

# Chimney (drawn before the roof so the roof overlaps its base)
canvas.create_rectangle(300, 120, 330, 175, fill="dimgray", outline="black", width=2)

# Square body (200 x 200)
canvas.create_rectangle(150, 180, 350, 380, fill="lightpink", outline="black", width=2)

# Triangle roof
canvas.create_polygon(130, 180, 250, 80, 370, 180, fill="navy", outline="black", width=2)

# Two small square windows (different colors)
canvas.create_rectangle(170, 215, 210, 255, fill="lightskyblue", outline="black", width=2)
canvas.create_rectangle(290, 215, 330, 255, fill="orchid", outline="black", width=2)

# Door and doorknob
canvas.create_rectangle(225, 310, 275, 380, fill="darkgreen", outline="black", width=2)
canvas.create_oval(260, 342, 268, 350, fill="gold", outline="black")

root.mainloop()