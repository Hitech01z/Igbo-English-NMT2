import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";

export default function Home() {
  return (
    <div>
      <section className="relative overflow-hidden bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-700 text-white">
        <div className="max-w-7xl mx-auto px-6 py-28">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <motion.h1
                initial={{ opacity: 0, y: 40 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-6xl font-bold leading-tight"
              >
                English ↔ Igbo
                <br />
                Neural Machine
                <br />
                Translation
              </motion.h1>

              <p className="mt-8 text-blue-100 text-lg">
                A Transformer-based Neural Machine Translation System powered by
                Self-Attention Mechanism.
              </p>

              <div className="mt-10 flex gap-5">
                <button className="px-8 py-4 rounded-xl bg-white text-blue-700 font-semibold">
                  Start Translating
                </button>

                <button className="px-8 py-4 rounded-xl border border-white flex items-center gap-2">
                  Explore Dataset
                  <ArrowRight size={18} />
                </button>
              </div>
            </div>

            <div className="flex justify-center">
              <div className="w-96 h-96 rounded-full bg-white/10 backdrop-blur-lg flex items-center justify-center">
                <div className="w-72 h-72 rounded-full bg-gradient-to-r from-sky-400 to-purple-500 animate-pulse" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}