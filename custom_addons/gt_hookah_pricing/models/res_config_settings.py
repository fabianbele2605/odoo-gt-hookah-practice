from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    gt_pricing_priority = fields.Selection(
        selection=[
            ("special_product_qty_category", "Special > Product Qty Break > Category Qty Break"),
            ("special_category_product", "Special > Category Qty Break > Product Qty Break"),
        ],
        string="GT Pricing Priority",
        config_parameter="gt_hookah_pricing.priority",
        default="special_product_qty_category",
    )
