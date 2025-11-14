import pandas as pd
import numpy as np
import random
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import os
from datetime import datetime, timedelta

def generate_all_students():
    """
    生成所有班级的所有学生基本信息
    """
    students = []

    # 定义班级
    classes = [f'{i}' for i in range(1, 16)]

    # 常见姓氏和名字
    surnames = ['李', '王', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴',
                '徐', '孙', '胡', '朱', '高', '林', '何', '郭', '马', '罗']
    given_names = ['明', '华', '强', '伟', '芳', '娜', '秀英', '敏', '静', '磊',
                   '军', '杰', '娟', '艳', '勇', '超', '婷', '鹏', '鑫', '浩',
                   '宇', '晨', '旭', '阳', '欣', '怡', '悦', '博', '文', '哲']

    student_id = 1
    for class_name in classes:
        # 每个班级40名学生
        for i in range(1, 41):
            name = random.choice(surnames) + random.choice(given_names)
            students.append({
                '班级': class_name,
                '学号': f"{student_id:04d}",
                '姓名': name
            })
            student_id += 1

    return students

def generate_exam_scores(students, exam_number):
    """
    为某次考试生成成绩数据
    """
    exam_data = []

    for student in students:
        # 基础能力水平（模拟学生的真实水平）
        base_level = random.randint(60, 130)

        # 不同科目有不同的成绩特点
        scores = {
            '语文': max(0, min(150, base_level + random.randint(-15, 15))),
            '数学': max(0, min(150, base_level + random.randint(-20, 20))),
            '英语': max(0, min(150, base_level + random.randint(-18, 18))),
            '物理': max(0, min(100, (base_level * 0.7) + random.randint(-10, 10))),
            '化学': max(0, min(100, (base_level * 0.72) + random.randint(-8, 12))),
            '生物': max(0, min(100, (base_level * 0.75) + random.randint(-10, 10))),
            '政治': max(0, min(100, (base_level * 0.68) + random.randint(-5, 15))),
            '地理': max(0, min(100, (base_level * 0.65) + random.randint(-8, 12))),
            '历史': max(0, min(100, (base_level * 0.7) + random.randint(-6, 14)))
        }

        # 添加考试场次的影响（有些考试难，有些简单）
        exam_difficulty = random.uniform(0.9, 1.1)
        for subject in scores:
            if subject in ['语文', '数学', '英语']:
                scores[subject] = int(scores[subject] * exam_difficulty)
            else:
                scores[subject] = int(scores[subject] * (0.95 + exam_difficulty * 0.1))

            # 确保分数在合理范围内
            if subject in ['语文', '数学', '英语']:
                scores[subject] = max(0, min(150, scores[subject]))
            else:
                scores[subject] = max(0, min(100, scores[subject]))

        student_record = student.copy()
        student_record.update(scores)
        exam_data.append(student_record)

    return exam_data

def create_excel_with_styles(filename, data, exam_title):
    """
    创建带有样式的Excel文件
    """
    df = pd.DataFrame(data)

    # 使用openpyxl引擎来添加样式
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=exam_title, index=False)

        # 获取workbook和worksheet
        workbook = writer.book
        worksheet = writer.sheets[exam_title]

        # 设置列宽
        column_widths = {
            'A': 10,  # 班级
            'B': 8,   # 学号
            'C': 8,   # 姓名
            'D': 6,   # 语文
            'E': 6,   # 数学
            'F': 6,   # 英语
            'G': 6,   # 物理
            'H': 6,   # 化学
            'I': 6,   # 生物
            'J': 6,   # 政治
            'K': 6,   # 地理
            'L': 6    # 历史
        }

        for col, width in column_widths.items():
            worksheet.column_dimensions[col].width = width

        # 设置数据区域居中对齐
        for row in worksheet.iter_rows(min_row=2, max_row=len(data)+1, max_col=12):
            for cell in row:
                cell.alignment = Alignment(horizontal='center', vertical='center')

def main():
    """
    主函数：生成15次考试的数据表格
    """
    # 创建输出目录
    output_dir = './'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 生成所有学生基本信息
    print("正在生成学生基本信息...")
    all_students = generate_all_students()
    print(f"共生成 {len(all_students)} 名学生数据")

    # 考试名称列表
    exam_names = [
        "第一学期期中考试",
        "第一学期期末考试",
        "第二学期期中考试",
        "第二学期期末考试",
        "第三次月考",
        "第四次月考",
        "第五次月考",
        "第六次月考",
        "第一次模拟考试",
        "第二次模拟考试",
        "第三次模拟考试",
        "第四次模拟考试",
        "第五次模拟考试",
        "学业水平考试",
        "毕业考试"
    ]

    print("\n正在生成考试数据表格...")

    for i, exam_name in enumerate(exam_names, 1):
        # 为这次考试生成成绩
        exam_data = generate_exam_scores(all_students, i)

        # 创建文件名
        filename = f"{output_dir}/第{i:02d}次考试_{exam_name}.xlsx"

        # 创建Excel文件
        create_excel_with_styles(filename, exam_data, f"{exam_name}成绩单")

        print(f"已生成: 第{i:02d}次考试 - {exam_name} (包含{len(exam_data)}名学生数据)")

    print(f"\n完成！共生成{len(exam_names)}个考试数据表格，保存在 '{output_dir}' 目录中。")

    # 显示统计信息
    print("\n数据统计:")
    print(f"总学生数: {len(all_students)}")
    print(f"班级分布: 高一5个班, 高二5个班, 高三5个班")
    print(f"每班学生: 40人")

    # 显示样例数据
    sample_exam = generate_exam_scores(all_students[:5], 1)
    df_sample = pd.DataFrame(sample_exam)
    print("\n样例数据（前5名学生）:")
    print(df_sample.head())

if __name__ == "__main__":
    main()