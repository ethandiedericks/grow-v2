$(document).ready(function(){
  $('.dropdown').hover(function(){
    $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(300);
  }, function(){
    $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(300);
  });
});

// header

let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');
let ticking = false;

window.addEventListener('scroll', function() {
  lastScrollTop = window.scrollY;

  if (!ticking) {
    window.requestAnimationFrame(function() {
      if (window.scrollY > lastScrollTop) {
        navbar.classList.add('hidden');
      } else {
        navbar.classList.remove('hidden');
      }
      ticking = false;
    });
    ticking = true;
  }
});