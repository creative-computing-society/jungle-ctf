let dice = document.getElementById("dice");
let dice2 = document.getElementById("dice2");
var outputDiv = document.getElementById("diceResult");

function rollDice() {
  let result = outputDiv.innerText;
  // let result = 5;
  //   let result = {{result}};
  dice.dataset.side = result;
  dice.classList.toggle("reRoll");
  dice2.dataset.side = result;

  console.log(result);

  // outputDiv.classList.remove("reveal");
  // outputDiv.classList.add("hide");
  // outputDiv.innerHTML = "You've got " + result;
  // setTimeout(function () {
  //   outputDiv.classList.add("reveal");
  // }, 1500);
}

dice.addEventListener("click", rollDice);
