import { Clock } from "lucide-react";

const history=[

{

from:"English",

to:"Igbo",

text:"The farmer planted maize.",

result:"Onye ọrụ ugbo kụrụ ọka."

},

{

from:"Igbo",

to:"English",

text:"Akwụkwọ ahụ dị mma.",

result:"The book is good."

}

];

export default function History(){

return(

<div>

<h1 className="text-3xl font-bold mb-8">

Translation History

</h1>

<div className="space-y-5">

{history.map((item,index)=>(

<div

key={index}

className="bg-white rounded-xl shadow p-6"

>

<div className="flex items-center gap-3">

<Clock size={18}/>

<p>

{item.from}

↓

{item.to}

</p>

</div>

<p className="mt-4">

{item.text}

</p>

<hr className="my-4"/>

<p>

{item.result}

</p>

</div>

))}

</div>

</div>

)

}