$(document).ready(function() {
    $home_link = $("#home-link");
    $('#nav').affix({
        offset: {
            top: $('#nav').offset().top
        }
    });

    //change the navbar active link to home when on home page
    if (window.location.pathname == '/home') {
        $home_link.addClass('active');
    } else {
        $home_link.removeClass('active');
    }

})