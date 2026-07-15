import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const data = [
  { name: "Agriculture", value: 180 },
  { name: "Health", value: 160 },
  { name: "Education", value: 220 },
  { name: "Technology", value: 140 },
  { name: "Culture", value: 222 },
];

const COLORS = [
  "#2563EB",
  "#7C3AED",
  "#38BDF8",
  "#8B5CF6",
  "#06B6D4",
];

export default function DomainChart() {
  return (
    <div className="bg-white rounded-2xl shadow p-6 h-[350px]">
      <h2 className="font-semibold mb-4">
        Dataset Distribution
      </h2>

      <ResponsiveContainer width="100%" height="100%">
        <PieChart>

          <Pie
            data={data}
            dataKey="value"
            outerRadius={120}
          >

            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index]}
              />
            ))}

          </Pie>

          <Tooltip />

        </PieChart>

      </ResponsiveContainer>

    </div>
  );
}