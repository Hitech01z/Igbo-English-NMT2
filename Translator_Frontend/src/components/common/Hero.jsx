import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { ArrowRight, Languages, Cpu } from "lucide-react";

export default function Hero() {
  return (
    <section className="relative overflow-hidden bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 text-white">

      {/* Background Blur */}
      <div className="absolute inset-0">
        <div className="absolute left-20 top-16 h-72 w-72 rounded-full bg-blue-600/20 blur-3xl" />
        <div className="absolute right-10 bottom-10 h-72 w-72 rounded-full bg-purple-600/20 blur-3xl" />
      </div>

      <div className="relative mx-auto flex min-h-[90vh] max-w-7xl items-center px-6">

        <div className="grid items-center gap-16 lg:grid-cols-2">

          {/* LEFT */}

          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >

            <span className="rounded-full border border-blue-400 px-4 py-2 text-sm font-semibold text-blue-300">
              Group B • Self-Attention Transformer
            </span>

            <h1 className="mt-8 text-5xl font-black leading-tight lg:text-7xl">

              English ↔ Igbo

              <span className="block bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">

                Neural Machine Translation

              </span>

            </h1>

            <p className="mt-8 max-w-xl text-lg text-slate-300">

              A custom Transformer architecture implementing
              Multi-Head Self-Attention for low-resource
              English–Igbo Neural Machine Translation.

            </p>

            <div className="mt-10 flex flex-wrap gap-4">

              <Link
                to="/translation"
                className="flex items-center gap-2 rounded-xl bg-blue-600 px-8 py-4 font-semibold transition hover:bg-blue-700"
              >
                Start Translating
                <ArrowRight size={18} />
              </Link>

              <Link
                to="/dashboard"
                className="rounded-xl border border-white/20 px-8 py-4 font-semibold transition hover:bg-white/10"
              >
                View Dashboard
              </Link>

            </div>

          </motion.div>

          {/* RIGHT */}

          <motion.div
            initial={{ opacity: 0, scale: .9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: .8 }}
            className="flex justify-center"
          >

            <div className="w-full max-w-md rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

              <div className="space-y-6">

                <div className="flex items-center gap-4">

                  <div className="rounded-xl bg-blue-600 p-3">

                    <Languages />

                  </div>

                  <div>

                    <h3 className="font-bold">
                      Translation
                    </h3>

                    <p className="text-sm text-slate-400">
                      English ↔ Igbo
                    </p>

                  </div>

                </div>

                <div className="flex items-center gap-4">

                  <div className="rounded-xl bg-purple-600 p-3">

                    <Cpu />

                  </div>

                  <div>

                    <h3 className="font-bold">
                      Self-Attention
                    </h3>

                    <p className="text-sm text-slate-400">
                      Transformer Encoder–Decoder
                    </p>

                  </div>

                </div>

                <div className="rounded-2xl bg-slate-900/70 p-5">

                  <p className="text-sm text-slate-300">
                    "A custom implementation of the Transformer
                    architecture for improving English–Igbo Neural
                    Machine Translation in low-resource settings."
                  </p>

                </div>

              </div>

            </div>

          </motion.div>

        </div>

      </div>

    </section>
  );
}