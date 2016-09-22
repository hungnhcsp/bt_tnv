# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_exam_assign_employees_structure(models.Model):
    _name = 'vnpt_exam_assign_employees_structure'
    _rec_name = 'employee_id'
    _inherit = ['mail.thread']
    _description = u'Danh sách nhân viên tham gia khảo sát'

    structure_id = fields.Many2one(comodel_name="vnpt_exams_structures", string=u"Cấu trúc đề thi", required=True, )
    department_id = fields.Many2one(comodel_name="hr.department", string=u"Phòng ban", required=True, )
    employee_id = fields.Many2one(comodel_name="hr.employee",
                                  domain="[('department_id', '=', department_id),('status', '=', 'confirmed')]",
                                  string=u"Nhân viên tham gia", required=True, )
    is_active = fields.Boolean(string=u"Hoạt động", default=False, required=True)
    ma_nv = fields.Char(related='employee_id.vnpt_ma_nhan_vien', string=u'Mã nhân viên', store=True, readonly=True)
    note = fields.Text(string=u"Ghi chú", required=False, )


vnpt_exam_assign_employees_structure()
