$(document).ready(function() {
    $admin_dash = $("#admin-dash");
    $admin_home = $("#admin-home");
    $admin_blog = $("#admin-blog");
    $admin_opp = $("#admin-opp");
    $admin_prog = $("#admin-prog");
    $admin_members = $("#admin-members");
    if (window.location.pathname == '/admin_dashboard') {
            $admin_dash.addClass('active-cust');
    } else {
        $admin_dash.removeClass('active-cust');
    }

    if (window.location.pathname == '/admin_home') {
        $admin_home.addClass('active-cust');
    } else {
        $admin_home.removeClass('active-cust');
    }

    if (window.location.pathname == '/admin_blog') {
        $admin_blog.addClass('active-cust');
    } else {
        $admin_blog.removeClass('active-cust');
    }

    if (window.location.pathname == '/admin_opp') {
        $admin_opp.addClass('active-cust');
    } else {
        $admin_opp.removeClass('active-cust');
    }

    if (window.location.pathname == '/admin_prog') {
        $admin_prog.addClass('active-cust');
    } else {
        $admin_prog.removeClass('active-cust');
    }

    if (window.location.pathname == '/admin_members') {
        $admin_members.addClass('active-cust');
    } else {
        $admin_members.removeClass('active-cust');
    }
})