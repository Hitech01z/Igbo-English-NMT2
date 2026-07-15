import { useState } from "react";

import LanguageSelector from "./LanguageSelector";

export default function TranslatorBox(){

const[source,setSource]=useState("");

const[target,setTarget]=useState("");

return(

<div className="bg-white rounded-2xl shadow-xl p-8">

<div className="grid lg:grid-cols-2 gap-8">

<div>

<LanguageSelector/>

<textarea

rows={10}

value={source}

onChange={(e)=>setSource(e.target.value)}

className="mt-4 w-full border rounded-xl p-4"

/>

</div>

<div>

<LanguageSelector/>

<textarea

rows={10}

value={target}

readOnly

className="mt-4 w-full border rounded-xl p-4 bg-gray-50"

/>

</div>

</div>

<button

className="mt-8 px-8 py-4 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 text-white"

>

Translate

</button>

</div>

)

}