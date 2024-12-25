from odoo import models, fields


class AsepticChannel(models.Model):
    _name = "aseptic_roots.channel"
    _description = "Aseptic roots channels"

    aseptic_channel_url = fields.Char()
    aseptic_channel_type = fields.Char()
    aseptic_channel_authorized = fields.Boolean()
    aseptic_channel_origin = fields.Char()
