$('.modal').delay(3000).fadeOut();

$('.plan').hover(function(){
  $(this).find('.btn').slideDown();
},function(){
  $(this).find('.btn').slideUp();
});

$(function () {
  $(document).scroll(function () {
    var $nav = $("nav");
    $('.menu-resp').toggleClass('scrolled', $(this).scrollTop() > $('.menu-resp').height());
    if(window.screen.width>768){
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      if($(this).scrollTop() > $nav.height()){
        $('#logoAID').show(200);
      }else{
        $('#logoAID').hide();
      }
    }
  });
});

function goToByScroll(id){
  id = id.replace("link", "");
  if(id === 'inicio'){
    $('html,body').animate({
      scrollTop: 0},
      'slow');
    if(window.screen.width < 728){
      $('nav').toggleClass('expanded');
    }
  }else{
    $('html,body').animate({
      scrollTop: $("#"+id).offset().top - 100},
      'slow');
      if(window.screen.width < 728){
        $('nav').toggleClass('expanded');
      }
  }
}

$(".nav-item").click(function(e) { 
  e.preventDefault(); 
  goToByScroll($(this).attr("id"));           
});

$(".fa-bars").click(function(e) {
  //$("nav").slideDown(200);
  $('nav').toggleClass('expanded');
});

$(".fa-times").click(function() {
  //$("nav").slideUp(200);
  $('nav').toggleClass('expanded');
})

$('.contact').click(function() {
  goToByScroll("contactlink");
});

$('.contactar').click(function() {
  goToByScroll("contactlink");
});

$('.test').click(function() {
  goToByScroll("clientslink");
});