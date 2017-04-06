$(document).ready(function() {
    $admin_dash = $("#admin-dash");
    $admin_home = $("#admin-home");
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
})