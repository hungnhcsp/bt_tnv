# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_questions(models.Model):
    _name = 'vnpt_questions'
    _rec_name = 'name'
    _description = u'Bảng câu hỏi'

    name = fields.Char(string=u"Tên câu hỏi", required=True, )
    competency_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Năng lực", required=True,
                                    domain="[('type', '=', '1')]")
    competency_level_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Mức năng lực",
                                          required=True, domain="[('type', 'in', ['2','3'])]")
    type = fields.Selection(string=u"Loại câu hỏi",
                            selection=[('0', u'Đúng/sai'), ('1', u'Chọn nhiều câu trả lời'), ('2', u'Tự luận'), ],
                            required=True, )
    duration_time = fields.Integer(string=u"Thời gian trả lời", required=False, )
    point = fields.Float(string=u"Điểm câu hỏi",  required=True,digits=(5, 2) )
    is_active = fields.Boolean(string=u"Active/deactive",default=True  )
    answer_options = fields.One2many(comodel_name="vnpt_anwsers", inverse_name="questions_id", string=u"Đáp án", required=True, )
    tag = fields.Many2many(comodel_name="vnpt_exam_tags", relation="question_tag_rel", column1="question_id", column2="tag_id", string="Tag", )