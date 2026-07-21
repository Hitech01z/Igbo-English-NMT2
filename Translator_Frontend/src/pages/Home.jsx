import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div>
      <section className="relative overflow-hidden bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-700 text-white">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8 lg:py-28">
          <div className="grid items-center gap-10 lg:grid-cols-2 lg:gap-12">
            <div className="text-center lg:text-left">
              <motion.h1
                initial={{ opacity: 0, y: 40 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-4xl font-bold leading-tight sm:text-5xl lg:text-6xl"
              >
                English ↔ Igbo
                <br />
                Neural Machine
                <br />
                Translation
              </motion.h1>

              <p className="mx-auto mt-6 max-w-xl text-base text-blue-100 sm:mt-8 sm:text-lg lg:mx-0">
                A Transformer-based Neural Machine Translation System powered by
                Self-Attention Mechanism.
              </p>

              <div className="mt-8 flex flex-col gap-3 sm:mt-10 sm:flex-row sm:gap-5 lg:justify-start">
                <Link
                  to="/translation"
                  className="w-full rounded-xl bg-white px-6 py-3 text-center font-semibold text-blue-700 shadow-lg transition hover:scale-[1.01] sm:w-auto sm:px-8 sm:py-4"
                >
                  Start Translating
                </Link>

                <Link
                  to="/dataset"
                  className="flex w-full items-center justify-center gap-2 rounded-xl border border-white/80 px-6 py-3 transition hover:bg-white/10 sm:w-auto sm:px-8 sm:py-4"
                >
                  Explore Dataset
                  <ArrowRight size={18} />
                </Link>
              </div>
            </div>

            <div className="flex justify-center">
              <div className="flex aspect-square w-full max-w-[18rem] items-center justify-center rounded-full bg-white/10 backdrop-blur-lg sm:max-w-[22rem] lg:max-w-[24rem]">
                <div className="aspect-square w-[75%] rounded-full bg-gradient-to-r from-sky-400 to-purple-500 animate-pulse" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}