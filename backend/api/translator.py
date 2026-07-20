from model.inference import translate


class TranslatorService:

    def translate(self, text: str):

        result = translate(text)

        return {
            "input": text,
            "translation": result,
        }


translator_service = TranslatorService()