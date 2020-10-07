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

//Forms are at risk for Cross Site Request Forgeries (CSRF) attacks. When it comes to AJAX requests, we need to add custom header that includes the token to watch our back.

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      // Only send the token to relative URLs i.e. locally.
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    }
  },
});

// Block to get cookie with javaScript only.

function getCookie(c_name) {
  if (document.cookie.length > 0) {
    c_start = document.cookie.indexOf(c_name + "=");
    if (c_start != -1) {
      c_start = c_start + c_name.length + 1;
      c_end = document.cookie.indexOf(";", c_start);
      if (c_end == -1) c_end = document.cookie.length;
      return unescape(document.cookie.substring(c_start, c_end));
    }
  }
  return "";
}

function writeMessage(response) {
  console.log("response writeMessage ", response);
  response = JSON.parse(response);
  let userID = response.user_id;
  console.log("USERID ", userID);
  // Get values from input to update content and from user_info to update owner.
  let new_message = document.getElementById("message").value;
  let new_owner = response.username;
  console.log(`owner: ${new_owner} message: ${new_message}`);

  //Callback to activate alert.
  messageSent();

  //POST request to create message.
  fetch(
    `user_info/${userID}`,
    {
      method: "POST",
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      body: JSON.stringify(document.getElementById("message").value),
    },
    console.log("FETCH POST DONE")
  )
    .then((response) => response.json())
    .then((result) => {
      console.log("result ->", result);
    });
  //Prevent reloading the page
  return false;
}

function messageSent() {
  alert("Message sent successfully. Thank you!");
}
