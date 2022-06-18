
let dark = localStorage.getItem('dark');
let twice = false;






if (dark !== 'disabled'){
if (dark === 'enabled') {
  darkmode();
}
}

function darkmode(){

    let name = document.body;

    if (twice){
    name.classList.toggle("darkmode");
    localStorage.setItem('dark', 'disabled');
    twice = false;

    document.getElementById("something").innerHTML = '<i class="bi bi-moon-fill"></i>';

    }
    else if (twice == false){
    name.classList.toggle("darkmode");
    localStorage.setItem('dark', 'enabled');
    twice = true;

    document.getElementById("something").innerHTML = '<i class="bi bi-brightness-high-fill"></i>';

    }
    console.log(dark);

}



