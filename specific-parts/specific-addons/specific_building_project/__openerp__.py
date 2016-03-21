# -*- coding: utf-8 -*-
# © 2015 Yannick Vaucher (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Building project ",
    "summary": "New type of analytic account",
    "version": "9.0.1.0.0",
    "category": "Swisslux Modules",
    "website": "https://odoo-community.org/",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "analytic",
        "crm",
        "sale",
        "sale_crm",
        "specific_partner",
    ],
    "data": [
        "data/calendar_event_type.xml",
        "data/building_project_tag.xml",
        "data/building_project_type.xml",
        "views/calendar_event.xml",
        "views/res_partner.xml",
        "views/crm_lead.xml",
        "views/sale_order.xml",
        "views/building_project.xml",
        "wizards/create_opportunity_quotation_view.xml",
        "security/ir.model.access.csv",
        "security/account_analytic_account.xml"
    ],
    "demo": [
    ],
}
