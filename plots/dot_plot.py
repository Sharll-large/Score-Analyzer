import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


def plot_score_distribution_3bin(exam_data, figsize=(12, 8)):
    """
    使用3分分箱绘制考试分数分布图

    参数:
    exam_data: dict, 格式为 {"考试名称": {分数: 人数, ...}}
    """
    plt.figure(figsize=figsize)

    colors = plt.cm.Set3(np.linspace(0, 1, len(exam_data)))
    bin_width = 3  # 固定3分分箱

    for i, (exam_name, score_dist) in enumerate(exam_data.items()):
        # 展开分数数据（将每个分数重复对应的人数次）
        all_scores = []
        for score, count in score_dist.items():
            all_scores.extend([score] * count)

        all_scores = np.array(all_scores)

        # 创建3分分箱
        min_score = np.floor(min(all_scores) / bin_width) * bin_width
        max_score = np.ceil(max(all_scores) / bin_width) * bin_width
        bins = np.arange(min_score, max_score + bin_width, bin_width)

        # 计算每个箱的人数
        hist, bin_edges = np.histogram(all_scores, bins=bins)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

        # 计算百分比
        total_students = len(all_scores)
        percentages = (hist / total_students) * 100

        # 移除空箱
        non_zero_mask = hist > 0
        bin_centers_clean = bin_centers[non_zero_mask]
        percentages_clean = percentages[non_zero_mask]

        # 创建平滑曲线
        if len(bin_centers_clean) > 3:
            x_smooth = np.linspace(bin_centers_clean.min(), bin_centers_clean.max(), 300)
            spl = make_interp_spline(bin_centers_clean, percentages_clean, k=3)
            y_smooth = spl(x_smooth)

            plt.plot(x_smooth, y_smooth,
                     label=f'{exam_name} (总人数: {total_students})',
                     linewidth=3, color=colors[i])

        # 绘制柱状图背景
        plt.bar(bin_centers, percentages,
                width=bin_width * 0.7, alpha=0.3, color=colors[i],
                edgecolor=colors[i], linewidth=1)

        # 在柱子上标注百分比
        for center, percent in zip(bin_centers, percentages):
            if percent > 0:  # 只标注非零柱子
                plt.text(center, percent + 0.5, f'{percent:.1f}%',
                         ha='center', va='bottom', fontsize=9, color=colors[i])

    plt.xlabel('考试分数', fontsize=12)
    plt.ylabel('百分比 (%)', fontsize=12)
    plt.title('考试分数分布对比图 (3分分箱)', fontsize=14, fontweight='bold', pad=20)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def get_binned_statistics(exam_data):
    """
    获取分箱后的统计信息
    """
    bin_width = 3
    stats = {}

    for exam_name, score_dist in exam_data.items():
        # 展开数据
        all_scores = []
        for score, count in score_dist.items():
            all_scores.extend([score] * count)

        all_scores = np.array(all_scores)

        # 分箱统计
        min_score = np.floor(min(all_scores) / bin_width) * bin_width
        max_score = np.ceil(max(all_scores) / bin_width) * bin_width
        bins = np.arange(min_score, max_score + bin_width, bin_width)

        hist, bin_edges = np.histogram(all_scores, bins=bins)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

        # 找到人数最多的分箱（众数区间）
        max_count_idx = np.argmax(hist)
        mode_bin = f"{bin_edges[max_count_idx]}-{bin_edges[max_count_idx + 1]}分"
        mode_percent = (hist[max_count_idx] / len(all_scores)) * 100

        stats[exam_name] = {
            '总人数': len(all_scores),
            '分数范围': f"{min(all_scores):.1f}-{max(all_scores):.1f}",
            '平均分': np.mean(all_scores),
            '众数区间': mode_bin,
            '众数区间占比': f"{mode_percent:.1f}%"
        }

    return stats
