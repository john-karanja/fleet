"""Swiftfleet world-class Lexend build. Run: python3 kit.py  -> out/*.svg"""
import sys, os; sys.path.insert(0,'.')
from build import *
from wordmark import custom, TEXT, ROWS
import pathops
NAVY='#1E3F78'; TEAL='#1FA3A9'; TEAL_D='#32BFC4'; TEAL_S='#147B80'; NIGHT='#10213F'; WHITE='#FFFFFF'
os.makedirs('out',exist_ok=True)

def idot(w):
    d=op(gpath('i',w),rect(-100,560,1000,2000),'int'); rp=RecordingPen(); d.draw(rp)
    pts=[q for o,a in rp.value for q in a]
    return max(p[0] for p in pts), min(p[1] for p in pts), max(p[1] for p in pts)

def thin(p,t):
    """inset outline by t units (reversed/dark version)"""
    if t<=0: return p
    p=op(p,rect(0,0,0.1,0.1),'union') if False else p
    q=pathops.Path(); p.draw(q.getPen()); q.simplify(); p=q
    s=pathops.Path(); p.draw(s.getPen())
    s.stroke(2*t,pathops.LineCap.BUTT_CAP,pathops.LineJoin.MITER_JOIN,4)
    return op(p,s,'diff')

def layout(gl,G,GMIN):
    profs=[profile(p,ROWS) for p in gl]; xs=[0.0]
    for i in range(1,len(gl)):
        RA=profs[i-1][1]; LB=profs[i][0]
        d=sorted((RA[y]-LB[y] for y in ROWS if y in RA and y in LB),reverse=True)
        k=max(3,int(len(d)*.4)); xs.append(xs[-1]+max(sum(d[:k])/k+G,d[0]+GMIN))
    return xs

def wordmark(cs,cf,cd,bg=None,join=False,w=800,G=58,GMIN=34,dash_len=4.2,dash_grow=0,t=0,name=None):
    gl=[custom(ch,w) if (ch!='t' or w==800) else gpath('t',w) for ch in TEXT]
    xs=layout(gl,G,GMIN)
    placed=[translate(p,xs[i]) for i,p in enumerate(gl)]
    if join:
        placed[3]=op(placed[3],rect(xs[3]+370,367,xs[5]+30,516),'union')
    dx1,dy0,dy1=idot(w); H=dy1-dy0
    dash=rrect(xs[2]+dx1-dash_len*H, dy0-dash_grow, xs[2]+dx1, dy1, 22)
    placed=[thin(p,t) for p in placed]; dash=thin(dash,t)
    s=0.16; ox=24; base=150
    out=[f'<path fill="{cs if i<5 else cf}" d="{svgd(p,s,ox,base)}"/>' for i,p in enumerate(placed)]
    out.append(f'<path fill="{cd}" d="{svgd(dash,s,ox,base)}"/>')
    W=round(ox*2+(xs[-1]+400)*s+(820*SL*s))
    bgr=f'<rect width="{W}" height="190" fill="{bg}"/>' if bg else ''
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 190"><title>Swiftfleet</title>{bgr}{"".join(out)}</svg>'
    if name: open(f'out/{name}.svg','w').write(svg)
    return svg

def symbol(cs,cd,tile=None,w=800,small=False,name=None,radius=58):
    s_=custom('s',w); dx1,dy0,dy1=idot(w); H=dy1-dy0
    if small: H*=1.3                       # thicker dash for 16-32 px
    gap = 100 if small else 80
    L = 2.3*H if not small else 2.0*H
    top=544+gap; RX=389                     # dash right end = s top-terminal cut line (one construction line)
    dash=rrect(RX-L, top, RX, top+H, 22)
    # fit into 256 box: content bbox in slanted space
    P=op(s_,dash,'union'); L,R=profile(P,list(range(-12,int(top+H)+2,4)))
    x0=min(L.values()); x1=max(R.values()); y0=-10; y1=top+H
    cw=x1-x0; ch=y1-y0; area=(168 if tile else 224) if not small else (188 if tile else 236)
    sc=area/max(cw,ch); ox=128-(x0+cw/2)*sc; base=128+(y0+ch/2)*sc
    paths=f'<path fill="{cs}" d="{svgd(s_,sc,ox,base)}"/><path fill="{cd}" d="{svgd(dash,sc,ox,base)}"/>'
    bg=f'<rect width="256" height="256" rx="{radius}" fill="{tile}"/>' if tile else ''
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><title>Swiftfleet</title>{bg}{paths}</svg>'
    if name: open(f'out/{name}.svg','w').write(svg)
    return svg

if __name__=='__main__':
    # primary wordmarks
    wordmark(NAVY,TEAL,TEAL,name='B-wordmark-light')
    wordmark(NAVY,NAVY,TEAL,name='A-wordmark-light')
    wordmark(WHITE,TEAL_D,TEAL_D,bg=NIGHT,t=6,name='B-wordmark-dark')
    wordmark(WHITE,WHITE,TEAL_D,bg=NIGHT,t=6,name='A-wordmark-dark')
    wordmark(NAVY,NAVY,NAVY,name='wordmark-mono-navy')
    wordmark(WHITE,WHITE,WHITE,bg=NIGHT,t=6,name='wordmark-mono-white')
    # join study
    wordmark(NAVY,TEAL,TEAL,join=True,name='B-wordmark-join-light')
    wordmark(NAVY,NAVY,TEAL,join=True,name='A-wordmark-join-light')
    # small-size wordmark (<= 120 px wide): heavier, looser, thicker dash, deep teal
    wordmark(NAVY,TEAL_S,TEAL_S,w=900,G=90,GMIN=60,dash_grow=45,name='B-wordmark-small')
    wordmark(NAVY,NAVY,TEAL_S,w=900,G=90,GMIN=60,dash_grow=45,name='A-wordmark-small')
    # symbol + icons
    symbol(NAVY,TEAL,name='symbol')
    symbol(NAVY,NAVY,name='symbol-mono')
    symbol(WHITE,TEAL_D,tile=NAVY,name='app-icon')
    symbol(WHITE,TEAL_D,tile=NAVY,w=900,small=True,name='app-icon-small')
    symbol(NAVY,TEAL_S,w=900,small=True,name='symbol-small')
    print('ok', sorted(os.listdir('out')))
