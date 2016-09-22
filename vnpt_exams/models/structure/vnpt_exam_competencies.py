# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_exam_competencies(models.Model):
    _name = 'vnpt_exam_competencies'
    _rec_name = 'name'
    _description = u'Từ điển năng lực'

    code_competency = fields.Char(string=u"Mã năng lực", required=True, )
    name = fields.Char(string=u"Tên năng lực", required=True, )
    type = fields.Selection(string=u"Nhóm năng lực",
                            selection=[('0', u'Nhóm năng lực'), ('1', u'Năng lực'), ('2', u'Mức năng lực'),
                                       ('3', u'Mức năng lực chi tiết')],
                            required=True, )
    competency_level = fields.Integer(string=u"Mức năng lực", required=False, )
    note = fields.Text(string=u"Ghi chú", required=False, )
    parent_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Từ điển năng lực cha", required=False, )
    child_ids = fields.One2many(comodel_name="vnpt_exam_competencies", inverse_name="parent_id",
                                string=u"Từ điển năng lực con", required=False, )
    is_active = fields.Boolean(string=u"Active/deactive", default=True)


vnpt_exam_competencies()
