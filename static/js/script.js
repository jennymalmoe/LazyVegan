$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
});

/* Show Image Preview
    Sourced from http://jsfiddle.net/2d7axmdr */
    function recipeImg() {
        // For recipes
        $(".new-img").css("display", "flex");
        $(".current-img").css("display", "none");
        var url = $("#recipe_img").val();
        $('.img-window').attr('src',url);
    }
    function userImg() {
        // For users
        $(".new-img").css("display", "flex");
        $(".current-img").css("display", "none");
        var url = $("#user_img").val();
        $('.img-window').attr('src',url);
    }
    