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
  fetch(`user_info/${userId}`)
    .then((response) => console.log("The response 1-", response))
    // response.json())
    .then((response) => {
      console.log("The response 2-", response);
    });

  //POST request to create message.
  // Get value from input to update content.
  // let new_content = document.getElementById("content").value;

  // fetch(`/edit_post/${post_id}`, {
  //   method: "PUT",
  //   body: JSON.stringify({
  //     content: new_content,
  //   }),
  // })
  //   .then((response) => response.json())
  //   .then((result) => {
  //     console.log("result ->", result);
  //   });

  //Prevent reloading the page
  return false;
}
