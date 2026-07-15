import { GitBranch, Mail, Globe } from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-slate-900 text-white mt-20">
      <div className="max-w-7xl mx-auto py-12 px-6">
        <div className="grid md:grid-cols-3 gap-10">
          <div>
            <h2 className="text-2xl font-bold">IgboNMT</h2>

            <p className="mt-4 text-slate-300">
              Transformer-based Neural Machine Translation using Self-Attention.
            </p>
          </div>

          <div>
            <h3 className="font-semibold">Navigation</h3>

            <ul className="space-y-3 mt-4">
              <li>Home</li>

              <li>Dashboard</li>

              <li>Dataset</li>

              <li>Translation</li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold">Contact</h3>

            <div className="space-y-4 mt-4">
              <div className="flex gap-3">
                <Mail />
                info@example.com
              </div>

              <div className="flex gap-3">
                <GitBranch />
                GitHub
              </div>

              <div className="flex gap-3">
                <Globe />
                Project Website
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
