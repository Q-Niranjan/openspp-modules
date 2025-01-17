{
    "name": "OpenSPP Theme (Muk Theme)",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "category": "OpenSPP",
    "version": "17.0.1.3.0",
    "depends": [
        "base",
        "web",
        "muk_web_theme",
    ],
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "data": [
        "views/main_view.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            "theme_openspp_muk/static/src/scss/colors.scss",
            "theme_openspp_muk/static/src/scss/colors_light.scss",
        ],
        "web.assets_web_dark": ["theme_openspp_muk/static/src/scss/colors_dark.scss"],
        "web.assets_backend": ["theme_openspp_muk/static/src/scss/navbar.scss"],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
