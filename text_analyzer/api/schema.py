from dataclasses import dataclass
import re

from marshmallow import Schema, ValidationError, validates
from marshmallow.fields import Str, Integer, List

NOT_CYRILLIC_PATTERN = r"^[^A-Za-z]*$"
IS_ALNUM_PATTERN = r"\W+"
NOT_WHITE_SPACE = r"[^ ]"


class SentenceRequsetSchema(Schema):
    sentence = Str(required=True)

    @validates("sentence")
    def validate_sentence(self, text: str):
        if not re.match(NOT_WHITE_SPACE, text):
            raise ValidationError("Sentence cannot be empty")
        if not re.match(NOT_CYRILLIC_PATTERN, text):
            raise ValidationError("Sentence can contain only cyrillic symbols")


class SentenceResponseSchema(Schema):
    first_declined_word = List(Str)
    last_norm_form = List(Str)
    num_words = Integer()


@dataclass
class Analyzed:
    first_declined_word: list[str]
    last_norm_form: list[str]
    num_words: int

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return (
                self.num_words == __o.num_words
                and self.last_norm_form == __o.last_norm_form
                and self.first_declined_word.sort() == self.first_declined_word.sort()
            )
        return False
