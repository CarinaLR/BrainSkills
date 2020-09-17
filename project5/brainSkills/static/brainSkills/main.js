document.addEventListener("DOMContentLoaded", function () {
  //Use user_type button to give a status to user.
  // document
  //   .querySelector("#student")
  //   .addEventListener("click", () => change_user_status("student"));
  // document
  //   .querySelector("#teacher")
  //   .addEventListener("click", () => change_user_status("teacher"));
  // document
  //   .querySelector("#guest")
  //   .addEventListener("click", () => change_user_status("guest"));
  document.querySelector("#edit_student").onsubmit = () => {
    console.log("I'm here");
  };
});

function change_user_status(status) {
  console.log("reach change_user_status");
  //Change status according to the select button.
  if (status === student) {
    console.log("STUDENT");
    //Load user info
    fetch("status/student")
      .then((response) => response.json())
      .then((users) => {
        console.log("student - ", users);
      });
  }
  if (status === teacher) {
    console.log("TEACHER");
    //Load user info
    fetch("status/teacher")
      .then((response) => response.json())
      .then((users) => {
        console.log("teacher - ", users);
      });
  }
  if (status === guest) {
    console.log("GUEST");
    //Load user info
    fetch("status/guest")
      .then((response) => response.json())
      .then((users) => {
        console.log("guest - ", users);
      });
  }
  return false;
}
