import aiohttp
import pytest

from aioresponses import aioresponses

from data import testdata, success_data


class TestSentenceAnalyzerView:
    URL_PATH = "/api/v1/sentence"

    @pytest.mark.parametrize("status, payload, headers, expected", testdata)
    async def test_unauthorized(self, status, payload, headers, expected, api_client):
        resp = await api_client.post(self.URL_PATH, json=payload, headers=headers)
        assert resp.status == status
        data = await resp.json()
        assert data == expected

    async def test_success(self):

        with aioresponses() as mocked:
            mocked.post(self.URL_PATH, status=200, payload=success_data)
            session = aiohttp.ClientSession()
            resp = await session.post(
                self.URL_PATH,
                json={
                    "sentence": "тестовая строка",
                },
                headers={
                    "content-type": "application/json",
                    "key": "ziax",
                },
            )

            assert resp.status == 200
            data = await resp.json()
            assert data == success_data
