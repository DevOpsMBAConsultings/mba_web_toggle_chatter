# mba_web_toggle_chatter

Port a **Odoo 20** del módulo OCA `web_toggle_chatter` (colapsar/expandir el
chatter en las vistas form del backend).

## Por qué existe

Adaptación del comportamiento de OCA (`OCA/web`) a la suite de MBA Consultings,
renombrada a `mba_web_toggle_chatter` (módulo individual, `_`).

## Migración 19 → 20 (Owl 3)

- `useState` → `proxy`.
- `this.el` → `this.rootRef()` (FormRenderer usa `rootRef = signal.ref()`).
- Íconos FontAwesome (`fa fa-angle-right/left`) → `oi` + `data-icon="chevron_right/left"`.
- `author` / `website` normalizados a la convención MBA.

Depende solo de `web` (el chatter lo provee `mail` en los modelos `mail.thread`).
