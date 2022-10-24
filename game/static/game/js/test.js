var pointsText = parseInt(document.getElementById("pointsText").innerText);
const answerSpace = document.getElementById("answer-space");

const reRoll = document.getElementById("reroll");
const sneakPeek = document.getElementById("sneak-peek");
const hint = document.getElementById("hint");
const proceed = document.getElementById("continue");
const closeButton = document.querySelector(".close");

const reRollWrapper = document.getElementById("reRollWrapper");
const sneakPeekWrapper = document.getElementById("sneakPeekWrapper");
const hintWrapper = document.getElementById("hintWrapper");

const popup = document.querySelector(".popup");
const popupContent = document.querySelector(".popup .content");
const popupBoosterGif = document.getElementById("boosterGif3");
const popupOpposerGif = document.getElementById("opposerGif3");
const popupNoneGif = document.getElementById("noneGif1");
const popupImage = document.getElementById("popupImage");

const points = document.querySelector(".points");
const middle_cont = document.querySelector(".middle-container");
const bottom_cont = document.querySelector(".bottom-container");
const middle_cont2 = document.querySelector(".middle-container2");
const bottom_cont2 = document.querySelector(".bottom-container2");
const grid_cont = document.querySelector(".grid-container");

const tickMarkGif1 = document.getElementById('tickMarkGif1');
const tickMarkGif2 = document.getElementById('tickMarkGif2');
const opposerGif1 = document.getElementById('opposerGif1');
const opposerGif2 = document.getElementById('opposerGif2');
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

const hintPointsCost = document.getElementById("hintPointsCost");

reRoll.addEventListener("click", function () {
  if(pointsText>=15) {
    reRollWrapper.classList.add("hidden");
    reRollLoading.classList.remove("hidden");
      fetchReRoll();
  }
});

sneakPeek.addEventListener("click", function () {
  if(pointsText>=25) {
    sneakPeekWrapper.classList.add("hidden");
    sneakPeekLoading.classList.remove("hidden");
      fetchsneakPeek();
  }
});

hint.addEventListener("click", function () {
  if(pointsText>=10) {
    hintWrapper.classList.add("hidden");
    hintLoading.classList.remove("hidden");
      fetchHint();
  }
});

proceed.addEventListener("click", function () {
  middle_cont.classList.add("hidden");
  bottom_cont.classList.add("hidden");
  grid_cont.classList.remove("hidden");
});

closeButton.addEventListener("click", function () {
  popup.classList.add("hidden");
  popupOpposerGif.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popupContent.classList.add("hidden");
  popupImage.classList.add("hidden");
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
  popup.style.background = "rgba(31, 31, 31, 0.979)";
  popupContent.innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>";
  pointsText = data.points;
  popupOpposerGif.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popupImage.classList.add("hidden");
  popup.classList.remove("hidden");
  popupContent.classList.remove("hidden");
  hintLoading.classList.add("hidden");
  hintWrapper.classList.remove("hidden");
  hintPointsCost.innerHTML = "POINTS=0";
  setButtonsByPoints();
}

async function fetchsneakPeek() {
  let response = await fetch('/sneak-peek/', options);
  let data = await response.json();
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>";
  pointsText = data.points;
  popup.classList.remove("hidden");
  popupOpposerGif.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popupContent.classList.add("hidden");
  popupImage.classList.add("hidden");
  if(data.value=='opposer') {
    setSneakPeekOpposerBgImg();
    popupOpposerGif.classList.remove("hidden");
  }
  else if(data.value=='none') {
    setSneakPeekNoneBgImg();
    popupNoneGif.classList.remove("hidden");
  }
  else if(data.value=='booster') {
    setSneakPeekBoosterBgImg();
    popupBoosterGif.classList.remove("hidden");
  }
  sneakPeekLoading.classList.add("hidden");
  sneakPeekWrapper.classList.remove("hidden");
  setButtonsByPoints();
}

async function fetchReRoll() {
  let response = await fetch('/re-roll/', options);
  let data = await response.json();
  document.getElementById("diceResult").innerHTML = data.value;
  points.innerHTML = "<h2 class='text'><b>POINTS:</b> "+data.points+"</h2>";
  pointsText = data.points;
  rollDice();
  reRollLoading.classList.add("hidden");
  reRollWrapper.classList.remove("hidden");
  setButtonsByPoints();
}

answerSpace.addEventListener("focus", function() {
  answerSpace.placeholder = "";
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
  setTimeout(normaliseCorrectAns, 2500);
};

const currentLocation = function() {
  beforeLocText.classList.add("hidden");
  currLocText.classList.remove("hidden");
};

const beforeLocation = function() {
  currLocText.classList.add("hidden");
  beforeLocText.classList.remove("hidden");
  setTimeout(currentLocation, 4000);
};

const normaliseOpposer = function() {
  opposerGif1.classList.add("hidden");
  opposerGif2.classList.add("hidden");
  prevLocText.classList.remove("hidden");
  nextLocText.classList.remove("hidden");
};

const opposerReached = function() {
  opposerGif1.classList.remove("hidden");
  opposerGif2.classList.remove("hidden");
  prevLocText.classList.add("hidden");
  nextLocText.classList.add("hidden");
  setTimeout(normaliseOpposer, 4500);
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
  setTimeout(normaliseBooster, 4500);
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
    sneakPeekWrapper.style.cursor = 'not-allowed';
  }
  if(pointsText<15) {
    reRoll.style.pointerEvents = 'none';
    reRollWrapper.style.cursor = 'not-allowed';
  }
  if(pointsText<10) {
    hint.style.pointerEvents = 'none';
    hintWrapper.style.cursor = 'not-allowed';
  }
};

setButtonsByPoints();

const hintPop = document.getElementsByClassName("hint-pop")

const mouseenter = function () {
  hintPop[0].classList.add("hidden");
  hintPop[1].classList.remove("hidden");
};

const mouseleave = function () {
  hintPop[0].classList.remove("hidden");
  hintPop[1].classList.add("hidden");
};

hint.addEventListener("mouseenter", function () {
  setTimeout(mouseenter, 100);
});

hint.addEventListener("mouseleave", function () {
  setTimeout(mouseleave, 150);
});

const showPopupImage = function() {
  popupContent.classList.add("hidden");
  popupBoosterGif.classList.add("hidden");
  popupOpposerGif.classList.add("hidden");
  popupNoneGif.classList.add("hidden");
  popup.style.background = "rgba(31, 31, 31, 0.979)";
  popupImage.classList.remove("hidden");
  popup.classList.remove("hidden");
};
