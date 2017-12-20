function check() {

    var password = $('#login_password').val();
    var newPassword = md5(password);
    $('#login_password').val(newPassword);
    return true;

}