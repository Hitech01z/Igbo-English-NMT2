import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

export default function DatasetChart({ data }) {

    const chartData = data.labels.map((label, i) => ({
        name: label,
        value: data.values[i],
    }));

    return (

        <div className="bg-white rounded-xl p-6 shadow">

            <ResponsiveContainer
                width="100%"
                height={300}
            >

                <BarChart data={chartData}>

                    <XAxis dataKey="name" />

                    <YAxis />

                    <Tooltip />

                    <Bar
                        dataKey="value"
                        fill="#6366F1"
                    />

                </BarChart>

            </ResponsiveContainer>

        </div>

    );

}