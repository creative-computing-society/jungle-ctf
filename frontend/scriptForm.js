const errorEmail = document.querySelectorAll(".errEmail");
const errorRoll = document.querySelectorAll(".errRoll");
const errorPhone = document.querySelectorAll(".errPhone");
const errorDiscord = document.querySelectorAll(".errDiscord");
const errorPassword = document.querySelectorAll(".errPassword");

const popEmail = function () {
  errorEmail[0].classList.toggle("hidden");
  errorEmail[1].classList.toggle("hidden");
};
const popRoll = function () {
  errorRoll[0].classList.toggle("hidden");
  errorRoll[1].classList.toggle("hidden");
};
const popPhone = function () {
  errorPhone[0].classList.toggle("hidden");
  errorPhone[1].classList.toggle("hidden");
};
const popDiscord = function () {
  errorDiscord[0].classList.toggle("hidden");
  errorDiscord[1].classList.toggle("hidden");
};
const popPassword = function () {
  errorPassword[0].classList.toggle("hidden");
  errorPassword[1].classList.toggle("hidden");
};

// popEmail();
// popRoll();
// popPhone();
// popDiscord();
// popPassword();
