"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')
    
    map.connect('/', controller='index', action='index')
    map.connect('/contact', controller='contact', action='index')
    map.connect('/food-options', controller='foodoptions', action='index')
    map.connect('/gallery', controller='gallery', action='index')
    map.connect('/information', controller='information', action='index')
    map.connect('/news', controller='news', action='index')
    map.connect('/rules', controller='rules', action='index')
    map.connect('/seatbooking', controller='seatbooking', action='index')
    map.connect('/seatbooking/statusimage', controller='seatbooking', action='statusimage')
    map.connect('/tournaments', controller='tournaments', action='index')
    return map
