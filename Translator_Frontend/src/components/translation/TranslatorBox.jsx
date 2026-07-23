import { useState } from "react";

import {
  ArrowLeftRight,
  Copy,
  Trash2,
} from "lucide-react";

import toast from "react-hot-toast";

import api from "../../services/api";

import LanguageSelector from "./LanguageSelector";

import TranslateButton from "./TranslateButton";


export default function TranslatorBox() {

  const [sourceLanguage, setSourceLanguage] =
    useState("English");

  const [targetLanguage, setTargetLanguage] =
    useState("Igbo");

  const [source, setSource] =
    useState("");

  const [target, setTarget] =
    useState("");

  const [loading, setLoading] =
    useState(false);


  function handleSourceLanguageChange(language) {

    setSourceLanguage(language);

    setTargetLanguage(
      language === "English"
        ? "Igbo"
        : "English"
    );

    setTarget("");
  }


  function swapLanguages() {

    const oldSourceLanguage =
      sourceLanguage;

    const oldTargetLanguage =
      targetLanguage;

    const oldSource =
      source;

    const oldTarget =
      target;


    setSourceLanguage(
      oldTargetLanguage
    );

    setTargetLanguage(
      oldSourceLanguage
    );

    setSource(oldTarget);

    setTarget(oldSource);
  }


  function clearTranslation() {

    setSource("");

    setTarget("");

  }


  function autoResize(event) {

    event.target.style.height =
      "auto";

    event.target.style.height =
      `${event.target.scrollHeight}px`;

  }


  async function copyTranslation() {

    if (!target.trim()) {

      toast.error(
        "There is no translation to copy."
      );

      return;
    }


    try {

      await navigator.clipboard.writeText(
        target
      );

      toast.success(
        "Translation copied!"
      );

    } catch (error) {

      toast.error(
        "Unable to copy translation."
      );

    }

  }


  async function handleTranslate() {

    if (!source.trim()) {

      toast.error(
        "Please enter text to translate."
      );

      return;
    }


    setLoading(true);

    setTarget("");


    try {

      const response =
        await api.post(
          "/translate",
          {
            text: source,

            source: sourceLanguage,

            target: targetLanguage,
          }
        );


      setTarget(
        response.data.translation
      );


      toast.success(
        "Translation completed!"
      );


    } catch (error) {

      console.error(
        "Translation error:",
        error
      );


      if (
        error.response
        ?.data
        ?.detail
      ) {

        toast.error(
          error.response.data.detail
        );

      } else {

        toast.error(
          "Translation failed. Please try again."
        );

      }


    } finally {

      setLoading(false);

    }

  }


  return (

    <div className="space-y-8">


      {/* Main Translator Card */}

      <div
        className="
          bg-white
          rounded-3xl
          shadow-xl
          p-6
          md:p-8
        "
      >


        {/* Language Controls */}

        <div
          className="
            grid
            lg:grid-cols-[1fr_auto_1fr]
            gap-4
            items-center
          "
        >


          {/* Source Language */}

          <div>

            <label
              className="
                block
                text-sm
                font-bold
                text-gray-600
                mb-2
              "
            >

              Translate from

            </label>


            <LanguageSelector

              value={
                sourceLanguage
              }

              onChange={
                handleSourceLanguageChange
              }

            />

          </div>


          {/* Swap Button */}

          <div
            className="
              flex
              justify-center
              items-end
              lg:pb-0
            "
          >

            <button

              type="button"

              onClick={
                swapLanguages
              }

              title="Swap languages"

              className="
                p-3
                rounded-full
                bg-indigo-600
                text-white
                hover:bg-indigo-700
                hover:rotate-180
                transition
                duration-300
              "
            >

              <ArrowLeftRight
                size={20}
              />

            </button>

          </div>


          {/* Target Language */}

          <div>

            <label
              className="
                block
                text-sm
                font-bold
                text-gray-600
                mb-2
              "
            >

              Translate to

            </label>


            <LanguageSelector

              value={
                targetLanguage
              }

              disabled={true}

            />

          </div>

        </div>


        {/* Text Areas */}

        <div
          className="
            grid
            lg:grid-cols-2
            gap-6
            mt-8
          "
        >


          {/* Input */}

          <div>

            <div
              className="
                flex
                justify-between
                items-center
                mb-2
              "
            >

              <h3
                className="
                  font-bold
                  text-gray-700
                "
              >

                {sourceLanguage}

              </h3>


              <span
                className="
                  text-sm
                  text-gray-400
                "
              >

                {source.length}/500

              </span>

            </div>


            <textarea

              rows={10}

              maxLength={500}

              value={source}

              onChange={(event) =>
                setSource(
                  event.target.value
                )
              }

              onInput={autoResize}

              placeholder={
                `Enter ${sourceLanguage} text here...`
              }

              className="
                w-full
                min-h-[250px]
                resize-none
                border
                border-gray-200
                rounded-2xl
                p-5
                outline-none
                focus:ring-2
                focus:ring-indigo-500
                transition
              "

            />

          </div>


          {/* Output */}

          <div>

            <div
              className="
                flex
                justify-between
                items-center
                mb-2
              "
            >

              <h3
                className="
                  font-bold
                  text-gray-700
                "
              >

                {targetLanguage}

              </h3>


              <span
                className="
                  text-sm
                  text-gray-400
                "
              >

                {target.length} characters

              </span>

            </div>


            <textarea

              rows={10}

              value={target}

              readOnly

              placeholder={
                "Your translation will appear here..."
              }

              className="
                w-full
                min-h-[250px]
                resize-none
                border
                border-gray-200
                rounded-2xl
                p-5
                outline-none
                bg-gray-50
                text-gray-700
              "

            />


            {/* Copy Button */}

            <button

              type="button"

              onClick={
                copyTranslation
              }

              className="
                mt-3
                flex
                items-center
                gap-2
                text-indigo-600
                font-semibold
                hover:text-indigo-800
              "
            >

              <Copy
                size={18}
              />

              Copy translation

            </button>

          </div>

        </div>


        {/* Buttons */}

        <div
          className="
            mt-8
            flex
            flex-col
            md:flex-row
            gap-4
          "
        >


          <div
            className="
              flex-1
            "
          >

            <TranslateButton

              loading={
                loading
              }

              onClick={
                handleTranslate
              }

            />

          </div>


          <button

            type="button"

            onClick={
              clearTranslation
            }

            className="
              px-6
              py-4
              rounded-3xl
              bg-gray-100
              text-gray-700
              font-bold
              flex
              items-center
              justify-center
              gap-2
              hover:bg-gray-200
              transition
            "
          >

            <Trash2
              size={20}
            />

            Clear

          </button>

        </div>


        {/* Loading Indicator */}

        {loading && (

          <div
            className="
              flex
              justify-center
              mt-6
            "
          >

            <div
              className="
                w-8
                h-8
                border-4
                border-indigo-600
                border-t-transparent
                rounded-full
                animate-spin
              "
            />

          </div>

        )}

      </div>

    </div>

  );

}