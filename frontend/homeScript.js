const popupContainer = document.querySelector(".popup-container");
const para = document.querySelectorAll(".para");

const popConvert = function () {
  popupContainer.classList.toggle("background-red");
  para[0].classList.toggle("hidden");
  para[1].classList.toggle("hidden");
};

// popConvert();

const popout = function () {
  popupContainer.classList.toggle("hidden");
};

// popout();

setTimeout(popout, 10000);
