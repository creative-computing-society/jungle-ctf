const errorTeamName = document.querySelectorAll(".errTeamName");
const errorPassword = document.querySelectorAll(".errPassword");

const popTeamName = function () {
  errorTeamName[0].classList.toggle("hidden");
  errorTeamName[1].classList.toggle("hidden");
};

const popPassword = function () {
  errorPassword[0].classList.toggle("hidden");
  errorPassword[1].classList.toggle("hidden");
};

// popTeamName();
popPassword();
