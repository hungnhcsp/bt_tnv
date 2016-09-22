# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError

class vnpt_anwsers(models.Model):
    _name = 'vnpt_anwsers'
    _rec_name = 'name'
    _description = u'Danh sách câu trả lời'

    name = fields.Char(string=u"Đáp án", required=True, )
    questions_id = fields.Many2one(comodel_name="vnpt_questions", string=u"Danh sách câu hỏi", required=True, )
    is_true = fields.Boolean(string=u"Đúng",  )
    is_active = fields.Boolean(string=u"Active/Deactive",  )

