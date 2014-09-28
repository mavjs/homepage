from pyramid.config import Configurator
from mavjsorg.views import default_view

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('contact', '/contact')
    config.add_view(
        default_view,
        route_name='home',
        renderer='templates/home.pt')
    config.add_view(
        default_view,
        route_name='about',
        renderer='templates/about.pt')
    config.add_view(
        default_view,
        route_name='contact',
        renderer='templates/contact.pt')
    config.scan()
    return config.make_wsgi_app()
