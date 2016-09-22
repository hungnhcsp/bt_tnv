# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError

class vnpt_exam_tags(models.Model):
    _name = 'vnpt_exam_tags'
    _rec_name = 'name'
    _description = u'Danh sách tags'

    name = fields.Char(string=u"Tên tag", required=True, )
    text_color = fields.Char(string=u"Màu text", required=False, )
    background_color = fields.Char(string=u"Màu nền", required=False, )
    is_active = fields.Boolean(string=u"Active/Deactive", default=True,required=True )
