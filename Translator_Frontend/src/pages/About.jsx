export default function About(){

return(

<div className="space-y-8">

<h1 className="text-4xl font-bold">

About This Project

</h1>

<div className="bg-white rounded-2xl shadow p-8">

<h2 className="text-2xl font-semibold">

Overview

</h2>

<p className="mt-4 text-gray-600">

This project implements an English-Igbo Neural Machine Translation system using a Transformer architecture based on the Self-Attention mechanism.

</p>

</div>

<div className="bg-white rounded-2xl shadow p-8">

<h2 className="text-2xl font-semibold">

Technology Stack

</h2>

<ul className="mt-4 list-disc pl-6">

<li>React + Vite</li>

<li>Tailwind CSS</li>

<li>FastAPI</li>

<li>PyTorch</li>

<li>Transformers</li>

<li>Self-Attention Mechanism</li>

</ul>

</div>

</div>

)

}