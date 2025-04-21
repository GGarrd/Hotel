# models/rooms.py
from odoo import models, fields, api

class Rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Rooms'

    name = fields.Char(string="Room No.", required=True)
    description = fields.Char(string="Room Description")
    room_type_id = fields.Many2one('hotel.roomtypes', string='Room Type')
    price = fields.Float(string="Price", required=True)
    is_available = fields.Boolean(string="Is Available", default=True)