import { Database } from "lucide-react";

export default function EmptyState(){

return(

<div className="text-center py-20">

<Database size={60} className="mx-auto text-gray-400"/>

<h2 className="mt-5 text-xl font-semibold">

No Records Found

</h2>

<p className="text-gray-500 mt-2">

Nothing available yet.

</p>

</div>

)

}