function loginData(){
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    var errorBox = document.getElementById("errorBox")

    $.ajax({
        url: "/loginData",
        type: "GET",         
        data: { 
            username: username,
            password: password,
        },  
        success: function( response ) {
            //gets "user_logged_in" from the response
            if (response.user_logged_in){  
                window.location.href = "/";
            }
            errorBox.innerHTML = response.error;

            console.log(response)
        }
    });
}