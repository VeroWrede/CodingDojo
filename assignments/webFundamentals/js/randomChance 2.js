function GenerateRandomNumOfCoins(){
  var amount = Math.floor(Math.random()*50) + 51;
  return  amount;
}

function GenerateRandomNum(){
  var num = Math.floor(Math.random()*101) ;
  return num;
}

function WinOrLoss(){
  var winningNumber = GenerateRandomNum();
  var randomNumber = GenerateRandomNum();
  var outcome = false;
  if(winningNumber == randomNumber){
    outcome = true;
  }
  return outcome;
}

function Game(){
  var myMoney = GenerateRandomNumOfCoins();
  var gameCount = 0;
  while (myMoney > 0) {
    myMoney --;
    gameCount ++;
    var win = WinOrLoss();
    if (win == true) {
      var prize = GenerateRandomNumOfCoins();
      console.log('----------------------------');
      console.log('you won ', prize, ' coins!');
      console.log('----------------------------');
      myMoney += prize;
    }
    console.log('this was game #', gameCount, ' you have ',myMoney, ' coins');

  }
}

Game()
