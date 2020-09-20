document.addEventListener("DOMContentLoaded", function () {
  //Use user_type button to give a status to user.
  document
    .querySelector("#w_message")
    .addEventListener("click", () => user_info(user_id));
});

function user_info(user_id) {
  userId = user_id;
  console.log("reach message - user_id", userId);
  // Get request by id.
  fetch(`user_info/${userId}`)
    .then((response) => response.json())
    .then((response) => writeMessage(response));
  //Prevent reloading the page
  return false;
}

function writeMessage(response) {
  console.log("response writeMessage ", response);
  response = JSON.parse(response);
  // Get values from input to update content and from user_info to update owner.
  let new_message = document.getElementById("message").value;
  let new_owner = response.username;

  //POST request to create message.
  // fetch(`/new_message`, {
  //   method: "POST",
  //   body: JSON.stringify({
  //     owner: new_owner,
  //     content: new_message,
  //   }),
  // })
  //   .then((response) => response.json())
  //   .then((result) => {
  //     console.log("result ->", result);
  //   });

  //Prevent reloading the page
  return false;
}
