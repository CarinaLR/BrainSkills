document.addEventListener("DOMContentLoaded", function () {
  //Use user_type button to give a status to user.
  document
    .querySelector("#w_message")
    .addEventListener("click", () => write_message(user_id));
});

function write_message(user_id) {
  userId = user_id;
  console.log("reach message - user_id", userId);
  return false;
}
