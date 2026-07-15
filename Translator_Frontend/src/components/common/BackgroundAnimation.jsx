export default function BackgroundAnimation(){

return(

<div className="fixed inset-0 -z-10 overflow-hidden">

<div className="absolute w-96 h-96 bg-blue-500 opacity-10 rounded-full blur-3xl top-10 left-10 animate-pulse"/>

<div className="absolute w-[450px] h-[450px] bg-purple-500 opacity-10 rounded-full blur-3xl bottom-0 right-0 animate-pulse"/>

</div>

)

}