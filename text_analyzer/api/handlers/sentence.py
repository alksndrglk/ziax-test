from http import HTTPStatus
from aiohttp_apispec import docs, request_schema, response_schema

from text_analyzer.api.schema import (
    SentenceRequsetSchema,
    SentenceResponseSchema,
)
from text_analyzer.utils.web import json_response
from text_analyzer.api.morpholyzer import SentenceAnalyze
from .base import BaseView


class SentenceAnalyzerView(BaseView):
    URL_PATH = "/api/v1/sentence"

    @docs(tags=["Sentence"], summary="Alalyze sentence")
    @request_schema(SentenceRequsetSchema)
    @response_schema(SentenceResponseSchema(), code=HTTPStatus.OK.value)
    async def post(self):
        text = self.request["data"]["sentence"]
        response_data = SentenceAnalyze.analyze(text)
        return json_response(data=SentenceResponseSchema().dump(response_data))
