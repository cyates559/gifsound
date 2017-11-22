$(document).ready(function () {
    $("#login").on("click", function (e) {
        e.preventDefault();
        (async function () {
            const {value: formvalues} = await swal({
                title: "Log In",
                imageUrl: '/static/login.jpg',
                html:
                "<small>Username</small>" +
                "<input id='username' class='form-control' required><br>" +
                "<small>Password</small>" +
                "<input id='password' class='form-control' type='password' required>",
                focusConfirm: true,
                showConfirmButton: true,
                showCancelButton: true,
                preConfirm: function () {
                    return [
                        $('#username').val(),
                        $('#password').val()
                    ]
                }

            });
            if (formvalues) {
                if (ValidateUserName(formvalues[1])) {
                    let data = JSON.stringify(formvalues);
                    swal(formvalues[0]);
                    swal({
                        title: 'Logging In!',
                        text: 'Please Wait',
                        timer: 2000,
                        onOpen: function () {
                            swal.showLoading()
                        }
                    })
                    $.ajax({
                        url: "/login/" + formvalues[0],
                        type: 'POST',
                        success: function (response) {
                            swal({
                                title: 'Welcome ' + response.some_data + '!',
                                text: 'Login Successful!',
                                type:  'success',
                                timer: 2000
                            }).then(function(response) {
                                location.reload();
                            })
                        },
                        error: function (XMLHttpRequest, textStatus, errorThrown) {
                            swal({
                                title: 'Oops..',
                                text: 'Login Failed!',
                                type: 'error',
                                animation: true,
                            })
                        }
                    })
                } else {
                    swal({
                        title: '...',
                        type: 'error',
                        text: 'Please enter valid Login Information'
                    })
                }
            }
        })();
    });

    function ValidateUserName(inputText) {
        var usernameFormat = /^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$/;
        if (inputText.match(usernameFormat)) {
            return true;
        } else {
            return false;
        }
    }

    function ValidateEmail(inputText) {
        var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (inputText.match(mailformat)) {
            return true;
        }
        else {
            return false;
        }
    }

});


