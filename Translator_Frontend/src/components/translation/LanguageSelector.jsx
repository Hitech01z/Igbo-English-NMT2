export default function LanguageSelector({
  value,
  onChange,
  disabled = false,
}) {
  return (
    <select
      value={value}
      onChange={(e) => onChange?.(e.target.value)}
      disabled={disabled}
      className="
        w-full
        border
        border-gray-200
        rounded-xl
        px-4
        py-3
        bg-white
        font-semibold
        text-gray-700
        outline-none
        focus:ring-2
        focus:ring-indigo-500
        disabled:bg-gray-100
        disabled:cursor-not-allowed
      "
    >
      <option value="English">English</option>
      <option value="Igbo">Igbo</option>
    </select>
  );
}