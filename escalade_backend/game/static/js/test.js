const answerSpace = document.getElementsByName("text-submit");
// console.log(answerSpace);

const reRoll = document.getElementById("reroll");
const sneakPeek = document.getElementById("sneak-peek");
const proceed = document.getElementById("continue");
const closeButton = document.querySelector(".close");
const popup = document.querySelector(".popup");
console.log(closeButton);

reRoll.addEventListener("click", function () {
  popup.classList.remove("hidden");
});
sneakPeek.addEventListener("click", function () {
  popup.classList.remove("hidden");
});
proceed.addEventListener("click", function () {
  popup.classList.remove("hidden");
});
// document.addEventListener("click", function () {
//   if (!popup.classList.contains("hidden")) {
//     popup.classList.add("hidden");
//   }
// });
closeButton.addEventListener("click", function () {
  popup.classList.add("hidden");
});
