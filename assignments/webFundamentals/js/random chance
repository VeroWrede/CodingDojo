

var amount = Math.floor(Math.random()*50) + 51;
var gameCount = 0;

while(amount > 0){
  amount --;
  var winningNumber = Math.floor(Math.random()*101);
  var randomNumber = Math.floor(Math.random()*101);

  if(winningNumber == randomNumber){
    var win = Math.floor(Math.random()*50) + 51;
    console.log('----------------------------');
    console.log('you won ', win, ' coins!');
    console.log('----------------------------');

    amount += win;
  }
  gameCount ++
  console.log('this is game #', gameCount, ' you have ',amount, ' coins');
}
