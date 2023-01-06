from odoo import models


class CustomFilterMixin(models.AbstractModel):
    _name = "custom.filter.mixin"
    _description = "Custom Filter Mixin"

    def fields_get(self, allfields=None, attributes=None):
        """Customizing searchable attribute for fields in model.

        Usage:

        - Create / Inherit a model then set new model to inherit this model.

        - Add a field [even stored field] / Altering an old field [even stored field]

        - Add param `allow_filter=False` if you want to hide field from UI filtering.

        ```python
        class ResPartner(models.Model):
            _name = "res.partner"
            _inherit = ["res.partner", "custom.filter.mixin"]

            active = fields.Boolean(
                ...,
                allow_filter=False,
                ...
            )
            newfield = fields.Text(
                ...,
                allow_filter=False,
                ...
            )
        ```


        Args:
            :allfields: list of fields to document, all if empty or not provided

            :attributes: list of description attributes to return for each field,
                all if empty or not provided

        Returns:
            type: dictionary
        """
        res = super().fields_get(allfields, attributes)

        for fname in res.keys():
            res[fname]["searchable"] = (
                getattr(self._fields[fname], "allow_filter", True)
                and res[fname]["searchable"]
            )

        return res
