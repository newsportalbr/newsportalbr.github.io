import json
from datetime import datetime

# ===== CONFIGURAÇÕES DO SITE =====
SITE_CONFIG = {
    "name": "NewsPortal",
    "title": "NewsPortal - Últimas Notícias em Tempo Real",
    "description": "Portal de notícias atualizado constantemente com as principais manchetes do Brasil e do mundo.",
    "keywords": "notícias, portal, atualidades, Brasil, mundo",
    "author": "NewsPortal",
    "theme_color": "#08111f",
    "logo_url": "https://via.placeholder.com/512x512?text=NP",
    "site_url": "https://newsportalbr.github.io/",
    "twitter_handle": "#",
    "facebook_page": "#",
    "instagram": "#",
    "analytics_id": "UA-XXXXXXX-X",
    
    # Adsterra - Múltiplos Formatos
    "adsterra_display_key": "59b1a95083fc4642ac472862070573fb",
    "adsterra_native_script": "https://pl29431522.profitablecpmratenetwork.com/3f11c2602609b7e16615caec1c58202c/invoke.js",
    "adsterra_native_div": "container-3f11c2602609b7e16615caec1c58202c",
    "adsterra_popunder": "https://pl29431520.profitablecpmratenetwork.com/2f/d6/1d/2fd61d919a93eebbd3c62ee7335040f7.js",
    "adsterra_socialbar": "https://pl29431523.profitablecpmratenetwork.com/31/d8/66/31d8661dee905c0b02e59f1bb4fea352.js",
    "adsterra_smartlink": "https://www.profitablecpmratenetwork.com/zjzqqe59f?key=6f6f1e33349a28bab842c78ae04fa617",
    
    # Monetag
    "monetag_id": "bef2ac0b5aadbad6579cb5eb660e44f8",
}

# ===== CONFIGURAÇÕES VISUAIS =====
THEME_CONFIG = {
    "primary_color": "#49a7ff",
    "secondary_color": "#0d1726",
    "background_color": "#08111f",
    "card_bg": "#0f1a2e",
    "text_color": "#ffffff",
    "text_secondary": "#a0b3d9",
    "accent_color": "#ff6b35",
    "font_family": "'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif",
    "enable_dark_mode": True,
    "enable_reading_time": True,
    "enable_sharing": True,
    "ads_frequency": 3,  # Display ads a cada X notícias
    "enable_popunder": True,  # Ativar popunder
    "enable_socialbar": True,  # Ativar social bar
    "enable_native": True,  # Ativar native banner
}

# ===== LEITURA DOS ARTIGOS =====
with open("articles.json", encoding="utf-8") as f:
    articles = json.load(f)

# ===== FUNÇÕES AUXILIARES =====
def get_reading_time(text):
    words_per_minute = 200
    word_count = len(text.split()) if isinstance(text, str) else 100
    minutes = max(1, round(word_count / words_per_minute))
    return minutes

def generate_breadcrumb_schema():
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "name": "Início",
            "item": SITE_CONFIG["site_url"]
        }]
    }

