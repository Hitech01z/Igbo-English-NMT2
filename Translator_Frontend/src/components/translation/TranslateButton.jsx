import { Languages } from "lucide-react";

export default function TranslateButton({
  loading,
  onClick,
  disabled = false,
}) {
  return (
    <button
      onClick={onClick}
      disabled={loading || disabled}
      className="
        w-full
        py-4
        rounded-3xl
        bg-gradient-to-r
        from-indigo-600
        to-violet-600
        text-white
        font-bold
        flex
        items-center
        justify-center
        gap-3
        hover:scale-[1.02]
        transition
        disabled:opacity-60
        disabled:cursor-not-allowed
        disabled:hover:scale-100
      "
    >
      <Languages size={20} />

      {loading ? "Translating..." : "Translate"}
    </button>
  );
}