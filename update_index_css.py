from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
start = text.find('<style>')
end = text.find('</style>', start)
if start == -1 or end == -1:
    raise SystemExit('style block not found')
new_css = '''    <style>
        :root {
            --anc-green: #00853F;
            --anc-black: #111111;
            --anc-gold: #FFD700;
            --anc-light: #F7F7F5;
            --anc-muted: #5A5A5A;
            --anc-transparent-green: rgba(0, 133, 63, 0.92);
        }

        *, *::before, *::after {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            color: #1d1d1d;
            background: linear-gradient(180deg, #f6f7f2 0%, #f2f3ee 100%);
            min-height: 100vh;
        }

        img {
            max-width: 100%;
            display: block;
        }

        a {
            text-decoration: none;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Satoshi', sans-serif;
            font-weight: 700;
            color: var(--anc-green);
            line-height: 1.15;
            text-align: center;
        }

        .section-title {
            position: relative;
            display: inline-block;
            font-size: clamp(2rem, 4vw, 2.8rem);
            margin: 0 auto 2.5rem;
            color: var(--anc-green);
        }

        .section-title::after {
            content: '';
            position: absolute;
            left: 50%;
            bottom: -16px;
            transform: translateX(-50%);
            width: 90px;
            height: 4px;
            background: var(--anc-gold);
            border-radius: 999px;
        }

        .navbar {
            background: rgba(0, 133, 63, 0.96);
            border-bottom: 4px solid var(--anc-gold);
            padding: 1rem 0;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.14);
            transition: transform 0.4s ease, background-color 0.4s ease, box-shadow 0.4s ease;
        }

        .navbar-brand {
            display: flex;
            align-items: center;
            gap: 14px;
            color: var(--anc-gold) !important;
            font-size: 1.05rem;
            letter-spacing: 0.08em;
            font-weight: 700;
            text-transform: uppercase;
        }

        .navbar-brand img {
            height: 54px;
            border-radius: 12px;
            box-shadow: 0 8px 18px rgba(0, 0, 0, 0.16);
        }

        .navbar-toggler {
            border-color: rgba(255, 255, 255, 0.55);
        }

        .navbar-toggler-icon {
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255,255,255,0.9)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
        }

        .navbar-nav .nav-link {
            color: rgba(255, 255, 255, 0.92) !important;
            font-weight: 600;
            position: relative;
            padding: 0.55rem 0.85rem !important;
            transition: color 0.3s ease;
        }

        .navbar-nav .nav-link::after {
            content: '';
            position: absolute;
            left: 50%;
            bottom: 0;
            width: 0;
            height: 3px;
            background: var(--anc-gold);
            border-radius: 999px;
            transform: translateX(-50%);
            transition: width 0.35s ease;
        }

        .navbar-nav .nav-link:hover,
        .navbar-nav .nav-link.active {
            color: #fff !important;
        }

        .navbar-nav .nav-link:hover::after,
        .navbar-nav .nav-link.active::after {
            width: calc(100% - 1rem);
        }

        .hero {
            position: relative;
            min-height: calc(100vh - 96px);
            display: flex;
            align-items: center;
            justify-content: center;
            background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.42), rgba(0, 0, 0, 0.18)), url('main.jpg');
            background-size: cover;
            background-position: center;
            color: #fff;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top, rgba(255, 255, 255, 0.08), transparent 40%);
            pointer-events: none;
        }

        .hero .container {
            position: relative;
            z-index: 2;
            padding: 6rem 0;
        }

        .hero h1 {
            font-size: clamp(2.4rem, 5vw, 4rem);
            margin-bottom: 1.4rem;
            text-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
        }

        .hero p.lead {
            font-size: clamp(1.05rem, 2vw, 1.5rem);
            max-width: 780px;
            margin: 0 auto 2.2rem;
            color: rgba(255, 255, 255, 0.92);
        }

        .hero .btn {
            background: var(--anc-gold);
            color: var(--anc-black);
            font-weight: 700;
            padding: 1rem 2.8rem;
            border-radius: 999px;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.2);
            transition: transform 0.35s ease, background 0.35s ease;
        }

        .hero .btn:hover {
            background: #ffffff;
            color: var(--anc-green);
            transform: translateY(-2px);
        }

        section {
            padding: 6rem 0;
        }

        .bg-white {
            background: #ffffff;
        }

        .bg-light {
            background: #f6f7f2;
        }

        .card {
            border: 0;
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12);
            transition: transform 0.45s ease, box-shadow 0.45s ease;
            background: #ffffff;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 32px 70px rgba(0, 0, 0, 0.16);
        }

        .card img {
            height: 280px;
            object-fit: cover;
        }

        .card .card-body {
            padding: 2rem;
        }

        .card h5 {
            margin-bottom: 1rem;
            color: var(--anc-black);
            font-size: 1.22rem;
        }

        .card p {
            color: var(--anc-muted);
            margin-bottom: 1.8rem;
        }

        .card .btn {
            background: var(--anc-green);
            color: var(--anc-gold);
            padding: 0.9rem 1.9rem;
            border-radius: 999px;
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .card .btn:hover {
            background: var(--anc-gold);
            color: var(--anc-black);
            transform: translateY(-2px);
        }

        .moments-container {
            position: relative;
            padding: 2rem;
            border-radius: 32px;
            background: #ffffff;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.14);
            overflow: hidden;
        }

        .moments-container::before {
            content: '';
            position: absolute;
            inset: 0;
            margin: -4px;
            border-radius: inherit;
            background: linear-gradient(135deg, #00853F, #00a854, #00853F);
            z-index: -1;
        }

        .moments-swiper {
            height: 620px;
            border-radius: 28px;
            overflow: hidden;
        }

        .moments-slide {
            position: relative;
            overflow: hidden;
            border-radius: 24px;
        }

        .moments-slide img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 1.2s ease;
        }

        .moments-slide:hover img {
            transform: scale(1.08);
        }

        .moments-caption {
            position: absolute;
            left: 50%;
            bottom: 24px;
            transform: translateX(-50%);
            max-width: 84%;
            padding: 1.6rem 1.8rem;
            border-radius: 24px;
            background: rgba(0, 0, 0, 0.62);
            color: var(--anc-gold);
            font-family: 'Satoshi', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.28);
        }

        .moments-button-prev,
        .moments-button-next {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 72px;
            height: 72px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.75);
            color: var(--anc-gold);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.22);
            z-index: 10;
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .moments-button-prev {
            left: 24px;
        }

        .moments-button-next {
            right: 24px;
        }

        .moments-button-prev:hover,
        .moments-button-next:hover {
            background: var(--anc-gold);
            color: var(--anc-black);
            transform: translateY(-50%) scale(1.05);
        }

        .youtube-container {
            position: relative;
            max-width: 860px;
            margin: 0 auto;
            padding: 6px;
            border-radius: 28px;
            background: linear-gradient(135deg, #00853F, #00a854, #00853F);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.2);
            transition: transform 0.35s ease;
        }

        .youtube-container:hover {
            transform: translateY(-8px);
        }

        .youtube-container::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: inherit;
            background: #ffffff;
            z-index: -1;
        }

        .youtube-thumbnail {
            width: 100%;
            display: block;
            border-radius: 22px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }

        .play-button {
            position: absolute;
            inset: 0;
            margin: auto;
            width: 96px;
            height: 96px;
            background: rgba(255, 215, 0, 0.95);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease;
        }

        .play-button::after {
            content: '';
            width: 0;
            height: 0;
            border-left: 28px solid var(--anc-black);
            border-top: 18px solid transparent;
            border-bottom: 18px solid transparent;
            margin-left: 6px;
        }

        .play-button:hover {
            transform: scale(1.1);
        }

        .bg-dark {
            background: #121212 !important;
        }

        .bg-dark .section-title,
        .bg-dark h1,
        .bg-dark h2,
        .bg-dark p,
        .bg-dark .lead {
            color: #ffffff;
        }

        footer {
            background: var(--anc-black);
            color: var(--anc-gold);
            padding: 4.5rem 0 2.5rem;
            text-align: center;
        }

        footer a {
            color: var(--anc-gold);
            margin: 0 0.75rem;
            transition: transform 0.3s ease, color 0.3s ease;
        }

        footer a:hover {
            color: #ffffff;
            transform: translateY(-2px);
        }

        .fadeInUp {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }

        .fadeInUp.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .stagger-1 { transition-delay: 0.1s; }
        .stagger-2 { transition-delay: 0.25s; }
        .stagger-3 { transition-delay: 0.4s; }

        @media (max-width: 992px) {
            .hero {
                min-height: 58vh;
            }

            .hero h1 {
                font-size: 2.7rem;
            }

            .hero p.lead {
                font-size: 1.2rem;
            }

            section {
                padding: 4.5rem 0;
            }

            .moments-swiper {
                height: 520px;
            }
        }

        @media (max-width: 768px) {
            .navbar {
                padding: 0.9rem 0.5rem;
            }

            .hero {
                min-height: 55vh;
            }

            .hero h1 {
                font-size: 2.4rem;
            }

            .hero p.lead {
                font-size: 1.1rem;
            }

            .card img {
                height: 240px;
            }

            .moments-swiper {
                height: 420px;
            }
        }
    </style>'''
path.write_text(text[:start] + new_css + text[end+8:], encoding='utf-8')
print('Updated homepage CSS')
