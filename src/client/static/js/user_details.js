$(function(){
    function success(data) {
       console.log(data);
       $("#user_details").text(JSON.stringify(data));
    }

    function error(data) {
       console.log(data);
    }

    function logout_success(data) {
        Cookies.remove('token');
        window.location.replace("/");
    }

    $( document ).ready(function() {
        if(window.location.pathname === "/details/"){
            let token = Cookies.get('token');
            if(token){
                $.ajax({
                    type: "GET",
                    contentType: "application/json",
                    headers: { "X-CSRFToken": Cookies.get("csrftoken"), "Authorization": "Bearer " + token },
                    url: `/authentication/session_details/`,
                    success: success,
                    error: error
                });
            } else {
                window.location.replace("/");
            }
        }
    });

    $("#logout").click(function(){
        let token = Cookies.get('token');
        let data = {
            "token": token
        };

        $.ajax({
            type: "POST",
            contentType: "application/json",
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            url: `/authentication/token/revoke/`,
            data: JSON.stringify(data),
            success: logout_success,
            error: error
        });
    });
});