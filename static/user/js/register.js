$(function () {
    $("#reg_username").blur(function () {
        //    获取输入框中的内容, 需要将输入框的内容发送到服务器验证
        var uname = $(this).val();
        // 向服务器发送用户名进行验证
        $.getJSON('http://127.0.0.1:8000/axf/checkuser/', {'uname': uname}, function (data) {
            if (data['state'] == 200) {
                $('#username_check').css('color', 'green');
            } else if (data['state'] == 201) {
                $('#username_check').css('color', 'red');
            }
            $("#username_check").html(data['msg'])
        })
    });

});


function check() {
    // 在这做提交前的验证
    // 验证密码和确认密码
    var password = $('#reg_password').val();
    var password_confirm = $('#reg_password_confirm').val();
    if (password == password_confirm) {
        $("#password_check").html('两次密码一致').css('color', 'green');
    } else {
        $("#password_check").html('两次密码不一致').css('color', 'red');
        return false;
    }

    var newPwd = md5(password);
    $('#reg_password').val(newPwd);
    return true
}