from pyramid.view import view_config

def default_view(request):
    """
    This is the default view, used to render most routes since it's just static
    views.
    """
    return {}

