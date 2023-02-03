alert("pixie");
addEventListener("DOMContentLoaded", function () {
    
    document.querySelectorAll(".Alien").forEach( k => {
        off(k);
    })
    on(document.querySelector(".cont1"));
    on(document.querySelector(".img1"))
})

function on(x){
    x.style.display = "block";
}
function off(x){
    x.style.display = "none";
}