# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	config = [
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Customer",
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Supplier",
					"onboard": 1,
				}
			]
		},
		{
			"label": _("Sales"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"onboard": 1,
					"dependencies": ["Customer","Item"]
				}
			]
		},
		{
			"label": _("Purchase"),
			"items": [
				{
					"type": "doctype",
					"name": "Purchase Invoice",
					"onboard": 1,
					"dependencies": ["Supplier","Item"]
				}
			]
		},
        {
			"label": _("Stock"),
			"items": [
				{
					"type": "doctype",
					"name": "Stock Entry",
					"onboard": 1,
					"dependencies": ["Item"]
				},
                {
					"type": "doctype",
					"name": "Warehouse",
					"onboard": 1
				}
			]
		},
        {
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name":"General Ledger"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Item-wise Sales Register"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Profit and Loss Statement"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Stock Ledger"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Stock Balance"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Total Stock Summary"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Purchase Analytics"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Items To Be Requested"
				},
                {
					"type": "report",
					"is_query_report": True,
					"name":"Item-wise Purchase History"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name":"Sales Analytics"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name":"Stock Projected Qty"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name":"Stock Ageing"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name":"Item Price Stock"
				}
				
				
				
				
                
			]
		}
	]

	return config

