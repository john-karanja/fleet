import sys,re; sys.path.insert(0,'.')
from kit import *
def inner(f):
    s=open(f).read(); return re.search(r'<svg[^>]*>(.*)</svg>',s,re.S).group(1), re.search(r'viewBox="([^"]+)"',s).group(1)
def svg(f,h=None,cls=''):
    b,vb=inner(f); return f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="Swiftfleet">{b}</svg>'
# construction overlay
gl=[custom(ch,800) for ch in TEXT]; xs=layout(gl,58,34); s=0.16; ox=24; base=150
X=lambda x,y: ox+(x+y*SL)*s; Y=lambda y: base-y*s
dx1,dy0,dy1=idot(800); H=dy1-dy0
lines=[]
for y,lab in [(0,'baseline'),(544,'x-height'),(367,'crossbar'),(516,''),(744,'ascender'),(dy0,'dash = i-dot height'),(dy1,'')]:
    lines.append(f'<line x1="0" x2="900" y1="{Y(y):.1f}" y2="{Y(y):.1f}" class="g"/>'+(f'<text x="4" y="{Y(y)-2:.1f}">{lab}</text>' if lab else ''))
for i,c in [(0,389),(0,115),(2,dx1),(3,372),(5,372),(7,455),(8,455),(2,dx1-4.2*H)]:
    x=xs[i]+c; lines.append(f'<line x1="{X(x,-60):.1f}" y1="{Y(-60):.1f}" x2="{X(x,900):.1f}" y2="{Y(900):.1f}" class="k"/>')
wm,vb=inner('out/B-wordmark-light.svg')
construction=f'<svg viewBox="{vb}" class="big">{wm}<g class="ov">{"".join(lines)}</g></svg>'
pal=[('Navy','#1E3F78','“swift”, symbol, all one-colour use','#fff'),('Teal','#1FA3A9','“fleet” and dash at 24 px+ (3.1:1 on white, graphics only)','#fff'),
     ('Teal deep','#147B80','small sizes and any text-sized use (5.0:1 on white)','#fff'),('Teal on dark','#32BFC4','on Night / Navy backgrounds','#10213F'),('Night','#10213F','dark background','#fff')]
