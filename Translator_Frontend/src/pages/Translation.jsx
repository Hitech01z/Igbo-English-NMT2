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
          text-4xl
          md:text-5xl
          font-black
          mb-3
        "
      >

        Translate

      </h1>


      <p
        className="
          text-gray-500
          mb-10
        "
      >

        Translate between English and Igbo
        using our neural machine translation model.

      </p>


      <TranslatorBox />

    </div>

  );

}