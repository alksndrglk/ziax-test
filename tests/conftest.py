import pytest

from aiohttp.test_utils import TestClient

from text_analyzer.api.__main__ import parser
from text_analyzer.api.app import create_app


@pytest.fixture
def arguments(aiomisc_unused_port):
    return parser.parse_args(
        [
            "--log-level=debug",
            "--api-address=127.0.0.1",
            f"--api-port={aiomisc_unused_port}",
            "--api-key=ziax",
        ]
    )


@pytest.fixture
async def api_client(aiohttp_client, arguments):
    app = create_app(arguments)
    client = await aiohttp_client(app, server_kwargs={"port": arguments.api_port})

    try:
        yield client
    finally:
        await client.close()
