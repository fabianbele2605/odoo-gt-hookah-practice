from odoo import api, fields, models
from odoo.exceptions import ValidationError


class GTHookahPricingRule(models.Model):
    _name = "gt.hookah.pricing.rule"
    _description = "GT Hookah Pricing Rule"
    _rec_name = "display_name"

    partner_id = fields.Many2one("res.partner", required=True, string="Customer")
    product_id = fields.Many2one("product.product", required=True, string="Product")
    special_price = fields.Float(required=True, string="Special Price")
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
    )
    display_name = fields.Char(
        compute="_compute_display_name",
        store=True,
    )

    _sql_constraints = [
        (
            "gt_unique_customer_product_company",
            "unique(partner_id, product_id, company_id)",
            "Only one active rule per customer-product-company is allowed.",
        )
    ]

    @api.depends("partner_id", "product_id", "special_price")
    def _compute_display_name(self):
        for rule in self:
            partner = rule.partner_id.name or "-"
            product = rule.product_id.display_name or "-"
            rule.display_name = f"{partner} - {product} - {rule.special_price}"

    @api.constrains("special_price")
    def _check_special_price(self):
        for rule in self:
            if rule.special_price < 0:
                raise ValidationError("Special price must be non-negative.")
