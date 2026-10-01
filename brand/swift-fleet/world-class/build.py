import math, sys
import pathops
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.recordingPen import RecordingPen
SL=math.tan(math.radians(12))
_cache={}
def font(w):
    if w not in _cache:
        f=TTFont('../refine/lettering/Lexend.ttf'); i=instantiateVariableFont(f,{"wght":w}); _cache[w]=(i.getGlyphSet(),i.getBestCmap(),i['hmtx'])
    return _cache[w]
def gpath(ch,w=800):
    gs,cmap,_=font(w); n=cmap[0x131] if ch=='ı' else cmap[ord(ch)]
    p=pathops.Path(); gs[n].draw(p.getPen()); return p
def adv(ch,w=800):
    gs,cmap,h=font(w); n=cmap[0x131] if ch=='ı' else cmap[ord(ch)]; return h[n][0]
def rect(x0,y0,x1,y1):
    p=pathops.Path(); pen=p.getPen(); pen.moveTo((x0,y0)); pen.lineTo((x1,y0)); pen.lineTo((x1,y1)); pen.lineTo((x0,y1)); pen.closePath(); return p
def rrect(x0,y0,x1,y1,r):
    k=0.5523*r; p=pathops.Path(); pen=p.getPen()
    pen.moveTo((x0+r,y0)); pen.lineTo((x1-r,y0)); pen.curveTo((x1-r+k,y0),(x1,y0+r-k),(x1,y0+r)); pen.lineTo((x1,y1-r)); pen.curveTo((x1,y1-r+k),(x1-r+k,y1),(x1-r,y1))
    pen.lineTo((x0+r,y1)); pen.curveTo((x0+r-k,y1),(x0,y1-r+k),(x0,y1-r)); pen.lineTo((x0,y0+r)); pen.curveTo((x0,y0+r-k),(x0+r-k,y0),(x0+r,y0)); pen.closePath(); return p
def op(a,b,kind):
    return pathops.op(a,b,{'diff':pathops.PathOp.DIFFERENCE,'union':pathops.PathOp.UNION,'int':pathops.PathOp.INTERSECTION}[kind])
def translate(p,dx,dy=0):
    rp=RecordingPen(); p.draw(rp); q=pathops.Path(); pen=q.getPen()
    for o,a in rp.value: getattr(pen,o)(*[(x+dx,y+dy) for x,y in a])
    return q
# --- signature: vertical recut of diagonal terminals (in upright space) ---
CUTS={'s':[(400,330,'R'),(100,0,'Lb')],   # (x, y-threshold, side)
      'e':[(470,0,'Rb')],
      'f':[(352,600,'R')]}
def recut(ch,p,depth):
    for x,y,side in CUTS.get(ch,[]):
        if side=='R': p=op(p,rect(x+depth,y,2000,2000),'diff')
        elif side=='Rb': p=op(p,rect(x+depth,-200,2000,y+260),'diff')
        elif side=='Lb': p=op(p,rect(-500,-200,x-depth,y+200),'diff')
    return p
# --- flatten for optical spacing ---
def polys(p,steps=12):
    rp=RecordingPen(); p.draw(rp); out=[];cur=[];last=None
    for o,a in rp.value:
        if o=='moveTo': cur=[a[0]]; last=a[0]
        elif o=='lineTo': cur.append(a[0]); last=a[0]
        elif o=='qCurveTo':
            pts=[last]+list(a)
            # treat as chain of quadratic segments (implied on-curve midpoints)
            ctrl=pts[1:-1]; end=pts[-1]; start=last
            seq=[start]
            for i,c in enumerate(ctrl):
                nxt = end if i==len(ctrl)-1 else ((c[0]+ctrl[i+1][0])/2,(c[1]+ctrl[i+1][1])/2)
                s0=seq[-1]
                for t in range(1,steps+1):
                    t/=steps; cur.append(((1-t)**2*s0[0]+2*(1-t)*t*c[0]+t*t*nxt[0],(1-t)**2*s0[1]+2*(1-t)*t*c[1]+t*t*nxt[1]))
                seq.append(nxt)
            last=end
        elif o=='curveTo':
            c1,c2,e=a; s0=last
            for t in range(1,steps+1):
                t/=steps; mt=1-t
                cur.append((mt**3*s0[0]+3*mt*mt*t*c1[0]+3*mt*t*t*c2[0]+t**3*e[0], mt**3*s0[1]+3*mt*mt*t*c1[1]+3*mt*t*t*c2[1]+t**3*e[1]))
            last=e
        elif o in('closePath','endPath'):
            if cur: out.append(cur); cur=[]
    return out
def profile(p,rows):
    """left/right extent per row (after slant applied via x+=y*SL)"""
    P=[[(x+y*SL,y) for x,y in poly] for poly in polys(p)]
    L={};R={}
    for y in rows:
        xs=[]
        for poly in P:
            for (x1,y1),(x2,y2) in zip(poly,poly[1:]+poly[:1]):
                if (y1<=y<y2) or (y2<=y<y1):
                    xs.append(x1+(y-y1)*(x2-x1)/(y2-y1))
        if xs: L[y]=min(xs); R[y]=max(xs)
    return L,R
def svgd(p,s,ox,base):
    rp=RecordingPen(); p.draw(rp); d=[]
    T=lambda x,y:(ox+(x+y*SL)*s, base-y*s)
    for o,a in rp.value:
        pts=[T(*q) for q in a]
        if o=='moveTo': d.append('M%.2f %.2f'%pts[0])
        elif o=='lineTo': d.append('L%.2f %.2f'%pts[0])
        elif o=='curveTo': d.append('C'+' '.join('%.2f %.2f'%q for q in pts))
        elif o=='qCurveTo':
            # expand implied points into Q segments
            cur=None
            ctrl=pts[:-1]; end=pts[-1]
            for i,c in enumerate(ctrl):
                nxt=end if i==len(ctrl)-1 else ((c[0]+ctrl[i+1][0])/2,(c[1]+ctrl[i+1][1])/2)
                d.append('Q%.2f %.2f %.2f %.2f'%(c[0],c[1],nxt[0],nxt[1]))
        elif o=='closePath': d.append('Z')
    return ''.join(d)
