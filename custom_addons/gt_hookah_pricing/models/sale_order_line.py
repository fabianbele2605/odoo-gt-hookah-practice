from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_id", "order_id.partner_id", "product_uom_qty")
    def _onchange_gt_hookah_special_price(self):
        for line in self:
            if not line.product_id or not line.order_id.partner_id:
                continue

            priority = self.env["ir.config_parameter"].sudo().get_param(
                "gt_hookah_pricing.priority",
                default="special_product_qty_category",
            )

            special_rule = self.env["gt.hookah.pricing.rule"].search(
                [
                    ("partner_id", "=", line.order_id.partner_id.id),
                    ("product_id", "=", line.product_id.id),
                    ("company_id", "=", line.order_id.company_id.id),
                    ("active", "=", True),
                ],
                limit=1,
            )
            if special_rule:
                line.price_unit = special_rule.special_price
                continue

            product_qty_break = self.env["gt.hookah.qty.break"].search(
                [
                    ("product_id", "=", line.product_id.id),
                    ("company_id", "=", line.order_id.company_id.id),
                    ("active", "=", True),
                    ("min_qty", "<=", line.product_uom_qty or 0.0),
                ],
                order="min_qty desc",
                limit=1,
            )

            category_qty_break = self.env["gt.hookah.category.qty.break"].search(
                [
                    ("categ_id", "=", line.product_id.categ_id.id),
                    ("company_id", "=", line.order_id.company_id.id),
                    ("active", "=", True),
                    ("min_qty", "<=", line.product_uom_qty or 0.0),
                ],
                order="min_qty desc",
                limit=1,
            )

            if priority == "special_category_product":
                if category_qty_break:
                    line.price_unit = category_qty_break.price
                    continue
                if product_qty_break:
                    line.price_unit = product_qty_break.price
                    continue
            else:
                if product_qty_break:
                    line.price_unit = product_qty_break.price
                    continue
                if category_qty_break:
                    line.price_unit = category_qty_break.price
