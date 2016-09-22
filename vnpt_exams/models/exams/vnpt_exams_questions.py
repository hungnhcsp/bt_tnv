# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError

class vnpt_exams_questions(models.Model):
    _name = 'vnpt_exams_questions'
    _rec_name = 'questions_id'
    _description = u'Danh sách câu hỏi'

    exams_id = fields.Many2one(comodel_name="vnpt_exams", string=u"Thuộc đề thi", required=True, )
    questions_id = fields.Many2one(comodel_name="vnpt_questions", string=u"Danh sách câu hỏi", required=True, )
    is_active = fields.Boolean(string=u"Active/Deactive", required=True )
