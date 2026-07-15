import { NavLink } from "react-router-dom";
import { Menu, X, Moon, Sun } from "lucide-react";
import { motion } from "framer-motion";
import { useState } from "react";

const links = [
  { name: "Home", path: "/" },
  { name: "Dashboard", path: "/dashboard" },
  { name: "Translation", path: "/translation" },
  { name: "Dataset", path: "/dataset" },
  { name: "History", path: "/history" },
  { name: "Contribute", path: "/contribute" },
  { name: "About", path: "/about" },
];

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [dark, setDark] = useState(false);

  return (
    <motion.nav
      initial={{ y: -80 }}
      animate={{ y: 0 }}
      className="sticky top-0 z-50 backdrop-blur-md bg-white/70 border-b border-gray-200"
    >
      <div className="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center">

        <div className="flex items-center gap-3">

          <div className="w-10 h-10 rounded-full bg-gradient-to-r from-blue-600 to-purple-600 flex items-center justify-center text-white font-bold">
            AI
          </div>

          <div>
            <h1 className="font-bold text-lg">
              IgboNMT
            </h1>
            <p className="text-xs text-gray-500">
              Group B
            </p>
          </div>

        </div>

        <div className="hidden lg:flex gap-8">

          {links.map((item) => (

            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                isActive
                  ? "text-blue-600 font-semibold"
                  : "text-gray-600 hover:text-blue-600 transition"
              }
            >
              {item.name}
            </NavLink>

          ))}

        </div>

        <div className="flex items-center gap-4">

          <button
            onClick={() => setDark(!dark)}
            className="p-2 rounded-full bg-gray-100"
          >
            {dark ? <Sun size={18}/> : <Moon size={18}/>}
          </button>

          <button
            className="lg:hidden"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            {menuOpen ? <X/> : <Menu/>}
          </button>

        </div>

      </div>

      {menuOpen && (

        <motion.div
          initial={{ opacity:0 }}
          animate={{ opacity:1 }}
          className="lg:hidden bg-white border-t"
        >

          {links.map(link => (

            <NavLink
              key={link.path}
              to={link.path}
              className="block px-6 py-4 hover:bg-gray-50"
            >
              {link.name}
            </NavLink>

          ))}

        </motion.div>

      )}

    </motion.nav>
  );
}