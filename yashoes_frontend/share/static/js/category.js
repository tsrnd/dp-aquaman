$(document).ready(function () {
    $('.product-categories li').click(function () {
        $(this).children("span").toggle();
        $('li > ul').not($(this).children("ul")).hide();
        $(this).children("ul").stop().slideToggle(400);
        return false;
    });
    $('.product-categories li ul li a').click(function () {
        var id = $(this).attr('id')
        window.location.href = "http://localhost:8000/products" + "?cat_id="+id;
        return false;
    });
})