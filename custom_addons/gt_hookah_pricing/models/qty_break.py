from odoo import api, fields, models
from odoo.exceptions import ValidationError


class GTHookahQtyBreak(models.Model):
    _name = "gt.hookah.qty.break"
    _description = "GT Hookah Quantity Break"
    _order = "product_id, min_qty desc"

    product_id = fields.Many2one("product.product", required=True, string="Product")
    min_qty = fields.Float(required=True, string="Minimum Quantity", default=1.0)
    price = fields.Float(required=True, string="Unit Price")
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
    )

    _sql_constraints = [
        (
            "gt_unique_product_min_qty_company",
            "unique(product_id, min_qty, company_id)",
            "Only one qty break per product/min_qty/company is allowed.",
        )
    ]

    @api.constrains("min_qty", "price")
    def _check_values(self):
        for rec in self:
            if rec.min_qty <= 0:
                raise ValidationError("Minimum quantity must be greater than zero.")
            if rec.price < 0:
                raise ValidationError("Price must be non-negative.")
