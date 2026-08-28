"""
Verifica que ninguna sección del sitio desborde horizontalmente.

Recorre las 7 rutas en 15 anchos distintos (de 320 a 1920 px) y reporta
cualquier elemento que se salga del viewport.

Correlo cada vez que agregues algo a la barra superior o al menú.

    pip install playwright && playwright install chromium
    python tools/check_responsive.py
"""
from playwright.sync_api import sync_playwright
import pathlib, json
url = 'file://' + str((pathlib.Path(__file__).parent.parent / 'index.html').resolve())
routes = ['inicio','escuela','curso','pre-curso','proximamente','inscripcion','contacto']
widths = [320,360,390,414,600,768,900,1024,1180,1200,1280,1366,1440,1600,1920]
problems=[]
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in widths:
        pg = b.new_page(viewport={'width':w,'height':900})
        for r in routes:
            pg.goto(url + '#/' + r)
            pg.wait_for_timeout(120)
            res = pg.evaluate("""() => {
              const vw = document.documentElement.clientWidth;
              const over = [];
              document.querySelectorAll('body *').forEach(el=>{
                if (el.closest('.tablewrap')) return;
                const r = el.getBoundingClientRect();
                if (r.right > vw + 1 || r.left < -1) {
                  over.push({t:el.tagName, c:(el.className||'').toString().slice(0,42),
                             l:Math.round(r.left), r:Math.round(r.right)});
                }
              });
              return {vw, sw: document.documentElement.scrollWidth, over: over.slice(0,4)};
            }""")
            if res['sw'] > res['vw'] + 1 or res['over']:
                problems.append({'w':w,'route':r,'scrollW':res['sw'],'over':res['over']})
        pg.close()
    b.close()
print(json.dumps(problems, indent=1, ensure_ascii=False) if problems else 'SIN DESBORDE HORIZONTAL en ninguna ruta ni ancho')
