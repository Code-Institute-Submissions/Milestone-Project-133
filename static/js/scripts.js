$(document).ready(function () {

  // smooth scroll to screen top
  $(".back-to-top-link").click(function () {      
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  // shows or hides back to top arrow
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".fixed-arrow").show();
    } else {
      $(".fixed-arrow").hide();
    }
  });

});
