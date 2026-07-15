export default function LanguageSelector({

value,

onChange

}){

return(

<select

value={value}

onChange={onChange}

className="w-full rounded-xl border p-3"

>

<option value="en">

English

</option>

<option value="ig">

Igbo

</option>

</select>

)

}