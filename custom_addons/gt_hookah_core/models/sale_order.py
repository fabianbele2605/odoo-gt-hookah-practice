from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_source = fields.Selection(
        selection=[
            ("web_woo", "WEB_WOO"),
            ("sales_rep", "SALES_REP"),
            ("pos", "POS"),
            ("backoffice", "BACKOFFICE"),
            ("crm_handoff", "CRM_HANDOFF"),
        ],
        string="Order Source",
        required=True,
        tracking=True,
        help="Mandatory source for every sales order.",
    )
