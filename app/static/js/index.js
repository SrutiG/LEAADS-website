$(document).ready(function() {
    $home_link = $("#home-link");
    $opp_link = $("#opp-link");
    $about_link = $("#about-link");
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

    if (window.location.pathname == '/opportunities_list') {
        $opp_link.addClass('active');
    } else {
        $opp_link.removeClass('active');
    }

    if (window.location.pathname == '/about_us') {
        $about_link.addClass('active');
    } else {
        $about_link.removeClass('active');
    }

})