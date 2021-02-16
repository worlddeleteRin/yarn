$(document).ready(function() {

  const swiper = new Swiper('.page_main_slider ', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    autoHeight: true,
    // If we need pagination
    // pagination: {
    //   el: '.swiper-pagination',
    // },

    // Navigation arrows
    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',
    // },

    // And if we need scrollbar
    // scrollbar: {
    //   el: '.swiper-scrollbar',
    // },
  });

});


// $(document).ready(function() {
//   $(".page_main_slider").owlCarousel({
//     loop: true,
//     slidesToShow: 1,
//     autoplay: true,
//     autoplayTimeout: 30000,
//     autoplayHoverPause: true,
//   });
// });

// $(document).ready(function() {
//   $(".main_slider").owlCarousel({
//     loop: true,
//     // margin: 10,
//     // autoWidth: true,
//     nav: true,
//     // navText: ["<div class='owl__nav owl__nav__left'><i class='gg-chevron-left'></i></div>","<div class='owl__nav owl__nav__right'><i class='gg-chevron-right'></i></div>" ],
//     dots: true,
//     slidesToShow: 1,
//     rewind: true,
//     lazyLoad: true,
//     autoplay: true,
//     autoplayTimeout: 30000,
//     autoplayHoverPause: true,
//     // animateOut: true,
//     // animateIn: true,
//   });
// });




function showModal(item) {
    $(item).addClass("show")
    $(".pform__wrap__wrapper").addClass("show")
}
function closeModal() {
    $(".pform__wrap").removeClass("show")
    $(".pform__wrap__wrapper").removeClass("show")
}

$(".pform__wrap__close").click(function() {
    closeModal()
})
$(".pform__wrap__wrapper").click(function() {
    closeModal()
})


function setDeliveryActive(current) {
  $("#cart_input_own").removeClass("show")
  $("#cart_input_cura").removeClass("show")
    $(".delivery__method").removeClass("active")
    $(current).addClass("active")
    var curr_content = $(current).attr('data-toogle')
    $(curr_content).addClass("show")
}

function setPaymentActive(current) {
    $(".payment__method").removeClass("active")
    $(current).addClass("active")
}





















