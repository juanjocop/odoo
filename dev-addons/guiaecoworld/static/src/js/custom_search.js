odoo.define("website_search_autocomplete.custom_search", function (require) {
   "use strict";
   require('web.dom_ready');
   var base = require("web_editor.base");
   var ajax = require('web.ajax');
   var utils = require('web.utils');
   var core = require('web.core');
   var config = require('web.config');
   require("website.content.zoomodoo");
   
    $('#search_autocomplete').devbridgeAutocomplete({
        serviceUrl: '/guiaecoworld/get_suggest',
        onSelect: function (suggestion) {
             window.location.replace(window.location.origin +
                '/guiaecoworld/' + suggestion.data.id + '?search=' + suggestion.value);
        }
    });
});
