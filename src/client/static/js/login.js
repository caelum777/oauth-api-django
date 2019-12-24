$(function(){
    function success(data){
       console.log(data);
       Cookies.set('token', data.access_token, { expires: data.expires_in })
       window.location.replace("/details/");
    }

    function error(data){
       console.log(data);
       $("#login-error").text(data.responseJSON.error_description);
    }

    $('#loginForm').submit(function (e) {
        e.preventDefault();
        let email = $("#email").val();
        let password = $("#password").val();

        let data = {
            "email": email,
            "password": password
        };
        $.ajax({
            type: "POST",
            contentType: "application/json",
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: `/authentication/token/`,
            data: JSON.stringify(data),
            success: success,
            error: error
        });
    });
});