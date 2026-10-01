import sys; sys.path.insert(0,'.')
from build import *
TEXT='swıftfleet'
ROWS=list(range(-6,760,8))
GMIN=34
CUT2={'s':[rect(389,330,900,620),rect(-300,-40,115,200)],
      'e':[rect(455,-40,900,195)],
      'f':[rect(372,540,900,800)]}
def custom(ch,w=800):
    if ch=='t':   # Lexend t is pure rectangles; rebuild with crossbar aligned to f (367-516)
        return op(rect(105,0,291,668),rect(17,367,384,516),'union')
    p=gpath(ch,w)
    for r in CUT2.get(ch,[]): p=op(p,r,'diff')
    return p
def glyphs(w=800,depth=0):
    return [custom(ch,w) for ch in TEXT]
def layout(G=58,w=800,depth=0):
    gl=glyphs(w,depth); profs=[profile(p,ROWS) for p in gl]; xs=[0.0]
    for i in range(1,len(gl)):
        RA=profs[i-1][1]; LB=profs[i][0]
        rows=[y for y in ROWS if y in RA and y in LB]
        # gap(y)=xB+LB-(xA+RA); choose xB so mean gap over the 40% tightest rows = G (optical approx)
        diffs=sorted(RA[y]-LB[y] for y in rows)[::-1]
        k=max(3,int(len(diffs)*0.4)); need=max(sum(diffs[:k])/k+G, diffs[0]+GMIN)
        xs.append(xs[-1]+need)
    return gl,xs
def crossbar_band(p):
    L,R=profile(p,list(range(380,560,4))); w={y:R[y]-L[y] for y in L}
    mx=max(w.values()); band=[y for y in w if w[y]>mx*0.85]; return min(band),max(band)
def build(cs,cf,cd,G=58,join=False,w=800,dash_mul=4.2,bg=None,thin=0,s=0.16,depth=0):
    gl,xs=layout(G,w,depth)
    # i-dot box
    idot=op(gpath('i',w),rect(-100,560,1000,2000),'int'); rp=RecordingPen(); idot.draw(rp)
    pts=[q for o,a in rp.value for q in a]; dx1=max(p[0] for p in pts); dy0=min(p[1] for p in pts); dy1=max(p[1] for p in pts); H=dy1-dy0
    placed=[translate(p,xs[i]) for i,p in enumerate(gl)]
    if join:
        bar=rect(xs[3]+370,367,xs[5]+30,516)
        placed[3]=op(placed[3],bar,'union'); placed[5]=op(placed[5],rect(xs[5]+18,367,xs[5]+30,516),'union')
    dash=rrect(xs[2]+dx1-dash_mul*H, dy0, xs[2]+dx1, dy1, 22)
    if thin:
        for i in range(len(placed)):
            st=placed[i].clone() if hasattr(placed[i],'clone') else placed[i]
    base=150; ox=40
    paths=[]
    for i,p in enumerate(placed):
        col=cs if i<5 else cf
        paths.append(f'<path fill="{col}" d="{svgd(p,s,ox,base)}"/>')
    paths.append(f'<path fill="{cd}" d="{svgd(dash,s,ox,base)}"/>')
    W=int(ox*2+(xs[-1]+adv("t",w))*s)
    bgr=f'<rect width="{W}" height="190" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 190"><title>Swiftfleet</title>{bgr}{"".join(paths)}</svg>'
if __name__=='__main__':
    N='#1E3F78';T='#1FA3A9'
    open('wc-B.svg','w').write(build(N,T,T))
    open('wc-B-join.svg','w').write(build(N,T,T,join=True))
    open('wc-A.svg','w').write(build(N,N,T))
