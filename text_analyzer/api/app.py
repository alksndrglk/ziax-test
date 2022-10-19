import logging
from types import MappingProxyType
from typing import Mapping

from aiohttp import PAYLOAD_REGISTRY, JsonPayload
from aiohttp.web_app import Application
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from text_analyzer.api.handlers import HANDLERS
from text_analyzer.api.middleware import (
    error_middleware,
    handle_validation_error,
    auth_middleware,
)

log = logging.getLogger(__name__)


def create_app(args) -> Application:
    app = Application(
        middlewares=[error_middleware, auth_middleware, validation_middleware]
    )
    app["api_key"] = args.api_key
    for handler in HANDLERS:
        log.debug("Registering handler %r as %r", handler, handler.URL_PATH)
        app.router.add_route("*", handler.URL_PATH, handler)

    setup_aiohttp_apispec(
        app=app,
        title="Sentence API",
        swagger_path="/",
        error_callback=handle_validation_error,
        securityDefinitions={"user": {"type": "apiKey", "name": "key", "in": "header"}},
        security=[{"user": []}],
    )

    PAYLOAD_REGISTRY.register(JsonPayload, (Mapping, MappingProxyType))
    return app
