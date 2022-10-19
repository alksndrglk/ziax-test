import re

import pymorphy2

from text_analyzer.api.schema import IS_ALNUM_PATTERN, Analyzed

morph = pymorphy2.MorphAnalyzer()


class SentenceAnalyze:
    MORPH = morph

    @classmethod
    def analyze(cls, sentence: str) -> Analyzed:
        text = re.sub(IS_ALNUM_PATTERN, " ", sentence).split()
        first_declined_word = cls.inflect(
            next(x for x in text if not x.isdigit())
        )  # cls.inflect(text[0])
        last_norm_form = cls.normalize(text[-1])
        return Analyzed(
            first_declined_word=first_declined_word,
            last_norm_form=last_norm_form,
            num_words=len(text),
        )

    @staticmethod
    def inflect(word: str) -> list[str]:
        return list(set((p.word for p in SentenceAnalyze.MORPH.parse(word)[0].lexeme)))

    @staticmethod
    def normalize(word: str) -> list[str]:
        return [SentenceAnalyze.MORPH.parse(word)[0].normal_form]
