function steps(start, step, end)
{
    var num = start;
    if(end < start) 
    {
        
        while(num > end)
        {
            console.log(num);
            num += step;
        }
    }
    console.log('end 1');
    
    while(num < end)
    {
        console.log(num);
        num += step;
    }
}

steps(1, 3, 48)
console.log('------------------------------------');


steps(20, -3, 5)