import Navbar from "../components/common/Navbar";
import Footer from "../components/common/Footer";
import BackgroundAnimation from "../components/common/BackgroundAnimation";
import { Outlet } from "react-router-dom";

export default function MainLayout(){

return(

<>

<BackgroundAnimation/>

<Navbar/>

<main className="min-h-screen max-w-7xl mx-auto px-6 py-10">

<Outlet/>

</main>

<Footer/>

</>

)

}