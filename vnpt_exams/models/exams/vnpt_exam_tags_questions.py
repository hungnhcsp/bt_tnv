# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError

class vnpt_exam_tags_questions(models.Model):
    _name = 'vnpt_exam_tags_questions'

    _description = u'Quản lý danh sách tag gán câu hỏi'

    tags_id = fields.Many2one(comodel_name="vnpt_exam_tags", string=u"Danh sách tag", required=True, )
    questions_id = fields.Many2one(comodel_name="vnpt_questions", string=u"Danh sách câu hỏi", required=True, )
    is_active = fields.Boolean(string=u"Active/Deactive", default=True, required=True)
