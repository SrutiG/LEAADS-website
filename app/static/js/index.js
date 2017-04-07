$(document).ready(function() {
    $home_link = $("#home-link");
    $opp_link = $("#opp-link");
    $about_link = $("#about-link");
    $blog_link = $("#blog-link");
    $prog_link = $("#prog-link");
    $home_learn_more = $("#home-learn-more");
    $view_events = $("#view_events");

    $('#nav').affix({
        offset: {
            top: $('#nav').offset().top
        }
    });

    $home_learn_more.click(function() {
        window.location.href = '/about_us';
    });

    $view_events.click(function() {
        window.location.href = '/opportunities_list_category/Event';
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

    if (window.location.pathname == '/blog' || window.location.pathname == '/about_us') {
        $about_link.addClass('active');
    } else {
        $about_link.removeClass('active');
    }

    if (window.location.pathname == '/programs') {
        $prog_link.addClass('active');
    } else {
        $prog_link.removeClass('active');
    }


})