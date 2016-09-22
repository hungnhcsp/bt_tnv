# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_exams_structures(models.Model):
    _name = 'vnpt_exams_structures'
    _inherit = ['mail.thread']
    _description = u'Cấu trúc đề thi'

    name = fields.Char(string=u"Tên", required=True, )
    duration_time = fields.Integer(string=u"Thời gian làm bài (Phút)", required=True, )
    pass_point = fields.Float(string=u"Điểm đỗ", required=True, digits=(5, 2))
    is_question_reverse = fields.Boolean(string=u"Đảo câu hỏi", default=True)
    date_start = fields.Date(string=u"Ngày bắt đầu", required=True, )
    date_end = fields.Date(string=u"Ngày kết thúc", required=False, )
    exam_num = fields.Integer(string=u"Số đề", required=False, default=10)
    chucdanh_id = fields.Many2many(comodel_name="hr.job", relation="exams_structures_hr_job_rel",
                                   column1="structure_id", column2="job_id", string=u"Chức danh", )
    vitri_id = fields.Many2many(comodel_name="vnpt.hr.vitricongviec", relation="exams_structures_hr_vtcv_rel",
                                column1="structure_id", column2="vitri_id", string=u"Vị trí", )
    note = fields.Text(string=u"Ghi chú", required=False, )
    department_id = fields.Many2many(comodel_name="hr.department", relation="exams_structures_hr_department",
                                     column1="structure_id", column2="department_id", string=u"Phòng ban", )
    dsnv_thamgiathem = fields.One2many(comodel_name="vnpt_exam_assign_employees_structure", inverse_name="structure_id",
                                       string=u"Ds nhân viên tham gia thêm", required=False, )
    status = fields.Selection(string=u"Trạng thái",
                              selection=[('draft', u'Soạn thảo'), ('open', u'Mở'), ('close', u'Đóng'),
                                         ('finish', u'Kết thúc')], required=False, default='draft')
    is_create = fields.Boolean(string=u"Is create", )
    list_exam_config = fields.One2many(comodel_name="vnpt_structure_exam_config", inverse_name="structure_id",
                                       string=u"Danh sách cấu trúc đề thi", required=False, )
    is_active = fields.Boolean(string=u"Active/deactive", default=True)
    error_messase = fields.Text(string=u"Error Message", required=False, ) # cho việc check dữ liệu job

    @api.multi
    def action_draft(self):
        self.status = 'draft'

    @api.multi
    def action_open(self):
        self.status = 'open'

    @api.multi
    def action_close(self):
        self.status = 'close'

    @api.multi
    def action_finish(self):
        self.status = 'finish'


vnpt_exams_structures()
