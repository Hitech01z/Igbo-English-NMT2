import { motion } from "framer-motion";

export default function StatCard({

icon,

title,

value,

color

}){

return(

<motion.div

whileHover={{scale:1.04}}

className="rounded-2xl bg-white shadow-lg p-6"

>

<div className="flex justify-between items-center">

<div>

<p className="text-gray-500">

{title}

</p>

<h2 className="text-4xl font-bold mt-2">

{value}

</h2>

</div>

<div

className={`w-14 h-14 rounded-xl flex items-center justify-center ${color}`}

>

{icon}

</div>

</div>

</motion.div>

)

}