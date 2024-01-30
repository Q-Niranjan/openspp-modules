# Part of OpenSPP. See LICENSE file for full copyright and licensing details.


{
    "name": "OpenSPP Base",
    "category": "OpenSPP",
    "version": "16.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "utm",
        "mail",
        "dms",
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_registry_group",
        "g2p_registry_membership",
        "spp_area",
        "spp_idpass",
        "spp_idqueue",
        "spp_service_points",
        "spp_custom_field",
        "spp_custom_fields_ui",
        "spp_programs",
        "spp_helpdesk",
    ],
    "external_dependencies": {},
    "data": [
        "data/top_up_card.xml",
        "views/registrant_view.xml",
        "views/hide_menu_view.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
