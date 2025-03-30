from elrahapi.router.route_config import RouteConfig
from .cruds import myapp_crud
from ..settings.auth.configs import authentication
from elrahapi.router.router_default_routes_name import DefaultRoutesName
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/entities",
    tags=["entity"],
    crud=myapp_crud,
    authentication= authentication,
    roles=["ADMIN"]
)
count=RouteConfig(
    route_name=DefaultRoutesName.COUNT,
    is_activated=True,
    is_protected=True,
    roles=["MANAGER"]
)
app_myapp = router_provider.get_custom_protected_router(
    init_data=[count]
)
##app_myapp = router_provider.get_protected_router()

