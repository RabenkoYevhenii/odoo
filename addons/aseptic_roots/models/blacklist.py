from odoo import models, fields


class AsepticBlacklist(models.Model):
    _name = 'aseptic_roots.blacklist'
    _description = 'Aseptic roots blacklists'

    aseptic_blacklist_text = fields.Char()
    aseptic_blacklist_comment = fields.Char()
