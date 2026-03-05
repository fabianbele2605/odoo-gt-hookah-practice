# Odoo GT Hookah Practice

Práctica técnica en Odoo 18 para simular parte de la arquitectura ERP de GT Hookah.

## Alcance actual

Se implementaron 2 módulos custom:

- `gt_hookah_core`
- `gt_hookah_pricing`

### 1) `gt_hookah_core`

Extiende `sale.order` con campo obligatorio `order_source`.

Valores:
- `WEB_WOO`
- `SALES_REP`
- `POS`
- `BACKOFFICE`
- `CRM_HANDOFF`

También agrega filtros y agrupación por origen en Cotizaciones para reporting.

### 2) `gt_hookah_pricing`

Implementa motor base de precios con prioridad:

1. Precio especial por cliente-producto (`gt.hookah.pricing.rule`)
2. Quantity break por producto (`gt.hookah.qty.break`)

Comportamiento validado:
- Si existe precio especial activo, gana sobre cualquier quantity break.
- Si no existe precio especial, aplica quantity break por cantidad mínima.

## Estructura

```text
custom_addons/
  gt_hookah_core/
    models/
    views/
  gt_hookah_pricing/
    models/
    views/
    security/
```

## Requisitos

- Docker
- Docker Compose

## Levantar entorno local

Desde la raíz del proyecto:

```bash
docker compose up -d
```

Odoo quedará en:

- `http://localhost:8069`

## Actualizar módulos

```bash
docker compose exec odoo odoo -d odoo18_test -u gt_hookah_core --db_host=db --db_port=5432 --db_user=odoo --db_password=odoo --stop-after-init
docker compose exec odoo odoo -d odoo18_test -u gt_hookah_pricing --db_host=db --db_port=5432 --db_user=odoo --db_password=odoo --stop-after-init
docker compose restart odoo
```

## Flujo de prueba funcional

### A. Order Source obligatorio

1. Ir a `Ventas > Cotizaciones > Nuevo`
2. Verificar que `Order Source` aparece
3. Intentar guardar sin `Cliente` y sin `Order Source` (debe marcar error)
4. Completar y guardar

### B. Special Price

1. Ir a `GT Pricing > Pricing Rules`
2. Crear regla:
   - Customer: `Cliente Prueba`
   - Product: `Producto Prueba`
   - Special Price: `10`
3. Crear cotización con ese cliente/producto
4. Verificar `price_unit = 10`

### C. Quantity Break

1. Ir a `GT Pricing > Quantity Breaks`
2. Crear regla:
   - Product: `Producto Prueba`
   - Minimum Quantity: `5`
   - Price: `8`
3. Desactivar temporalmente Special Price
4. En cotización con qty `5`, verificar `price_unit = 8`

### D. Prioridad de reglas

1. Reactivar Special Price (`10`)
2. En cotización con qty `5`, verificar que aplica `10` (no `8`)

## Git

Subir cambios:

```bash
git add .
git commit -m "mensaje"
git push
```

## Próximos pasos sugeridos

- Quantity break por categoría
- Prioridad configurable (no hardcoded)
- Matriz de pruebas (10 a 30 escenarios)
- Base para integración Woo ↔ Odoo con logs e idempotencia
