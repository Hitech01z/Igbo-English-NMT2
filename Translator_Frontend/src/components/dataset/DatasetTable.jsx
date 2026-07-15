const rows = [

{

igbo:"Onye ọrụ ugbo gara n'ubi.",

english:"The farmer went to the farm.",

domain:"Agriculture"

},

{

igbo:"Akwụkwọ ahụ dị mma.",

english:"The book is good.",

domain:"Education"

}

];

export default function DatasetTable(){

return(

<div className="overflow-x-auto rounded-2xl bg-white shadow">

<table className="w-full">

<thead className="bg-blue-600 text-white">

<tr>

<th className="p-4 text-left">Igbo</th>

<th className="p-4 text-left">English</th>

<th className="p-4 text-left">Domain</th>

</tr>

</thead>

<tbody>

{rows.map((item,index)=>(

<tr
key={index}
className="border-b hover:bg-gray-50"
>

<td className="p-4">

{item.igbo}

</td>

<td className="p-4">

{item.english}

</td>

<td className="p-4">

<span className="px-3 py-1 rounded-full bg-blue-100 text-blue-700">

{item.domain}

</span>

</td>

</tr>

))}

</tbody>

</table>

</div>

)

}