export default function Button({
  children,
  ...props
}) {
  return (
    <button
      {...props}
      className="
        rounded-2xl
        bg-blue-600
        hover:bg-blue-700
        px-6
        py-3
        text-white
        font-medium
        transition
      "
    >
      {children}
    </button>
  );
}