import { AlertCircle } from "lucide-react";

export default function ErrorMessage(){

return(

<div className="bg-red-50 border border-red-200 rounded-xl p-5 flex gap-4">

<AlertCircle className="text-red-600"/>

<div>

<h3 className="font-semibold">

Something went wrong

</h3>

<p>

Please try again.

</p>

</div>

</div>

)

}