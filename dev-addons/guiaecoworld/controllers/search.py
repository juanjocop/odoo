import json
from difflib import SequenceMatcher

from odoo import http, tools, _
from odoo.http import request


class WebsiteSearchGuia(http.Controller):
    @http.route(['/guiaecoworld/get_suggest'], type='http', auth="public", methods=['GET'], website=True)
    def get_suggest_json(self, **kw):
        query = kw.get('query')
        names = query.split(' ')
        domain = ['|' for k in range(len(names) - 1)] + [('name', 'ilike', name) for name in names]
        provincias = request.env['res.country.state'].search(domain)
        provincias = sorted(provincias, key=lambda x: SequenceMatcher(None, query.lower(), x.name.lower()).ratio(),
                          reverse=True)
        results = []
        for provincia in provincias:
            results.append({'value': provincia.name, 'data': {'id': provincia.id, 'after_selected': provincia.name}})
        return json.dumps({
            'query': 'Unit',
            'suggestions': results
        })

    @http.route(['/guiaecoworld/get_localidad'], type='http', auth="public", methods=['GET'], website=True)
    def get_suggest_json(self, **kw):
        query = kw.get('query')
        names = query.split(' ')
        domain = ['|' for k in range(len(names) - 1)] + [('city', 'ilike', name) for name in names] + [('activo', '=', True)]
        clientes = request.env['guiaeco.clientes'].search(domain)
        clientes = sorted(clientes, key=lambda x: SequenceMatcher(None, query.lower(), x.name.lower()).ratio(),
                          reverse=True)
        results = []
        for cliente in clientes:
            results.append({'value': cliente.city, 'data': {'id': cliente.id, 'after_selected': cliente.city}})
        return json.dumps({
            'query': 'Unit',
            'suggestions': results
        })
