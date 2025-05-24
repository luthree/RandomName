import tkinter as tk
import random

class NamePicker:
    def __init__(self, master):
        self.master = master

        self.count = 0  # 初始化计数器
        
        master.title("点名器")

        self.label = tk.Label(master, text="     点名结果:      ", font=("宋体", 30))
        self.label.pack(pady=20)

        self.result = tk.Label(master, text="", font=("宋体", 34), fg="red")
        self.result.pack(pady=20)

        self.pick_button = tk.Button(master, text="开始点名", command=self.toggle_picking, font=("宋体", 28))
        self.pick_button.pack(pady=20)

        # 读取名字列表
        with open("names.txt", "r", encoding="utf-8") as tf:
            self.names = tf.read().split("\n")
            
        # 跳过的名字列表
        self.skip_names = ["张三"]

        # 记录已经点过名的名单
        self.named = []

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
        self.count += 1  # 点名次数增加

        final_name = self.choose_name()

        # 显示最终点名结果
        self.result.config(text=final_name)

        # 如果记录的名字超过20次，移除最早的名字
        if self.count >= 20:
            self.named.pop(0)
        self.named.append(final_name)

    def choose_name(self):
        # 限制最大重试次数，防止死循环
        max_attempts = 100  
        attempts = 0

        while attempts < max_attempts:
            attempts += 1

            # 过滤出有效的名字列表，排除跳过名单和已经点过的名字
            available_names = [name for name in self.names if name not in self.named]
            # 如果点名次数 <= 10，跳过 `skip_names` 中的所有名字
            if self.count <= 10:
                available_names = [name for name in available_names if name not in self.skip_names]
            # 如果点名次数 > 10，只对第一个名字 50% 概率跳过
            elif self.count > 10 and self.skip_names[0] in available_names and random.random() < 0.5:
                available_names.remove(self.skip_names[0])

            # 如果没有可选名字，则直接返回 "无可选名字"
            if not available_names:
                return "无可选名字，请重启应用后重试"

            final_name = random.choice(available_names)

            # 如果选中的名字不在最近20次内，则返回这个名字
            if final_name not in self.named:
                return final_name

        # 如果达到最大尝试次数，返回最后选中的名字以避免死循环
        return final_name

if __name__ == "__main__":
    root = tk.Tk()
    app = NamePicker(root)
    root.mainloop()
