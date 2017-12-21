$(function () {
    $('.ischose').click(function () {
        // 将当前点击的选项的id发送给服务器
        var cart_id = $(this).attr('cartid');
        var cart_selected = $(this).attr('cartselect');
        if (cart_selected == 'True'){
            $(this).attr("cartselect", 'False');
        }else{
            $(this).attr("cartselect", 'True');
        }
        $(this).attr('cartselect', !cart_selected);
        var child = $(this).find('span');
        $.getJSON('http://127.0.0.1:8000/axf/changeselect/', {'cartid': cart_id, 'cartselected': cart_selected}, function (data) {
            if (data['msg'] == 'ok'){
                $(child).toggle();
            }
        })
    });

    $(".subShopping").click(function () {
        var cartid = $(this).attr('cartid');
        var sub = $(this);
        $.getJSON('http://127.0.0.1:8000/axf/cartgoossub/', {'cartid': cartid}, function (data) {
            // alert(data['num'])
            if (data['num'] == 0){
                sub.parents('li').remove();
            }else {
                sub.next("span").html(data['num'])
            }
        })
    });

    $('#select_ok').click(function () {
        var spans = $('.ischose').find('span');
        var cartids = [];

        for(var i=0; i<spans.length; i++){
            if ($(spans[i]).css('display') == 'block'){
                console.log($(spans[i]).attr('id'));
                cartids.push($(spans[i]).attr('id'));
            }
        }

        $.getJSON('http://127.0.0.1:8000/axf/genorder/', {'cartids': cartids.join('#')}, function (data) {
            // 接收到订单id， 拿着id进行页面跳转， 去付款
            window.open('http://127.0.0.1:8000/axf/pay/'+data['orderid'], '_self');
        })
    })
});