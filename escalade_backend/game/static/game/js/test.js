var pointsText = parseInt(document.getElementById("pointsText").innerText);
const answerSpace = document.getElementById("answer-space");

const reRoll = document.getElementById("reroll");
const sneakPeek = document.getElementById("sneak-peek");
const hint = document.getElementById("hint");
const proceed = document.getElementById("continue");
const closeButton = document.querySelector(".close");

const popup = document.querySelector(".popup");
const popupContent = document.querySelector(".popup .content");
const popupBoosterGif = document.getElementById("boosterGif3");
const popupMonsterGif = document.getElementById("monsterGif3");
const popupNoneGif = document.getElementById("noneGif1");

const points = document.querySelector(".points");
const middle_cont = document.querySelector(".middle-container");
const bottom_cont = document.querySelector(".bottom-container");
const middle_cont2 = document.querySelector(".middle-container2");
const bottom_cont2 = document.querySelector(".bottom-container2");
const grid_cont = document.querySelector(".grid-container");

const tickMarkGif1 = document.getElementById('tickMarkGif1');
const tickMarkGif2 = document.getElementById('tickMarkGif2');
const monsterGif1 = document.getElementById('monsterGif1');
const monsterGif2 = document.getElementById('monsterGif2');
const boosterGif1 = document.getElementById('boosterGif1');
const boosterGif2 = document.getElementById('boosterGif2');
const prevLocText = document.getElementById('prevLocText');
const nextLocText = document.getElementById('nextLocText');
const currLocText = document.getElementById('currLocText');
const beforeLocText = document.getElementById('beforeLocText')

const answerForm = document.querySelector('.answer')

const hintLoading = document.getElementById("hintLoading");
const reRollLoading = document.getElementById("reRollLoading");
const sneakPeekLoading = document.getElementById("sneakPeekLoading");
const formSubmitLoading = document.getElementById("formSubmitLoading");

reRoll.addEventListener("click", function () {
  // popup.classList.remove("hidden");
  if(pointsText>=15) {
    reRoll.classList.add("hidden");
    reRollLoading.classList.remove("hidden");
      fetchReRoll();
  }
});

sneakPeek.addEventListener("click", function () {
  // popup.classList.remove("hidden");
  if(pointsText>=25) {
    sneakPeek.classList.add("hidden");
    sneakPeekLoading.classList.remove("hidden");
      fetchSneakPeak();
  }
});

hint.addEventListener("click", function () {
  if(pointsText>=10) {
    hint.classList.add("hidden");
    hintLoading.classList.remove("hidden");
      fetchHint();
  }
});

