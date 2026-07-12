# masters.md — Plan maestro & tracker de experimentos

> Documento vivo. Fuente única de verdad para la estrategia de marca, los
> experimentos de landing, las campañas de ads y sus resultados.
> **Última actualización:** 2026-07-12

---

## 0. Posicionamiento (no tocar sin motivo)

- **Promesa central:** *El trading no necesita más gurús. Necesita ciencia.*
- **Diferenciador:** una página de ventas con **bibliografía**. Método (6 filtros) > señales.
- **Audiencia:** traders de LatAm con capital de riesgo real que prefieren una verdad incómoda a una promesa bonita.
- **Oferta:** mentoría 1-a-1 de 12 semanas · escalera de precios $1,997 → $4,997 → $9,997 → $24,997 (ancla).
- **Marca personal:** el fundador debe tener cara y nombre. La gente sigue a una persona, no a un logo. *(Pendiente: rellenar bloque de fundador en `index.html`.)*

---

## 1. Activos del repo

| Activo | Ruta | Rol |
|--------|------|-----|
| Landing principal | `index.html` | Página completa · destino de tráfico caliente y orgánico |
| Gracias | `gracias.html` | Confirmación post-formulario (conversión medible) |
| Playbook de contenido | `contenido/auditoria-en-vivo.md` | Motor de tráfico orgánico ("La Autopsia") |
| **Landers de campaña** | `landings/*.html` | Páginas de una sola idea para validar ángulos con ads |
| CSS de landers | `assets/css/landing.css` | Estilos compartidos de los landers |
| Este plan | `masters.md` | Estrategia + tracker |

---

## 2. Experimentos de landing (para validar ángulos con ads)

Cada lander aísla **un solo ángulo** para medir cuál convierte mejor. Todos capturan
el mismo lead (email + contacto) y redirigen a `gracias.html`. El campo oculto
`Campaña` etiqueta cada envío para atribución.

| Var | Archivo | Ángulo (hipótesis) | Hook principal |
|-----|---------|--------------------|----------------|
| **A** | `landings/a-97-pierde.html` | **Aversión a la pérdida.** El miedo a estar en el 97% mueve más que la ambición. | "El 97% de los day traders pierde. ¿De qué lado estás?" |
| **B** | `landings/b-10-sistemas.html` | **Curiosidad / secreto.** La brecha de información ("los 10 sistemas") genera clics. | "Existen 10 sistemas que sí sobrevivieron la década." |
| **C** | `landings/c-sin-gurus.html` | **Identidad / contrarian.** El trader escéptico se auto-selecciona. | "El trading no necesita más gurús. Necesita ciencia." |

**Cómo probar:** una campaña por lander (o un ad set por lander dentro de una campaña
de tráfico), mismo presupuesto e idéntico público. Corre 5–7 días. Gana el que tenga
menor **coste por lead cualificado**, no el de más clics.

> Nota de publicación: estos landers usan rutas relativas (`../assets/...`). Funcionan
> en GitHub Pages bajo `/tradingcientifico/landings/`. Verifica que las imágenes carguen
> antes de gastar en ads.

---

## 3. Creatividades de anuncios (listas para producir)

> ⚠️ **Cumplimiento (Meta/TikTok):** los anuncios financieros están restringidos.
> **Nunca** prometas rentabilidad, ingresos ni "hazte rico". Enfoca en *educación*,
> *método* y *evidencia*. Todo copy abajo ya respeta esto. Puede requerir revisión
> manual de la plataforma — es normal.

### Ad 1 — «El 97%» → Lander A  *(aversión a la pérdida)*
- **Formato:** imagen estática o video 15 s (vertical 9:16 + cuadrado 1:1).
- **Gancho visual (primeros 3 s):** curva de capital que sube… y de golpe se desploma. Texto: *"El 97% pierde."*
- **Primary text:**
  > 19.646 day traders. 300+ sesiones cada uno. El 97% perdió dinero. No fue mala suerte — fue falta de método. Aprende a auditar cualquier sistema de trading con rigor científico, antes de arriesgar un dólar. Diagnóstico gratis 👇
- **Titular:** *El 97% de los day traders pierde. ¿Sabes de qué lado estás?*
- **CTA:** "Más información".

