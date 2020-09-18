document.addEventListener("DOMContentLoaded", function () {
  //Use user_type button to give a status to user.
  document
    .querySelector("#w_message")
    .addEventListener("click", () => write_message(user_id));
});

function write_message(user_id) {
  userId = user_id;
  console.log("reach message - user_id", userId);
  // Get request by id.
  fetch(`/user_info/${userId}`)
    .then((response) => response.json())
    .then((response) => {
      if (response) {
        console.log("response ", response);
      } else {
        console.log("not found");
      }
    });
  return false;
}
