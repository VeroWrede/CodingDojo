var mins;
var hrs;
var period;
var insert;
var time;

if (mins > 45) 
{
    insert = 'quarter to';
    hours += 1;
}
else if (mins > 30)
{
    insert = 'almost';
    hrs += 1;
}else{
    insert = 'just after';
}

if (period == 'am')
{
    time = 'in the morning'
}
else 
{
    time = 'in the evening'
}

console.log('it is ', insert, hrs, time);