### Ad 2 — «Los 10 sistemas» → Lander B  *(curiosidad)*
- **Formato:** carrusel (3–4 tarjetas) o video 20 s.
- **Gancho visual:** tabla borrosa con candados (reutiliza el estilo de la Tabla 1 del sitio).
- **Primary text:**
  > Existen 10 sistemas de trading publicados en journals de primer nivel que sobrevivieron replicación independiente en la última década. No decimos sus nombres aquí — cuando una estrategia se populariza, su retorno cae un 58%. Pero sí te mostramos la evidencia. ¿El que usas hoy está en la lista?
- **Titular:** *Los 10 sistemas que la evidencia respalda (con bibliografía).*
- **CTA:** "Más información".

### Ad 3 — «Sin gurús» → Lander C  *(identidad / contrarian)*
- **Formato:** video del fundador a cámara 20–30 s (¡marca personal!).
- **Gancho (a cámara, primeros 3 s):** *"Deja de seguir gurús de trading. Te explico por qué con datos."*
- **Primary text:**
  > Nada de señales para copiar. Nada de capturas con 3 operaciones ganadoras. Solo el proceso que usa la academia para separar una estrategia real del ruido — traducido a decisiones de trading. Con bibliografía. Mentoría 1-a-1 basada en evidencia para LatAm.
- **Titular:** *El trading no necesita más gurús. Necesita ciencia.*
- **CTA:** "Más información".

### Variaciones de gancho para Shorts/Reels orgánicos (reciclables como ads)
1. "La única pregunta que hace colapsar el 90% de los backtests que te venden."
2. "Un t-stat de 2 ya no prueba nada. Te explico por qué en 30 segundos."
3. "Le pasé el sistema de un gurú famoso por 6 filtros científicos. Mira qué quedó."

---

## 4. Plan de segmentación (borrador para Meta)

- **Ubicación:** México, Colombia, Argentina, Chile, Perú (arranca con los 5 de mayor volumen).
- **Edad:** 25–55.
- **Intereses:** trading, inversión, bolsa de valores, análisis técnico, criptomonedas, finanzas personales, Interactive Brokers, TradingView.
- **Objetivo de campaña:** Leads (formulario en el sitio) o Tráfico para la fase de validación.
- **Presupuesto de prueba sugerido:** USD 15–25/día por ad set, 5–7 días → suficiente para ~50 leads y una señal estadística temprana.
- **Regla de decisión:** pausa el ad set cuyo CPL sea >2× el mejor tras 50 leads acumulados en la campaña.

---

## 5. Estado de lanzamiento de ads

| Paso | Estado | Notas |
|------|--------|-------|
| Landers publicados | ⬜ Pendiente | Merge del PR + verificar en GitHub Pages |
| Bloque de fundador con datos reales | ⬜ Pendiente | Solo lo puede hacer Ney (nombre, foto, historia) |
| Cuenta de anuncios conectada | ⬜ Pendiente | Requiere autorización explícita de Ney |
| Presupuesto y método de pago | ⬜ Pendiente | Definir tope diario/total |
| Creatividades producidas (imagen/video) | ⬜ Pendiente | Guiones listos arriba |
| Campañas creadas en PAUSA | ⬜ Pendiente | Se crean en borrador; no gastan hasta aprobar |
| **Lanzamiento en vivo** | 🔴 Bloqueado | **No se activa sin OK explícito de Ney** (gasto real + público) |

> **Por qué está bloqueado:** activar ads gasta dinero real y publica bajo las cuentas
> de Ney. Se prepara todo en borrador/pausa; el "play" lo da una persona, no el agente.

---

## 6. Log de resultados (rellenar durante las pruebas)

| Fecha | Lander | Ad | Gasto | Impres. | Clics | CTR | Leads | CPL | Notas |
|-------|--------|----|-------|---------|-------|-----|-------|-----|-------|
| — | — | — | — | — | — | — | — | — | — |

---

## 7. Próximas acciones

- [ ] Ney rellena el bloque de fundador (`index.html`) + sube `assets/img/fundador.jpg`.
- [ ] Merge del PR y verificación de los 3 landers en producción.
- [ ] Producir 1 imagen/video por ad (los guiones ya están en §3).
- [ ] Ney autoriza cuenta de ads + presupuesto → se crean campañas en PAUSA.
- [ ] Revisión conjunta → lanzamiento.
- [ ] Tras 5–7 días: llenar §6 y quedarse con el ángulo ganador.
