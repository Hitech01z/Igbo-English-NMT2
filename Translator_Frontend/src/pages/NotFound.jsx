import { Link } from "react-router-dom";

export default function NotFound(){

return(

<div className="h-screen flex flex-col justify-center items-center">

<h1 className="text-8xl font-bold text-blue-600">

404

</h1>

<p className="mt-6">

Page not found.

</p>

<Link

to="/"

className="mt-8 bg-blue-600 text-white px-6 py-3 rounded-xl"

>

Go Home

</Link>

</div>

)

}