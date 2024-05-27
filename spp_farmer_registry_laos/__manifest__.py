# Part of OpenSPP. See LICENSE file for full copyright and licensing details.


{
    "name": "Farmer Registry: Laos",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Beta",
    "external_dependencies": {"python": ["faker"]},
    "maintainers": ["jeremi", "gonzalesedwin1123", "reichie020212"],
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_registry_group",
        "g2p_registry_individual",
        "g2p_registry_membership",
        "spp_farmer_registry_base",
        "spp_registry_group_hierarchy",
        "spp_event_data",
        "spp_area",
        "g2p_programs",
        "queue_job",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/group_kind_data.xml",
        "data/ethnic_group_data.xml",
        "data/crops_data.xml",
        "data/livestock_data.xml",
        "views/farmer_group_view.xml",
        "views/group_view.xml",
        "views/individual_view.xml",
        "views/event_data_view.xml",
        "views/event_data_gen_info_view.xml",
        "views/generate_farmer_data_view.xml",
        "views/event_data_poverty_indicator_view.xml",
        "views/event_data_hh_labor_view.xml",
        "views/event_data_hh_assets_view.xml",
        "views/event_data_agri_land_ownership_use_view.xml",
        "views/event_data_food_security_view.xml",
        "views/event_data_agri_ws_view.xml",
        "views/event_data_agri_tech_ws_view.xml",
        "views/event_data_agri_ds_view.xml",
        "views/event_data_agri_ds_hot_view.xml",
        "views/event_data_permanent_crops_view.xml",
        "views/event_data_livestock_farming_view.xml",
        "views/event_data_inc_agri_view.xml",
        "views/event_data_inc_non_agri_view.xml",
        "views/event_data_wash_ind_view.xml",
        "views/event_data_hh_resilience_index_view.xml",
        "views/event_data_min_dietary_score_view.xml",
        "wizard/create_event_wizard.xml",
        "wizard/create_event_farm_wizard.xml",
        "wizard/create_event_gen_info_wizard.xml",
        "wizard/create_event_poverty_indicator_wizard.xml",
        "wizard/create_event_hh_labor_wizard.xml",
        "wizard/create_event_hh_assets_wizard.xml",
        "wizard/create_event_agri_land_ownership_use_wizard.xml",
        "wizard/create_event_food_security_wizard.xml",
        "wizard/create_event_agri_ws_wizard.xml",
        "wizard/create_event_agri_tech_ws_wizard.xml",
        "wizard/create_event_agri_ds_wizard.xml",
        "wizard/create_event_agri_ds_hot_wizard.xml",
        "wizard/create_event_permanent_crops_wizard.xml",
        "wizard/create_event_livestock_farming_wizard.xml",
        "wizard/create_event_inc_agri_wizard.xml",
        "wizard/create_event_inc_non_agri_wizard.xml",
        "wizard/create_event_wash_ind_wizard.xml",
        "wizard/create_event_hh_resilience_index_wizard.xml",
        "wizard/create_event_min_dietary_score_wizard.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