P=''.join(f'<div class="sw"><i style="background:{h}"></i><b>{n}</b><code>{h}</code><span>{u}</span></div>' for n,h,u,_ in pal)
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Swiftfleet World-Class</title>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F4F6F8;--card:#fff;--line:#DFE5EB;--ink:#15223B;--mute:#5B6B82;--navy:#1E3F78}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0C1730;--card:#13213F;--line:#24365A;--ink:#E8EEF7;--mute:#9DB0CC}}}}
:root[data-theme="dark"]{{--bg:#0C1730;--card:#13213F;--line:#24365A;--ink:#E8EEF7;--mute:#9DB0CC}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 "Source Sans 3",system-ui,sans-serif}}
main{{max-width:1120px;margin:0 auto;padding:40px 16px 80px}}h1,h2{{font-family:Lexend,sans-serif;font-weight:700;margin:0 0 6px}}h1{{font-size:30px}}h2{{font-size:20px;margin-top:8px}}
p.sub{{color:var(--mute);margin:0 0 28px}}section{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:24px;margin:0 0 20px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}@media(max-width:760px){{.two{{grid-template-columns:1fr}}}}
.tile{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:22px;display:flex;align-items:center;justify-content:center;min-height:150px}}
.tile.dark{{background:#10213F}} .tile svg{{width:100%;max-width:440px;height:auto}} .lab{{font-size:13px;color:var(--mute);margin:8px 0 0}}
ul{{margin:8px 0 0;padding-left:20px}}li{{margin:4px 0}}
.big{{width:100%;height:auto;background:#fff;border-radius:10px;border:1px solid var(--line)}}
.ov .g{{stroke:#C2185B;stroke-width:.5;stroke-dasharray:3 3}} .ov .k{{stroke:#C2185B;stroke-width:.6}} .ov text{{font:7px sans-serif;fill:#C2185B}}
.icons{{display:flex;gap:18px;flex-wrap:wrap;align-items:flex-end}} .icons div{{text-align:center;font-size:12px;color:var(--mute)}}
.sw{{display:grid;grid-template-columns:44px 120px 90px 1fr;gap:12px;align-items:center;padding:8px 0;border-top:1px solid var(--line)}} .sw i{{width:44px;height:28px;border-radius:6px;display:block;border:1px solid var(--line)}}
@media(max-width:640px){{.sw{{grid-template-columns:44px 1fr}} .sw span,.sw code{{grid-column:2}}}}
.dont{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}} .dont .tile{{min-height:100px;padding:14px}} .x{{font-size:13px;color:#B42318;margin-top:6px}}
</style></head><body><main>
<h1>Swiftfleet logo · world-class pass</h1><p class="sub">Lexend kit, rebuilt 2 Oct 2026. Same idea and colours, refined craft. Nothing in <code>final/</code> or <code>final-lexend/</code> was replaced.</p>

<section><h2>Before / after</h2><div class="two">
<div><div class="tile">{svg('../final-lexend/B-wordmark-light.svg')}</div><p class="lab">Before: Lexend ExtraBold slanted, stock letter endings, rounded dash.</p></div>
<div><div class="tile">{svg('out/B-wordmark-light.svg')}</div><p class="lab">After: one cut angle for every stroke end, aligned crossbars, measured spacing.</p></div>
<div><div class="tile dark">{svg('../final-lexend/B-wordmark-dark.svg')}</div><p class="lab">Before: dark uses the same outline, so it glows heavier.</p></div>
<div><div class="tile dark">{svg('out/B-wordmark-dark.svg')}</div><p class="lab">After: dark cut is about 8% lighter, so it matches the light version optically.</p></div>
</div>
<ul>
<li><b>Signature cut:</b> the s, e and f endings were diagonal in Lexend. They are recut so that after the 12° slant every stroke end, every stem and both ends of the dash run on one angle. That consistency is what makes it look drawn, not typed.</li>
<li><b>Dash:</b> drawn upright and slanted with the word, so its ends are parallel to the stems. It is exactly as tall as the i-dot, and its right end continues the i stem.</li>
<li><b>Crossbars:</b> Lexend's t crossbar sat higher than the f's. Both now share one height, so “ftf” reads as one even rhythm.</li>
<li><b>Spacing:</b> every pair is spaced from the measured letter shapes, with a minimum gap so f, t and f never touch.</li>
</ul></section>

<section><h2>Construction</h2><p class="lab" style="margin:0 0 10px">Solid lines: the 12° cut lines through the terminals, the i stem and both ends of the dash. Dashed: the shared heights.</p>{construction}</section>

<section><h2>Join study (optional)</h2><div class="two">
<div><div class="tile">{svg('out/B-wordmark-light.svg')}</div><p class="lab">No join (recommended as primary): every letter reads at every size.</p></div>
<div><div class="tile">{svg('out/B-wordmark-join-light.svg')}</div><p class="lab">f–t–f join: one continuous crossbar, like a convoy. More ownable, slightly harder to read small. Use only for large display if chosen.</p></div>
</div></section>

<section><h2>Small sizes</h2><div class="two">
<div><div class="tile">{svg('out/B-wordmark-small.svg')}</div><p class="lab">Small wordmark (under 24 px tall): heavier letters, looser spacing, a thicker dash, deep teal.</p></div>
<div class="icons" style="justify-content:center">
<div>{svg('out/app-icon.svg').replace('<svg ','<svg width="112" height="112" ')}<br>App icon</div>
<div>{svg('out/app-icon-small.svg').replace('<svg ','<svg width="64" height="64" ')}<br>Small icon (≤ 48 px)</div>
<div>{svg('out/symbol-small.svg').replace('<svg ','<svg width="32" height="32" ')}<br>Favicon cut</div>
<div><img src="kit/favicon-16.png" width="16" height="16" alt="16 px favicon"><br>16 px</div>
</div></div>
<p class="lab">In the icon, the dash's right end continues the s's top cut line, so the icon is built on the same construction line as the word.</p></section>

<section><h2>Usage guide</h2>
<div class="two"><div><h3 style="margin:0">Colours</h3>{P}</div>
<div><h3 style="margin:0">Rules</h3><ul>
<li><b>Clear space:</b> one dash height on every side.</li>
<li><b>Minimum size:</b> main wordmark 24 px tall; small wordmark 16–24 px; under 16 px, use the symbol.</li>
<li><b>Symbol:</b> use the regular cut from 48 px up and the small cut below that.</li>
<li><b>In county apps:</b> the county leads. Swiftfleet appears once, in one colour, as “Powered by”.</li>
<li><b>Motion:</b> the dash arrives from behind and settles: 0.2 s fade, then 0.6 s. Respect reduced-motion settings.</li>
</ul></div></div>
<h3>Don't</h3><div class="dont">
<div><div class="tile">{svg('out/B-wordmark-light.svg').replace('<svg ','<svg style="transform:skewX(-10deg)" ')}</div><p class="x">Don't slant it again.</p></div>
<div><div class="tile">{svg('out/B-wordmark-light.svg').replace('<svg ','<svg style="transform:scaleX(1.35)" ')}</div><p class="x">Don't stretch or squash.</p></div>
<div><div class="tile" style="background:#1FA3A9">{svg('out/B-wordmark-light.svg')}</div><p class="x">Don't put teal on teal.</p></div>
<div><div class="tile">{svg('out/B-wordmark-light.svg').replace('#1FA3A9','#E8590C')}</div><p class="x">Don't recolour.</p></div>
</div></section>

<section><h2>Honest limits</h2><ul>
<li>This is a refined slanted Lexend, not a true drawn italic. A type designer would rebalance the curves (s spine, e bowl) so they don't look mechanically sheared. Worth doing if this becomes primary.</li>
<li>Peer test passed against Adyen, Go, Next.js and Wire at equal size. Go uses speed lines; our dash is a single i-dot, not a motion effect, but keep it that way.</li>
<li>No trademark search has been done yet. Professional clearance is needed before launch.</li>
</ul></section>
</main></body></html>'''
open('index.html','w').write(html); print(len(html))
