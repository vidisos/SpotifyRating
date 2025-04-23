function signupData(){
    //this might prevent automatic refreshing
    //function signupData(event)
    //event.preventDefault()
    
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    var confirmPassword = document.getElementById("confirmPassword").value
    var errorBox = document.getElementById("errorBox")
    console.log(username, password, confirmPassword, errorBox)

    if (password != confirmPassword){
        errorBox.innerHTML = "Passwords don't match"
        return //if the passwords dont match then it doesnt do anything with the server and sends an error
    }

    $.ajax({
        url: "/signupData",
        type: "GET",         
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