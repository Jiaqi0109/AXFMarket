$(function () {
    $('#all_type').click(function () {
        $('#all_type_content').show().click(function () {
            $(this).hide()
        });
        $('#sort_rule_content').hide()
    });

    $('#sort_rule').click(function () {
        $('#sort_rule_content').show().click(function () {
            $(this).hide()
        });
        $('#all_type_content').hide()
    });

    $('.goods_add').click(function () {
        // 将商品数据发送到服务器中, 添加到购物车里
        var goods_id = $(this).attr('goods_id');
        // 写地址的时候，浏览器上写的是ip就写ip， 使用域名就写域名
        $.get('http://127.0.0.1:8000/axf/addtocart/', {'goodsid': goods_id}, function (data) {
            alert(data['msg'])
        })
    })
});