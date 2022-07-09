let dice = document.getElementById("dice");
var outputDiv = document.getElementById("diceResult");

function rollDice() {
  let result = Math.floor(Math.random() * (6 - 1 + 1)) + 1;
  // let result = 5;
  //   let result = {{result}};
  dice.dataset.side = result;
  dice.classList.toggle("reRoll");

  console.log(result);

  // outputDiv.classList.remove("reveal");
  // outputDiv.classList.add("hide");
  // outputDiv.innerHTML = "You've got " + result;
  // setTimeout(function () {
  //   outputDiv.classList.add("reveal");
  // }, 1500);
}

dice.addEventListener("click", rollDice);
