async function loadNotes(){

let res=await fetch("/notes");
let data=await res.json();

let list=document.getElementById("notes");
list.innerHTML="";

data.forEach(note=>{
let li=document.createElement("li");

li.innerHTML=note+
`<button onclick="deleteNote('${note}')">x</button>`;

list.appendChild(li);
});
}

async function addNote(){

let text=document.getElementById("noteInput").value;

await fetch("/add",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({text:text})
});

document.getElementById("noteInput").value="";
loadNotes();
}

async function deleteNote(text){

await fetch("/delete",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({text:text})
});

loadNotes();
}

loadNotes();