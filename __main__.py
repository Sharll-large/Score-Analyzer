# coding: gbk

import tkinter as tk
import tkinter.ttk as ttk

import matplotlib.pyplot as plt

import const
import data_loader
import ui
from structs import Student

root = tk.Tk()
root.title = const.title
root.geometry(f"{const.win_width}x{const.win_height}")
root.resizable = False

ttk.Style().configure("TButton", padding=6, relief="flat",
                      background="#ccc")

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Microsoft YaHei', 'SimHei', 'Arial'],
    'font.size': 12,
    'axes.unicode_minus': False
})


if __name__ == "__main__":
    ui.load(root)

    root.mainloop()
    # import plots.single_student
    # import plots.single_stu_radar_chart
    # data_loader.try_load()
    # plots.single_student.show(Student("刘杰", 16, 1))
    # plots.single_stu_radar_chart.show_radar_chart(Student("刘杰", 16, 1))
