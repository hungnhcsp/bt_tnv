# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError


class vnpt_structure_exam_config(models.Model):
    _name = 'vnpt_structure_exam_config'
    _rec_name = 'competency_id'
    _description = u'Cấu hình cấu trúc đề thi'

    competency_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Năng lực", required=False,
                                    domain="[('type', '=', '1')]")
    code_competency = fields.Char(related='competency_id.code_competency', store=True, string=u"Mã năng lực",
                                  required=False, )
    competency_level_id = fields.Many2one(comodel_name="vnpt_exam_competencies", string=u"Mức năng lực",
                                          required=False, domain="[('type', 'in', ['2','3'])]")
    structure_id = fields.Many2one(comodel_name="vnpt_exams_structures", string=u"Cấu trúc đề thi", required=False, )
    question_num = fields.Integer(string=u"Số câu hỏi", required=False, )
    duration_time = fields.Integer(string=u"Thời gian", required=False, )
    point = fields.Integer(string=u"Điểm", required=False, )
    manager_rate = fields.Float(string=u"Tỷ trọng (%)", required=False, )
    is_active = fields.Boolean(string=u"Active/deactive", default=True)


vnpt_structure_exam_config()
