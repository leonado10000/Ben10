img_c = 1
function next(n){
    //to move left
    
    off(document.querySelector(`.img${img_c}`));
    off(document.querySelector(`.cont${img_c}`));
    
    if (n==0){
        if(img_c == 1){
            img_c = 10
        }
        else{
            img_c -= 1;
        }
    }
    if (n == 1){
        if(img_c == 10){
            img_c = 1
        }
        else{
            img_c += 1;
        }
    }
    //document.querySelector(`.img${img_c}`).className +=" w3-container w3-center w3-animate-right";
    on(document.querySelector(`.img${img_c}`));
    on(document.querySelector(`.cont${img_c}`));

}