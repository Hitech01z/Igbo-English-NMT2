import {

LineChart,

Line,

XAxis,

YAxis,

Tooltip,

CartesianGrid,

ResponsiveContainer

} from "recharts";

const data = [

{month:"Jan",pairs:80},

{month:"Feb",pairs:160},

{month:"Mar",pairs:260},

{month:"Apr",pairs:400},

{month:"May",pairs:610},

{month:"Jun",pairs:922}

];

export default function DatasetGrowthChart(){

return(

<div className="bg-white rounded-2xl shadow p-6 h-[350px]">

<h2 className="font-semibold mb-4">

Dataset Growth

</h2>

<ResponsiveContainer>

<LineChart data={data}>

<CartesianGrid strokeDasharray="3 3"/>

<XAxis dataKey="month"/>

<YAxis/>

<Tooltip/>

<Line

type="monotone"

dataKey="pairs"

stroke="#2563EB"

strokeWidth={3}

/>

</LineChart>

</ResponsiveContainer>

</div>

)

}