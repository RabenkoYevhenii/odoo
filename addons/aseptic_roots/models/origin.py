from odoo import models, fields


class AsepticOrigin(models.Model):
    _name = "aseptic_roots.origin"
    _description = "Aseptic roots origin"

    aseptic_origin_name = fields.Char()
    aseptic_origin_type = fields.Char()
    aseptic_origin_country = fields.Many2one('res.country')
    aseptic_origin_blocked = fields.Many2one('aseptic_roots.blocked')


class AsepticOriginBlocked(models.Model):
    _name = "aseptic_roots.blocked"
    _description = "Aseptic roots blocked"

    aseptic_blocked_status = fields.Boolean()
    aseptic_blocked_reason = fields.Char()
