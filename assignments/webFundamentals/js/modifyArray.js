var ary = [2, 'word', 4, true, 6, 'uon'];
console.log('len is  ',ary.length);


for(var idx = 0; idx < ary.length; idx++){

  if(typeof ary[idx] != 'number'){
    ary.splice(idx, 1);
  }
  console.log(ary);
}
