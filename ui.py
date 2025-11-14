# coding: gbk

import tkinter as tk
import tkinter.ttk

import const


def get_middle_x(child: tk.Widget) -> int:
    # 返回一个空间居中时的x坐标。
    return const.win_width / 2 - child.winfo_reqwidth() / 2


def load(parent: tk.Tk):
    # 创建主标签（保持不变）
    title = tk.ttk.Label(parent, text="成绩分析器", font=("宋体", 40))
    authors = tk.ttk.Label(parent, text=f"By {' '.join(const.author)}", font=("宋体", 16))
    info = tk.ttk.Label(parent, text="已加载 {} 个数据。", font=("宋体", 20))

    title.place(x=get_middle_x(title), y=30)
    authors.place(x=get_middle_x(authors), y=80)
    info.place(x=get_middle_x(info), y=120)

    def place(buttons, start, dis):
        """布局按钮的辅助函数"""
        for i in range(len(buttons)):
            buttons[i].place(x=get_middle_x(buttons[i]), y=start+i*dis)

    def create_main_buttons():
        """创建主菜单按钮"""
        # 清除现有按钮
        if hasattr(create_main_buttons, 'current_buttons'):
            for btn in create_main_buttons.current_buttons:
                btn.destroy()
        
        # 创建新的主菜单按钮
        buttons = [
            tk.ttk.Button(parent, text="导入新的考试数据..."),
            tk.ttk.Button(parent, text="刷新考试数据...", command=lambda: parent.update()),
            tk.ttk.Button(parent, text="分析：单场考试", command=create_single_test_buttons),
            tk.ttk.Button(parent, text="分析：多场考试", command=create_many_tests_buttons),
            tk.ttk.Button(parent, text="分析：个人数据", command=create_single_data_buttons),
            tk.ttk.Button(parent, text="分析：班级情况", command=create_class_condition_buttons)
        ]
        
        place(buttons, 220, 40)
        create_main_buttons.current_buttons = buttons

    def create_single_test_buttons():
        """创建单场考试分析按钮"""
        # 清除现有按钮
        if hasattr(create_main_buttons, 'current_buttons'):
            for btn in create_main_buttons.current_buttons:
                btn.destroy()
        
        buttons = [tk.ttk.Button(parent, text="返回", command=create_main_buttons)]
        place(buttons, 460, 40)
        create_main_buttons.current_buttons = buttons

    def create_many_tests_buttons():
        """创建多场考试分析按钮"""
        if hasattr(create_main_buttons, 'current_buttons'):
            for btn in create_main_buttons.current_buttons:
                btn.destroy()
        
        buttons = [tk.ttk.Button(parent, text="返回", command=create_main_buttons)]
        place(buttons, 460, 40)
        create_main_buttons.current_buttons = buttons

    def create_single_data_buttons():
        """创建个人数据分析按钮"""
        if hasattr(create_main_buttons, 'current_buttons'):
            for btn in create_main_buttons.current_buttons:
                btn.destroy()
        
        buttons = [tk.ttk.Button(parent, text="返回", command=create_main_buttons)]
        place(buttons, 460, 40)
        create_main_buttons.current_buttons = buttons

    def create_class_condition_buttons():
        """创建班级情况分析按钮"""
        if hasattr(create_main_buttons, 'current_buttons'):
            for btn in create_main_buttons.current_buttons:
                btn.destroy()
        
        buttons = [tk.ttk.Button(parent, text="返回", command=create_main_buttons)]
        place(buttons, 460, 40)
        create_main_buttons.current_buttons = buttons

    # 初始化显示主菜单按钮
    create_main_buttons()
