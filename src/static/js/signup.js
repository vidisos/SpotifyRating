function signupData(){
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    var confirmPassword = document.getElementById("confirmPassword").value
    var errorBox = document.getElementById("errorBox")
    console.log(username, password, confirmPassword, errorBox)

    if (password != confirmPassword){
        errorBox.innerHTML = "Passwords don't match"
        return //if the passwords dont match then it doesnt send anything to the server and sends an error
    }

    $.ajax({
        url: "/signupData",
        type: "POST",         
        data: { 
            username: username,
            password: password,
            confirmPassword: confirmPassword
        },  
        success: function( response ) {
            if (response.user_signed_up){
                window.location.href = "/";
            }
            errorBox.innerHTML = response.error;

            console.log(response)
        }
    });
}