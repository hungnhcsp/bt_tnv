# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError

class vnpt_exams(models.Model):
    _name = 'vnpt_exams'
    _rec_name = 'structure_id'
    _description = u'Quản lý đề thi'

    name = fields.Char(string=u"Tên đề thi", required=False, )
    structure_id = fields.Many2one(comodel_name="vnpt_exams_structures", string=u"Cấu trúc đề thi", required=True, )
    structure_exam_config_id = fields.Many2one(comodel_name="vnpt_structure_exam_config", string=u"Cấu hình cấu trúc đề", required=True, )
    competency_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Năng lực", required=False,
                                    domain="[('type', '=', '1')]")
    type = fields.Selection(string=u"Dạng đề thi",
                            selection=[('0', u'thi viết nhân viên'), ('1', u'Quản lý đánh giá'), ], required=True, )
    is_active = fields.Boolean(string=u"Active/deactive",required=True  )
    duration_time = fields.Integer(string=u"Thời gian làm bài (Phút)", required=True, )
    pass_point = fields.Float(string=u"Điểm đỗ", required=True, digits=(5, 2))
    is_question_reverse = fields.Boolean(string=u"Đảo câu hỏi", default=True)
    date_start = fields.Date(string=u"Ngày bắt đầu", required=True, )
    date_end = fields.Date(string=u"Ngày kết thúc", required=False, )
    status = fields.Selection(string=u"Trạng thái",
                              selection=[('draft', u'Soạn thảo'), ('open', u'Mở'), ('close', u'Đóng'),
                                         ], required=False, default='draft')

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


