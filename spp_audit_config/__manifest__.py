{
    "name": "SPP Audit Config",
    "category": "OpenSPP",
    "version": "16.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "g2p_registry_membership",
        "spp_programs",
        "spp_service_points",
        "spp_audit_log",
        "spp_audit_post",
    ],
    "external_dependencies": {},
    "data": [
        "data/audit_rule_data.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
