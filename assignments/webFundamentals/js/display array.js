function displayArr(ary, symb, param) {
    if (param == true){
        for(var idx = ary.length-1; idx >= 0; idx--){
            console.log(idx, symb, ary[idx]); 
        }
    }
    else{ 
        for (var idx = 0; idx < ary.length; idx++){
            console.log(idx, symb, ary[idx]);
            
        }
    } 
    
}

ary1 = ['Mina', 'Pat', 'Lennard'];

displayArr(ary1, '**',true)