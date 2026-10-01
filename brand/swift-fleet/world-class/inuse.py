import re
def sv(f,attrs=''):
    s=open(f).read(); vb=re.search(r'viewBox="([^"]+)"',s).group(1); b=re.search(r'<svg[^>]*>(.*)</svg>',s,re.S).group(1)
    b=re.sub(r'<rect width="\d+" height="190" fill="[^"]+"/>','',b)
    return f'<svg viewBox="{vb}" {attrs} aria-hidden="true">{b}</svg>'
CSS='''
.use{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.m{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;color:#15223B}
.m .cap{font-size:13px;color:#5B6B82;padding:8px 12px;border-top:1px solid #DFE5EB;background:#FAFBFC}
.app{display:grid;grid-template-columns:120px 1fr;height:210px;font-size:11px}
.app .side{background:#fff;border-right:1px solid #DFE5EB;padding:12px 10px;display:flex;flex-direction:column;gap:8px}
.app .crest{width:26px;height:26px;border-radius:50%;background:#E6EEF6;display:grid;place-items:center;font-size:8px;color:#5B6B82}
.app .nav{height:8px;border-radius:4px;background:#EBF1F7}.app .nav.on{background:#D6E4F5}
.app .pb{margin-top:auto;font-size:8px;color:#5B6B82;display:flex;align-items:center;gap:4px}
.app .mc{background:#F4F6F8;padding:14px}.app .card{background:#fff;border:1px solid #DFE5EB;border-radius:8px;height:46px;margin-bottom:8px}
.login{height:210px;display:grid;place-items:center;background:#F4F6F8}.login .box{background:#fff;border:1px solid #DFE5EB;border-radius:12px;padding:18px 22px;width:220px;text-align:center}
.login .f{height:22px;border:1px solid #DFE5EB;border-radius:6px;margin:8px 0}.login .b{height:24px;border-radius:12px;background:#1E3F78}
.phones{height:210px;display:flex;gap:18px;justify-content:center;align-items:center;background:#E9EDF2}
.ph{width:96px;height:186px;border-radius:18px;padding:8px;box-sizing:border-box}
.ph.home{background:linear-gradient(160deg,#5A7DA8,#1C2E4E);display:grid;grid-template-columns:repeat(3,1fr);gap:8px;align-content:start;padding-top:22px}
.ph.home i{display:block;width:22px;height:22px;border-radius:6px;background:rgba(255,255,255,.28);margin:auto}
.ph.home .lbl{font-size:6px;color:#fff;text-align:center;margin-top:2px}
.ph.splash{background:#1E3F78;display:grid;place-items:center}
.door{height:210px;background:linear-gradient(180deg,#FDFDFD,#E9ECEF);position:relative}
.door .win{position:absolute;left:0;right:0;top:0;height:62px;background:linear-gradient(180deg,#3A4A5E,#1F2A38);clip-path:polygon(6% 0,100% 0,100% 100%,0 100%)}
.door .handle{position:absolute;right:26px;top:84px;width:40px;height:8px;border-radius:4px;background:#C9CFD6}
.door .county{position:absolute;left:24px;top:84px;font-size:10px;font-weight:700;color:#15223B;display:flex;gap:6px;align-items:center}
.door .reg{position:absolute;left:24px;top:110px;font:700 13px monospace;color:#15223B}
.door .tag{position:absolute;left:24px;bottom:18px;display:flex;gap:6px;align-items:center;font-size:8px;color:#5B6B82}
.id{height:210px;display:grid;place-items:center;background:#E9EDF2}.id .card{width:130px;height:186px;border-radius:10px;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.15);overflow:hidden;font-size:8px;text-align:center}
.id .top{background:#1E3F78;padding:10px}.id .pic{width:48px;height:56px;margin:10px auto 6px;border-radius:6px;background:#DFE5EB}
.mail{height:210px;padding:18px 20px;font-size:11px;line-height:1.5;box-sizing:border-box}.mail hr{border:0;border-top:1px solid #DFE5EB;margin:10px 0}
.tab{height:210px;background:#DEE3EA;padding:14px}.tab .bar{display:flex;gap:6px}.tab .t{background:#fff;border-radius:8px 8px 0 0;padding:6px 10px;font-size:11px;display:flex;gap:6px;align-items:center}
.tab .t.off{background:transparent;color:#5B6B82}.tab .page{background:#fff;height:150px;padding:14px}
.tab .hdr{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:#5B6B82}
'''
def fragment():
    sym=sv('out/symbol.svg','width="22" height="22"')
    return f'''<div class="use">
<div class="m"><div class="app"><div class="side"><div style="display:flex;gap:6px;align-items:center"><div class="crest">crest</div><b style="font-size:9px">County Fleet</b></div>
<div class="nav on"></div><div class="nav"></div><div class="nav"></div><div class="nav"></div>
<div class="pb">Powered by {sv('out/wordmark-mono-navy.svg','height="11"')}</div></div>
<div class="mc"><div class="card"></div><div class="card"></div><div class="card"></div></div></div>
<div class="cap">County app: the county leads. Swiftfleet appears once, in one colour, as “Powered by”.</div></div>

<div class="m"><div class="login"><div class="box">{sv('out/B-wordmark-light.svg','width="150"')}<div class="f"></div><div class="f"></div><div class="b"></div></div></div>
<div class="cap">Swiftfleet's own sign-in, the full-colour wordmark.</div></div>

<div class="m"><div class="phones"><div class="ph home">{"".join('<div><i></i></div>' for _ in range(4))}<div>{sv('out/app-icon.svg','width="22" height="22" style="display:block;margin:auto"')}<div class="lbl">Swiftfleet</div></div>{"".join('<div><i></i></div>' for _ in range(4))}</div>
<div class="ph splash">{sv('out/symbol-mono.svg','width="54" height="54" style="filter:brightness(0) invert(1)"').replace('<svg','<svg',1)}</div></div>
<div class="cap">Driver app: home-screen icon and splash (the dash slides in on launch).</div></div>

<div class="m"><div class="door"><div class="win"></div><div class="handle"></div><div class="county"><div class="crest" style="width:22px;height:22px;border-radius:50%;background:#E6EEF6;font-size:6px;display:grid;place-items:center">crest</div>COUNTY GOVERNMENT</div>
<div class="reg">GKB 123A</div><div class="tag">{sv('out/wordmark-mono-navy.svg','height="10"')} tracked</div></div>
<div class="cap">Vehicle door: county identity first; a small one-colour Swiftfleet tag near the sill.</div></div>

<div class="m"><div class="id"><div class="card"><div class="top">{sv('out/A-wordmark-dark.svg','width="96"')}</div><div class="pic"></div><b>Driver name</b><div style="color:#5B6B82">Driver · Badge 0421</div></div></div>
<div class="cap">Staff badge for Swiftcent field teams: scheme A on navy.</div></div>

<div class="m"><div class="mail"><b>Support team</b><br><span style="color:#5B6B82">Swiftfleet customer success</span><hr>{sv('out/B-lockup-endorsed-light.svg','width="230"')}</div>
<div class="cap">Email signature: the “by Swiftcent” lockup at 230 px. Below 220 px wide, “by Swiftcent” gets too small: use the wordmark alone.</div></div>

<div class="m"><div class="tab"><div class="bar"><div class="t"><img src="kit/favicon-16.png" width="16" height="16" alt="">Swiftfleet · Requests</div><div class="t off">Inbox</div></div>
<div class="page"><div class="hdr">{sv('out/B-wordmark-small.svg','height="16"')}<span>Help · Account</span></div></div></div>
<div class="cap">Browser tab: favicon at real 16 px; small wordmark in the header (16 px tall).</div></div>
</div>'''
if __name__=='__main__':
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>:root{{--line:#DFE5EB}}body{{margin:0;padding:24px;background:#F4F6F8;font-family:system-ui}}{CSS}</style></head><body>{fragment()}</body></html>'
    open('in-use.html','w').write(html)
