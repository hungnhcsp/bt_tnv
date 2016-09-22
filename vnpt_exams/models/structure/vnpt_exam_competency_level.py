# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_exam_competency_level(models.Model):
    _name = 'vnpt_exam_competency_level'
    _rec_name = 'name'
    _description = u'Danh sách các mức từ điển năng lực'

    name = fields.Char(string=u"Tên mức năng lực", required=False, )
    competency_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Thuộc mức năng lực",
                                    required=False, )
    competency_level = fields.Integer(string=u"Mức năng lực", required=False, )
    note = fields.Text(string=u"Ghi chú", required=False, )
    parent_id = fields.Many2one(comodel_name="vnpt_exam_competency_level", string=u"Danh sách mức năng lực cha", required=False, )
    child_ids = fields.One2many(comodel_name="vnpt_exam_competency_level", inverse_name="parent_id",
                                string=u"Danh sách mức năng lực con", required=False, )
    is_active = fields.Boolean(string=u"Active/deactive", default=True)

vnpt_exam_competency_level()