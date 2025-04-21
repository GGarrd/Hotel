from odoo import models, fields, api

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'  # Model name
    _description = 'Room Types'

    name = fields.Char("Room Type", required=True)
    description = fields.Char("Room Type Description")
    photobed = fields.Image("Bed Photo")
    photorestroom = fields.Image("Comfort Room Photo")
    room_image = fields.Image(string="Room Image")
    bathroom_image = fields.Image(string="Bathroom Image")
    daily_charge = fields.Float(string="Daily Charge", required=True)
    charge_description = fields.Text(string="Charge Description")