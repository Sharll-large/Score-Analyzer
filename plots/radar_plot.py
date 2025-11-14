import numpy as np
from matplotlib import pyplot as plt


def create_advanced_comparison_radar(students_data, title=None, figsize=(12, 10), ylim=(60, 100)):
    """
    增强版多学生成绩对比雷达图

    参数:
    students_data: list of dict, 每个dict包含'name'和'scores'
    title: 图表标题，如果为None则自动生成
    figsize: 图形尺寸
    ylim: 径向坐标范围
    """
    subjects = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(projection='polar'))

    colors = plt.cm.Set3(np.linspace(0, 1, len(students_data)))

    # 为每个学生绘制
    for i, student in enumerate(students_data):
        scores_list = [student['scores'][subject] for subject in subjects]
        scores_list.append(scores_list[0])

        angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False).tolist()
        angles.append(angles[0])

        ax.plot(angles, scores_list, 'o-', linewidth=2.5,
                label=student['name'], color=colors[i], markersize=6)
        ax.fill(angles, scores_list, alpha=0.15, color=colors[i])

    # 设置坐标轴
    angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
    ax.set_xticks(angles)
    ax.set_xticklabels(subjects, fontsize=11)

    ax.set_ylim(ylim[0], ylim[1])
    ax.set_yticks(np.arange(ylim[0], ylim[1] + 1, 10))

    # 设置标题
    if title is None:
        student_names = [s['name'] for s in students_data]
        title = f'学生成绩对比雷达图 ({", ".join(student_names)})'

    plt.title(title, size=14, fontweight='bold', pad=25)
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.1), fontsize=11)

    plt.tight_layout()
    plt.show()

    return fig