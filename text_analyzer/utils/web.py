import logging
from typing import Any

from aiohttp.web import Response, json_response as aiohttp_json_response

log = logging.getLogger(__name__)


def json_response(data: Any = None, status: str = "ok") -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(data={"status": status, **data})
