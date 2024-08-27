import tkinter as tk
import random

class NamePicker:
    def __init__(self, master):
        self.master = master
        master.title("点名器")

        self.label = tk.Label(master, text="点名结果:", font=("Arial", 16))
        self.label.pack(pady=20)

        self.result = tk.Label(master, text="", font=("Arial", 20), fg="red")
        self.result.pack(pady=20)

        self.pick_button = tk.Button(master, text="开始点名", command=self.toggle_picking, font=("Arial", 14))
        self.pick_button.pack(pady=20)

        self.names = ["A", "B"]
        self.is_picking = False

    def toggle_picking(self):
        if not self.is_picking:
            self.is_picking = True
            self.pick_button.config(text="停止点名")
            self.roll_names()
        else:
            self.is_picking = False
            self.pick_button.config(text="开始点名")
            self.pick_final_name()

    def roll_names(self):
        if self.is_picking:
            name = random.choice(self.names)
            self.result.config(text=name)
            self.master.after(100, self.roll_names)

    def pick_final_name(self):
        final_name = "A"
        while final_name == "A":
            final_name = random.choice(self.names)
        self.result.config(text=final_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = NamePicker(root)
    root.mainloop()
