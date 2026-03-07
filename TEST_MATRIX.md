# Test Matrix

Matriz base de pruebas funcionales para la práctica de Odoo GT Hookah.

## Cobertura actual

- `gt_hookah_core`
- `gt_hookah_pricing`

## Escenarios validados

| ID | Escenario | Datos | Resultado esperado | Estado |
| --- | --- | --- | --- | --- |
| TM-01 | `order_source` visible en cotización | Nueva cotización | El campo aparece en formulario | OK |
| TM-02 | `order_source` obligatorio | Cotización sin cliente y sin origen | Odoo marca campos inválidos | OK |
| TM-03 | Cotización con origen guardado | Cliente + `WEB_WOO` | La orden se crea y conserva el origen | OK |
| TM-04 | Filtro por origen | Lista de cotizaciones | Se puede filtrar por `WEB_WOO`, `SALES_REP`, `POS`, `BACKOFFICE`, `CRM_HANDOFF` | OK |
| TM-05 | Agrupar por origen | Lista de cotizaciones | Las cotizaciones se agrupan por `order_source` | OK |
| TM-06 | Special price cliente-producto | Cliente Prueba + Producto Prueba + precio 10 | `price_unit = 10.00` | OK |
| TM-07 | Qty break por producto | Producto Prueba + qty 5 + precio 8, sin special price | `price_unit = 8.00` | OK |
| TM-08 | Prioridad special price sobre qty break producto | Cliente Prueba + Producto Prueba + qty 5 | `price_unit = 10.00` | OK |
| TM-09 | Qty break por categoría | Categoría de Producto Prueba + qty 3 + precio 7 | `price_unit = 7.00` cuando no hay special ni qty break de producto | OK |
| TM-10 | Prioridad configurable categoría > producto | Qty break producto = 9, qty break categoría = 7, prioridad categoría primero | `price_unit = 7.00` | OK |
| TM-11 | Prioridad configurable producto > categoría | Qty break producto = 9, qty break categoría = 7, prioridad producto primero | `price_unit = 9.00` | OK |

## Prioridad actual del motor

1. `gt.hookah.pricing.rule`
2. `gt.hookah.qty.break`
3. `gt.hookah.category.qty.break`

## Casos pendientes

| ID | Escenario | Motivo |
| --- | --- | --- |
| TM-12 | Cantidad menor al mínimo de categoría | Validar que mantenga precio base |
| TM-13 | Múltiples qty breaks por producto | Confirmar que toma el `min_qty` más alto aplicable |
| TM-14 | Múltiples qty breaks por categoría | Confirmar que toma el `min_qty` más alto aplicable |
| TM-15 | Multiempresa | Validar aislamiento por `company_id` |
| TM-16 | Categorías jerárquicas | Definir si debe heredar reglas desde categorías padre |
