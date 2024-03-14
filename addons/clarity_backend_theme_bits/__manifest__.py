{
    "name": "AEOS Theme",
    "version": "1.0.0.1",
    'author': "Atlanexis Enterprise",
    'summary': """   
        The default theme for Atlanexis Enterprise OS
    """,
    "sequence": 7,
    "license": "OPL-1",
    "category": "Themes/Backend",
    "website": "https://atlanexis.com",
    "depends": ["web"],
    "data": [ 
        'views/res_config_setting.xml',
        'views/res_users.xml',
        'views/webclient_templates.xml'
    ],
    "assets": {
        "web.assets_frontend": [
            'clarity_backend_theme_bits/static/src/scss/login.scss'
        ],
        "web.assets_backend": [   
            'clarity_backend_theme_bits/static/src/xml/WebClient.xml',
            'clarity_backend_theme_bits/static/src/xml/navbar/sidebar.xml', 
            'clarity_backend_theme_bits/static/src/xml/systray_items/user_menu.xml',
            'clarity_backend_theme_bits/static/src/js/SidebarBottom.js',  
            'clarity_backend_theme_bits/static/src/js/WebClient.js', 
            'clarity_backend_theme_bits/static/src/scss/layout.scss',
            'clarity_backend_theme_bits/static/src/scss/navbar.scss', 
            'clarity_backend_theme_bits/static/src/js/navbar.js',  
        ],
    }, 
    'installable': True,
    'application': True,
    'auto_install': False,  
    'images': [
        'static/description/logo.gif',
        'static/description/theme_screenshot.gif',
    ],
}
