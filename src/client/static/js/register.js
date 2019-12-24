$(function(){
    function success(data){
       console.log(data);
       window.location.replace("/");
    }

    function error(data){
       console.log(data);
    }

    $('#regForm').submit(function (e) {
        e.preventDefault();
        let email = $("#email").val();
        let password = $("#password").val();
        let confirm_password = $("#confirm_password").val();
        if(password === confirm_password){
            let data = {
                "email": email,
                "password": password
            };
            $.ajax({
                type: "POST",
                contentType: "application/json",
                headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                url: `/authentication/register/`,
                data: JSON.stringify(data),
                success: success,
                error: error
            });
        } else {
            alert("Passwords are not the same, please check!");
        }
    });
});