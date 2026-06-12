# Trading Científico — Landing Page

Página de ventas para la mentoría de trading basada en evidencia de [tradingcientifico.com](https://www.tradingcientifico.com), enfocada en coaching high-ticket para Latinoamérica.

**Sitio en vivo:** https://neyt.github.io/tradingcientifico/

## Posicionamiento

- **Diferenciación:** usamos ciencia (literatura académica de finanzas + backtests propios) para separar los sistemas de trading que funcionan de los que no.
- **Promesa:** aprender a auditar cualquier sistema (los "6 filtros") + dominar los 10 sistemas con evidencia en la última década.
- **Modelo:** mentoría 1-a-1 de 12 semanas, precio conversado en llamada de diagnóstico (high-ticket).

## Stack

HTML + CSS + JS puro, sin build ni dependencias. Diseño "paper académico × terminal de trading": secciones numeradas (§), figuras con caption, footnotes y bibliografía real (13 referencias).

```
index.html              página completa (una sola página)
assets/css/styles.css   estilos (tokens de color/tipografía arriba del archivo)
assets/js/main.js       reveals, contadores, curva animada, CTA fijo móvil
assets/img/             imágenes del sitio original (renombradas)
```

## El formulario de aplicación (IMPORTANTE — activar 1 vez)

Las aplicaciones se envían por **FormSubmit.co** a `info@neytrading.com` sin necesidad de backend.
**La primera vez** que alguien envíe el formulario, FormSubmit mandará un correo de activación a
`info@neytrading.com` — hay que hacer clic en **"Activate"** en ese correo (una sola vez). Hasta
entonces los envíos no llegan. Recomendado: envía tú mismo una aplicación de prueba apenas puedas
y activa el servicio.

- Tras enviar, el visitante aterriza en `gracias.html`.
- Si el sitio cambia de dominio, actualiza el campo oculto `_next` en el formulario de `index.html`.
- Opcional (anti-spam): tras activar, FormSubmit te da un *hash* — puedes reemplazar
  `formsubmit.co/info@neytrading.com` por `formsubmit.co/<hash>` para ocultar el email del HTML.

## Cosas que probablemente quieras cambiar

| Qué | Dónde |
|---|---|
| **Email que recibe aplicaciones** | Busca `info@neytrading.com` en `index.html` (action del form + mailto del footer) |
| **Precios** ($1,997 / $4,997 / $9,997) | Sección `id="inversion"` en `index.html` + respuesta de la FAQ "¿Cuánto cuesta?" |
| Textos de cualquier sección | `index.html` — el copy está en español, ordenado por secciones comentadas |
| Colores / fuentes | Variables `:root` al inicio de `styles.css` |
| Imagen de compartir (WhatsApp/redes) | `assets/img/og.jpg` (1200×630) |

## Publicar cambios

```bash
git add -A
git commit -m "Actualiza copy"
git push
```

GitHub Pages se actualiza solo en ~1 minuto.

## Conectar el dominio tradingcientifico.com

1. En el repo: **Settings → Pages → Custom domain** → escribe `www.tradingcientifico.com` y guarda (esto crea el archivo `CNAME`).
2. En tu proveedor de DNS (donde compraste el dominio):
   - Registro `CNAME`: `www` → `neyt.github.io`
   - Registros `A` para el dominio raíz (`tradingcientifico.com`): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Espera la propagación (minutos a horas) y activa **Enforce HTTPS** en Settings → Pages.

> Nota: mientras el dominio siga apuntando al funnel actual (GoHighLevel), el sitio de GitHub vive en la URL de github.io. El cambio de DNS es el interruptor.

## Aviso

Las fotos de traders (Kullamägi, Weschler, Tilson, Kupperman, Pabrai, Van Tharp) provienen del sitio original y se usan como casos de estudio con disclaimer de no-afiliación. El sitio incluye aviso de riesgo y aclaración de que el programa es educativo, no asesoría financiera.
