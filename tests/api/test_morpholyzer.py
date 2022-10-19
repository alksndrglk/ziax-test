from text_analyzer.api.morpholyzer import SentenceAnalyze
from text_analyzer.api.schema import Analyzed
from data import success_data


class TestMorpholyzer:
    def test_analyze(self):
        assert SentenceAnalyze.analyze("тестовая строка") == Analyzed(
            num_words=success_data["num_words"],
            last_norm_form=success_data["last_norm_form"],
            first_declined_word=success_data["first_declined_word"],
        )

    def test_normalize(self):
        assert SentenceAnalyze.normalize("строка") == success_data["last_norm_form"]

    def test_inflect(self):
        assert (
            SentenceAnalyze.inflect("тестовая").sort()
            == success_data["first_declined_word"].sort()
        )
