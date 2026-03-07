{
    "name": "GT Hookah Pricing",
    "summary": "Customer-product special pricing rules",
    "version": "18.0.1.0.0",
    "author": "GT Hookah",
    "license": "OEEL-1",
    "depends": ["sale_management", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/pricing_rule_views.xml",
        "views/qty_break_views.xml",
        "views/category_qty_break_views.xml",
    ],
    "installable": True,
    "application": False,
}
