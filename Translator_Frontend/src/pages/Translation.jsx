import TranslatorBox
from "../components/translation/TranslatorBox";

export default function Translation() {

  return (

    <div
      className="
      max-w-7xl
      mx-auto
      px-6
      py-10
    "
    >

      <h1
        className="
        text-5xl
        font-black
        mb-10
      "
      >
        Translate
      </h1>

      <TranslatorBox />

    </div>

  );

}