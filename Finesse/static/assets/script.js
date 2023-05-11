var swiper = new Swiper(".cloth-slider", {
   loop:true,
   centeredSlides:true,
   autoplay:{
      delay:9500,
      disableOnInteraction:false,
   },
   breakpoints: {
     0: {
       slidesPerView: 1,
  
     },
     768: {
       slidesPerView: 2,
     },
     1024: {
       slidesPerView: 3,
     },
   },
});


var swiper = new Swiper(".bestseller-slider", {
   loop:true,
   centeredSlides:true,
   autoplay:{
      delay:9500,
      disableOnInteraction:false,
   },

   breakpoints: {
     0: {
       slidesPerView: 1,
  
     },
     768: {
       slidesPerView: 2,
     },
     1024: {
       slidesPerView: 3,
     },
   },
});


function redirectToRegister() {
   window.location.href = "register.html";
}
