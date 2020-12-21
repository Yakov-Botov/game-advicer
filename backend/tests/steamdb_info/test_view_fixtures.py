import pytest


@pytest.fixture
def make_tag_info_result():
    return {'tag_products_count': '49175', 'tag_name': 'Indie', 'tag_steam_id': '492'}


@pytest.fixture
def make_tag_info_html():
    return """
    <!DOCTYPE HTML>
<html lang="en" class="dark-mode">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Steam Game Tags · SteamDB</title>
<link rel="stylesheet" integrity="sha512-u4ANqiUgKArWikGDNn9/99ZY0F9CAJYs00iDywyttoMV5FjpBx/bWMpRTkFan4HpIyNOOJhrUJKn9RkEbNZ8AA==" href="/static/css/headcrab.css?v=bb800daa2520280a"><link rel="stylesheet" integrity="sha512-2vJprXVY2N1Ss9GvIJIQewPxdcz7MoKU3ZZJ9vzTK9x6tBONQg4Nk9KgL7NXYNiZfMWrbJ9RLHjLBIDdtpIIaQ==" href="/static/css/houndeye.css?v=daf269ad7558d8dd">
<link rel="alternate" type="application/rss+xml" title="SteamDB Blog" href="https://steamdb.info/api/BlogRSS/">
<link rel="canonical" href="https://steamdb.info/tags/">
<meta property="twitter:card" content="summary">
<meta property="twitter:site" content="@SteamDB">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SteamDB">
<meta property="og:title" content="Steam Game Tags">
<meta name="description" content="List of all game tags on Steam. Tags help Steam determine where games are displayed to customers.">
<meta property="og:description" content="List of all game tags on Steam. Tags help Steam determine where games are displayed to customers.">
<meta property="og:image" content="https://steamdb.info/static/logos/512px.png">
<link rel="image_src" href="https://steamdb.info/static/logos/512px.png">
<meta name="theme-color" content="#000000">
<meta name="application-name" content="SteamDB">
<meta name="apple-mobile-web-app-title" content="SteamDB">
<link rel="manifest" href="/steamdb.webmanifest">
<link rel="icon" type="image/png" href="/static/logos/32px.png">
<link rel="icon" type="image/svg+xml" href="/static/logos/vector_prefers_schema.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/static/logos/512px_maskable.png">
<link rel="mask-icon" href="/static/logos/vector_16px.svg" color="#000000">
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="SteamDB">
<link rel="webmention" href="https://steamdb.info/api/Webmention/">
<link rel="preconnect" href="https://cdn.cloudflare.steamstatic.com/">
</head>
<body class="page-tags" itemscope itemtype="http://schema.org/WebSite" data-steam-cdn="https://cdn.cloudflare.steamstatic.com/">
<div class="footer-wrap">
<div class="body-content">
<div id="announcement">
<style>
#announcement {
    color: #66c0f4;
    background-color: #000;
}

#announcement a {
    color: inherit;
    text-decoration: none;
}

#announcement a:hover {
    text-decoration: underline;
}

.page-tokendumper #announcement {
    display: none;
}

@media (max-width: 980px) {
    #announcement {
        display: none;
    }
}
</style>
<div class="container">
<svg class="octicon" style="width:25px;height:20px;margin-left:5px;margin-right:14px" aria-hidden="true" focusable="false" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M436 17.5c-30.8-26.7-76.7-21.9-104.9 7.7L320 36.9l-11.1-11.6C280.7-4.4 234.8-9.2 204 17.5c-35.3 30.6-37.2 85.6-5.6 118.8l108.9 114.2c7 7.4 18.4 7.4 25.5 0l108.9-114.2c31.5-33.2 29.7-88.2-5.7-118.8zM204.8 230.4c-10.6-14.1-30.7-17-44.8-6.4-14.1 10.6-17 30.7-6.4 44.8l38.1 50.8c4.8 6.4 4.1 15.3-1.5 20.9l-12.8 12.8c-6.7 6.7-17.6 6.2-23.6-1.1L64 244.4V96c0-17.7-14.3-32-32-32S0 78.3 0 96v218.4c0 10.9 3.7 21.5 10.5 30l104.1 134.3c5 6.5 8.4 13.9 10.4 21.7 1.8 6.9 8.1 11.6 15.3 11.6H272c8.8 0 16-7.2 16-16V384c0-27.7-9-54.6-25.6-76.8l-57.6-76.8zM608 64c-17.7 0-32 14.3-32 32v148.4l-89.8 107.8c-6 7.2-17 7.7-23.6 1.1l-12.8-12.8c-5.6-5.6-6.3-14.5-1.5-20.9l38.1-50.8c10.6-14.1 7.7-34.2-6.4-44.8-14.1-10.6-34.2-7.7-44.8 6.4l-57.6 76.8C361 329.4 352 356.3 352 384v112c0 8.8 7.2 16 16 16h131.7c7.1 0 13.5-4.7 15.3-11.6 2-7.8 5.4-15.2 10.4-21.7l104.1-134.3c6.8-8.5 10.5-19.1 10.5-30V96c0-17.7-14.3-32-32-32z"></path></svg><a href="/tokendumper/">Contribute to SteamDB: Use our token dumper program to help us track hidden games and packages</a>
</div>
</div>
<div class="header">
<div class="container">
<ul class="header-navbar">
<li class="header-brand mobile-visible"><a href="/" itemprop="url" aria-label="Homepage"><svg version="1.1" width="30" height="30" viewBox="0 0 128 128" class="octicon octicon-steamdb" aria-hidden="true"><path fill-rule="evenodd" d="M63.9 0C30.5 0 3.1 11.9.1 27.1l35.6 6.7c2.9-.9 6.2-1.3 9.6-1.3l16.7-10c-.2-2.5 1.3-5.1 4.7-7.2 4.8-3.1 12.3-4.8 19.9-4.8 5.2-.1 10.5.7 15 2.2 11.2 3.8 13.7 11.1 5.7 16.3-5.1 3.3-13.3 5-21.4 4.8l-22 7.9c-.2 1.6-1.3 3.1-3.4 4.5-5.9 3.8-17.4 4.7-25.6 1.9-3.6-1.2-6-3-7-4.8L2.5 38.4c2.3 3.6 6 6.9 10.8 9.8C5 53 0 59 0 65.5c0 6.4 4.8 12.3 12.9 17.1C4.8 87.3 0 93.2 0 99.6 0 115.3 28.6 128 64 128c35.3 0 64-12.7 64-28.4 0-6.4-4.8-12.3-12.9-17 8.1-4.8 12.9-10.7 12.9-17.1 0-6.5-5-12.6-13.4-17.4 8.3-5.1 13.3-11.4 13.3-18.2 0-16.5-28.7-29.9-64-29.9zm22.8 14.2c-5.2.1-10.2 1.2-13.4 3.3-5.5 3.6-3.8 8.5 3.8 11.1 7.6 2.6 18.1 1.8 23.6-1.8s3.8-8.5-3.8-11c-3.1-1-6.7-1.5-10.2-1.5zm.3 1.7c7.4 0 13.3 2.8 13.3 6.2 0 3.4-5.9 6.2-13.3 6.2s-13.3-2.8-13.3-6.2c0-3.4 5.9-6.2 13.3-6.2zM45.3 34.4c-1.6.1-3.1.2-4.6.4l9.1 1.7a10.8 5 0 1 1-8.1 9.3l-8.9-1.7c1 .9 2.4 1.7 4.3 2.4 6.4 2.2 15.4 1.5 20-1.5s3.2-7.2-3.2-9.3c-2.6-.9-5.7-1.3-8.6-1.3zM109 51v9.3c0 11-20.2 19.9-45 19.9-24.9 0-45-8.9-45-19.9v-9.2c11.5 5.3 27.4 8.6 44.9 8.6 17.6 0 33.6-3.3 45.2-8.7zm0 34.6v8.8c0 11-20.2 19.9-45 19.9-24.9 0-45-8.9-45-19.9v-8.8c11.6 5.1 27.4 8.2 45 8.2s33.5-3.1 45-8.2z" /></svg></a></li>
<li class="header-search mobile-visible">
<form id="js-header-form" method="GET" action="/search/" itemprop="potentialAction" itemscope itemtype="http://schema.org/SearchAction">
<input type="hidden" name="a" value="app">
<meta itemprop="target" content="https://steamdb.info/search/?a=app&amp;q={q}">
<input type="search" class="field" id="js-header-search" name="q" placeholder="Search…" itemprop="query-input" aria-label="Search">
<button type="submit" class="submit" aria-label="Perform search"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-search" aria-hidden="true"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg></button>
</form>
</li>
<li><a href="/sales/">Sales</a></li>
<li><a href="/calculator/">Calculator</a></li>
<li><a href="/patchnotes/">Patch notes</a></li>
<li><a href="/graph/">Charts</a></li>
<li><a href="/upcoming/">Upcoming</a></li>
<li class="header-hamburger"><span>More</span><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-chevron-down" aria-hidden="true"><path fill-rule="evenodd" d="M12.78 6.22a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06 0L3.22 7.28a.75.75 0 011.06-1.06L8 9.94l3.72-3.72a.75.75 0 011.06 0z"></path></svg></li>
<li class="header-hamburger mobile-visible"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-three-bars" aria-hidden="true"><path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path></svg></li>
<li class="header-user">
<a class="header-login" href="/login/?page=tags">
<span>Sign in</span>
<svg class="header-piston" viewBox="0 0 20 16" width="20" height="16">
<circle stroke-width="1.5" cy="4.5" cx="15.5" r="3.75" class="stroke" />
<circle cx="15.5" cy="4.5" r="1.855" class="fill" />
<path d="M11.656 4.2L12.75 7.14l2.865 1.387-5.13 3.853-.867-2.09-1.773-.942z" class="fill" />
<circle cy="12.5" cx="7.5" r="3" class="stroke" />
<rect transform="matrix(.92432 .3816 -.38727 .92196 0 0)" ry="1.526" width="9.477" y="7.155" x="3.767" height="3.053" class="fill" />
</svg>
</a>
</li>
</ul>
</div>
<div class="header-search-suggestions">
<div class="container" id="js-search-suggestions">
<p>Start typing to see game suggestions. This only suggests apps that are available on the Steam store.</p>
<p>Shortcuts:</p>
<ul>
<li>Enter an appid to be redirected to the app page.</li>
<li>Enter a steamid (765...) to be redirected to calculator.</li>
<li>Paste a profile link (/id/ or /profiles/) to be redirected to calculator.</li>
<li>Paste any url that contains app/, sub/, bundle/, or /depot to be redirected to the relevant page.</li>
</ul>
<p>Click anywhere outside the search field to close this popup.</p>
<p>Search suggestions are powered by Algolia instant search.</p>
</div>
</div>
<div class="header-menu">
<div class="container">
<ul>
<li><a href="/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-home" aria-hidden="true"><path fill-rule="evenodd" d="M8.156 1.835a.25.25 0 00-.312 0l-5.25 4.2a.25.25 0 00-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 01.75-.75h3.5a.75.75 0 01.75.75v5.25h2.75a.25.25 0 00.25-.25V6.23a.25.25 0 00-.094-.195l-5.25-4.2zM6.906.664a1.75 1.75 0 012.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0113.25 15h-3.5a.75.75 0 01-.75-.75V9H7v5.25a.75.75 0 01-.75.75h-3.5A1.75 1.75 0 011 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2h-.001z"></path></svg> Homepage</a></li>
<li><a href="/blog/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-megaphone" aria-hidden="true"><path fill-rule="evenodd" d="M15.571.572A.75.75 0 0116 1.25L14.777.668c.001 0 0 0 0 0l-.015.012-.076.056a5.508 5.508 0 01-.345.224 9.982 9.982 0 01-1.463.719c-1.322.528-3.351 1.07-6.124 1.071a1.6 1.6 0 00-.861-.25H4a4 4 0 00-1.499 7.71.758.758 0 00-.001.04c0 2.32.486 3.93.813 4.75.262.66.897 1 1.517 1h1.197c.685 0 1.228-.389 1.546-.857.317-.466.468-1.09.31-1.696-.2-.767-.382-1.835-.383-3.183 2.394.086 4.177.577 5.378 1.057a9.965 9.965 0 011.463.719 5.7 5.7 0 01.421.28l.014.012h.002A.75.75 0 0016 11.75V1.25L14.777.668a.75.75 0 01.794-.096zM4.002 10.5c.033 1.969.45 3.306.704 3.946.004.01.01.02.027.03a.185.185 0 00.097.024h1.197c.083 0 .202-.047.305-.2a.608.608 0 00.1-.475 14.036 14.036 0 01-.43-3.329 1.64 1.64 0 01-.11.004h-1.89zM7.5 8.763c2.601.087 4.573.62 5.935 1.166.41.164.766.33 1.065.483V2.588c-.3.154-.654.319-1.065.483C12.073 3.616 10.1 4.15 7.5 4.237v4.526zM14.777.668zM1.5 6.5A2.5 2.5 0 014 4h1.893c.059 0 .107.048.107.107v4.786A.107.107 0 015.893 9H4a2.5 2.5 0 01-2.5-2.5z"></path></svg> Blog</a></li>
<li><a href="/faq/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-question" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg> FAQ &amp; Help</a></li>
<li class="mobile-visible"><a href="/sales/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-credit-card" aria-hidden="true"><path d="M10.75 9a.75.75 0 000 1.5h1.5a.75.75 0 000-1.5h-1.5z"></path><path fill-rule="evenodd" d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0114.25 14H1.75A1.75 1.75 0 010 12.25v-8.5zm14.5 0V5h-13V3.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25zm0 2.75h-13v5.75c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V6.5z"></path></svg> Sales</a></li>
<li class="mobile-visible"><a href="/calculator/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-smiley" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg> Calculator</a></li>
<li class="mobile-visible"><a href="/patchnotes/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-megaphone" aria-hidden="true"><path fill-rule="evenodd" d="M15.571.572A.75.75 0 0116 1.25L14.777.668c.001 0 0 0 0 0l-.015.012-.076.056a5.508 5.508 0 01-.345.224 9.982 9.982 0 01-1.463.719c-1.322.528-3.351 1.07-6.124 1.071a1.6 1.6 0 00-.861-.25H4a4 4 0 00-1.499 7.71.758.758 0 00-.001.04c0 2.32.486 3.93.813 4.75.262.66.897 1 1.517 1h1.197c.685 0 1.228-.389 1.546-.857.317-.466.468-1.09.31-1.696-.2-.767-.382-1.835-.383-3.183 2.394.086 4.177.577 5.378 1.057a9.965 9.965 0 011.463.719 5.7 5.7 0 01.421.28l.014.012h.002A.75.75 0 0016 11.75V1.25L14.777.668a.75.75 0 01.794-.096zM4.002 10.5c.033 1.969.45 3.306.704 3.946.004.01.01.02.027.03a.185.185 0 00.097.024h1.197c.083 0 .202-.047.305-.2a.608.608 0 00.1-.475 14.036 14.036 0 01-.43-3.329 1.64 1.64 0 01-.11.004h-1.89zM7.5 8.763c2.601.087 4.573.62 5.935 1.166.41.164.766.33 1.065.483V2.588c-.3.154-.654.319-1.065.483C12.073 3.616 10.1 4.15 7.5 4.237v4.526zM14.777.668zM1.5 6.5A2.5 2.5 0 014 4h1.893c.059 0 .107.048.107.107v4.786A.107.107 0 015.893 9H4a2.5 2.5 0 01-2.5-2.5z"></path></svg> Patch notes</a></li>
<li class="mobile-visible"><a href="/graph/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-pulse" aria-hidden="true"><path fill-rule="evenodd" d="M6 2a.75.75 0 01.696.471L10 10.731l1.304-3.26A.75.75 0 0112 7h3.25a.75.75 0 010 1.5h-2.742l-1.812 4.528a.75.75 0 01-1.392 0L6 4.77 4.696 8.03A.75.75 0 014 8.5H.75a.75.75 0 010-1.5h2.742l1.812-4.529A.75.75 0 016 2z"></path></svg> Charts</a></li>
<li><a href="/donate/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-key" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 5.5a4 4 0 112.731 3.795.75.75 0 00-.768.18L7.44 10.5H6.25a.75.75 0 00-.75.75v1.19l-.06.06H4.25a.75.75 0 00-.75.75v1.19l-.06.06H1.75a.25.25 0 01-.25-.25v-1.69l5.024-5.023a.75.75 0 00.181-.768A3.995 3.995 0 016.5 5.5zm4-5.5a5.5 5.5 0 00-5.348 6.788L.22 11.72a.75.75 0 00-.22.53v2C0 15.216.784 16 1.75 16h2a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V14h.75a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V12h.75a.75.75 0 00.53-.22l.932-.932A5.5 5.5 0 1010.5 0zm.5 6a1 1 0 100-2 1 1 0 000 2z"></path></svg> Donate</a></li>
<li><a href="/extension/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-desktop-download" aria-hidden="true"><path fill-rule="evenodd" d="M8.75 5V.75a.75.75 0 00-1.5 0V5H5.104a.25.25 0 00-.177.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 5H8.75zM1.5 2.75a.25.25 0 01.25-.25h3a.75.75 0 000-1.5h-3A1.75 1.75 0 000 2.75v7.5C0 11.216.784 12 1.75 12h3.727c-.1 1.041-.52 1.872-1.292 2.757A.75.75 0 004.75 16h6.5a.75.75 0 00.565-1.243c-.772-.885-1.193-1.716-1.292-2.757h3.727A1.75 1.75 0 0016 10.25v-7.5A1.75 1.75 0 0014.25 1h-3a.75.75 0 000 1.5h3a.25.25 0 01.25.25v7.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25v-7.5zM9.018 12H6.982a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5z"></path></svg> Browser extension</a></li>
</ul>
<ul>
<li><a href="/apps/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-list-ordered" aria-hidden="true"><path fill-rule="evenodd" d="M2.003 2.5a.5.5 0 00-.723-.447l-1.003.5a.5.5 0 00.446.895l.28-.14V6H.5a.5.5 0 000 1h2.006a.5.5 0 100-1h-.503V2.5zM5 3.25a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5A.75.75 0 015 3.25zm0 5a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5A.75.75 0 015 8.25zm0 5a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5a.75.75 0 01-.75-.75zM.924 10.32l.003-.004a.851.851 0 01.144-.153A.66.66 0 011.5 10c.195 0 .306.068.374.146a.57.57 0 01.128.376c0 .453-.269.682-.8 1.078l-.035.025C.692 11.98 0 12.495 0 13.5a.5.5 0 00.5.5h2.003a.5.5 0 000-1H1.146c.132-.197.351-.372.654-.597l.047-.035c.47-.35 1.156-.858 1.156-1.845 0-.365-.118-.744-.377-1.038-.268-.303-.658-.484-1.126-.484-.48 0-.84.202-1.068.392a1.858 1.858 0 00-.348.384l-.007.011-.002.004-.001.002-.001.001a.5.5 0 00.851.525zM.5 10.055l-.427-.26.427.26z"></path></svg> Apps</a></li>
<li><a href="/subs/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-package" aria-hidden="true"><path fill-rule="evenodd" d="M8.878.392a1.75 1.75 0 00-1.756 0l-5.25 3.045A1.75 1.75 0 001 4.951v6.098c0 .624.332 1.2.872 1.514l5.25 3.045a1.75 1.75 0 001.756 0l5.25-3.045c.54-.313.872-.89.872-1.514V4.951c0-.624-.332-1.2-.872-1.514L8.878.392zM7.875 1.69a.25.25 0 01.25 0l4.63 2.685L8 7.133 3.245 4.375l4.63-2.685zM2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432L2.5 5.677zm6.25 8.271l4.625-2.683a.25.25 0 00.125-.216V5.677L8.75 8.432v5.516z"></path></svg> Packages</a></li>
<li><a href="/bundles/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-package-dependents" aria-hidden="true"><path fill-rule="evenodd" d="M6.122.392a1.75 1.75 0 011.756 0l5.25 3.045c.54.313.872.89.872 1.514V7.25a.75.75 0 01-1.5 0V5.677L7.75 8.432v6.384a1 1 0 01-1.502.865L.872 12.563A1.75 1.75 0 010 11.049V4.951c0-.624.332-1.2.872-1.514L6.122.392zM7.125 1.69l4.63 2.685L7 7.133 2.245 4.375l4.63-2.685a.25.25 0 01.25 0zM1.5 11.049V5.677l4.75 2.755v5.516l-4.625-2.683a.25.25 0 01-.125-.216zm10.828 3.684a.75.75 0 101.087 1.034l2.378-2.5a.75.75 0 000-1.034l-2.378-2.5a.75.75 0 00-1.087 1.034L13.501 12H10.25a.75.75 0 000 1.5h3.251l-1.173 1.233z"></path></svg> Bundles</a></li>
<li><a href="/history/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-history" aria-hidden="true"><path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path></svg> History</a></li>
<li><a href="/instantsearch/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-search" aria-hidden="true"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg> Instant Search</a></li>
</ul>
<ul>
<li><a href="/realtime/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-hubot" aria-hidden="true"><path fill-rule="evenodd" d="M0 8a8 8 0 1116 0v5.25a.75.75 0 01-1.5 0V8a6.5 6.5 0 10-13 0v5.25a.75.75 0 01-1.5 0V8zm5.5 4.25a.75.75 0 01.75-.75h3.5a.75.75 0 010 1.5h-3.5a.75.75 0 01-.75-.75zM3 6.75C3 5.784 3.784 5 4.75 5h6.5c.966 0 1.75.784 1.75 1.75v1.5A1.75 1.75 0 0111.25 10h-6.5A1.75 1.75 0 013 8.25v-1.5zm1.47-.53a.75.75 0 011.06 0l.97.97.97-.97a.75.75 0 011.06 0l.97.97.97-.97a.75.75 0 111.06 1.06l-1.5 1.5a.75.75 0 01-1.06 0L8 7.81l-.97.97a.75.75 0 01-1.06 0l-1.5-1.5a.75.75 0 010-1.06z"></path></svg> Realtime Updates</a></li>
<li><a href="/pricechanges/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-mirror" aria-hidden="true"><path fill-rule="evenodd" d="M8.75 1.75a.75.75 0 00-1.5 0v.5a.75.75 0 001.5 0v-.5zM8 4a.75.75 0 01.75.75v.5a.75.75 0 01-1.5 0v-.5A.75.75 0 018 4zm.75 3.75a.75.75 0 00-1.5 0v.5a.75.75 0 001.5 0v-.5zM8 10a.75.75 0 01.75.75v.5a.75.75 0 01-1.5 0v-.5A.75.75 0 018 10zm0 3a.75.75 0 01.75.75v.5a.75.75 0 01-1.5 0v-.5A.75.75 0 018 13zm7.547-9.939A.75.75 0 0116 3.75v8.5a.75.75 0 01-1.265.545l-4.5-4.25a.75.75 0 010-1.09l4.5-4.25a.75.75 0 01.812-.144zM11.842 8l2.658 2.51V5.49L11.842 8zM0 12.25a.75.75 0 001.265.545l4.5-4.25a.75.75 0 000-1.09l-4.5-4.25A.75.75 0 000 3.75v8.5zm1.5-6.76L4.158 8 1.5 10.51V5.49z"></path></svg> Price Tracking</a></li>
<li><a href="/tags/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-tag" aria-hidden="true"><path fill-rule="evenodd" d="M2.5 7.775V2.75a.25.25 0 01.25-.25h5.025a.25.25 0 01.177.073l6.25 6.25a.25.25 0 010 .354l-5.025 5.025a.25.25 0 01-.354 0l-6.25-6.25a.25.25 0 01-.073-.177zm-1.5 0V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 010 2.474l-5.026 5.026a1.75 1.75 0 01-2.474 0l-6.25-6.25A1.75 1.75 0 011 7.775zM6 5a1 1 0 100 2 1 1 0 000-2z"></path></svg> Tags</a></li>
<li><a href="/upcoming/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-calendar" aria-hidden="true"><path fill-rule="evenodd" d="M4.75 0a.75.75 0 01.75.75V2h5V.75a.75.75 0 011.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0113.25 16H2.75A1.75 1.75 0 011 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 014.75 0zm0 3.5h8.5a.25.25 0 01.25.25V6h-11V3.75a.25.25 0 01.25-.25h2zm-2.25 4v6.75c0 .138.112.25.25.25h10.5a.25.25 0 00.25-.25V7.5h-11z"></path></svg> Upcoming</a></li>
<li><a href="/upcoming/free/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-gift" aria-hidden="true"><path fill-rule="evenodd" d="M4.75 1.5a1.25 1.25 0 100 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707zM2 2.75c0 .45.108.875.3 1.25h-.55A1.75 1.75 0 000 5.75v2c0 .698.409 1.3 1 1.582v4.918c0 .966.784 1.75 1.75 1.75h10.5A1.75 1.75 0 0015 14.25V9.332c.591-.281 1-.884 1-1.582v-2A1.75 1.75 0 0014.25 4h-.55a2.75 2.75 0 00-2.45-4c-.984 0-1.874.42-2.57 1.23A5.086 5.086 0 008 2.274a5.086 5.086 0 00-.68-1.042C6.623.42 5.733 0 4.75 0A2.75 2.75 0 002 2.75zM8.941 4h2.309a1.25 1.25 0 100-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793zm-1.84 1.5H1.75a.25.25 0 00-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-.149zm1.649 0V8h5.5a.25.25 0 00.25-.25v-2a.25.25 0 00-.25-.25h-5.5zm0 4h4.75v4.75a.25.25 0 01-.25.25h-4.5v-5zm-1.5 0v5h-4.5a.25.25 0 01-.25-.25V9.5h4.75z"></path></svg> Free Promotions</a></li>
</ul>
<ul>
<li><a href="/stats/gameratings/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-graph" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path></svg> Top Rated Games</a></li>
<li><a href="/badge/13/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-play" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path></svg> Top Game Owners</a></li>
<li><a href="/stats/toplevels/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-people" aria-hidden="true"><path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path></svg> Top Steam Levels</a></li>
<li><a href="/topsellers/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-credit-card" aria-hidden="true"><path d="M10.75 9a.75.75 0 000 1.5h1.5a.75.75 0 000-1.5h-1.5z"></path><path fill-rule="evenodd" d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0114.25 14H1.75A1.75 1.75 0 010 12.25v-8.5zm14.5 0V5h-13V3.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25zm0 2.75h-13v5.75c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V6.5z"></path></svg> Top Selling Games</a></li>
<li><a href="/badges/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-bookmark" aria-hidden="true"><path fill-rule="evenodd" d="M4.75 2.5a.25.25 0 00-.25.25v9.91l3.023-2.489a.75.75 0 01.954 0l3.023 2.49V2.75a.25.25 0 00-.25-.25h-6.5zM3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 01-1.227.579L8 11.722l-3.773 3.107A.75.75 0 013 14.25V2.75z"></path></svg> Badges</a></li>
</ul>
<ul>
<li><a href="/freepackages/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-gift" aria-hidden="true"><path fill-rule="evenodd" d="M4.75 1.5a1.25 1.25 0 100 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707zM2 2.75c0 .45.108.875.3 1.25h-.55A1.75 1.75 0 000 5.75v2c0 .698.409 1.3 1 1.582v4.918c0 .966.784 1.75 1.75 1.75h10.5A1.75 1.75 0 0015 14.25V9.332c.591-.281 1-.884 1-1.582v-2A1.75 1.75 0 0014.25 4h-.55a2.75 2.75 0 00-2.45-4c-.984 0-1.874.42-2.57 1.23A5.086 5.086 0 008 2.274a5.086 5.086 0 00-.68-1.042C6.623.42 5.733 0 4.75 0A2.75 2.75 0 002 2.75zM8.941 4h2.309a1.25 1.25 0 100-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793zm-1.84 1.5H1.75a.25.25 0 00-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-.149zm1.649 0V8h5.5a.25.25 0 00.25-.25v-2a.25.25 0 00-.25-.25h-5.5zm0 4h4.75v4.75a.25.25 0 01-.25.25h-4.5v-5zm-1.5 0v5h-4.5a.25.25 0 01-.25-.25V9.5h4.75z"></path></svg> Free Packages</a></li>
<li><a href="/login/?page=tags"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-sign-in" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm6.56 4.5l1.97-1.97a.75.75 0 10-1.06-1.06L6.22 7.47a.75.75 0 000 1.06l3.25 3.25a.75.75 0 101.06-1.06L8.56 8.75h5.69a.75.75 0 000-1.5H8.56z"></path></svg> Sign in via Steam</a></li>
<li><a href="https://steamstat.us/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-sun" aria-hidden="true"><path fill-rule="evenodd" d="M8 10.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5zM8 12a4 4 0 100-8 4 4 0 000 8zM8 0a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0V.75A.75.75 0 018 0zm0 13a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5A.75.75 0 018 13zM2.343 2.343a.75.75 0 011.061 0l1.06 1.061a.75.75 0 01-1.06 1.06l-1.06-1.06a.75.75 0 010-1.06zm9.193 9.193a.75.75 0 011.06 0l1.061 1.06a.75.75 0 01-1.06 1.061l-1.061-1.06a.75.75 0 010-1.061zM16 8a.75.75 0 01-.75.75h-1.5a.75.75 0 010-1.5h1.5A.75.75 0 0116 8zM3 8a.75.75 0 01-.75.75H.75a.75.75 0 010-1.5h1.5A.75.75 0 013 8zm10.657-5.657a.75.75 0 010 1.061l-1.061 1.06a.75.75 0 11-1.06-1.06l1.06-1.06a.75.75 0 011.06 0zm-9.193 9.193a.75.75 0 010 1.06l-1.06 1.061a.75.75 0 11-1.061-1.06l1.06-1.061a.75.75 0 011.061 0z"></path></svg> Steam Status</a></li>
<li><a href="https://steamapi.xpaw.me/"><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-telescope" aria-hidden="true"><path fill-rule="evenodd" d="M14.184 1.143a1.75 1.75 0 00-2.502-.57L.912 7.916a1.75 1.75 0 00-.53 2.32l.447.775a1.75 1.75 0 002.275.702l11.745-5.656a1.75 1.75 0 00.757-2.451l-1.422-2.464zm-1.657.669a.25.25 0 01.358.081l1.422 2.464a.25.25 0 01-.108.35l-2.016.97-1.505-2.605 1.85-1.26zM9.436 3.92l1.391 2.41-5.42 2.61-.942-1.63 4.97-3.39zM3.222 8.157l-1.466 1a.25.25 0 00-.075.33l.447.775a.25.25 0 00.325.1l1.598-.769-.83-1.436zm6.253 2.306a.75.75 0 00-.944-.252l-1.809.87a.75.75 0 00-.293.253L4.38 14.326a.75.75 0 101.238.848l1.881-2.75v2.826a.75.75 0 001.5 0v-2.826l1.881 2.75a.75.75 0 001.238-.848l-2.644-3.863z"></path></svg> Steam Web API</a></li>
</ul>
<div class="header-disclaimer">SteamDB is a community website and is not affiliated with Valve or Steam. All times on the site are UTC.</div >
</div>
</div>
</div>
<script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" integrity="sha512-DUdMb4bmDtpcKC2s1cO+j0zokQtXteSEGLy27Cnf3dr/L5RapKECOPy+tb6x5XoU0taqXvBLDMtEbZ1WQQAd6A==" src="/static/js/global.js?v=0d474c6f86e60eda"></script>
<div class="header-wrapper">
<div class="container">
<h1 class="header-title">All Steam Game Tags</h1>
<h2 class="header-subtitle">Tags help <a href="https://partner.steamgames.com/doc/store/tags">Steam determine</a> where games are displayed to customers.</h2>
</div>
</div>
<style>
.label {
display: inline-block;
height: 34px;
padding: 0 10px;
font-size: 16px;
font-weight: bold;
line-height: 34px;
border-radius: 6px;
color: #FFF;
overflow: hidden;
text-overflow: ellipsis;
max-width: 190px;
white-space: nowrap;
box-shadow: inset 0 -2px 0 rgba(0, 0, 0, 0.2);
}
.label-count {
line-height: 34px;
}
.label:hover {
color: #FFF;
 opacity: 0.85;
}
.label-color-0 { background-color: #00BCD4; }
.label-color-1 { background-color: #03A9F4; }
.label-color-2 { background-color: #3F51B5; }
.label-color-3 { background-color: #4CAF50; }
.label-color-4 { background-color: #9C27B0; }
.label-color-5 { background-color: #558B2F; }
.label-color-6 { background-color: #607D8B; }
.label-color-7 { background-color: #673AB7; }
.label-color-8 { background-color: #2196F3; }
.label-color-9 { background-color: #009688; }
.label-color-10 { background-color: #E91E63; }
.label-color-11 { background-color: #EF6C00; }
.label-color-12 { background-color: #F44336; }
.label-color-13 { background-color: #FF5722; }
</style>
<div class="container">
<div id="list">
<div class="row">
<div class="span12">
<input class="input-block search" type="text" placeholder="Search">
<br>
</div>
</div>
<div class="row list">
<div class="span4">
<span class="label-count pull-right muted">49175 products</span>
<a class="label label-link label-color-0" href="/tag/492/">Indie</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">34698 products</span>
<a class="label label-link label-color-1" href="/tag/19/">Action</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">32187 products</span>
<a class="label label-link label-color-2" href="/tag/1003823/">Low Confidence Metric</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">28727 products</span>
<a class="label label-link label-color-3" href="/tag/21/">Adventure</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">28590 products</span>
<a class="label label-link label-color-4" href="/tag/597/">Casual</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">20170 products</span>
<a class="label label-link label-color-5" href="/tag/4182/">Singleplayer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">19643 products</span>
<a class="label label-link label-color-6" href="/tag/599/">Simulation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">18128 products</span>
<a class="label label-link label-color-7" href="/tag/9/">Strategy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">16647 products</span>
<a class="label label-link label-color-8" href="/tag/122/">RPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">10087 products</span>
<a class="label label-link label-color-9" href="/tag/3871/">2D</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">7780 products</span>
<a class="label label-link label-color-10" href="/tag/4166/">Atmospheric</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">7657 products</span>
<a class="label label-link label-color-11" href="/tag/113/">Free to Play</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">7502 products</span>
<a class="label label-link label-color-12" href="/tag/1664/">Puzzle</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">7379 products</span>
<a class="label label-link label-color-13" href="/tag/493/">Early Access</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">6656 products</span>
<a class="label label-link label-color-0" href="/tag/3859/">Multiplayer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">6285 products</span>
<a class="label label-link label-color-1" href="/tag/1742/">Story Rich</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5880 products</span>
<a class="label label-link label-color-2" href="/tag/4667/">Violent</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5811 products</span>
<a class="label label-link label-color-3" href="/tag/1684/">Fantasy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5492 products</span>
<a class="label label-link label-color-4" href="/tag/1756/">Great Soundtrack</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5400 products</span>
<a class="label label-link label-color-5" href="/tag/4085/">Anime</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5252 products</span>
<a class="label label-link label-color-6" href="/tag/3964/">Pixel Graphics</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5144 products</span>
<a class="label label-link label-color-7" href="/tag/6650/">Nudity</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">5029 products</span>
<a class="label label-link label-color-8" href="/tag/21978/">VR</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4897 products</span>
<a class="label label-link label-color-9" href="/tag/12095/">Sexual Content</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4819 products</span>
<a class="label label-link label-color-10" href="/tag/3839/">First-Person</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4673 products</span>
<a class="label label-link label-color-11" href="/tag/4345/">Gore</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4629 products</span>
<a class="label label-link label-color-12" href="/tag/4136/">Funny</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4513 products</span>
<a class="label label-link label-color-13" href="/tag/3942/">Sci-fi</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4443 products</span>
<a class="label label-link label-color-0" href="/tag/1773/">Arcade</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4405 products</span>
<a class="label label-link label-color-1" href="/tag/1667/">Horror</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4365 products</span>
<a class="label label-link label-color-2" href="/tag/4026/">Difficult</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4327 products</span>
<a class="label label-link label-color-3" href="/tag/4726/">Cute</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4315 products</span>
<a class="label label-link label-color-4" href="/tag/1774/">Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4244 products</span>
<a class="label label-link label-color-5" href="/tag/701/">Sports</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4177 products</span>
<a class="label label-link label-color-6" href="/tag/4305/">Colorful</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4170 products</span>
<a class="label label-link label-color-7" href="/tag/1625/">Platformer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">4108 products</span>
<a class="label label-link label-color-8" href="/tag/4004/">Retro</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3866 products</span>
<a class="label label-link label-color-9" href="/tag/3834/">Exploration</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3830 products</span>
<a class="label label-link label-color-10" href="/tag/5350/">Family Friendly</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3657 products</span>
<a class="label label-link label-color-11" href="/tag/4191/">3D</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3502 products</span>
<a class="label label-link label-color-12" href="/tag/1695/">Open World</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3441 products</span>
<a class="label label-link label-color-13" href="/tag/7208/">Female Protagonist</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3428 products</span>
<a class="label label-link label-color-0" href="/tag/1685/">Co-op</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3371 products</span>
<a class="label label-link label-color-1" href="/tag/1654/">Relaxing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3343 products</span>
<a class="label label-link label-color-2" href="/tag/1662/">Survival</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3324 products</span>
<a class="label label-link label-color-3" href="/tag/128/">Massively Multiplayer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3309 products</span>
<a class="label label-link label-color-4" href="/tag/699/">Racing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3244 products</span>
<a class="label label-link label-color-5" href="/tag/3799/">Visual Novel</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3062 products</span>
<a class="label label-link label-color-6" href="/tag/1663/">FPS</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">3043 products</span>
<a class="label label-link label-color-7" href="/tag/1677/">Turn-Based</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2989 products</span>
<a class="label label-link label-color-8" href="/tag/1719/">Comedy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2610 products</span>
<a class="label label-link label-color-9" href="/tag/3843/">Online Co-Op</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2587 products</span>
<a class="label label-link label-color-10" href="/tag/1697/">Third Person</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2523 products</span>
<a class="label label-link label-color-11" href="/tag/3810/">Sandbox</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2489 products</span>
<a class="label label-link label-color-12" href="/tag/4106/">Action-Adventure</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2365 products</span>
<a class="label label-link label-color-13" href="/tag/4175/">Realistic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2359 products</span>
<a class="label label-link label-color-0" href="/tag/3968/">Physics</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2339 products</span>
<a class="label label-link label-color-1" href="/tag/1698/">Point & Click</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2251 products</span>
<a class="label label-link label-color-2" href="/tag/1755/">Space</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2117 products</span>
<a class="label label-link label-color-3" href="/tag/4791/">Top-Down</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2105 products</span>
<a class="label label-link label-color-4" href="/tag/5716/">Mystery</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2080 products</span>
<a class="label label-link label-color-5" href="/tag/6426/">Choices Matter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2078 products</span>
<a class="label label-link label-color-6" href="/tag/4711/">Replay Value</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2041 products</span>
<a class="label label-link label-color-7" href="/tag/1721/">Psychological Horror</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2035 products</span>
<a class="label label-link label-color-8" href="/tag/12472/">Management</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2029 products</span>
<a class="label label-link label-color-9" href="/tag/65443/">Adult Content</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2022 products</span>
<a class="label label-link label-color-10" href="/tag/1775/">PvP</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">2005 products</span>
<a class="label label-link label-color-11" href="/tag/4252/">Stylized</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1941 products</span>
<a class="label label-link label-color-12" href="/tag/7368/">Local Multiplayer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1922 products</span>
<a class="label label-link label-color-13" href="/tag/1643/">Building</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1892 products</span>
<a class="label label-link label-color-0" href="/tag/4094/">Minimalist</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1856 products</span>
<a class="label label-link label-color-1" href="/tag/1708/">Tactical</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1850 products</span>
<a class="label label-link label-color-2" href="/tag/4342/">Dark</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1814 products</span>
<a class="label label-link label-color-3" href="/tag/84/">Design & Illustration</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1786 products</span>
<a class="label label-link label-color-4" href="/tag/4195/">Cartoony</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1762 products</span>
<a class="label label-link label-color-5" href="/tag/3798/">Side Scroller</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1664 products</span>
<a class="label label-link label-color-6" href="/tag/4255/">Shoot 'Em Up</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1662 products</span>
<a class="label label-link label-color-7" href="/tag/5537/">Puzzle-Platformer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1658 products</span>
<a class="label label-link label-color-8" href="/tag/8013/">Software</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1657 products</span>
<a class="label label-link label-color-9" href="/tag/1693/">Classic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1646 products</span>
<a class="label label-link label-color-10" href="/tag/6971/">Multiple Endings</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1605 products</span>
<a class="label label-link label-color-11" href="/tag/10695/">Party-Based RPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1569 products</span>
<a class="label label-link label-color-12" href="/tag/1036/">Education</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1560 products</span>
<a class="label label-link label-color-13" href="/tag/3916/">Old School</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1555 products</span>
<a class="label label-link label-color-0" href="/tag/1716/">Rogue-like</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1540 products</span>
<a class="label label-link label-color-1" href="/tag/87/">Utilities</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1534 products</span>
<a class="label label-link label-color-2" href="/tag/1741/">Turn-Based Strategy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1512 products</span>
<a class="label label-link label-color-3" href="/tag/3841/">Local Co-Op</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1511 products</span>
<a class="label label-link label-color-4" href="/tag/5379/">2D Platformer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1500 products</span>
<a class="label label-link label-color-5" href="/tag/3978/">Survival Horror</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1498 products</span>
<a class="label label-link label-color-6" href="/tag/4700/">Movie</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1496 products</span>
<a class="label label-link label-color-7" href="/tag/4747/">Character Customization</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1489 products</span>
<a class="label label-link label-color-8" href="/tag/5611/">Mature</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1477 products</span>
<a class="label label-link label-color-9" href="/tag/1734/">Fast-Paced</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1453 products</span>
<a class="label label-link label-color-10" href="/tag/4231/">Action RPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1445 products</span>
<a class="label label-link label-color-11" href="/tag/4234/">Short</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1422 products</span>
<a class="label label-link label-color-12" href="/tag/3959/">Rogue-lite</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1421 products</span>
<a class="label label-link label-color-13" href="/tag/1659/">Zombies</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1389 products</span>
<a class="label label-link label-color-0" href="/tag/7481/">Controller</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1326 products</span>
<a class="label label-link label-color-1" href="/tag/6815/">Hand-drawn</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1319 products</span>
<a class="label label-link label-color-2" href="/tag/5125/">Procedural Generation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1313 products</span>
<a class="label label-link label-color-3" href="/tag/4434/">JRPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1306 products</span>
<a class="label label-link label-color-4" href="/tag/1702/">Crafting</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1304 products</span>
<a class="label label-link label-color-5" href="/tag/1738/">Hidden Object</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1294 products</span>
<a class="label label-link label-color-6" href="/tag/5577/">RPGMaker</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1272 products</span>
<a class="label label-link label-color-7" href="/tag/3987/">Historical</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1240 products</span>
<a class="label label-link label-color-8" href="/tag/1678/">War</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1229 products</span>
<a class="label label-link label-color-9" href="/tag/4885/">Bullet Hell</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1219 products</span>
<a class="label label-link label-color-10" href="/tag/1646/">Hack and Slash</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1219 products</span>
<a class="label label-link label-color-11" href="/tag/3993/">Combat</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1219 products</span>
<a class="label label-link label-color-12" href="/tag/4325/">Turn-Based Combat</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1216 products</span>
<a class="label label-link label-color-13" href="/tag/10397/">Memes</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1187 products</span>
<a class="label label-link label-color-0" href="/tag/1676/">RTS</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1184 products</span>
<a class="label label-link label-color-1" href="/tag/1038/">Web Publishing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1183 products</span>
<a class="label label-link label-color-2" href="/tag/4057/">Magic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1177 products</span>
<a class="label label-link label-color-3" href="/tag/4172/">Medieval</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1172 products</span>
<a class="label label-link label-color-4" href="/tag/4947/">Romance</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1166 products</span>
<a class="label label-link label-color-5" href="/tag/13782/">Experimental</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1165 products</span>
<a class="label label-link label-color-6" href="/tag/4295/">Futuristic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1156 products</span>
<a class="label label-link label-color-7" href="/tag/8945/">Resource Management</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1110 products</span>
<a class="label label-link label-color-8" href="/tag/1687/">Stealth</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1100 products</span>
<a class="label label-link label-color-9" href="/tag/4562/">Cartoon</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1097 products</span>
<a class="label label-link label-color-10" href="/tag/1743/">Fighting</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1091 products</span>
<a class="label label-link label-color-11" href="/tag/1621/">Music</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1083 products</span>
<a class="label label-link label-color-12" href="/tag/5900/">Walking Simulator</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1064 products</span>
<a class="label label-link label-color-13" href="/tag/14139/">Turn-Based Tactics</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1057 products</span>
<a class="label label-link label-color-0" href="/tag/1720/">Dungeon Crawler</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1052 products</span>
<a class="label label-link label-color-1" href="/tag/5395/">3D Platformer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1052 products</span>
<a class="label label-link label-color-2" href="/tag/4486/">Choose Your Own Adventure</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1043 products</span>
<a class="label label-link label-color-3" href="/tag/6730/">PvE</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1037 products</span>
<a class="label label-link label-color-4" href="/tag/6129/">Logic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1034 products</span>
<a class="label label-link label-color-5" href="/tag/3835/">Post-apocalyptic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1025 products</span>
<a class="label label-link label-color-6" href="/tag/9551/">Dating Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1022 products</span>
<a class="label label-link label-color-7" href="/tag/5411/">Beautiful</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1019 products</span>
<a class="label label-link label-color-8" href="/tag/4637/">Top-Down Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1009 products</span>
<a class="label label-link label-color-9" href="/tag/11014/">Interactive Fiction</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">1001 products</span>
<a class="label label-link label-color-10" href="/tag/4604/">Dark Fantasy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">999 products</span>
<a class="label label-link label-color-11" href="/tag/5851/">Isometric</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">989 products</span>
<a class="label label-link label-color-12" href="/tag/7332/">Base Building</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">984 products</span>
<a class="label label-link label-color-13" href="/tag/5984/">Drama</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">981 products</span>
<a class="label label-link label-color-0" href="/tag/7250/">Linear</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">974 products</span>
<a class="label label-link label-color-1" href="/tag/1666/">Card Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">972 products</span>
<a class="label label-link label-color-2" href="/tag/1710/">Surreal</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">934 products</span>
<a class="label label-link label-color-3" href="/tag/3878/">Competitive</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">925 products</span>
<a class="label label-link label-color-4" href="/tag/4840/">4 Player Local</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">906 products</span>
<a class="label label-link label-color-5" href="/tag/4168/">Military</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">899 products</span>
<a class="label label-link label-color-6" href="/tag/1644/">Driving</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">890 products</span>
<a class="label label-link label-color-7" href="/tag/4115/">Cyberpunk</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">890 products</span>
<a class="label label-link label-color-8" href="/tag/31275/">Text-Based</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">890 products</span>
<a class="label label-link label-color-9" href="/tag/1645/">Tower Defense</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">869 products</span>
<a class="label label-link label-color-10" href="/tag/3814/">Third-Person Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">864 products</span>
<a class="label label-link label-color-11" href="/tag/7948/">Soundtrack</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">838 products</span>
<a class="label label-link label-color-12" href="/tag/4695/">Economy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">832 products</span>
<a class="label label-link label-color-13" href="/tag/5154/">Score Attack</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">831 products</span>
<a class="label label-link label-color-0" href="/tag/15045/">Flight</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">818 products</span>
<a class="label label-link label-color-1" href="/tag/1770/">Board Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">815 products</span>
<a class="label label-link label-color-2" href="/tag/5752/">Robots</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">804 products</span>
<a class="label label-link label-color-3" href="/tag/5094/">Narration</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">779 products</span>
<a class="label label-link label-color-4" href="/tag/6691/">1990's</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">776 products</span>
<a class="label label-link label-color-5" href="/tag/4975/">2.5D</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">771 products</span>
<a class="label label-link label-color-6" href="/tag/42804/">Action Roguelike</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">771 products</span>
<a class="label label-link label-color-7" href="/tag/4400/">Abstract</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">752 products</span>
<a class="label label-link label-color-8" href="/tag/9130/">Hentai</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">743 products</span>
<a class="label label-link label-color-9" href="/tag/4328/">City Builder</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">742 products</span>
<a class="label label-link label-color-10" href="/tag/44868/">LGBTQ+</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">738 products</span>
<a class="label label-link label-color-11" href="/tag/5923/">Dark Humor</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">723 products</span>
<a class="label label-link label-color-12" href="/tag/1673/">Aliens</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">720 products</span>
<a class="label label-link label-color-13" href="/tag/1628/">Metroidvania</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">712 products</span>
<a class="label label-link label-color-0" href="/tag/872/">Animation & Modeling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">707 products</span>
<a class="label label-link label-color-1" href="/tag/5613/">Detective</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">707 products</span>
<a class="label label-link label-color-2" href="/tag/1669/">Moddable</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">696 products</span>
<a class="label label-link label-color-3" href="/tag/1759/">Perma Death</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">691 products</span>
<a class="label label-link label-color-4" href="/tag/4158/">Beat 'em up</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">681 products</span>
<a class="label label-link label-color-5" href="/tag/3955/">Character Action Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">680 products</span>
<a class="label label-link label-color-6" href="/tag/7743/">1980s</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">659 products</span>
<a class="label label-link label-color-7" href="/tag/5711/">Team-Based</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">651 products</span>
<a class="label label-link label-color-8" href="/tag/17389/">Tabletop</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">631 products</span>
<a class="label label-link label-color-9" href="/tag/5547/">Arena Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">630 products</span>
<a class="label label-link label-color-10" href="/tag/16689/">Time Management</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">628 products</span>
<a class="label label-link label-color-11" href="/tag/8369/">Investigation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">604 products</span>
<a class="label label-link label-color-12" href="/tag/4064/">Thriller</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">593 products</span>
<a class="label label-link label-color-13" href="/tag/8122/">Level Editor</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">591 products</span>
<a class="label label-link label-color-0" href="/tag/24904/">NSFW</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">591 products</span>
<a class="label label-link label-color-1" href="/tag/4758/">Twin Stick Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">591 products</span>
<a class="label label-link label-color-2" href="/tag/4150/">World War II</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">582 products</span>
<a class="label label-link label-color-3" href="/tag/3813/">Real Time Tactics</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">579 products</span>
<a class="label label-link label-color-4" href="/tag/1100687/">Automobile Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">574 products</span>
<a class="label label-link label-color-5" href="/tag/30358/">Nature</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">571 products</span>
<a class="label label-link label-color-6" href="/tag/1027/">Audio Production</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">565 products</span>
<a class="label label-link label-color-7" href="/tag/4145/">Cinematic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">558 products</span>
<a class="label label-link label-color-8" href="/tag/5608/">Emotional</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">557 products</span>
<a class="label label-link label-color-9" href="/tag/5186/">Psychological</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">556 products</span>
<a class="label label-link label-color-10" href="/tag/379975/">Clicker</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">555 products</span>
<a class="label label-link label-color-11" href="/tag/17305/">Strategy RPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">554 products</span>
<a class="label label-link label-color-12" href="/tag/4684/">Wargame</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">539 products</span>
<a class="label label-link label-color-13" href="/tag/5363/">Destruction</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">536 products</span>
<a class="label label-link label-color-0" href="/tag/13906/">Game Development</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">526 products</span>
<a class="label label-link label-color-1" href="/tag/9204/">Immersive Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">514 products</span>
<a class="label label-link label-color-2" href="/tag/12057/">Tutorial</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">511 products</span>
<a class="label label-link label-color-3" href="/tag/4364/">Grand Strategy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">507 products</span>
<a class="label label-link label-color-4" href="/tag/3877/">Precision Platformer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">507 products</span>
<a class="label label-link label-color-5" href="/tag/1714/">Psychedelic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">501 products</span>
<a class="label label-link label-color-6" href="/tag/21725/">Tactical RPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">498 products</span>
<a class="label label-link label-color-7" href="/tag/6378/">Crime</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">493 products</span>
<a class="label label-link label-color-8" href="/tag/4190/">Addictive</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">483 products</span>
<a class="label label-link label-color-9" href="/tag/10235/">Life Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">480 products</span>
<a class="label label-link label-color-10" href="/tag/1752/">Rhythm</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">475 products</span>
<a class="label label-link label-color-11" href="/tag/1665/">Match 3</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">468 products</span>
<a class="label label-link label-color-12" href="/tag/784/">Video Production</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">464 products</span>
<a class="label label-link label-color-13" href="/tag/9541/">Demons</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">463 products</span>
<a class="label label-link label-color-0" href="/tag/15172/">Conversation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">461 products</span>
<a class="label label-link label-color-1" href="/tag/4236/">Loot</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">460 products</span>
<a class="label label-link label-color-2" href="/tag/4598/">Alternate History</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">459 products</span>
<a class="label label-link label-color-3" href="/tag/4736/">2D Fighter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">454 products</span>
<a class="label label-link label-color-4" href="/tag/4242/">Episodic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">453 products</span>
<a class="label label-link label-color-5" href="/tag/4036/">Parkour</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">453 products</span>
<a class="label label-link label-color-6" href="/tag/5030/">Dystopian </a>
</div>
<div class="span4">
<span class="label-count pull-right muted">451 products</span>
<a class="label label-link label-color-7" href="/tag/1754/">MMORPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">440 products</span>
<a class="label label-link label-color-8" href="/tag/1751/">Comic Book</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">436 products</span>
<a class="label label-link label-color-9" href="/tag/5673/">Modern</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">432 products</span>
<a class="label label-link label-color-10" href="/tag/11123/">Mouse only</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">428 products</span>
<a class="label label-link label-color-11" href="/tag/8666/">Runner</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">426 products</span>
<a class="label label-link label-color-12" href="/tag/16598/">Space Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">423 products</span>
<a class="label label-link label-color-13" href="/tag/4161/">Real-Time</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">418 products</span>
<a class="label label-link label-color-0" href="/tag/1445/">Software Training</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">415 products</span>
<a class="label label-link label-color-1" href="/tag/1100689/">Open World Survival Craft</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">411 products</span>
<a class="label label-link label-color-2" href="/tag/6869/">Nonlinear</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">405 products</span>
<a class="label label-link label-color-3" href="/tag/19995/">Dark Comedy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">400 products</span>
<a class="label label-link label-color-4" href="/tag/7432/">Lovecraftian</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">392 products</span>
<a class="label label-link label-color-5" href="/tag/5794/">Science</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">388 products</span>
<a class="label label-link label-color-6" href="/tag/4474/">CRPG</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">379 products</span>
<a class="label label-link label-color-7" href="/tag/10808/">Supernatural</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">379 products</span>
<a class="label label-link label-color-8" href="/tag/6276/">Inventory Management</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">376 products</span>
<a class="label label-link label-color-9" href="/tag/10816/">Split Screen</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">370 products</span>
<a class="label label-link label-color-10" href="/tag/5228/">Blood</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">369 products</span>
<a class="label label-link label-color-11" href="/tag/29482/">Souls-like</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">353 products</span>
<a class="label label-link label-color-12" href="/tag/7782/">Cult Classic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">350 products</span>
<a class="label label-link label-color-13" href="/tag/1777/">Steampunk</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">336 products</span>
<a class="label label-link label-color-0" href="/tag/3854/">Lore-Rich</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">335 products</span>
<a class="label label-link label-color-1" href="/tag/1732/">Voxel</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">328 products</span>
<a class="label label-link label-color-2" href="/tag/7926/">Artificial Intelligence</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">328 products</span>
<a class="label label-link label-color-3" href="/tag/6052/">Noir</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">327 products</span>
<a class="label label-link label-color-4" href="/tag/16094/">Mythology</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">326 products</span>
<a class="label label-link label-color-5" href="/tag/4821/">Mechs</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">323 products</span>
<a class="label label-link label-color-6" href="/tag/4608/">Swordplay</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">320 products</span>
<a class="label label-link label-color-7" href="/tag/32322/">Deckbuilding</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">316 products</span>
<a class="label label-link label-color-8" href="/tag/15277/">Philosophical</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">312 products</span>
<a class="label label-link label-color-9" href="/tag/176981/">Battle Royale</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">310 products</span>
<a class="label label-link label-color-10" href="/tag/5055/">eSports</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">307 products</span>
<a class="label label-link label-color-11" href="/tag/7569/">Grid-Based Movement</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">306 products</span>
<a class="label label-link label-color-12" href="/tag/1670/">4X</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">305 products</span>
<a class="label label-link label-color-13" href="/tag/4046/">Dragons</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">302 products</span>
<a class="label label-link label-color-0" href="/tag/1616/">Trains</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">299 products</span>
<a class="label label-link label-color-1" href="/tag/791774/">Card Battler</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">298 products</span>
<a class="label label-link label-color-2" href="/tag/13276/">Tanks</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">298 products</span>
<a class="label label-link label-color-3" href="/tag/17894/">Cats</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">291 products</span>
<a class="label label-link label-color-4" href="/tag/4853/">Political</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">288 products</span>
<a class="label label-link label-color-5" href="/tag/1681/">Pirates</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">275 products</span>
<a class="label label-link label-color-6" href="/tag/7107/">Real-Time with Pause</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">273 products</span>
<a class="label label-link label-color-7" href="/tag/809/">Photo Editing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">273 products</span>
<a class="label label-link label-color-8" href="/tag/4878/">Parody </a>
</div>
<div class="span4">
<span class="label-count pull-right muted">270 products</span>
<a class="label label-link label-color-9" href="/tag/4835/">6DOF</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">268 products</span>
<a class="label label-link label-color-10" href="/tag/31579/">Otome</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">266 products</span>
<a class="label label-link label-color-11" href="/tag/5708/">Remake</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">264 products</span>
<a class="label label-link label-color-12" href="/tag/1717/">Hex Grid</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">257 products</span>
<a class="label label-link label-color-13" href="/tag/5796/">Bullet Time</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">253 products</span>
<a class="label label-link label-color-0" href="/tag/5502/">Hacking</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">252 products</span>
<a class="label label-link label-color-1" href="/tag/220585/">Colony Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">249 products</span>
<a class="label label-link label-color-2" href="/tag/4508/">Co-op Campaign</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">247 products</span>
<a class="label label-link label-color-3" href="/tag/4202/">Trading</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">247 products</span>
<a class="label label-link label-color-4" href="/tag/6910/">Naval</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">245 products</span>
<a class="label label-link label-color-5" href="/tag/1688/">Ninja</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">242 products</span>
<a class="label label-link label-color-6" href="/tag/1651/">Satire</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">240 products</span>
<a class="label label-link label-color-7" href="/tag/5652/">Collectathon</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">239 products</span>
<a class="label label-link label-color-8" href="/tag/1647/">Western</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">236 products</span>
<a class="label label-link label-color-9" href="/tag/1649/">GameMaker</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">236 products</span>
<a class="label label-link label-color-10" href="/tag/4155/">Class-Based</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">236 products</span>
<a class="label label-link label-color-11" href="/tag/1718/">MOBA</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">235 products</span>
<a class="label label-link label-color-12" href="/tag/87918/">Farming Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">231 products</span>
<a class="label label-link label-color-13" href="/tag/6625/">Time Manipulation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">228 products</span>
<a class="label label-link label-color-0" href="/tag/24003/">Word Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">228 products</span>
<a class="label label-link label-color-1" href="/tag/5153/">Kickstarter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">226 products</span>
<a class="label label-link label-color-2" href="/tag/5160/">Dinosaurs</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">226 products</span>
<a class="label label-link label-color-3" href="/tag/14153/">Dungeons & Dragons</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">225 products</span>
<a class="label label-link label-color-4" href="/tag/22602/">Agriculture</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">224 products</span>
<a class="label label-link label-color-5" href="/tag/25085/">Touch-Friendly</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">224 products</span>
<a class="label label-link label-color-6" href="/tag/4754/">Politics</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">222 products</span>
<a class="label label-link label-color-7" href="/tag/11104/">Vehicular Combat</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">221 products</span>
<a class="label label-link label-color-8" href="/tag/10679/">Time Travel</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">219 products</span>
<a class="label label-link label-color-9" href="/tag/5981/">Mining</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">218 products</span>
<a class="label label-link label-color-10" href="/tag/3952/">Gothic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">218 products</span>
<a class="label label-link label-color-11" href="/tag/13190/">America</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">216 products</span>
<a class="label label-link label-color-12" href="/tag/9564/">Hunting</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">215 products</span>
<a class="label label-link label-color-13" href="/tag/5300/">God Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">215 products</span>
<a class="label label-link label-color-0" href="/tag/7478/">Illuminati</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">213 products</span>
<a class="label label-link label-color-1" href="/tag/29363/">3D Vision</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">206 products</span>
<a class="label label-link label-color-2" href="/tag/9157/">Underwater</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">205 products</span>
<a class="label label-link label-color-3" href="/tag/5765/">Gun Customization</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">205 products</span>
<a class="label label-link label-color-4" href="/tag/4845/">Capitalism</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">201 products</span>
<a class="label label-link label-color-5" href="/tag/5432/">Programming</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">200 products</span>
<a class="label label-link label-color-6" href="/tag/15339/">Documentary</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">200 products</span>
<a class="label label-link label-color-7" href="/tag/6506/">3D Fighter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">196 products</span>
<a class="label label-link label-color-8" href="/tag/1671/">Superhero</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">194 products</span>
<a class="label label-link label-color-9" href="/tag/6915/">Martial Arts</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">192 products</span>
<a class="label label-link label-color-10" href="/tag/18594/">FMV</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">191 products</span>
<a class="label label-link label-color-11" href="/tag/9271/">Trading Card Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">190 products</span>
<a class="label label-link label-color-12" href="/tag/198631/">Mystery Dungeon</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">187 products</span>
<a class="label label-link label-color-13" href="/tag/9994/">Experience</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">185 products</span>
<a class="label label-link label-color-0" href="/tag/615955/">Idler</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">183 products</span>
<a class="label label-link label-color-1" href="/tag/15564/">Fishing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">181 products</span>
<a class="label label-link label-color-2" href="/tag/5179/">Cold War</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">181 products</span>
<a class="label label-link label-color-3" href="/tag/4102/">Combat Racing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">176 products</span>
<a class="label label-link label-color-4" href="/tag/255534/">Automation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">173 products</span>
<a class="label label-link label-color-5" href="/tag/4777/">Spectacle fighter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">172 products</span>
<a class="label label-link label-color-6" href="/tag/8093/">Minigames</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">169 products</span>
<a class="label label-link label-color-7" href="/tag/13070/">Solitaire</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">169 products</span>
<a class="label label-link label-color-8" href="/tag/5372/">Conspiracy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">169 products</span>
<a class="label label-link label-color-9" href="/tag/1730/">Sokoban</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">169 products</span>
<a class="label label-link label-color-10" href="/tag/620519/">Hero Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">167 products</span>
<a class="label label-link label-color-11" href="/tag/4018/">Vampire</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">167 products</span>
<a class="label label-link label-color-12" href="/tag/1638/">Dog</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">164 products</span>
<a class="label label-link label-color-13" href="/tag/26921/">Political Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">163 products</span>
<a class="label label-link label-color-0" href="/tag/21006/">Underground</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">159 products</span>
<a class="label label-link label-color-1" href="/tag/5390/">Time Attack</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">156 products</span>
<a class="label label-link label-color-2" href="/tag/1679/">Soccer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">155 products</span>
<a class="label label-link label-color-3" href="/tag/180368/">Faith</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">155 products</span>
<a class="label label-link label-color-4" href="/tag/4376/">Assassin</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">154 products</span>
<a class="label label-link label-color-5" href="/tag/9592/">Dynamic Narration</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">151 products</span>
<a class="label label-link label-color-6" href="/tag/3965/">Epic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">150 products</span>
<a class="label label-link label-color-7" href="/tag/4994/">Naval Combat</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">150 products</span>
<a class="label label-link label-color-8" href="/tag/7226/">Football</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">149 products</span>
<a class="label label-link label-color-9" href="/tag/1680/">Heist</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">145 products</span>
<a class="label label-link label-color-10" href="/tag/4559/">Quick-Time Events</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">144 products</span>
<a class="label label-link label-color-11" href="/tag/8075/">TrackIR</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">143 products</span>
<a class="label label-link label-color-12" href="/tag/5348/">Mod</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">141 products</span>
<a class="label label-link label-color-13" href="/tag/17770/">Asynchronous Multiplayer</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">134 products</span>
<a class="label label-link label-color-0" href="/tag/6310/">Diplomacy</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">133 products</span>
<a class="label label-link label-color-1" href="/tag/8253/">Music-Based Procedural Generation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">129 products</span>
<a class="label label-link label-color-2" href="/tag/4184/">Chess</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">125 products</span>
<a class="label label-link label-color-3" href="/tag/353880/">Looter Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">125 products</span>
<a class="label label-link label-color-4" href="/tag/1674/">Typing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">122 products</span>
<a class="label label-link label-color-5" href="/tag/7113/">Crowdfunded</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">121 products</span>
<a class="label label-link label-color-6" href="/tag/7178/">Party Game</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">121 products</span>
<a class="label label-link label-color-7" href="/tag/13577/">Sailing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">120 products</span>
<a class="label label-link label-color-8" href="/tag/56690/">On-Rails Shooter</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">118 products</span>
<a class="label label-link label-color-9" href="/tag/11333/">Villain Protagonist</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">118 products</span>
<a class="label label-link label-color-10" href="/tag/7108/">Party</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">117 products</span>
<a class="label label-link label-color-11" href="/tag/13382/">Archery</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">115 products</span>
<a class="label label-link label-color-12" href="/tag/10383/">Transportation</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">113 products</span>
<a class="label label-link label-color-13" href="/tag/10437/">Trivia</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">113 products</span>
<a class="label label-link label-color-0" href="/tag/150626/">Gaming</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">112 products</span>
<a class="label label-link label-color-1" href="/tag/776177/">360 Video</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">110 products</span>
<a class="label label-link label-color-2" href="/tag/3934/">Immersive</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">110 products</span>
<a class="label label-link label-color-3" href="/tag/7702/">Narrative</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">109 products</span>
<a class="label label-link label-color-4" href="/tag/6621/">Pinball</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">108 products</span>
<a class="label label-link label-color-5" href="/tag/7622/">Offroad</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">108 products</span>
<a class="label label-link label-color-6" href="/tag/3796/">Based On A Novel</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">107 products</span>
<a class="label label-link label-color-7" href="/tag/15954/">Silent Protagonist</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">106 products</span>
<a class="label label-link label-color-8" href="/tag/5230/">Sequel</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">104 products</span>
<a class="label label-link label-color-9" href="/tag/5382/">World War I</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">102 products</span>
<a class="label label-link label-color-10" href="/tag/6702/">Mars</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">102 products</span>
<a class="label label-link label-color-11" href="/tag/6041/">Horses</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">102 products</span>
<a class="label label-link label-color-12" href="/tag/5310/">Games Workshop</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">100 products</span>
<a class="label label-link label-color-13" href="/tag/7423/">Sniper</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">96 products</span>
<a class="label label-link label-color-0" href="/tag/9803/">Snow</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">89 products</span>
<a class="label label-link label-color-1" href="/tag/1736/">LEGO</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">86 products</span>
<a class="label label-link label-color-2" href="/tag/6948/">Rome</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">86 products</span>
<a class="label label-link label-color-3" href="/tag/12286/">Warhammer 40K</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">85 products</span>
<a class="label label-link label-color-4" href="/tag/12190/">Boxing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">84 products</span>
<a class="label label-link label-color-5" href="/tag/1084988/">Auto Battler</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">84 products</span>
<a class="label label-link label-color-6" href="/tag/454187/">Traditional Roguelike</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">84 products</span>
<a class="label label-link label-color-7" href="/tag/916648/">Creature Collector</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">84 products</span>
<a class="label label-link label-color-8" href="/tag/16250/">Gambling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">81 products</span>
<a class="label label-link label-color-9" href="/tag/51306/">Foreign</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">80 products</span>
<a class="label label-link label-color-10" href="/tag/1091588/">Roguelike Deckbuilder</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">78 products</span>
<a class="label label-link label-color-11" href="/tag/1733/">Unforgiving</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">76 products</span>
<a class="label label-link label-color-12" href="/tag/7038/">Golf</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">76 products</span>
<a class="label label-link label-color-13" href="/tag/1100688/">Medical Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">75 products</span>
<a class="label label-link label-color-0" href="/tag/17015/">Werewolves</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">74 products</span>
<a class="label label-link label-color-1" href="/tag/4137/">Transhumanism</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">73 products</span>
<a class="label label-link label-color-2" href="/tag/198913/">Motorbike</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">63 products</span>
<a class="label label-link label-color-3" href="/tag/14720/">Nostalgia</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">63 products</span>
<a class="label label-link label-color-4" href="/tag/61357/">Electronic Music</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">61 products</span>
<a class="label label-link label-color-5" href="/tag/123332/">Bikes</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">61 products</span>
<a class="label label-link label-color-6" href="/tag/4520/">Farming</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">58 products</span>
<a class="label label-link label-color-7" href="/tag/1746/">Basketball</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">58 products</span>
<a class="label label-link label-color-8" href="/tag/856791/">Asymmetric VR</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">55 products</span>
<a class="label label-link label-color-9" href="/tag/71389/">Spelling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">54 products</span>
<a class="label label-link label-color-10" href="/tag/22955/">Mini Golf</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">51 products</span>
<a class="label label-link label-color-11" href="/tag/14906/">Intentionally Awkward Controls</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">50 products</span>
<a class="label label-link label-color-12" href="/tag/922563/">Roguevania</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">50 products</span>
<a class="label label-link label-color-13" href="/tag/3920/">Cooking</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">47 products</span>
<a class="label label-link label-color-0" href="/tag/19780/">Submarine</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">46 products</span>
<a class="label label-link label-color-1" href="/tag/92092/">Jet</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">44 products</span>
<a class="label label-link label-color-2" href="/tag/1100686/">Outbreak Sim</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">42 products</span>
<a class="label label-link label-color-3" href="/tag/29855/">Ambient</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">39 products</span>
<a class="label label-link label-color-4" href="/tag/745697/">Social Deduction</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">36 products</span>
<a class="label label-link label-color-5" href="/tag/17927/">Pool</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">36 products</span>
<a class="label label-link label-color-6" href="/tag/47827/">Wrestling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">34 products</span>
<a class="label label-link label-color-7" href="/tag/4291/">Spaceships</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">32 products</span>
<a class="label label-link label-color-8" href="/tag/5727/">Baseball</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">32 products</span>
<a class="label label-link label-color-9" href="/tag/17337/">Lemmings</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">31 products</span>
<a class="label label-link label-color-10" href="/tag/233824/">Feature Film</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">31 products</span>
<a class="label label-link label-color-11" href="/tag/5914/">Tennis</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">27 products</span>
<a class="label label-link label-color-12" href="/tag/5407/">Benchmark</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">27 products</span>
<a class="label label-link label-color-13" href="/tag/189941/">Instrumental Music</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">25 products</span>
<a class="label label-link label-color-0" href="/tag/324176/">Hockey</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">25 products</span>
<a class="label label-link label-color-1" href="/tag/27758/">Voice Control</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">24 products</span>
<a class="label label-link label-color-2" href="/tag/15868/">Motocross</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">23 products</span>
<a class="label label-link label-color-3" href="/tag/1753/">Skateboarding</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">21 products</span>
<a class="label label-link label-color-4" href="/tag/143739/">Electronic</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">20 products</span>
<a class="label label-link label-color-5" href="/tag/96359/">Skating</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">18 products</span>
<a class="label label-link label-color-6" href="/tag/19568/">Cycling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">17 products</span>
<a class="label label-link label-color-7" href="/tag/7309/">Skiing</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">16 products</span>
<a class="label label-link label-color-8" href="/tag/337964/">Rock Music</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">16 products</span>
<a class="label label-link label-color-9" href="/tag/7328/">Bowling</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">16 products</span>
<a class="label label-link label-color-10" href="/tag/603297/">Hardware</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">13 products</span>
<a class="label label-link label-color-11" href="/tag/348922/">Steam Machine</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">13 products</span>
<a class="label label-link label-color-12" href="/tag/5941/">Reboot</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">11 products</span>
<a class="label label-link label-color-13" href="/tag/252854/">BMX</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">11 products</span>
<a class="label label-link label-color-0" href="/tag/28444/">Snowboarding</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">9 products</span>
<a class="label label-link label-color-1" href="/tag/8461/">Well-Written</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">8 products</span>
<a class="label label-link label-color-2" href="/tag/117648/">8-bit Music</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">8 products</span>
<a class="label label-link label-color-3" href="/tag/129761/">ATV</a>
</div>
<div class="span4">
<span class="label-count pull-right muted">6 products</span>
<a class="label label-link label-color-4" href="/tag/1723/">Action RTS</a>
</div>
</div>
</div>
<script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" integrity="sha512-AYlzeu/5Cexb6uN6uQ0LfoRx33CgMticI4+eEsmPz9QxxyuLr0zd4MA+4hxLqISNs8769A+FVnBCuaMne6d0+w==" src="/static/js/vendor/list.js?v=0189737aeff909ec"></script>
<script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=">
(function() {
new List('list', {
valueNames: ["label"]
});
}());
</script>
</div>
</div>
<div class="footer" id="steamdb-org" itemscope itemtype="http://schema.org/Organization" itemprop="publisher">
<meta itemprop="name" content="Steam Database">
<meta itemprop="alternateName" content="SteamDB">
<meta itemprop="url" content="https://steamdb.info/">
<span itemprop="logo" itemscope itemtype="https://schema.org/ImageObject">
<meta itemprop="url" content="https://steamdb.info/static/logos/512px.png">
<meta itemprop="width" content="512">
<meta itemprop="height" content="512">
</span>
<div class="container">
<div class="row">
<div class="span9 footer-attribution">
<div class="footer-steamdb">Steam Database</div>
<div>By <a href="https://xpaw.me">xPaw</a> and <a href="https://marlamin.com/">Marlamin</a></div>
<div class="footer-third-party">SteamDB is a community website and is not affiliated with Valve or Steam.<br>All times on the site are UTC.</div>
<a href="/?dark=0" id="dark-mode-toggle" rel="nofollow"><span class="dark-mode-slider"></span> <span class="dark-mode-disabled">Enable dark mode</span><span class="dark-mode-enabled">Disable dark mode</span></a>
</div>
<div class="span3">
<a class="btn-social" href="https://twitter.com/SteamDB" itemprop="sameAs">
<svg viewBox="0 0 32 32" height="24" width="60" class="btn-social-icon" aria-hidden="true">
<path d="M31.993 6.077c-1.177.523-2.44.876-3.77 1.033 1.355-.812 2.396-2.098 2.887-3.63-1.27.75-2.673 1.3-4.168 1.592C25.744 3.797 24.038 3 22.15 3c-3.626 0-6.563 2.938-6.563 6.563 0 .514.057 1.016.17 1.496C10.3 10.784 5.464 8.17 2.226 4.2c-.564.97-.888 2.098-.888 3.3 0 2.28 1.158 4.287 2.918 5.465-1.075-.035-2.087-.33-2.972-.82v.08c0 3.182 2.26 5.835 5.264 6.438-.55.15-1.13.23-1.73.23-.423 0-.833-.04-1.233-.117.834 2.606 3.26 4.504 6.13 4.558-2.245 1.76-5.075 2.81-8.15 2.81-.53 0-1.053-.03-1.566-.09C2.906 27.913 6.356 29 10.063 29c12.072 0 18.675-10 18.675-18.675 0-.284-.008-.568-.02-.85 1.283-.925 2.395-2.08 3.276-3.398z" />
</svg>
<span class="btn-social-title">Follow @SteamDB</span>
</a>
<a class="btn-social" href="https://twitter.com/thexpaw">
<svg viewBox="0 0 32 32" height="24" width="60" class="btn-social-icon" aria-hidden="true">
<path d="M31.993 6.077c-1.177.523-2.44.876-3.77 1.033 1.355-.812 2.396-2.098 2.887-3.63-1.27.75-2.673 1.3-4.168 1.592C25.744 3.797 24.038 3 22.15 3c-3.626 0-6.563 2.938-6.563 6.563 0 .514.057 1.016.17 1.496C10.3 10.784 5.464 8.17 2.226 4.2c-.564.97-.888 2.098-.888 3.3 0 2.28 1.158 4.287 2.918 5.465-1.075-.035-2.087-.33-2.972-.82v.08c0 3.182 2.26 5.835 5.264 6.438-.55.15-1.13.23-1.73.23-.423 0-.833-.04-1.233-.117.834 2.606 3.26 4.504 6.13 4.558-2.245 1.76-5.075 2.81-8.15 2.81-.53 0-1.053-.03-1.566-.09C2.906 27.913 6.356 29 10.063 29c12.072 0 18.675-10 18.675-18.675 0-.284-.008-.568-.02-.85 1.283-.925 2.395-2.08 3.276-3.398z" />
</svg>
<span class="btn-social-title">Follow @thexpaw</span>
</a>
<a class="btn-social" href="https://steamcommunity.com/groups/steamdb" itemprop="sameAs">
<svg viewBox="0 0 20 16" width="60" height="24" class="btn-social-icon" aria-hidden="true">
<circle stroke-width="1.5" cy="4.5" cx="15.5" r="3.75" class="stroke" />
<circle cx="15.5" cy="4.5" r="1.855" class="fill" />
<path d="M11.656 4.2L12.75 7.14l2.865 1.387-5.13 3.853-.867-2.09-1.773-.942z" class="fill" />
<circle cy="12.5" cx="7.5" r="3" class="stroke" />
<rect transform="matrix(.92432 .3816 -.38727 .92196 0 0)" ry="1.526" width="9.477" y="7.155" x="3.767" height="3.053" class="fill" />
</svg>
<span class="btn-social-title">Join our Steam Group</span>
</a>
<a class="btn-social" href="https://github.com/SteamDatabase" itemprop="sameAs">
<svg viewBox="0 0 16 16" width="60" height="24" class="btn-social-icon" aria-hidden="true">
<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
</svg>
<span class="btn-social-title">View our GitHub</span>
</a>
<a class="btn-social" href="/discord/" rel="nofollow">
<svg viewBox="0 0 24 24" width="60" height="24" class="btn-social-icon" aria-hidden="true">
<path d="M20.222 0c1.406 0 2.54 1.137 2.607 2.475V24l-2.677-2.273-1.47-1.338-1.604-1.398.67 2.205H3.71c-1.402 0-2.54-1.065-2.54-2.476V2.48C1.17 1.142 2.31.003 3.715.003h16.5L20.222 0zm-6.118 5.683h-.03l-.202.2c2.073.6 3.076 1.537 3.076 1.537-1.336-.668-2.54-1.002-3.744-1.137-.87-.135-1.74-.064-2.475 0h-.2c-.47 0-1.47.2-2.81.735-.467.203-.735.336-.735.336s1.002-1.002 3.21-1.537l-.135-.135s-1.672-.064-3.477 1.27c0 0-1.805 3.144-1.805 7.02 0 0 1 1.74 3.743 1.806 0 0 .4-.533.805-1.002-1.54-.468-2.14-1.404-2.14-1.404s.134.066.335.2h.06c.03 0 .044.015.06.03v.006c.016.016.03.03.06.03.33.136.66.27.93.4.466.202 1.065.403 1.8.536.93.135 1.996.2 3.21 0 .6-.135 1.2-.267 1.8-.535.39-.2.87-.4 1.397-.737 0 0-.6.936-2.205 1.404.33.466.795 1 .795 1 2.744-.06 3.81-1.8 3.87-1.726 0-3.87-1.815-7.02-1.815-7.02-1.635-1.214-3.165-1.26-3.435-1.26l.056-.02zm.168 4.413c.703 0 1.27.6 1.27 1.335 0 .74-.57 1.34-1.27 1.34-.7 0-1.27-.6-1.27-1.334.002-.74.573-1.338 1.27-1.338zm-4.543 0c.7 0 1.266.6 1.266 1.335 0 .74-.57 1.34-1.27 1.34-.7 0-1.27-.6-1.27-1.334 0-.74.57-1.338 1.27-1.338z" />
</svg>
<span class="btn-social-title">Join our Discord</span>
</a>
<a class="btn-social" href="https://steamcommunity.com/sharedfiles/filedetails/?id=2143864906" rel="nofollow" style="color:#ffc83d">
<svg viewBox="0 0 13 21" xmlns="http://www.w3.org/2000/svg" height="24" width="60" class="btn-social-icon" aria-hidden="true">
<path fill-rule="evenodd" clip-rule="evenodd" d="M5.8.2l-.6.42c-.24.15-.5.23-.81.2L3.93.73c-.5-.04-.97.19-1.2.65l-.3.65c-.16.27-.35.47-.62.58l-.42.2c-.46.19-.73.65-.7 1.15l.05.73c.03.3-.04.54-.24.77l-.26.39c-.31.38-.31.92-.04 1.34l.42.62c.15.23.2.5.2.8l-.08.47c-.04.5.19.96.65 1.2l.65.3c.27.15.46.35.58.62l.15.42c.23.46.66.73 1.2.7l.72-.05c.27-.04.54.04.77.23l.39.27c.38.31.92.31 1.34.04l.62-.42c.23-.16.5-.2.77-.2l.46.08c.5.04 1-.19 1.19-.65l.34-.66c.12-.27.31-.46.58-.57l.42-.16c.46-.23.77-.65.73-1.19l-.04-.73a.97.97 0 01.24-.77l.26-.39c.31-.38.31-.92.04-1.34l-.42-.62a1.1 1.1 0 01-.2-.77l.08-.46c.04-.5-.19-1-.65-1.2l-.65-.34c-.27-.12-.46-.3-.58-.58l-.2-.42C10 .97 9.55.66 9.05.7L8.3.74A.93.93 0 017.54.5L7.15.24C6.77-.07 6.23-.07 5.81.2zm.7 2.5a3.82 3.82 0 10-.04 7.65A3.82 3.82 0 006.5 2.7z" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M3.04 12.78v7.32l3.46-2.47 3.46 2.47v-7.32c-.3.12-.65.2-1 .16l-.42-.08a.65.65 0 00-.39.12l-.61.38c-.66.42-1.46.42-2.12-.04l-.34-.3c-.12-.08-.23-.08-.35-.08l-.73.04c-.34 0-.69-.04-.96-.2z" />
</svg>
<span class="btn-social-title">Give a Steam Award</span>
</a>
</div>
</div>
<div class="row">
<div class="span12 footer-menu hide-small">
<ul>
<li><a href="/blog/">Blog</a></li>
<li><a href="/faq/">FAQ &amp; Help</a></li>
<li><a href="/sales/">Sales</a></li>
<li><a href="/calculator/">Calculator</a></li>
<li><a href="/donate/">Donate</a></li>
</ul>
<ul>
<li><a href="/apps/">Apps</a></li>
<li><a href="/subs/">Packages</a></li>
<li><a href="/bundles/">Bundles</a></li>
<li><a href="/history/">History</a></li>
<li><a href="/instantsearch/">Instant Search</a></li>
</ul>
<ul>
<li><a href="/realtime/">Realtime Updates</a></li>
<li><a href="/pricechanges/">Price Tracking</a></li>
<li><a href="/tags/">Tags</a></li>
<li><a href="/upcoming/">Upcoming</a></li>
<li><a href="/graph/">Charts</a></li>
</ul>
<ul>
<li><a href="/stats/gameratings/">Top Rated Games</a></li>
<li><a href="/badge/13/">Top Game Owners</a></li>
<li><a href="/stats/toplevels/">Top Steam Levels</a></li>
<li><a href="/topsellers/">Top Selling Games</a></li>
<li><a href="/badges/">Badges</a></li>
</ul>
<ul>
<li><a href="/patchnotes/">Patch notes</a></li>
<li><a href="/upcoming/free/">Free Promotions</a></li>
<li><a href="/freepackages/">Free Packages</a></li>
<li><a href="https://steamstat.us/">Steam Status</a></li>
<li><a href="https://steamapi.xpaw.me/">Steam Web API</a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="hover" id="js-hover" style="display:none"></div>
<script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" integrity="sha512-wKI6fglMAcvISybKU1eGtOzU4maL+yP9nn7v1Augq3Ef6Bn9oq1LLwZpZjEe4t7QyQdW0yU9FS/Nm3tlEkQ+Kw==" src="/static/js/footer.js?v=c0a23a7e094c01cb" defer></script><script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" integrity="sha512-RFUXZ8W/1HCjNJijhwsrfDagLR8pyUIlItkKEUbZ1n3MmzGld2XlX1bhtnMF0sjtY7gTp2/RYtbQQDD9BN3e9A==" src="/static/js/vendor/popper.js?v=44551767c5bfd470" defer></script><script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" integrity="sha512-QpjQI5+G4M3AQ0YfM5MMCzBXZJvtin9aNDwhmZBh6VLVF9Qt2NgSDINA/iXzcriDNdWhKxGDUysI7w5kWY2MGw==" src="/static/js/hover.js?v=4298d0239f86e0cd" defer></script>
<noscript class="extension-warning"><svg version="1.1" width="32" height="32" viewBox="0 0 16 16" class="octicon octicon-alert" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg> For SteamDB to function correctly you must enable JavaScript.</noscript>
<script nonce="VqU59B5YG7eIoKzDMg7y3702UHI=" src="https://www.google-analytics.com/analytics.js" async></script>
</body>
</html>
    """

