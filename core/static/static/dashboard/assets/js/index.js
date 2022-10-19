document.getElementById('submit').addEventListener('click', function (e) {
    checkData(e);
});

var newPass = document.getElementById("id_new_password1");
var compass = document.getElementById("id_new_password2");

function checkData(e) {
    var newPassValue = newPass.value.trim();
    var comPassValue = compass.value.trim();
    if (newPassValue !== comPassValue) {
        e.preventDefault();
        var error = document.getElementById("error")
        error.innerHTML = "New Password and confirm password does not match."
        error.className = "alert alert-danger"
    }
}