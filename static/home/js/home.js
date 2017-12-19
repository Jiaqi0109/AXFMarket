$(document).ready(function () {
    setTimeout(function () {
        swiper1();
        swiper2();
    }, 500)
});

function swiper1() {
    var mySwiper1 = new Swiper('#topSwiper', {
        spaceBetween: 30,
        centeredSlides: true,
        loop: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        }
    });
}
function swiper2() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView: 3
    });
}
