from sanic import Blueprint
from . import views
hello_bp = Blueprint("hello", strict_slashes=False)

hello_bp.add_route(
    views.HelloView.as_view(),
    uri='/hello',
    methods=['GET']
)
