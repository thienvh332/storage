# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Storage Media",
    "summary": "Give the posibility to store media data in Odoo",
    "version": "10.0.1.0.0",
    "category": "Uncategorized",
    "website": "www.akretion.com",
    "author": " Akretion",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "storage_file",
    ],
    "data": [
        "views/storage_media_view.xml",
        "data/ir_parameter.xml",
        "security/res_group.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
