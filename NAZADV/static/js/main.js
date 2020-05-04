document.addEventListener('DOMContentLoaded', function () {
	var heroCarousel = document.querySelectorAll('.carousel');
	var fw_carousel = M.Carousel.init(heroCarousel[0], {
		fullWidth: true,
		indicators: true
	});
	var instances = M.Carousel.init(heroCarousel[1], {
		dist:0,
	});
	var mnv = document.querySelectorAll('.sidenav');
  	M.Sidenav.init(mnv);
	AOS.init({
		// initClassName: 'aos-init', // class applied after initialization
		// animatedClassName: 'aos-animate', // class applied on animation
		// useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
		// disableMutationObserver: false, // disables automatic mutations' detections (advanced)
		// debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
		// throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)
		
	  
		// Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
		offset: 150, // offset (in px) from the original trigger point
		delay: 0, // values from 0 to 3000, with step 50ms
		duration: 800, // values from 0 to 3000, with step 50ms
		easing: 'ease', // default easing for AOS animations
		once: true, // whether animation should happen only once - while scrolling down
	  });
});