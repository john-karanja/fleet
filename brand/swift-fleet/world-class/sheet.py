import re
def sv(f,label,cls=''):
    s=open(f).read(); vb=re.search(r'viewBox="([^"]+)"',s).group(1); b=re.search(r'<svg[^>]*>(.*)</svg>',s,re.S).group(1)
    b=re.sub(r'<rect width="\d+" height="190" fill="[^"]+"/>','',b); b=b.replace('<title>Swiftfleet</title>','')
    return f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="{label}">{b}</svg>'
WB=lambda: sv('out/B-wordmark-light.svg','Swiftfleet wordmark, navy and teal','wm')
WA=lambda: sv('out/A-wordmark-light.svg','Swiftfleet wordmark, all navy','wm')
WD=lambda: sv('out/B-wordmark-dark.svg','Swiftfleet wordmark for dark backgrounds','wm')
WAD=lambda: sv('out/A-wordmark-dark.svg','Swiftfleet wordmark, white with teal dash','wm')
MW=lambda: sv('out/wordmark-mono-white.svg','Swiftfleet wordmark, white','wm')
MN=lambda: sv('out/wordmark-mono-navy.svg','Swiftfleet wordmark, navy','wm')
def tile(bg,art,name,note,ink='#15223B',style=''):
    return f'<figure class="tile"><div class="sw" style="background:{bg};{style}">{art}</div><figcaption><b>{name}</b><span>{note}</span></figcaption></figure>'
backs=[
 tile('#FFFFFF',WB(),'White','Primary, navy + teal'),
 tile('#F4F6F8',WB(),'Canvas grey #F4F6F8','App background'),
 tile('#10213F',WD(),'Night #10213F','White “swift”, light teal'),
 tile('#1E3F78',WAD(),'Navy #1E3F78','White with light-teal dash'),
 tile('#147B80',MW(),'Teal deep #147B80','White, one colour'),
 tile('#0B0F14',MW(),'Black','White, one colour'),
 tile('linear-gradient(135deg,#6E5A45 0%,#2F3B2E 55%,#1B2430 100%)',MW(),'Photo','White, one colour, on darker areas'),
 tile('#EDE7DA',MN(),'Warm paper','Navy, one colour'),
]
one=[tile('#FFFFFF',WB(),'Scheme B','Default: navy “swift”, teal “fleet”'),tile('#FFFFFF',WA(),'Scheme A','All navy, teal dash: badges, signage'),
     tile('#FFFFFF',MN(),'One colour, navy','“Powered by”, print, stamps'),tile('#10213F',MW(),'One colour, white','Reversed, single-colour print')]
small=[tile('#FFFFFF',sv('out/B-wordmark-small.svg','Small wordmark','wm'),'Small wordmark','16–24 px tall: heavier, deep teal')]
def ic(f,px,label):
    art=sv(f,label).replace('<svg ','<svg width="%d" height="%d" '%(px,px),1)
    return '<div class="ic"><div class="icbox">%s</div><span>%d px</span></div>'%(art,px)
icons=''.join([ic('out/app-icon.svg',180,'App icon'),ic('out/app-icon.svg',120,'App icon'),ic('out/app-icon.svg',64,'App icon'),ic('out/app-icon-small.svg',48,'Small app icon'),ic('out/app-icon-small.svg',32,'Small app icon')])
import base64
B64=base64.b64encode(open("kit/favicon-16.png","rb").read()).decode()
fav='<div class="ic"><div class="icbox chipw"><img src="data:image/png;base64,%s" width="16" height="16" alt="Favicon at 16 px"></div><span>16 px favicon</span></div>'%B64
symbols=[tile('#FFFFFF',sv('out/symbol.svg','Symbol','sym'),'Symbol','48 px and up'),tile('#FFFFFF',sv('out/symbol-small.svg','Small symbol','sym'),'Small symbol','Under 48 px'),
         tile('#10213F',sv('kit/symbol-white.svg','White symbol','sym'),'White','On dark or photos'),tile('#FFFFFF',sv('out/symbol-mono.svg','Navy symbol','sym'),'One colour','Navy')]
lock=[tile('#FFFFFF',sv('out/B-lockup-endorsed-light.svg','Swiftfleet by Swiftcent','lk'),'By Swiftcent, light','Minimum 220 px wide'),
      tile('#10213F',sv('out/B-lockup-endorsed-dark.svg','Swiftfleet by Swiftcent on dark','lk'),'By Swiftcent, dark','Minimum 220 px wide')]
