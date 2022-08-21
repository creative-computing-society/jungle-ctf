let dice = document.getElementById("dice");
let dice2 = document.getElementById("dice2");
var outputDiv = document.getElementById("diceResult");

function rollDice() {
  let result = outputDiv.innerText;
  dice.dataset.side = result;
  dice.classList.toggle("reRoll");
  dice2.dataset.side = result;
  // console.log(result);
}

dice.addEventListener("click", rollDice);
