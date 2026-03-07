from odoo import api, fields, models
from odoo.exceptions import ValidationError


class GTHookahCategoryQtyBreak(models.Model):
    _name = "gt.hookah.category.qty.break"
    _description = "GT Hookah Category Quantity Break"
    _order = "categ_id, min_qty desc"

    categ_id = fields.Many2one("product.category", required=True, string="Product Category")
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
            "gt_unique_category_min_qty_company",
            "unique(categ_id, min_qty, company_id)",
            "Only one category qty break per category/min_qty/company is allowed.",
        )
    ]

    @api.constrains("min_qty", "price")
    def _check_values(self):
        for rec in self:
            if rec.min_qty <= 0:
                raise ValidationError("Minimum quantity must be greater than zero.")
            if rec.price < 0:
                raise ValidationError("Price must be non-negative.")
