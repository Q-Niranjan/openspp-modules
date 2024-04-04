# Part of OpenSPP. See LICENSE file for full copyright and licensing details.

from odoo import Command, fields, models


class SPPCreateEventPermanentCropsWizard(models.TransientModel):
    _name = "spp.create.event.permanent.crops.wizard"
    _description = "XI. Agricultural Production, Sales, Costs and Technologies During the Hot DS"

    event_id = fields.Many2one("spp.event.data")

    crop_prod_ids = fields.One2many(
        "spp.create.event.permanent.crops.prod.wizard",
        "crop_permanent_id",
        string="Agricultural Production During Cold DS",
    )
    crop_cost_ids = fields.One2many(
        "spp.create.event.permanent.crops.cost.wizard",
        "crop_permanent_id",
        string="Agricultural Cost During Cold DS",
    )
    crop_tech_ids = fields.One2many(
        "spp.create.event.permanent.crops.tech.wizard",
        "crop_permanent_id",
        string="Agricultural Technologies During Cold DS",
    )

    def create_event(self):
        for rec in self:
            vals_list = {}
            if rec.crop_prod_ids:
                produce_vals = []
                for produce in rec.crop_prod_ids:
                    produce_vals.append(
                        Command.create(
                            {
                                "crop_id": produce.crop_id.id,
                                "harvest_area": produce.harvest_area,
                                "harvest_amt_kg": produce.harvest_amt_kg,
                                "sales_qty_kg": produce.sales_qty_kg,
                                "sales_price_lak_kg": produce.sales_price_lak_kg,
                                "sales_value": produce.sales_value,
                                "contract_farming": produce.contract_farming,
                                "partner_name": produce.partner_name,
                            }
                        )
                    )
                vals_list.update({"crop_prod_ids": produce_vals})

            if rec.crop_cost_ids:
                cost_vals = []
                for cost in rec.crop_cost_ids:
                    cost_vals.append(
                        Command.create(
                            {
                                "crop_id": cost.crop_id.id,
                                "labor_input_days": cost.labor_input_days,
                                "preparation_farmland": cost.preparation_farmland,
                                "seeds": cost.seeds,
                                "labor_cost": cost.labor_cost,
                                "fertilizer": cost.fertilizer,
                                "pesticide": cost.pesticide,
                                "herbicide_oth": cost.herbicide_oth,
                                "water_fee": cost.water_fee,
                                "total_equipment": cost.total_equipment,
                                "oth_fees": cost.oth_fees,
                                "total_prod_cost": cost.total_prod_cost,
                            }
                        )
                    )
                vals_list.update({"crop_cost_ids": cost_vals})

            if rec.crop_tech_ids:
                tech_vals = []
                for tech in rec.crop_tech_ids:
                    tech_vals.append(
                        Command.create(
                            {
                                "crop_id": tech.crop_id.id,
                                "organic_fertilizer": tech.organic_fertilizer,
                                "greenhouse": tech.greenhouse,
                                "multing": tech.multing,
                                "irrigation": tech.irrigation,
                                "water_pump": tech.water_pump,
                                "drip_irrigation": tech.drip_irrigation,
                                "sprinkler": tech.sprinkler,
                                "machine_harvest": tech.machine_harvest,
                                "dry_processing": tech.dry_processing,
                                "post_harvest_treatment": tech.post_harvest_treatment,
                                "other": tech.other,
                            }
                        )
                    )
                vals_list.update({"crop_tech_ids": tech_vals})

            event = self.env["spp.event.permanent.crops"].create(vals_list)
            rec.event_id.res_id = event.id

            return event


class SPPCreateEventPermanentCropsProduceWizard(models.TransientModel):
    _name = "spp.create.event.permanent.crops.prod.wizard"
    _description = "XI. Agricultural Production During the Hot DS"

    crop_permanent_id = fields.Many2one(
        "spp.create.event.permanent.crops.wizard",
        string="Agricultural Production, Sales, Cost and Technologies during Cold DS",
    )
    crop_id = fields.Many2one("spp.farm.species", string="Crop", domain="[('species_type', '=', 'crop')]")
    harvest_area = fields.Float("Harvest Area (ha)")
    harvest_amt_kg = fields.Float("Harvest Amount (kg)")
    sales_qty_kg = fields.Float("Sales Quantity (kg)")
    sales_price_lak_kg = fields.Float("Sales Price (LAK/kg)")
    sales_value = fields.Float("Sales Value")
    contract_farming = fields.Selection([("1", "Yes"), ("2", "No")])
    partner_name = fields.Char("Name of partner in contact farming")


class SPPCreateEventPermanentCropsCostWizard(models.TransientModel):
    _name = "spp.create.event.permanent.crops.cost.wizard"
    _description = "XI. Agricultural Costs During the Hot DS"

    crop_permanent_id = fields.Many2one(
        "spp.create.event.permanent.crops.wizard",
        string="Agricultural Production, Sales, Cost and Technologies during Cold DS",
    )
    crop_id = fields.Many2one("spp.farm.species", string="Crop", domain="[('species_type', '=', 'crop')]")
    labor_input_days = fields.Integer("Labor Input (Days)")
    preparation_farmland = fields.Float("Cost of Farmland Preparation")
    seeds = fields.Float("Cost of Seeds")
    labor_cost = fields.Float("Cost of Labor")
    fertilizer = fields.Float("Cost of Fertilizer")
    pesticide = fields.Float("Cost of Pesticide")
    herbicide_oth = fields.Float("Cost of Herbicide and Other Agro-chem")
    water_fee = fields.Float("Water Fee")
    total_equipment = fields.Float("Cost of Tools or Equipment")
    oth_fees = fields.Float("Other Fees")
    total_prod_cost = fields.Float("Total Production Cost")


class SPPCreateEventPermanentCropsTechWizard(models.TransientModel):
    _name = "spp.create.event.permanent.crops.tech.wizard"
    _description = "XI. Agricultural Technologies During the Hot DS"

    crop_permanent_id = fields.Many2one(
        "spp.create.event.permanent.crops.wizard",
        string="Agricultural Production, Sales, Cost and Technologies during Cold DS",
    )
    crop_id = fields.Many2one("spp.farm.species", string="Crop", domain="[('species_type', '=', 'crop')]")
    organic_fertilizer = fields.Selection(
        [("1", "Selected"), ("0", "Not Selected")], string="Organic Fertilizer, Pesticide / Herbicide"
    )
    greenhouse = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Greenhouse")
    multing = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Multying")
    irrigation = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Irrigation (Normal)")
    water_pump = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Water Pump")
    drip_irrigation = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Drip Irrigation")
    sprinkler = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Sprinkler")
    machine_harvest = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Machine Harvest")
    dry_processing = fields.Selection([("1", "Selected"), ("0", "Not Selected")], string="Dry Processing")
    post_harvest_treatment = fields.Selection(
        [("1", "Selected"), ("0", "Not Selected")], string="Post Harvest Treatment (Fungicide)"
    )
    other = fields.Char("Others")