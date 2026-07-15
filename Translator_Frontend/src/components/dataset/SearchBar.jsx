import { Search } from "lucide-react";

export default function SearchBar() {

return(

<div className="relative">

<Search
className="absolute left-4 top-4 text-gray-400"
/>

<input

type="text"

placeholder="Search sentence..."

className="w-full border rounded-xl py-3 pl-12 pr-4"

/>

</div>

)

}