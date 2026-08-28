# Sitio — Escuela de Guardavidas, ONG Sumar Salud

Sitio de la formación de guardavidas de la **Asociación Civil Sumar Salud** (Santa Fe Capital).
Prototipo funcional, en revisión con la directiva. Deriva de sumarsalud.org pero se enfoca
**solo** en la formación de guardavidas.

## Estructura

- `index.html` — el sitio entero: estilos, contenido y navegación en un solo archivo. Sin build, sin dependencias.
- `img/` — las fotos. Ver `img/LEEME.txt` para los nombres exactos que la página busca.
- `tools/check_responsive.py` — verifica que ninguna sección desborde horizontalmente.

Es una SPA simple con enrutado por hash: `#/inicio`, `#/escuela`, `#/curso`, `#/pre-curso`,
`#/proximamente`, `#/inscripcion`, `#/contacto`. El router está al final de `index.html`.

## Reglas de contenido (acordadas con el cliente)

- **Es una "formación", no una "carrera".** El nombre propio es *Formación Profesional de Guardavidas*.
  No debe aparecer la palabra "carrera" en ningún texto del sitio.
- **Sin condicionales ni frases con dudas.** Nada de "suele", "en el primer o segundo mes",
  "aproximadamente", "a confirmar". Todo afirmado. Ejemplo: la inversión **se recupera en dos meses**.
- **El examen de ingreso se rinde, no se aprueba.** Se mantiene la palabra "obligatorio",
  pero sin énfasis en aprobar: la escuela no lo plantea como excluyente y el resultado se
  conversa personalmente con cada aspirante.
- **Oferta actual: solo la formación de guardavidas.** Las capacitaciones para guardavidas
  recibidos (oxigenoterapia en ahogamiento, entrenamientos y simulaciones con protocolos)
  se anuncian en `#/proximamente` sin fechas.
- **El alquiler de equipamiento y los cursos de RCP para la comunidad NO van acá.** Son de la
  ONG y viven en sumarsalud.org, enlazado desde el footer y desde Contacto.

## Datos de la escuela

| | |
|---|---|
| Sede | Club Gimnasia y Esgrima — 4 de Enero 2011, Santa Fe Capital |
| Formación | Abril a diciembre, más prácticas profesionalizantes en enero y febrero |
| Cursada | L/M/V 21:30–23:30 (natación y salvamento) · Ma/Ju 20:00–22:30 (teóricas) |
| Examen de ingreso | Abril. 600 m (300 crawl + 300 pecho) en 14 min, y 25 m subacuático |
| Pre-curso 2027 | Desde el lunes 16/11/2026 hasta marzo. L/M/V 21:30–22:30. $60.000/mes |
| Aranceles de la formación | Se publican el 20/02/2027 |
| Alias bancario | `sumarsaludong` |
| WhatsApp | +54 9 342 472 4998 |
| Correo | contacto@sumarsalud.org |
| Instagram | @guardavidas.sumarsalud |
| Portal de alumnos | https://portal-alumnos-opal.vercel.app/login |
| Razón social | Asociación Civil Sumar Salud — CUIT 30-71653650-1 |
| Marco legal | Reglamento GV01, Consejo Provincial de Guardavidas, Min. de Educación de Santa Fe |

## Diseño

Referencia visual pedida por el cliente: **epsa.org.ar** (sección de formación de guardavidas).
De ahí salen las tipografías, el fondo blanco y aireado, los botones pastilla y el ritmo de
secciones alternadas texto/foto.

- **Tipografías:** Quicksand (títulos, 600/700) y Nunito (texto). Vía Google Fonts.
- **Color principal:** turquesa `--aqua` #009AA8. Es el de Sumar Salud.
  **No usar el naranja de EPSA como color principal**: es la marca de ellos.
- **Ámbar** `--amber` #F2A03D: solo para avisos de "próximamente" y el bloque de aranceles.
- **Violeta/azul** `--violet` #2B2A7C y `--navy` #16255E: portadas y franjas oscuras.
- Todos los colores son variables CSS en `:root`, con su equivalente para modo oscuro.
  **Nunca declarar un color solo dentro del bloque de modo oscuro.**

### Barra superior — cuidado al tocarla

Son **dos filas** a propósito, y la razón es técnica: cuando todo estaba en una sola fila
(logo + menú + teléfono + portal + botón) sumaba ~1580 px contra un contenedor de 1180 y
generaba scroll horizontal. Al separarla, la fila principal quedó en ~1110 px.

- **Franja angosta azul:** solo el portal de alumnos, alineado a la derecha. El WhatsApp
  salió de acá; sigue en el footer y en Contacto.
- **Barra blanca:** logo, menú, botón "Inscribite".
- El portal va más discreto que "Inscribite": quien lo busca ya es alumno.
- Por debajo de 1180 px el menú colapsa en el botón hamburguesa.

**Si agregás un ítem al menú o a la barra, corré `tools/check_responsive.py` antes de publicar.**

## Fotos

Todavía no hay ninguna: la página muestra recuadros punteados con el nombre del archivo que
falta. Apenas se sube el archivo con el nombre correcto, aparece la foto. Ver `img/LEEME.txt`.

El logo actual es un marcador provisorio dibujado en SVG dentro de `index.html`.
**Falta el logo real de la ONG** (el circular con la estrella de la vida).

## Formularios

Los tres formularios (inscripción, aviso de próximas capacitaciones, contacto) son **maqueta**:
no envían ni guardan nada, y muestran un aviso al enviarse. La inscripción real sigue por
https://forms.gle/p51B1kGKeqsqCBLA9

Al pasar a producción en WordPress se montan con Fluent Forms, con notificación a
contacto@sumarsalud.org, copia a Google Sheets y autorespuesta.

**El campo "complicaciones médicas" es dato de salud.** Mantener siempre la leyenda que
aclara para qué se usa, y no exponerlo en mails reenviados ni planillas compartidas de más.

También hay una barra naranja de "Vista previa" arriba de todo: **sacarla antes de publicar
como sitio definitivo.**

## Pendientes

1. Corregir el apellido **Mendoza** (el PDF original dice "Mendonza") donde corresponda.
2. El PDF del pre-curso dice "16 de noviembre" arriba y "14" abajo. El sitio usa el 16.
3. Unificar el teléfono: sumarsalud.org muestra 342 5974998, los PDF y este sitio usan el 342 472 4998.
4. Cargar las fotos.
5. Logo real de la ONG.
6. Subdominio propio para el portal de alumnos (`alumnos.sumarsalud.org`).
7. Fecha y horario exactos del examen de ingreso, cuando se definan.

## Publicar

Está en Vercel. La idea es conectar el repo de GitHub para que cada push publique solo.
Es un sitio estático: sin framework, sin comando de build, directorio raíz.
