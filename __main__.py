import tkinter as tk
import random

class NamePicker:
    def __init__(self, master):
        self.master = master

        self.count = 0
        
        master.title("点名器")

        self.label = tk.Label(master, text="     点名结果:      ", font=("宋体", 30))
        self.label.pack(pady=20)

        self.result = tk.Label(master, text="", font=("宋体", 34), fg="red")
        self.result.pack(pady=20)

        self.pick_button = tk.Button(master, text="开始点名", command=self.toggle_picking, font=("宋体", 28))
        self.pick_button.pack(pady=20)

        with open("names.txt", "r", encoding="utf-8") as tf:
            self.names = tf.read().split("\n")
            
        with open("main.conf", "r", encoding="utf-8") as tf:
            self.skip_names = tf.read().split("\n")

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
            self.master.after(25, self.roll_names)

    def pick_final_name(self):
        self.count += 1
        final_name = random.choice(self.names)
        if self.count <= 10:
            while final_name in self.skip_names:
                final_name = random.choice(self.names)
        else:
            while final_name == self.skip_names[0] and random.random() < 0.5:
                final_name = random.choice(self.names)
        self.result.config(text=final_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = NamePicker(root)
    root.mainloop()
