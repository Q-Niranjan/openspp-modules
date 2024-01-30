from odoo import fields, models


class CustomGroup(models.Model):
    _inherit = "res.partner"

    geo_point = fields.GeoPoint("Address coordinates")
    geo_line = fields.GeoLine("Power supply line", index=True)
    geo_multipolygon = fields.GeoMultiPolygon("NPA Shape")
