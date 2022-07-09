const answerSpace = document.getElementById("answer-space");
// console.log(answerSpace);

const reRoll = document.getElementById("reroll");
const sneakPeek = document.getElementById("sneak-peek");
const hint = document.getElementById("hint");
const proceed = document.getElementById("continue");
const closeButton = document.querySelector(".close");
const popup = document.querySelector(".popup");

const popupContent = document.querySelector(".popup .content");
const points = document.querySelector(".points");
const middle_cont = document.querySelector(".middle-container");
const bottom_cont = document.querySelector(".bottom-container");
const middle_cont2 = document.querySelector(".middle-container2");
const bottom_cont2 = document.querySelector(".bottom-container2");


reRoll.addEventListener("click", function () {
  // popup.classList.remove("hidden");
    fetchReRoll();
});
sneakPeek.addEventListener("click", function () {
  // popup.classList.remove("hidden");
    fetchSneakPeak();
});
hint.addEventListener("click", function () {
    fetchHint();
});
proceed.addEventListener("click", function () {
  // popup.classList.remove("hidden");
  middle_cont.classList.add("hidden");
  bottom_cont.classList.add("hidden");
  middle_cont2.classList.remove("hidden");
  bottom_cont2.classList.remove("hidden");
});
// document.addEventListener("click", function () {
//   if (!popup.classList.contains("hidden")) {
//     popup.classList.add("hidden");
//   }
// });
closeButton.addEventListener("click", function () {
  popup.classList.add("hidden");
});


const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let options = {
    method: 'POST',
    headers: {
        'Content-Type':
            'application/json;charset=utf-8',
        'X-CSRFToken': csrftoken,
    },
}

async function fetchHint() {
  let response = await fetch('/hint/', options);
  let data = await response.json();
  console.log(data)
  popupContent.innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  popup.classList.remove("hidden");
}

async function fetchSneakPeak() {
  let response = await fetch('/sneak-peak/', options);
  let data = await response.json();
  console.log(data)
  popupContent.innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  popup.classList.remove("hidden");
}

async function fetchReRoll() {
  let response = await fetch('/re-roll/', options);
  let data = await response.json();
  console.log(data)
  document.getElementById("diceResult").innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  rollDice();
}

wrongAnsLabel.addEventListener("click", function () {
  answerSpace.focus();
});

answerSpace.addEventListener("focus", function() {
  wrongAnsLabel.classList.add("hidden");
});

