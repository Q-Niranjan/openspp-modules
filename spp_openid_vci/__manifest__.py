{
    "name": "OpenSPP OpenID VCI",
    "category": "OpenSPP",
    "version": "17.0.1.2.1",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Beta",
    "maintainers": ["jeremi", "gonzalesedwin1 123"],
    "depends": [
        "spp_encryption",
        "g2p_encryption_rest_api",
        "g2p_registry_base",
        "g2p_openid_vci",
        "g2p_openid_vci_rest_api",
    ],
    "external_dependencies": {"python": ["qrcode"]},
    "data": [
        "security/ir.model.access.csv",
        "wizard/vci_issuer_selection_view.xml",
        "data/paperformat.xml",
        "views/id_card.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
    "summary": "Enables the issuance and management of Verifiable Credentials (VCs) within the OpenSPP platform, leveraging OpenID Connect for Verifiable Presentations (OpenID4VP) to provide secure and verifiable digital credentials for registrants.",
}
