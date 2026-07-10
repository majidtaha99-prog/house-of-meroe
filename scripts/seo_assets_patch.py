from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, re, html
root=Path('C:/Users/TAHA/Desktop/house of meroe/site')
root.mkdir(parents=True, exist_ok=True)

def font(size,bold=False):
    candidates=[]
    if bold:
        candidates += ['C:/Windows/Fonts/CINZEL-BOLD.TTF','C:/Windows/Fonts/georgiab.ttf','C:/Windows/Fonts/Georgia Bold.ttf']
    candidates += ['C:/Windows/Fonts/CINZEL-REGULAR.TTF','C:/Windows/Fonts/cinzel.ttf','C:/Windows/Fonts/georgia.ttf','C:/Windows/Fonts/Georgia.ttf']
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p,size)
    return ImageFont.load_default()

ink=(6,4,10); gold=(201,162,83); gold2=(240,210,138); bone=(246,236,211); rust=(74,16,16)
for size,name in [(512,'favicon-512.png'),(192,'favicon-192.png'),(180,'apple-touch-icon.png'),(32,'favicon-32.png'),(16,'favicon-16.png')]:
    img=Image.new('RGBA',(size,size),ink+(255,))
    glow=Image.new('RGBA',(size,size),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.ellipse((size*.05,size*.05,size*.95,size*.95),fill=(*gold,28)); glow=glow.filter(ImageFilter.GaussianBlur(max(1,size//8))); img.alpha_composite(glow)
    d=ImageDraw.Draw(img)
    pad=size*0.12
    d.rounded_rectangle((pad,pad,size-pad,size-pad),radius=int(size*0.12),outline=gold,width=max(1,size//36))
    d.polygon([(size*.22,size*.70),(size*.50,size*.24),(size*.78,size*.70)],outline=gold2,fill=None,width=max(1,size//34))
    d.line((size*.50,size*.24,size*.50,size*.70),fill=gold,width=max(1,size//48))
    f=font(int(size*.34),bold=True); text='M'; bbox=d.textbbox((0,0),text,font=f)
    d.text(((size-(bbox[2]-bbox[0]))/2, size*.43),text,font=f,fill=bone)
    img.save(root/name)
Image.open(root/'favicon-192.png').save(root/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64)])
(root/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="House of Meroë mark"><rect width="512" height="512" rx="64" fill="#06040a"/><rect x="58" y="58" width="396" height="396" rx="54" fill="none" stroke="#c9a253" stroke-width="14"/><path d="M112 358 256 118 400 358Z" fill="none" stroke="#f0d28a" stroke-width="16" stroke-linejoin="round"/><path d="M256 118v240" stroke="#c9a253" stroke-width="10"/><text x="256" y="333" text-anchor="middle" font-family="Cinzel, Georgia, serif" font-size="170" font-weight="700" fill="#f6ecd3">M</text></svg>''',encoding='utf-8')

def make_og(path,title,subtitle,footer='houseofmeroe.com'):
    W,H=1200,630; img=Image.new('RGB',(W,H),ink); d=ImageDraw.Draw(img)
    for y in range(H):
        t=y/H; d.line((0,y,W,y),fill=(int(6*(1-t)+18*t),int(4*(1-t)+10*t),int(10*(1-t)+22*t)))
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.ellipse((-180,210,500,890),fill=(*rust,76)); gd.ellipse((740,-220,1420,460),fill=(*gold,47)); gd.ellipse((360,100,840,590),fill=(*gold,18))
    img=Image.alpha_composite(img.convert('RGBA'),glow.filter(ImageFilter.GaussianBlur(70))); d=ImageDraw.Draw(img)
    d.rectangle((54,54,W-54,H-54),outline=gold,width=3); d.rectangle((72,72,W-72,H-72),outline=(107,78,28,255),width=1)
    d.polygon([(402,390),(600,128),(798,390)],outline=(*gold2,215),fill=None,width=5); d.line((600,128,600,390),fill=(*gold,190),width=3); d.line((402,390,798,390),fill=(*gold,170),width=3)
    for text,y,f,fill in [(title,238,font(72,True),bone),(subtitle,335,font(32),gold2),(footer,500,font(24),bone)]:
        bbox=d.textbbox((0,0),text,font=f); d.text(((W-(bbox[2]-bbox[0]))/2,y),text,font=f,fill=fill)
    img.convert('RGB').save(root/path,quality=94,subsampling=0)
make_og('og-image.jpg','HOUSE OF MEROË','A TALENT ATELIER','Cultural fluency · Refined representation · New MENA wave')
make_og('og-radi.jpg','RADI BARAKAT','Arabic comedy and lifestyle creator','Represented by House of Meroë')
make_og('og-yourpop.jpg','YOURPOP','Stocks, crypto and finance commentary','Represented by House of Meroë')

manifest={'name':'House of Meroë','short_name':'Meroë','description':'A talent atelier for creators of the new MENA wave.','start_url':'/','scope':'/','display':'standalone','background_color':'#06040a','theme_color':'#06040a','icons':[{'src':'/favicon-192.png','sizes':'192x192','type':'image/png'},{'src':'/favicon-512.png','sizes':'512x512','type':'image/png','purpose':'any maskable'}]}
(root/'site.webmanifest').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://houseofmeroe.com/sitemap.xml\n',encoding='utf-8')
(root/'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://houseofmeroe.com/</loc><priority>1.0</priority></url>\n  <url><loc>https://houseofmeroe.com/radi</loc><priority>0.8</priority></url>\n  <url><loc>https://houseofmeroe.com/yourpop</loc><priority>0.8</priority></url>\n</urlset>\n''',encoding='utf-8')

pages={
 'index.html': {'title':'House of Meroë — A Talent Atelier','desc':'House of Meroë is a talent atelier for creators of the new MENA wave — cultural fluency, refined representation, and brand-ready creator partnerships.','url':'https://houseofmeroe.com/','image':'https://houseofmeroe.com/og-image.jpg','type':'website','schema':{'@context':'https://schema.org','@type':'Organization','name':'House of Meroë','url':'https://houseofmeroe.com/','logo':'https://houseofmeroe.com/favicon-512.png','description':'A talent atelier for creators of the new MENA wave.','sameAs':[]}},
 'radi.html': {'title':'Radi Barakat — House of Meroë','desc':'Radi Barakat is an Arabic comedy and lifestyle creator represented by House of Meroë. View audience, content, and partnership opportunities.','url':'https://houseofmeroe.com/radi','image':'https://houseofmeroe.com/og-radi.jpg','type':'profile','schema':{'@context':'https://schema.org','@type':'Person','name':'Radi Barakat','url':'https://houseofmeroe.com/radi','description':'Arabic comedy and lifestyle creator represented by House of Meroë.','affiliation':{'@type':'Organization','name':'House of Meroë','url':'https://houseofmeroe.com/'}}},
 'radi/index.html': {'title':'Radi Barakat — House of Meroë','desc':'Radi Barakat is an Arabic comedy and lifestyle creator represented by House of Meroë. View audience, content, and partnership opportunities.','url':'https://houseofmeroe.com/radi','image':'https://houseofmeroe.com/og-radi.jpg','type':'profile','schema':{'@context':'https://schema.org','@type':'Person','name':'Radi Barakat','url':'https://houseofmeroe.com/radi','description':'Arabic comedy and lifestyle creator represented by House of Meroë.','affiliation':{'@type':'Organization','name':'House of Meroë','url':'https://houseofmeroe.com/'}}},
 'yourpop/index.html': {'title':'YourPOP — House of Meroë','desc':'YourPOP is a stocks, cryptocurrency, and finance commentary creator represented by House of Meroë. View audience, content, and partnership opportunities.','url':'https://houseofmeroe.com/yourpop','image':'https://houseofmeroe.com/og-yourpop.jpg','type':'profile','schema':{'@context':'https://schema.org','@type':'Person','name':'YourPOP','url':'https://houseofmeroe.com/yourpop','description':'Stocks, cryptocurrency, and finance commentary creator represented by House of Meroë.','affiliation':{'@type':'Organization','name':'House of Meroë','url':'https://houseofmeroe.com/'}}},
}

def seo_block(meta):
    schema=json.dumps(meta['schema'],ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    return f'''<title>{html.escape(meta['title'])}</title>\n<meta name="description" content="{html.escape(meta['desc'])}">\n<meta name="theme-color" content="#06040a">\n<meta name="robots" content="index, follow, max-image-preview:large">\n<link rel="canonical" href="{meta['url']}">\n<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">\n<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">\n<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n<link rel="manifest" href="/site.webmanifest">\n<meta property="og:site_name" content="House of Meroë">\n<meta property="og:type" content="{meta['type']}">\n<meta property="og:title" content="{html.escape(meta['title'])}">\n<meta property="og:description" content="{html.escape(meta['desc'])}">\n<meta property="og:url" content="{meta['url']}">\n<meta property="og:image" content="{meta['image']}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:locale" content="en_US">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="{html.escape(meta['title'])}">\n<meta name="twitter:description" content="{html.escape(meta['desc'])}">\n<meta name="twitter:image" content="{meta['image']}">\n<script type="application/ld+json">{schema}</script>'''

for rel,meta in pages.items():
    path=root/rel
    txt=path.read_text(encoding='utf-8')
    pattern=re.compile(r'<title>.*?</title>\s*<meta name="description" content=".*?">\s*<meta name="theme-color" content=".*?">',re.S)
    if not pattern.search(txt):
        raise SystemExit(f'No metadata block matched in {rel}')
    txt=pattern.sub(seo_block(meta),txt, count=1)
    path.write_text(txt,encoding='utf-8')
print('generated brand assets, OG images, sitemap/robots/manifest, and patched metadata for', len(pages), 'HTML files')
