import {
  useState,
} from "react";

import {
  translateText,
} from "../services/translationService";

export function useTranslation() {

  const [loading,
    setLoading] =
    useState(false);

  const [result,
    setResult] =
    useState("");

  async function translate(
    text,
    source,
    target
  ) {

    setLoading(true);

    try {

      const data =
        await translateText(
          text,
          source,
          target
        );

      setResult(
        data.translation
      );

    }

    finally {

      setLoading(false);

    }

  }

  return {

    translate,
    loading,
    result,

  };

}