pal=[('Navy','#1E3F78','#FFFFFF','“swift”, symbol, one-colour'),('Teal','#1FA3A9','#10213F','“fleet” and dash, 24 px and up'),('Teal deep','#147B80','#FFFFFF','Small sizes and text (5.0:1)'),('Teal on dark','#32BFC4','#10213F','On Night and Navy'),('Night','#10213F','#FFFFFF','Dark background')]
P=''.join(f'<div class="chip"><div class="cs" style="background:{h};color:{t}">{n}</div><code>{h}</code><span>{u}</span></div>' for n,h,t,u in pal)
smallwm='<div class="ic"><div class="icbox chipw">%s</div><span>Small wordmark, 20 px tall</span></div>'%sv('out/B-wordmark-small.svg','Small wordmark').replace('<svg ','<svg height="20" width="83" ',1)
html=f'''<title>Swiftfleet Logo Sheet</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;700&family=Source+Sans+3:wght@400;600&display=swap">
<style>
/* Layout: a specimen sheet. Swatches keep their real backgrounds in both themes; only the page chrome follows the theme. */
:root{{--bg:#F4F6F8;--card:#FFFFFF;--line:#DFE5EB;--ink:#15223B;--mute:#5B6B82;--accent:#147B80;
--display:'Lexend',Arial,sans-serif;--body:'Source Sans 3',Arial,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0B1528;--card:#13213F;--line:#24365A;--ink:#E8EEF7;--mute:#9DB0CC;--accent:#32BFC4;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0B1528;--card:#13213F;--line:#24365A;--ink:#E8EEF7;--mute:#9DB0CC;--accent:#32BFC4;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font:16px/1.5 var(--body)}}
.wrap{{max-width:1160px;margin:0 auto;padding-inline:16px;padding-block:40px 72px;display:flex;flex-direction:column;gap:48px}}
header{{display:flex;flex-direction:column;gap:6px}}
h1,h2{{font-family:var(--display);font-weight:700;text-wrap:balance;margin:0}}h1{{font-size:clamp(26px,4vw,36px)}}h2{{font-size:22px}}
.eyebrow{{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0}}
.lede{{color:var(--mute);max-width:65ch;margin:0}}
section{{display:flex;flex-direction:column;gap:16px}} section>p{{color:var(--mute);margin:0;max-width:65ch}}
.hero{{background:#FFFFFF;border:1px solid var(--line);border-radius:16px;padding:clamp(28px,7vw,72px);display:flex;justify-content:center}}
.hero svg{{width:min(720px,100%);height:auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}}
.grid.two{{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){{.grid.two{{grid-template-columns:1fr}}}}
.chipw{{background:#FFFFFF;border:1px solid var(--line);border-radius:8px;padding:10px 12px;display:flex;align-items:center}}
.tile{{margin:0;display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;min-width:0}}
.sw{{aspect-ratio:16/9;max-width:100%;display:flex;align-items:center;justify-content:center;padding:24px}}
.sw .wm{{width:82%;height:auto}} .sw .sym{{height:70%;width:auto}} .sw .lk{{width:62%;height:auto}} .grid.two .sw{{aspect-ratio:2/1}}
figcaption{{padding:10px 14px;display:flex;flex-direction:column;font-size:14px;border-top:1px solid var(--line)}} figcaption span{{color:var(--mute)}}
.icons{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px;display:flex;flex-wrap:wrap;gap:28px;align-items:flex-end}}
.ic{{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:13px;color:var(--mute);font-variant-numeric:tabular-nums}}
.palette{{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:16px}}
.chip{{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;font-size:14px}}
.chip .cs{{height:84px;display:flex;align-items:flex-end;padding:10px 12px;font-weight:600}} .chip code,.chip span{{padding:0 12px}} .chip code{{padding-top:8px;font-size:14px}} .chip span{{color:var(--mute);padding-bottom:12px}}
.rules{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 24px}} .rules ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
</style>
<div class="wrap">
<header><p class="eyebrow">Swiftfleet · a Swiftcent product</p><h1>Logo sheet</h1>
<p class="lede">The Swiftfleet logo on every approved background, with its icons, lockups and colours. Proposed for approval, 2 October 2026.</p></header>
<div class="hero">{WB()}</div>
<section><h2>Backgrounds</h2><p>Pick the version by background. On colour or photos, use the one-colour white version.</p><div class="grid">{"".join(backs)}</div></section>
<section><h2>Colour versions</h2><div class="grid">{"".join(one)}</div></section>
<section><h2>App icon and small sizes</h2><p>From 48 px down, the small cut takes over: a thicker, shorter dash that stays visible. Shown at real size.</p><div class="icons">{icons}{fav}{smallwm}</div></section>
<section><h2>Symbol</h2><div class="grid">{"".join(symbols)}</div></section>
<section><h2>With Swiftcent</h2><div class="grid two">{"".join(lock)}</div></section>
<section><h2>Colours</h2><div class="palette">{P}</div></section>
<section><h2>Quick rules</h2><div class="rules"><ul>
<li>Leave clear space of one dash height around the logo.</li>
<li>Minimum size: 24 px tall for the wordmark, 16 px with the small wordmark; below that, use the symbol.</li>
<li>In county apps the county leads; Swiftfleet appears once, in one colour, as “Powered by”.</li>
<li>Don’t slant, stretch, recolour or outline it, and don’t put teal on teal.</li>
</ul></div></section>
</div>'''
open('logo-sheet.html','w').write(html); print(len(html))
