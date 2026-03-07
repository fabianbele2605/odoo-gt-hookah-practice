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

Implementa un motor base de precios con prioridad:

1. Precio especial por cliente-producto (`gt.hookah.pricing.rule`)
2. Quantity break por producto (`gt.hookah.qty.break`)
3. Quantity break por categoría (`gt.hookah.category.qty.break`)

Comportamiento validado:
- Si existe precio especial activo, gana sobre cualquier quantity break.
- Si no existe precio especial, aplica quantity break por producto.
- Si no existe precio especial ni quantity break por producto, aplica quantity break por categoría.

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

Modelos creados en `gt_hookah_pricing`:

- `gt.hookah.pricing.rule`
- `gt.hookah.qty.break`
- `gt.hookah.category.qty.break`

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

### C. Quantity Break por producto

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

### E. Quantity Break por categoría

1. Ir a `GT Pricing > Category Quantity Breaks`
2. Crear regla:
   - Product Category: categoría de `Producto Prueba`
   - Minimum Quantity: `3`
   - Unit Price: `7`
3. Desactivar temporalmente Special Price
4. Desactivar temporalmente Quantity Break por producto
5. Asegurar que `Producto Prueba` use esa categoría
6. En cotización con qty `3`, verificar `price_unit = 7`

## Git

Subir cambios:

```bash
git add .
git commit -m "mensaje"
git push
```

## Documentación adicional

- Ver [TEST_MATRIX.md](/mnt/n/fabian/odoo/TEST_MATRIX.md) para los escenarios funcionales validados.

## Próximos pasos sugeridos

- Prioridad configurable (no hardcoded)
- Quantity break por categoría de forma más robusta con categorías jerárquicas
- Matriz de pruebas extendida (10 a 30 escenarios)
- Base para integración Woo ↔ Odoo con logs e idempotencia
