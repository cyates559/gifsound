// COURSE: CST 205 - Multimedia Design & Programming
// TITLE: login.js
// ABSTRACT: Used for logging in user and signing up users. Performs valdation on user inputs.
// AUTHORS: Erick Shaffer
// DATE: 12/10/17
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
                        timer: 3000,
                        onOpen: function () {
                            swal.showLoading()
                        }
                    })
                    $.ajax({
                        url: "/login/" + formvalues[0] + '/' + formvalues[1],
                        type: 'POST',
                        success: function (response) {
                            swal.close()
                            console.log(response);
                            swal({
                                title: 'Welcome ' + response.name + '!',
                                text: 'Login Successful!',
                                type: 'success',
                                timer: 2000
                            }).then(function (response) {
                                console.log('should reload');
                                window.location.reload();
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

    $("#signup").on("click", function (e) {
        e.preventDefault();
        (async function () {
            const {value: formvalues} = await swal({
                title: "Sign Up",
                imageUrl: '/static/check.jpg',
                html:
                "<small>Username</small>" +
                "<input id='username' class='form-control' required><br>" +
                "<small>Email</small>" +
                "<input id='email' class='form-control' type='email' required><br>" +
                "<small>Password</small>" +
                "<input id='password' class='form-control' type='password' required>",
                focusConfirm: true,
                showConfirmButton: true,
                showCancelButton: true,
                preConfirm: function () {
                    return [
                        $('#username').val(),
                        $('#email').val(),
                        $('#password').val()
                    ]
                }

            });
            if (formvalues) {
                if (ValidateUserName(formvalues[0]) && ValidateEmail(formvalues[1])) {
                    let data = JSON.stringify(formvalues);
                    swal(formvalues[0]);
                    swal({
                        title: 'Signing Up!',
                        text: 'Please Wait',
                        timer: 2000,
                        onOpen: function () {
                            swal.showLoading()
                        }
                    })
                    $.ajax({
                        url: "/register/" + formvalues[0] + '/' + formvalues[1] + '/' + formvalues[2],
                        type: 'POST',
                        success: function (response) {
                            console.log(response);
                            swal({
                                title: 'Welcome!',
                                text: 'Sign Up Successful! Please Login',
                                type: 'success',
                                timer: 2000
                            }).then(function (response) {
                                location.reload();
                            })
                        },
                        error: function (XMLHttpRequest, textStatus, errorThrown) {
                            swal({
                                title: 'Oops..',
                                text: XMLHttpRequest.responseJSON.signup,
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

    $("#logout").on("click", function(e) {
        $.ajax({
            url: "/logout",
            type: 'POST',
            success: function () {
                location.reload();
            },
        });
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


