const errorEmail = document.querySelectorAll(".errEmail");
const errorRoll = document.querySelectorAll(".errRoll");
const errorPhone = document.querySelectorAll(".errPhone");
const errorDiscord = document.querySelectorAll(".errDiscord");
const errorEmail1 = document.querySelectorAll(".errEmail1");
const errorRoll1 = document.querySelectorAll(".errRoll1");
const errorPhone1 = document.querySelectorAll(".errPhone1");
const errorDiscord1 = document.querySelectorAll(".errDiscord1");
const loading = document.querySelector(".center");
const submit = document.querySelector(".submit-btn");

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

const popEmail1 = function () {
  errorEmail1[0].classList.toggle("hidden");
  errorEmail1[1].classList.toggle("hidden");
};
const popRoll1 = function () {
  errorRoll1[0].classList.toggle("hidden");
  errorRoll1[1].classList.toggle("hidden");
};
const popPhone1 = function () {
  errorPhone1[0].classList.toggle("hidden");
  errorPhone1[1].classList.toggle("hidden");
};
const popDiscord1 = function () {
  errorDiscord1[0].classList.toggle("hidden");
  errorDiscord1[1].classList.toggle("hidden");
};

// popEmail();
// popPhone();
// popDiscord();
// popRoll();

// popEmail1();
// popPhone1();
// popDiscord1();
// popRoll1();

const Name = document.querySelector(".name");
// console.log(Name);
const inputName = document.querySelector(".input-name");
// console.log(inputName);
const Email = document.querySelectorAll(".email");
// console.log(Email);
const inputEmail = document.querySelector(".input-email");
// console.log(inputEmail);
const Roll = document.querySelectorAll(".roll");
// console.log(Roll);
const inputRoll = document.querySelector(".input-roll");
// console.log(inputRoll);
const Discord = document.querySelectorAll(".discord");
// console.log(Discord);
const inputDiscord = document.querySelector(".input-discord");
// console.log(inputDiscord);
const Phone = document.querySelectorAll(".phone");
// console.log(Phone);
const inputPhone = document.querySelector(".input-phone");
// console.log(inputPhone);

const Name1 = document.querySelector(".name1");
// console.log(Name1);
const inputName1 = document.querySelector(".input-name1");
// console.log(inputName1);
const Email1 = document.querySelectorAll(".email1");
// console.log(Email1);
const inputEmail1 = document.querySelector(".input-email1");
// console.log(inputEmail1);
const Roll1 = document.querySelectorAll(".roll1");
// console.log(Roll1);
const inputRoll1 = document.querySelector(".input-roll1");
// console.log(inputRoll1);
const Discord1 = document.querySelectorAll(".discord1");
// console.log(Discord1);
const inputDiscord1 = document.querySelector(".input-discord1");
// console.log(inputDiscord1);
const Phone1 = document.querySelectorAll(".phone1");
// console.log(Phone1);
const inputPhone1 = document.querySelector(".input-phone1");
// console.log(inputPhone1);

const check1 = function () {
  if (inputName.textContent === "") Name.classList.add("fix");
};
const check2 = function () {
  if (inputEmail.textContent === "") Email[0].classList.add("fix");
  if (inputEmail.textContent === "") Email[1].classList.add("fix");
};
const check3 = function () {
  if (inputRoll.textContent === "") Roll[0].classList.add("fix");
  if (inputRoll.textContent === "") Roll[1].classList.add("fix");
};
const check4 = function () {
  if (inputDiscord.textContent === "") Discord[0].classList.add("fix");
  if (inputDiscord.textContent === "") Discord[1].classList.add("fix");
};
const check5 = function () {
  if (inputPhone.textContent === "") Phone[0].classList.add("fix");
  if (inputPhone.textContent === "") Phone[1].classList.add("fix");
};

const check6 = function () {
  if (inputName1.textContent === "") Name1.classList.add("fix");
};
const check7 = function () {
  if (inputEmail1.textContent === "") Email1[0].classList.add("fix");
  if (inputEmail1.textContent === "") Email1[1].classList.add("fix");
};
const check8 = function () {
  if (inputRoll1.textContent === "") Roll1[0].classList.add("fix");
  if (inputRoll1.textContent === "") Roll1[1].classList.add("fix");
};
const check9 = function () {
  if (inputDiscord1.textContent === "") Discord1[0].classList.add("fix");
  if (inputDiscord1.textContent === "") Discord1[1].classList.add("fix");
};
const check10 = function () {
  if (inputPhone1.textContent === "") Phone1[0].classList.add("fix");
  if (inputPhone1.textContent === "") Phone1[1].classList.add("fix");
};

// inputName.addEventListener("click", check);

const renderLoading = function () {
  submit.classList.toggle("hidden");
  loading.classList.toggle("hidden");
};

const startRenderLoading = function () {
  submit.addEventListener("click", renderLoading);
};

// startRenderLoading();

// submit.addEventListener("click", startRenderLoading);

document.getElementById("formId").addEventListener("submit", function (e) {
  // if (!isValid) {
  //   e.preventDefault(); //stop form from submitting
  // }
  // if (isValid) {
    renderLoading();
  // }
  //do whatever an submit the form
});
