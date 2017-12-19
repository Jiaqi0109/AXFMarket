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
    })
});