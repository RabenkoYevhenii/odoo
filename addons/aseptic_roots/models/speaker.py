from odoo import models, fields


class AsepticSpeaker(models.Model):
    _name = "aseptic_roots.speaker"
    _description = "Aseptic roots speaker"

    aseptic_speaker_name = fields.Char()
    aseptic_speaker_aliases = fields.Char()
    aseptic_speaker_blocked = fields.Boolean()
