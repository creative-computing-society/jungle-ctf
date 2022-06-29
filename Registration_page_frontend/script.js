const single = document.querySelector(".single");
const twoMember = document.querySelector(".two-member");
const threeMember = document.querySelector(".three-member");
const form = document.querySelector(".form");

const addForm = function () {
  const html = `
            <div class="row clearfix flex-form">
                <div class="col_half">
                  <div class="input_field">
                    <span><i aria-hidden="true" class="fa fa-user"></i></span>
                    <input
                      type="text"
                      name="name"
                      placeholder="Member name"
                    />
                  </div>
                </div>
                <div class="col_half">
                  <div class="input_field">
                    <span><i aria-hidden="true" class="fa fa-user"></i></span>
                    <input
                      type="email"
                      name="email"
                      placeholder="Thapar email id"
                      required
                    />
                  </div>
                </div>
                <div class="col_half">
                  <div class="input_field">
                    <span><i aria-hidden="true" class="fa fa-user"></i></span>
                    <input
                      type="tel"
                      name="name"
                      placeholder="Phone Number"
                      required
                    />
                  </div>
                </div>
                <div class="col_half">
                  <div class="input_field">
                    <span><i aria-hidden="true" class="fa fa-user"></i></span>
                    <input
                      type="text"
                      name="name"
                      placeholder="discord id"
                      required
                    />
                  </div>
                </div>
            </div>
  `;
  form.insertAdjacentHTML("beforeend", html);
};

const addRegister = function () {
  const html = `
  <input class="button" type="submit" value="Register" />
  `;
  form.insertAdjacentHTML("beforeend", html);
};

twoMember.addEventListener("click", function () {
  console.log("click");
  //   form.classList.add("hidden");
  addForm();
  addRegister();
});

threeMember.addEventListener("click", function () {
  console.log("click");
  //   form.classList.add("hidden");
  addForm();
  addForm();
  addRegister();
});
