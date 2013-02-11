import os
from logging import getLogger

from pylons import request
from genshi.input import HTML
from genshi.filters.transform import Transformer

from ckan.lib.accept import accept_types, accept_by_extension

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer
from ckan.plugins import IGenshiStreamFilter
from ckan.plugins import IRoutes

log = getLogger(__name__)


class DatapubPlugin(SingletonPlugin):
    """This plugin demonstrates how a theme packaged as a CKAN
    extension might extend CKAN behaviour.

    In this case, we implement three extension interfaces:

      - ``IConfigurer`` allows us to override configuration normally
        found in the ``ini``-file.  Here we use it to specify the site
        title, and to tell CKAN to look in this package for templates
        and resources that customise the core look and feel.
        
      - ``IGenshiStreamFilter`` allows us to filter and transform the
        HTML stream just before it is rendered.  In this case we use
        it to rename "frob" to "foobar"
        
      - ``IRoutes`` allows us to add new URLs, or override existing
        URLs.  In this example we use it to override the default
        ``/register`` behaviour with a custom controller
    """
    implements(IConfigurer, inherit=True)

    def update_config(self, config):
        """This IConfigurer implementation causes CKAN to look in the
        ```public``` and ```templates``` directories present in this
        package for any customisations.

        It also shows how to set the site title here (rather than in
        the main site .ini file), and causes CKAN to use the
        customised package form defined in ``package_form.py`` in this
        directory.
        """

        accept_types["text/turtle"] = ("text/turtle; charset=utf-8",    False, 'ttl')
        accept_by_extension["ttl"] = "text/turtle"
        accept_by_extension["n3"] = "text/turtle"

        accept_types["application/x-trig"] = ("application/x-trig; charset=utf-8", False, 'trig')
        accept_by_extension["trig"] = "application/x-trig"

        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        our_public_dir = os.path.join(rootdir, 'ckanext',
                                      'datapub', 'theme', 'public')
        template_dir = os.path.join(rootdir, 'ckanext',
                                    'datapub', 'theme', 'templates')
        # set our local template and resource overrides
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])
        # add in the extra.css
        #config['ckan.template_head_end'] = config.get('ckan.template_head_end', '') +\
        #                                   '<link rel="stylesheet" href="/css/extra.css" type="text/css"> '
        # set the title
        #config['ckan.site_title'] = "Example CKAN theme"
        # set the customised package form (see ``setup.py`` for entry point)
        #config['package_form'] = "example_form"
