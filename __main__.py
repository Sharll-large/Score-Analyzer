# coding: gbk

import tkinter as tk
import tkinter.ttk as ttk

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

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
    'font.sans-serif': ['Microsoft YaHei', 'simhei', 'arial'],
    'font.size': 12,
    'axes.unicode_minus': False
})



if __name__ == "__main__":
    ui.load(root)
    
    root.mainloop()
    


    from plots import dot_plot
    from plots import radar_plot
    data_loader.try_load()
    # radar_plot.create_advanced_comparison_radar(Student("赵秀英", 22, 1))
