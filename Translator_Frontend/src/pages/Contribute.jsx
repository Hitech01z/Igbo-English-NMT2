export default function Contribute(){

return(

<div className="max-w-4xl mx-auto">

<h1 className="text-3xl font-bold">

Contribute Dataset

</h1>

<div className="mt-8 bg-white shadow rounded-2xl p-8">

<input

placeholder="Igbo Sentence"

className="w-full border rounded-xl p-3 mb-5"

/>

<input

placeholder="English Sentence"

className="w-full border rounded-xl p-3 mb-5"

/>

<select

className="w-full border rounded-xl p-3 mb-5"

>

<option>Agriculture</option>

<option>Education</option>

<option>Health</option>

<option>Technology</option>

</select>

<button

className="w-full py-4 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 text-white"

>

Submit Contribution

</button>

</div>

</div>

)

}