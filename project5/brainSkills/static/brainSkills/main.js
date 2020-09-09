document.addEventListener("DOMContentLoaded", function () {
  //Use user_type button to give a status to user.
  document
    .querySelector("#student")
    .addEventListener("click", () => change_user_status("student"));
  document
    .querySelector("#teacher")
    .addEventListener("click", () => change_user_status("teacher"));
  document
    .querySelector("#guest")
    .addEventListener("click", () => change_user_status("guest"));
});

function change_user_status(status) {
  //Change status according to the select button.
  if (status === student) {
  }
}
