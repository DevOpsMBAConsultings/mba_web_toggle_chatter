{
    "name": "MBA - Web Toggle Chatter (MBA Consultings)",
    "summary": "Toggle chatter in backend form views (Port from OCA) | MBA Consultings",
    "version": "20.0.1.0.0",
    "category": "Extra Tools",
    "author": "MBA Consultings, Brooks Gonzalez",
    "website": "https://mbaconsultings.com",
    "license": "LGPL-3",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "mba_web_toggle_chatter/static/src/js/web_toggle_chatter.esm.js",
            "mba_web_toggle_chatter/static/src/xml/web_toggle_chatter.xml",
            "mba_web_toggle_chatter/static/src/scss/web_toggle_chatter.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
