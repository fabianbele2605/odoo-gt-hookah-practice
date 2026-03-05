# GT Hookah Core (Odoo 18)

Base addon for GT Hookah ERP architecture.

## Features

- Adds mandatory `order_source` field to `sale.order`.
- Source options: `WEB_WOO`, `SALES_REP`, `POS`, `BACKOFFICE`, `CRM_HANDOFF`.
- Shows source in sale order form.

## Why this matters

Implements requirement from architecture doc: no Sales Order can exist without an auditable source.

## Install

1. Add `custom_addons` path in Odoo config.
2. Update app list.
3. Install module `GT Hookah Core`.

## Quick functional test

1. Create quotation.
2. Confirm `Order Source` is mandatory.
3. Save with `WEB_WOO` and verify value persists after reload.
