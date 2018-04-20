

function countMoney(goal)
{
    var count = 1;
    var reached = false;
    var amount = goal.startingAmount;
    var limit = goal.wantedAmount;

    while(count <= 30)
    {
        amount *= 2;
        count ++;
        if(amount >= limit && reached == false)
        {
            console.log(amount, ' reached after: ', count, ' days');
            reached = true;
            // starting at 0.01$: 10485.76 ' reached after: ' 21 ' days
        }
    }
    
    console.log('amount after 30 days: ',amount);
    // amount after 30 days:   10737418.24
};

var object1 = {
    days : 30,
    startingAmount : 0.0001,
    wantedAmount : 10000
}

console.log(countMoney(object1));