# ===== PÁGINAS LEGAIS COM ANÚNCIOS =====
def generate_privacy_page():
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Política de Privacidade - NewsPortal</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Adsterra Display -->
    <script>
        atOptions = {{
            'key' : '{SITE_CONFIG["adsterra_display_key"]}',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {{}}
        }};
    </script>
    <script src="https://www.highperformanceformat.com/{SITE_CONFIG['adsterra_display_key']}/invoke.js"></script>
    
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #08111f; color: #fff; line-height: 1.6; }}
        .header {{ background: #0d1726; padding: 15px 20px; border-bottom: 3px solid #49a7ff; position: sticky; top: 0; z-index: 1000; }}
        .header-content {{ max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; gap: 15px; }}
        .logo {{ font-size: 24px; font-weight: bold; color: #49a7ff; text-decoration: none; display: flex; align-items: center; gap: 10px; }}
        .theme-toggle {{ background: #0f1a2e; border: 1px solid #49a7ff; padding: 8px 15px; border-radius: 25px; cursor: pointer; color: #fff; }}
        .main-container {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 300px; gap: 30px; }}
        .container {{ background: #0f1a2e; border-radius: 16px; padding: 30px; }}
        .sidebar {{ position: sticky; top: 100px; }}
        .ad-sidebar {{ background: linear-gradient(135deg, #0f1a2e, #0d1726); border-radius: 16px; padding: 20px; text-align: center; border: 2px dashed #49a7ff; margin-bottom: 20px; }}
        .ad-label {{ font-size: 11px; color: #49a7ff; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; }}
        h1 {{ color: #49a7ff; margin-bottom: 20px; }}
        h2 {{ color: #49a7ff; margin: 25px 0 15px; }}
        p {{ margin-bottom: 15px; color: #a0b3d9; }}
        .back-button {{ display: inline-block; margin-top: 30px; padding: 10px 20px; background: #49a7ff; color: white; text-decoration: none; border-radius: 8px; }}
        .footer {{ background: #0d1726; padding: 30px 20px; text-align: center; margin-top: 50px; }}
        @media (max-width: 768px) {{ .main-container {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <a href="index.html" class="logo"><i class="fas fa-newspaper"></i><span>NewsPortal</span></a>
            <button class="theme-toggle" onclick="toggleTheme()"><i class="fas fa-moon"></i></button>
        </div>
    </div>
    
    <div class="main-container">
        <div class="container">
            <h1><i class="fas fa-shield-alt"></i> Política de Privacidade</h1>
            <p><strong>Última atualização:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
            <h2>Cookies e Anúncios</h2>
            <p>Utilizamos a rede Adsterra e Monetag para exibir anúncios.</p>
            <a href="index.html" class="back-button"><i class="fas fa-arrow-left"></i> Voltar</a>
        </div>
        
        <div class="sidebar">
            <div class="ad-sidebar"><div class="ad-label"><i class="fas fa-ad"></i> Publicidade</div>
                <div><script>atOptions={{'key':'{SITE_CONFIG["adsterra_display_key"]}','format':'iframe','height':250,'width':300,'params':{{}}}};</script>
                <script src="https://www.highperformanceformat.com/{SITE_CONFIG['adsterra_display_key']}/invoke.js"></script></div>
            </div>
        </div>
    </div>
    
    <div class="footer"><p>&copy; 2024 NewsPortal</p></div>
    
    <script>
        function toggleTheme() {{
            const html = document.documentElement;
            const newTheme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }}
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
    </script>
    <style>
        [data-theme="light"] body {{ background: #f5f7fa; }}
        [data-theme="light"] .header {{ background: #fff; }}
        [data-theme="light"] .container {{ background: #fff; }}
        [data-theme="light"] p {{ color: #4a5a7a; }}
    </style>
</body>
</html>"""

def generate_terms_page():
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Termos de Uso - NewsPortal</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Adsterra Display -->
    <script>
        atOptions = {{
            'key' : '{SITE_CONFIG["adsterra_display_key"]}',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {{}}
        }};
    </script>
    <script src="https://www.highperformanceformat.com/{SITE_CONFIG['adsterra_display_key']}/invoke.js"></script>
    
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #08111f; color: #fff; line-height: 1.6; }}
        .header {{ background: #0d1726; padding: 15px 20px; border-bottom: 3px solid #49a7ff; }}
        .header-content {{ max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 24px; font-weight: bold; color: #49a7ff; text-decoration: none; display: flex; align-items: center; gap: 10px; }}
        .theme-toggle {{ background: #0f1a2e; border: 1px solid #49a7ff; padding: 8px 15px; border-radius: 25px; cursor: pointer; color: #fff; }}
        .main-container {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 300px; gap: 30px; }}
        .container {{ background: #0f1a2e; border-radius: 16px; padding: 30px; }}
        .sidebar {{ position: sticky; top: 100px; }}
        .ad-sidebar {{ background: linear-gradient(135deg, #0f1a2e, #0d1726); border-radius: 16px; padding: 20px; text-align: center; border: 2px dashed #49a7ff; margin-bottom: 20px; }}
        .ad-label {{ font-size: 11px; color: #49a7ff; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; }}
        h1 {{ color: #49a7ff; margin-bottom: 20px; }}
        h2 {{ color: #49a7ff; margin: 25px 0 15px; }}
        p {{ margin-bottom: 15px; color: #a0b3d9; }}
        .back-button {{ display: inline-block; margin-top: 30px; padding: 10px 20px; background: #49a7ff; color: white; text-decoration: none; border-radius: 8px; }}
        .footer {{ background: #0d1726; padding: 30px 20px; text-align: center; margin-top: 50px; }}
        @media (max-width: 768px) {{ .main-container {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <a href="index.html" class="logo"><i class="fas fa-newspaper"></i><span>NewsPortal</span></a>
            <button class="theme-toggle" onclick="toggleTheme()"><i class="fas fa-moon"></i></button>
        </div>
    </div>
    
    <div class="main-container">
        <div class="container">
            <h1><i class="fas fa-file-contract"></i> Termos de Uso</h1>
            <p><strong>Última atualização:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
            <h2>Uso do Site</h2>
            <p>Ao acessar o NewsPortal, você concorda com estes termos.</p>
            <h2>Anúncios</h2>
            <p>Utilizamos a rede Adsterra para exibir anúncios.</p>
            <a href="index.html" class="back-button"><i class="fas fa-arrow-left"></i> Voltar</a>
        </div>
        
        <div class="sidebar">
            <div class="ad-sidebar"><div class="ad-label"><i class="fas fa-ad"></i> Publicidade</div>
                <div><script>atOptions={{'key':'{SITE_CONFIG["adsterra_display_key"]}','format':'iframe','height':250,'width':300,'params':{{}}}};</script>
                <script src="https://www.highperformanceformat.com/{SITE_CONFIG['adsterra_display_key']}/invoke.js"></script></div>
            </div>
        </div>
    </div>
    
    <div class="footer"><p>&copy; 2024 NewsPortal</p></div>
    
    <script>
        function toggleTheme() {{
            const html = document.documentElement;
            const newTheme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }}
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
    </script>
</body>
</html>"""

# ===== FUNÇÕES DE ANÚNCIOS ADSTERRA =====
def generate_display_ad():
    """Display 300x250 - Principal"""
    return f"""
    <div class="card ad-card">
        <div class="ad-label"><i class="fas fa-ad"></i> Publicidade</div>
        <div style="width:100%; max-width:300px; margin:0 auto;">
            <script>
                atOptions = {{
                    'key' : '{SITE_CONFIG["adsterra_display_key"]}',
                    'format' : 'iframe',
                    'height' : 250,
                    'width' : 300,
                    'params' : {{}}
                }};
            </script>
            <script src="https://www.highperformanceformat.com/{SITE_CONFIG['adsterra_display_key']}/invoke.js"></script>
        </div>
    </div>
    """

def generate_native_ad():
    """Native Banner - Parece conteúdo natural"""
    return f"""
    <div class="ad-native">
        <div class="ad-label" style="text-align:center; margin-bottom:10px;">
            <i class="fas fa-star"></i> Conteúdo Patrocinado
        </div>
        <div id="{SITE_CONFIG['adsterra_native_div']}"></div>
        <script async="async" data-cfasync="false" 
                src="{SITE_CONFIG['adsterra_native_script']}"></script>
    </div>
    """

def generate_popunder():
    """Popunder - Abre atrás do site (1x por sessão)"""
    return f"""
    <script src="{SITE_CONFIG['adsterra_popunder']}"></script>
    """

def generate_socialbar():
    """Social Bar - Barra social na parte inferior"""
    return f"""
    <div class="socialbar-container">
        <script src="{SITE_CONFIG['adsterra_socialbar']}"></script>
    </div>
    """

# ===== INÍCIO DO HTML PRINCIPAL =====
html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    
    <title>{SITE_CONFIG['title']}</title>
    <meta name="description" content="{SITE_CONFIG['description']}">
    <meta name="keywords" content="{SITE_CONFIG['keywords']}">
    <meta name="author" content="{SITE_CONFIG['author']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE_CONFIG['site_url']}">
    
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE_CONFIG['site_url']}">
    <meta property="og:title" content="{SITE_CONFIG['title']}">
    <meta property="og:description" content="{SITE_CONFIG['description']}">
    <meta property="og:image" content="{SITE_CONFIG['logo_url']}">
    <meta property="og:site_name" content="{SITE_CONFIG['name']}">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{SITE_CONFIG['title']}">
    <meta name="twitter:description" content="{SITE_CONFIG['description']}">
    <meta name="twitter:image" content="{SITE_CONFIG['logo_url']}">
    
    <meta name="theme-color" content="{SITE_CONFIG['theme_color']}">
    
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📰</text></svg>">
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={SITE_CONFIG['analytics_id']}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{SITE_CONFIG['analytics_id']}');
    </script>
    
    <!-- Adsterra Display (Global) -->
    <script>
        atOptions = {{
            'key' : '{SITE_CONFIG["adsterra_display_key"]}',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {{}}
        }};
    </script>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {{
            --primary: {THEME_CONFIG['primary_color']};
            --secondary: {THEME_CONFIG['secondary_color']};
            --background: {THEME_CONFIG['background_color']};
            --card-bg: {THEME_CONFIG['card_bg']};
            --text: {THEME_CONFIG['text_color']};
            --text-secondary: {THEME_CONFIG['text_secondary']};
            --accent: {THEME_CONFIG['accent_color']};
            --shadow: rgba(0, 0, 0, 0.3);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        [data-theme="dark"] {{
            --background: #08111f;
            --card-bg: #0f1a2e;
            --text: #ffffff;
            --text-secondary: #a0b3d9;
        }}
        
        [data-theme="light"] {{
            --background: #f5f7fa;
            --card-bg: #ffffff;
            --text: #1a2a4a;
            --text-secondary: #4a5a7a;
            --shadow: rgba(0, 0, 0, 0.1);
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            background: var(--background);
            color: var(--text);
            font-family: {THEME_CONFIG['font_family']};
            line-height: 1.6;
            transition: var(--transition);
        }}
        
        .header {{
            background: linear-gradient(135deg, var(--secondary) 0%, var(--card-bg) 100%);
            padding: 15px 20px;
            border-bottom: 3px solid var(--primary);
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }}
        
        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
        }}
        
        .logo {{
            font-size: clamp(20px, 5vw, 28px);
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .logo i {{
            color: var(--primary);
            font-size: clamp(24px, 6vw, 32px);
        }}
        
        .logo span {{
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }}
        
        .theme-toggle {{
            background: var(--card-bg);
            border: 1px solid var(--primary);
            padding: 8px 15px;
            border-radius: 25px;
            cursor: pointer;
            color: var(--text);
            font-size: clamp(14px, 4vw, 18px);
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .theme-toggle:hover {{
            background: var(--primary);
            transform: scale(1.05);
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: clamp(15px, 4vw, 30px);
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: clamp(15px, 3vw, 30px);
        }}
        
        .card {{
            background: var(--card-bg);
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(73, 167, 255, 0.1);
            transition: var(--transition);
            position: relative;
        }}
        
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            transform: scaleX(0);
            transition: var(--transition);
        }}
        
        .card:hover::before {{
            transform: scaleX(1);
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px var(--shadow);
            border-color: var(--primary);
        }}
        
        .card a {{
            text-decoration: none;
            color: inherit;
            display: block;
        }}
        
        .image-container {{
            position: relative;
            overflow: hidden;
            background: var(--secondary);
        }}
        
        .thumb {{
            width: 100%;
            height: auto;
            aspect-ratio: 16/9;
            object-fit: cover;
            transition: var(--transition);
        }}
        
        .card:hover .thumb {{
            transform: scale(1.05);
        }}
        
        .badge {{
            position: absolute;
            top: 10px;
            left: 10px;
            background: var(--primary);
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: clamp(10px, 3vw, 12px);
            font-weight: bold;
        }}
        
        .reading-time {{
            position: absolute;
            bottom: 10px;
            right: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 4px 8px;
            border-radius: 20px;
            font-size: clamp(9px, 2.5vw, 11px);
        }}
        
        .content {{
            padding: clamp(12px, 4vw, 20px);
        }}
        
        .site {{
            color: var(--primary);
            font-size: clamp(10px, 3vw, 12px);
            margin-bottom: 8px;
            font-weight: bold;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        .title {{
            font-size: clamp(16px, 5vw, 20px);
            line-height: 1.4;
            font-weight: bold;
            margin-bottom: 10px;
            transition: var(--transition);
        }}
        
        .card:hover .title {{
            color: var(--primary);
        }}
        
        .description {{
            color: var(--text-secondary);
            font-size: clamp(12px, 3.5vw, 14px);
            margin-bottom: 12px;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: clamp(10px, 3vw, 12px);
            color: var(--text-secondary);
            border-top: 1px solid rgba(73, 167, 255, 0.1);
            padding-top: 10px;
            margin-top: 8px;
            flex-wrap: wrap;
            gap: 8px;
        }}
        
        .share-buttons {{
            display: flex;
            gap: 8px;
        }}
        
        .share-btn {{
            background: none;
            border: none;
            color: var(--text-secondary);
            cursor: pointer;
            transition: var(--transition);
            font-size: clamp(12px, 3.5vw, 14px);
            padding: 4px;
        }}
        
        .share-btn:hover {{
            color: var(--primary);
            transform: scale(1.1);
        }}
        
        .ad-card {{
            background: linear-gradient(135deg, var(--card-bg), var(--secondary));
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 300px;
            text-align: center;
            border: 2px dashed var(--primary);
            padding: 20px;
        }}
        
        .ad-label {{
            font-size: clamp(10px, 3vw, 11px);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 15px;
        }}
        
        .ad-native {{
            background: var(--card-bg);
            border-radius: 16px;
            padding: 20px;
            margin: 20px auto;
            border: 1px solid rgba(73, 167, 255, 0.2);
        }}
        
        .newsletter {{
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 16px;
            padding: clamp(20px, 5vw, 40px);
            text-align: center;
            margin: 20px auto;
            max-width: 90%;
            width: 800px;
        }}
        
        .newsletter h3 {{
            font-size: clamp(20px, 6vw, 28px);
            margin-bottom: 15px;
        }}
        
        .newsletter-form {{
            display: flex;
            gap: 10px;
            margin-top: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }}
        
        .newsletter-form input {{
            flex: 1;
            min-width: 200px;
            padding: 12px 20px;
            border: none;
            border-radius: 25px;
            font-size: clamp(14px, 4vw, 16px);
        }}
        
        .newsletter-form button {{
            background: var(--secondary);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: var(--transition);
        }}
        
        .footer {{
            background: var(--secondary);
            padding: 40px 20px 20px;
            margin-top: 50px;
        }}
        
        .footer-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }}
        
        .footer-section h4 {{
            color: var(--primary);
            margin-bottom: 15px;
        }}
        
        .footer-section a {{
            color: var(--text-secondary);
            text-decoration: none;
            display: block;
            margin-bottom: 10px;
            transition: var(--transition);
        }}
        
        .footer-section a:hover {{
            color: var(--primary);
            transform: translateX(5px);
        }}
        
        .social-links {{
            display: flex;
            gap: 15px;
            margin-top: 15px;
            flex-wrap: wrap;
        }}
        
        .social-links a {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(73, 167, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
        }}
        
        .social-links a:hover {{
            background: var(--primary);
            transform: translateY(-3px);
        }}
        
        .copyright {{
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid rgba(73, 167, 255, 0.1);
            color: var(--text-secondary);
        }}
        
        .back-to-top {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: var(--primary);
            color: white;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
            opacity: 0;
            visibility: hidden;
            z-index: 1000;
        }}
        
        .back-to-top.show {{
            opacity: 1;
            visibility: visible;
        }}
        
        .socialbar-container {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 999;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                grid-template-columns: 1fr;
            }}
            .footer-content {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
            .social-links {{
                justify-content: center;
            }}
        }}
        
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .card {{
            animation: fadeIn 0.6s ease-out;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo">
                <i class="fas fa-newspaper"></i>
                <span>NewsPortal</span>
            </div>
            <button class="theme-toggle" id="themeToggle">
                <i class="fas fa-moon"></i> <span id="themeText">Escuro</span>
            </button>
        </div>
    </div>
    
    <div class="container">
"""

# ===== GERAÇÕES DOS CARDS E ANÚNCIOS =====
# Controle de popunder (apenas uma vez por sessão)
popunder_added = False

for i, article in enumerate(articles):
    description = article.get('description', f'Leia as últimas notícias sobre {article["title"]}.')
    reading_time = get_reading_time(description)
    
    html += f"""
        <div class="card" data-url="{article['url']}" data-title="{article['title']}">
            <a href="{article['url']}" target="_blank">
                <div class="image-container">
                    <img class="thumb" 
                         src="{article['image'] if article['image'] else 'https://via.placeholder.com/800x600?text=News+Image'}" 
                         alt="{article['title']}"
                         loading="lazy"
                         onerror="this.src='https://via.placeholder.com/800x600?text=Imagem+Indisponível'">
                    <div class="badge">
                        <i class="fas fa-bolt"></i> Destaque
                    </div>
                    <div class="reading-time">
                        <i class="far fa-clock"></i> {reading_time} min
                    </div>
                </div>
                <div class="content">
                    <div class="site">
                        <i class="fas fa-globe"></i> {article['site']}
                    </div>
                    <div class="title">
                        {article['title']}
                    </div>
                    <div class="description">
                        {description[:150]}...
                    </div>
                    <div class="meta">
                        <span>
                            <i class="far fa-calendar-alt"></i> {datetime.now().strftime('%d/%m/%Y')}
                        </span>
                        <div class="share-buttons">
                            <button class="share-btn" onclick="shareArticle('twitter', this)">
                                <i class="fab fa-twitter"></i>
                            </button>
                            <button class="share-btn" onclick="shareArticle('facebook', this)">
                                <i class="fab fa-facebook"></i>
                            </button>
                            <button class="share-btn" onclick="shareArticle('whatsapp', this)">
                                <i class="fab fa-whatsapp"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </a>
        </div>
    """
    
    # Adiciona Display Ads a cada X notícias
    if (i + 1) % THEME_CONFIG['ads_frequency'] == 0 and (i + 1) != len(articles):
        html += generate_display_ad()
    
    # Adiciona Popunder apenas uma vez (no primeiro anúncio)
    if THEME_CONFIG['enable_popunder'] and not popunder_added and (i + 1) >= THEME_CONFIG['ads_frequency']:
        html += generate_popunder()
        popunder_added = True

# Adiciona Native Banner no final do container
if THEME_CONFIG['enable_native']:
    html += generate_native_ad()

html += """
    </div>
    
    <div class="newsletter">
        <h3><i class="fas fa-envelope"></i> Newsletter</h3>
        <p>Receba as principais notícias diretamente no seu email!</p>
        <form class="newsletter-form" onsubmit="subscribeNewsletter(event)">
            <input type="email" placeholder="Seu melhor email" required>
            <button type="submit">Inscrever-se</button>
        </form>
    </div>
    
    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h4><i class="fas fa-newspaper"></i> Sobre Nós</h4>
                <p>Portal de notícias comprometido com informações precisas.</p>
                <div class="social-links">
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-facebook"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
            <div class="footer-section">
                <h4>Legal</h4>
                <a href="privacidade.html"><i class="fas fa-chevron-right"></i> Política de Privacidade</a>
                <a href="termos.html"><i class="fas fa-chevron-right"></i> Termos de Uso</a>
            </div>
            <div class="footer-section">
                <h4>Contato</h4>
                <a href="#"><i class="fas fa-envelope"></i> newsportalbr@outlook.com</a>
            </div>
        </div>
        <div class="copyright">
            <p>&copy; 2024 NewsPortal - Todos os direitos reservados</p>
        </div>
    </div>
    
    <div class="back-to-top" id="backToTop" onclick="scrollToTop()">
        <i class="fas fa-arrow-up"></i>
    </div>
"""

# Adiciona Social Bar (se ativada)
if THEME_CONFIG['enable_socialbar']:
    html += generate_socialbar()

html += """
    <script>
        const themeToggle = document.getElementById('themeToggle');
        const themeText = document.getElementById('themeText');
        const currentTheme = localStorage.getItem('theme') || 'dark';
        
        function setTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            const icon = themeToggle.querySelector('i');
            if (theme === 'dark') {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
                themeText.textContent = 'Escuro';
            } else {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
                themeText.textContent = 'Claro';
            }
        }
        
        setTheme(currentTheme);
        
        themeToggle.addEventListener('click', () => {
            const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
        
        window.shareArticle = function(platform, element) {
            const card = element.closest('.card');
            const url = card.getAttribute('data-url');
            const title = card.getAttribute('data-title');
            const text = encodeURIComponent(title + '\\n\\n' + url);
            
            let shareUrl = '';
            switch(platform) {
                case 'twitter':
                    shareUrl = `https://twitter.com/intent/tweet?text=${text}`;
                    break;
                case 'facebook':
                    shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
                    break;
                case 'whatsapp':
                    shareUrl = `https://wa.me/?text=${text}`;
                    break;
            }
            
            if (shareUrl) {
                window.open(shareUrl, '_blank', 'width=600,height=400');
            }
        };
        
        window.subscribeNewsletter = function(event) {
            event.preventDefault();
            const email = event.target.querySelector('input[type="email"]').value;
            alert(`Obrigado por se inscrever! 📧 ${email}`);
            event.target.reset();
        };
        
        window.scrollToTop = function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        };
        
        window.addEventListener('scroll', () => {
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        });
        
        // Controle de popunder (apenas 1x por sessão)
        if (!sessionStorage.getItem('popunder_shown')) {
            sessionStorage.setItem('popunder_shown', 'true');
        }
    </script>
</body>
</html>
"""

# ===== SALVA OS ARQUIVOS =====
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("privacidade.html", "w", encoding="utf-8") as f:
    f.write(generate_privacy_page())

with open("termos.html", "w", encoding="utf-8") as f:
    f.write(generate_terms_page())
