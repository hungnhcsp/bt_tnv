# -*- coding: utf-8 -*-
{
    'name': 'Module Thi đánh giá khung năng lực nhân viên',
    'version': '1.0',
    'author': 'VNPT SOFT',
    'category': 'Human Resources',
    'summary': 'Module thi online',
    'description': """
Thi đánh giá năng lực nhân viên
---------------------------------
* Quản lý bộ từ điển năng lực
* Quản lý câu hỏi, câu trả lời
* Quản lý cấu trúc đề thi
* Quản lý đề thi
* Quản lý cấu hình
* Quản lý phần thi
* Chấm thi
* Báo cáo thống kê
    """,
    'website': 'http://www.vnptsoftware.vn/',
    'depends': ['base', 'vnpt_hr_core', 'web', 'website'],
    'data': [
        # config

        # structure
        'views/structure/vnpt_exam_assign_employees_structure.xml',
        'views/structure/vnpt_exams_structures.xml',
        # exams
        'views/exams/vnpt_exams.xml',
        'views/exams/vnpt_questions.xml',
        # statistic

        # security

        # report

        # menu
        'views/vnpt_exam_menu.xml',

        # data
        'data/vnpt_exam_competencies.csv',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
