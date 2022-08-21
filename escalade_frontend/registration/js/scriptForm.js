const errorEmail = document.querySelectorAll(".errEmail");
const errorRoll = document.querySelectorAll(".errRoll");
const errorPhone = document.querySelectorAll(".errPhone");
const errorDiscord = document.querySelectorAll(".errDiscord");
const errorTeamName = document.querySelectorAll(".errTeamName");

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
const popTeamName = function () {
  errorTeamName[0].classList.toggle("hidden");
  errorTeamName[1].classList.toggle("hidden");
};
