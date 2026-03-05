# Practice Plan - GT Hookah Odoo Interview

## Phase 1 - Done

- Module: `gt_hookah_core`
- Requirement covered: mandatory order source on `sale.order`

## Phase 2 - Pricing engine scaffold

Build module `gt_hookah_pricing`:
- Add pricing policy model with priority field.
- Add customer-product special price model.
- Add quantity break lines.
- Add service method on `sale.order.line` to resolve final unit price by rule priority.

Interview value:
- Explain deterministic pricing hierarchy and test scenarios.

## Phase 3 - Woo connector baseline

Build module `gt_hookah_woo_bridge`:
- Add `woo_external_id` on product and sale order.
- Add sync log model (`request`, `response`, `status`, `retries`).
- Add inbound webhook endpoint for Woo orders.
- Enforce write protection for stock/price from Woo side.

Interview value:
- Explain idempotency, retry policy, and observability.

## Phase 4 - Intercompany automation

Build module `gt_hookah_intercompany`:
- Add configuration for A->B relationship.
- On SO confirmation in company A, auto-create PO in company B.
- Transfer pricing support.
- Validate accounting separation and COGS per company.

Interview value:
- Show SO/PO automation and accounting implications.

## Phase 5 - UAT matrix

Create at least 30 scenarios:
- Pricing conflicts.
- Bundle/kit behavior.
- Multi-company stock isolation.
- Woo order ingestion edge cases.

Interview value:
- Demonstrates production readiness thinking.
