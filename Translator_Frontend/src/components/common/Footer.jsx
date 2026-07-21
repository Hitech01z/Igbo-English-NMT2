import { GitBranch, Mail, Globe } from "lucide-react";
import { Link } from "react-router-dom";

const navLinks = [
  { name: "Home", path: "/" },
  { name: "Dashboard", path: "/dashboard" },
  { name: "Dataset", path: "/dataset" },
  { name: "Translation", path: "/translation" },
];

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

            <ul className="mt-4 space-y-3">
              {navLinks.map((link) => (
                <li key={link.name}>
                  <Link
                    to={link.path}
                    className="transition hover:text-blue-300"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-semibold">Contact</h3>

            <div className="space-y-4 mt-4">
              <a
                href="mailto:info@example.com"
                className="flex gap-3 transition hover:text-blue-300"
              >
                <Mail />
                info@example.com
              </a>

              <a
                href="https://github.com/Hitech01z/Igbo-English-NMT2"
                target="_blank"
                rel="noreferrer"
                className="flex gap-3 transition hover:text-blue-300"
              >
                <GitBranch />
                GitHub
              </a>

              <a
                href="https://github.com/Hitech01z/Igbo-English-NMT2"
                target="_blank"
                rel="noreferrer"
                className="flex gap-3 transition hover:text-blue-300"
              >
                <Globe />
                Project Website
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
