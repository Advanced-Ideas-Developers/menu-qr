$('.plan').hover(function(){
  $(this).find('.btn').slideDown();
},function(){
  $(this).find('.btn').slideUp();
});

$(function () {
  $(document).scroll(function () {
    var $nav = $("nav");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    if($(this).scrollTop() > $nav.height()){
      $('#logoAID').show(200);
    }else{
      $('#logoAID').hide();
    }
  });
});

function goToByScroll(id){
  id = id.replace("link", "");
  if(id === 'inicio'){
    $('html,body').animate({
      scrollTop: 0},
      'slow');  
  }else{
    $('html,body').animate({
      scrollTop: $("#"+id).offset().top - 100},
      'slow');
  }
}

$(".nav-item").click(function(e) { 
  e.preventDefault(); 
  goToByScroll($(this).attr("id"));           
});