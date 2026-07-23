from model.inference import translate


class TranslatorService:

    def translate(
        self,
        text: str,
        source: str | None = None,
        target: str | None = None,
    ):

        result = translate(text)

        return {
            "input": text,
            "translation": result,
            "source": source,
            "target": target,
        }


translator_service = TranslatorService()