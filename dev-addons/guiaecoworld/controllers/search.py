import json
from difflib import SequenceMatcher

from odoo import http, tools, _
from odoo.http import request

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

class WebsiteSearchProvincia(http.Controller):
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


class WebsiteSearchLocalidad(http.Controller):
    @http.route(['/guiaecoworld/get_localidad'], type='http', auth="public", methods=['GET'], website=True)
    def get_suggest_json(self, **kw):
        query = kw.get('query')
        names = query.split(' ')
        domain = ['|' for k in range(len(names) - 1)] + [('city', 'ilike', name) for name in names] + [('activo', '=', True)]
        clientes = request.env['guiaeco.clientes'].search(domain)
        clientes = sorted(clientes, key=lambda x: SequenceMatcher(None, query.lower(), x.name.lower()).ratio(),
                          reverse=True)
        citys = []
        for cliente in clientes:
            citys.append(cliente.city)
        clientesSinDuplicados = remove_duplicates(citys)
        results = []
        for city in clientesSinDuplicados:
            results.append({'value': city, 'data': {'id': city, 'after_selected': city}})
        return json.dumps({
            'query': 'Unit',
            'suggestions': results
        })