proceed.addEventListener("click", function () {
  // popup.classList.remove("hidden");
  middle_cont.classList.add("hidden");
  bottom_cont.classList.add("hidden");
  grid_cont.classList.remove("hidden");
  // middle_cont2.classList.remove("hidden");
  // bottom_cont2.classList.remove("hidden");
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
  popup.style.background = "rgba(31, 31, 31, 0.979)";
  popupContent.innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  pointsText = data.points;
  popupMonsterGif.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popup.classList.remove("hidden");
  popupContent.classList.remove("hidden");
  hintLoading.classList.add("hidden");
  hint.classList.remove("hidden");
  setButtonsByPoints();
}

async function fetchSneakPeak() {
  let response = await fetch('/sneak-peak/', options);
  let data = await response.json();
  console.log(data)
  // popupContent.innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  pointsText = data.points;
  popup.classList.remove("hidden");
  popupMonsterGif.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popupContent.classList.add("hidden");
  if(data.value=='monster') {
    popup.style.backgroundImage = "url('../../static/game/img/bg_none.jpg')";
    // popupContent.innerHTML = "There is a Monster ahead!";
    popupMonsterGif.classList.remove("hidden");
  }
  else if(data.value=='none') {
    popup.style.backgroundImage = 'url("../../static/game/img/nonebg2.jpg")';
    // popupContent.innerHTML = "Nothing ahead.";
    popupNoneGif.classList.remove("hidden");
    
  }
  else if(data.value=='booster') {
    popup.style.backgroundImage = "url('../../static/game/img/Star.jpg')";
    // popupContent.innerHTML = "There is a Booster ahead!";
    popupBoosterGif.classList.remove("hidden");
  }
  sneakPeekLoading.classList.add("hidden");
  sneakPeek.classList.remove("hidden");
  setButtonsByPoints();
}

async function fetchReRoll() {
  let response = await fetch('/re-roll/', options);
  let data = await response.json();
  console.log(data)
  document.getElementById("diceResult").innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>"
  pointsText = data.points;
  rollDice();
  reRollLoading.classList.add("hidden");
  reRoll.classList.remove("hidden");
  setButtonsByPoints();
}

wrongAnsLabel.addEventListener("click", function () {
  answerSpace.focus();
});

answerSpace.addEventListener("focus", function() {
  wrongAnsLabel.classList.add("hidden");
});

const normaliseCorrectAns = function() {
  tickMarkGif1.classList.add("hidden");
  tickMarkGif2.classList.add("hidden");
  prevLocText.classList.remove("hidden");
  nextLocText.classList.remove("hidden");
  proceed.classList.remove("hidden");
  reRoll.style.pointerEvents = 'auto';
  sneakPeek.style.pointerEvents = 'auto';
  proceed.style.pointerEvents = 'auto';
  dice.style.pointerEvents = 'auto';
  setButtonsByPoints();
};

const correctAnswer = function() {
  tickMarkGif1.classList.remove("hidden");
  tickMarkGif2.classList.remove("hidden");
  prevLocText.classList.add("hidden");
  nextLocText.classList.add("hidden");
  reRoll.style.pointerEvents = 'none';
  sneakPeek.style.pointerEvents = 'none';
  proceed.style.pointerEvents = 'none';
  dice.style.pointerEvents = 'none';
  console.log("ask");
  setTimeout(normaliseCorrectAns, 2500);
};

const currentLocation = function() {
  beforeLocText.classList.add("hidden");
  currLocText.classList.remove("hidden");
};

const beforeLocation = function() {
  currLocText.classList.add("hidden");
  beforeLocText.classList.remove("hidden");
  setTimeout(currentLocation, 2500);
};

const normaliseMonster = function() {
  monsterGif1.classList.add("hidden");
  monsterGif2.classList.add("hidden");
  prevLocText.classList.remove("hidden");
  nextLocText.classList.remove("hidden");
};

const monsterReached = function() {
  monsterGif1.classList.remove("hidden");
  monsterGif2.classList.remove("hidden");
  prevLocText.classList.add("hidden");
  nextLocText.classList.add("hidden");
  setTimeout(normaliseMonster, 4000);
};

const normaliseBooster = function() {
  boosterGif1.classList.add("hidden");
  boosterGif2.classList.add("hidden");
  prevLocText.classList.remove("hidden");
  nextLocText.classList.remove("hidden");
};

const boosterReached = function() {
  boosterGif1.classList.remove("hidden");
  boosterGif2.classList.remove("hidden");
  prevLocText.classList.add("hidden");
  nextLocText.classList.add("hidden");
  setTimeout(normaliseBooster, 4000);
};

const display = function(){
  document.querySelector(".wrapper").classList.add("hidden");
  document.querySelector("#main_body").classList.remove("hidden");
};

answerForm.addEventListener('submit', function() {
  formSubmitLoading.classList.remove("hidden");
  answerSpace.classList.add("hidden");
})

const setButtonsByPoints = function() {
  if(pointsText<25) {
    sneakPeek.style.pointerEvents = 'none';
  }
  if(pointsText<15) {
    reRoll.style.pointerEvents = 'none';
  }
  if(pointsText<10) {
    hint.style.pointerEvents = 'none';
  }
};

setButtonsByPoints();
