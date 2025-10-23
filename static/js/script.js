$(document).ready(function () {

  /*------custom-cursor-----*/
  if ($(".custom-cursor").length) {
		var cursor = document.querySelector(".custom-cursor-one");
		var cursorinner = document.querySelector(".custom-cursor-two");
		var a = document.querySelectorAll("a");

		document.addEventListener("mousemove", function (e) {
			var x = e.clientX;
			var y = e.clientY;
			cursor.style.transform = `translate3d(calc(${e.clientX}px - 50%), calc(${e.clientY}px - 50%), 0)`;
		});

		document.addEventListener("mousemove", function (e) {
			var x = e.clientX;
			var y = e.clientY;
			cursorinner.style.left = x + "px";
			cursorinner.style.top = y + "px";
		});

		document.addEventListener("mousedown", function () {
			cursor.classList.add("click");
			cursorinner.classList.add("custom-cursor-innerhover");
		});

		document.addEventListener("mouseup", function () {
			cursor.classList.remove("click");
			cursorinner.classList.remove("custom-cursor-innerhover");
		});

		a.forEach((item) => {
			item.addEventListener("mouseover", () => {
				cursor.classList.add("custom-cursor-hover");
			});
			item.addEventListener("mouseleave", () => {
				cursor.classList.remove("custom-cursor-hover");
			});
		});
	}
  //------ testimonial-one-tabs
  $('.testimonial-one-tabs .owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    startPosition: 'URLHash'
  });
  $('.testimonial-one-btn li').on('click', function () {
    $('.testimonial-one-btn li').removeClass('active');
    $(this).addClass('active');
  })
 

  // -----testimonial-three-tabs
  $('.testimonial-three-tabs .owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    margin: 20,
    // autoplay: true,
    // autoplayTimeout: 5000,
    startPosition: 'URLHash'
  });
  $('.testimonial-three-btn li').on('click', function () {
    $('.testimonial-three-btn li').removeClass('active');
    $(this).addClass('active');
  })

  // -----movies-video-one-slider
  $('.movies-video-one-slider').owlCarousel({
    items: 4,
    loop: true,
    margin: 30,
    autoplay: true,
    autoplayTimeout: 5000,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
      1199: {
        items: 4,
      }
    }
  })

  // -----banner-four-bottom
  $('.banner-four-bottom .owl-carousel').owlCarousel({
    items: 9,
    loop: true,
    margin: 30,
    dots: false,
    autoplay: true,
    autoplayTimeout: 3000,
    slideTransition: 'linear',
    smartSpeed: 3000,
    responsive: {
      0: {
        items: 5,
      },
      768: {
        items: 5,
      },
      992: {
        items: 6,
      },
      1199: {
        items: 7,
      },
      1400: {
        items: 9,
      }
    }
  })

  // -----package-four
  $('.package-four-slider').owlCarousel({
    items: 2,
    loop: true,
    dots: true,
    autoplay: true,
    autoplayTimeout: 5000,
    slideTransition: 'linear',
    smartSpeed: 500,
    responsive: {
      0: {
        autoHeight: true,
        items: 1,
      },
      768: {
        items: 1,
      },
      992: {
        items: 2,
      },
      1199: {
        items: 2,
      }
    }
  })

  // -----featured-movies-two-slider
  $('.featured-movies-two-slider').owlCarousel({
    items: 1,
    loop: true,
    dots: false,
    margin: 30,
    nav: true,
    // animateOut: 'fadeOut',
    autoplay: true,
    autoplayTimeout: 5000,
    navText: [
      '<i class="icon-left-arrow-two" aria-hidden="true"></i>',
      '<i class="icon-right-arrow-two" aria-hidden="true"></i>'
    ],
  })

  // -----movies-six-slider
  $('.movies-six-slider, .comingsoon-popular-movie-six-slider').owlCarousel({
    items: 4,
    loop: true,
    dots: false,
    nav: true,
    // animateOut: 'fadeOut',
    autoplay: true,
    margin: 24,
    autoplayTimeout: 5000,
    navText: [
      '<i class="fas fa-arrow-left" aria-hidden="true"></i>',
      '<i class="fas fa-arrow-right" aria-hidden="true"></i>'
    ],
    responsive: {
      0: {
        autoHeight: true,
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
      1199: {
        items: 4,
      }
    }
  })

  // -----blog-four-slider
  $('.blog-four-slider').owlCarousel({
    items: 2,
    loop: true,
    dots: false,
    nav: true,
    animateOut: 'fadeOut',
    autoplay: true,
    autoplayTimeout: 5000,
    responsive: {
      0: {
        autoHeight: true,
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 2,
      },
      1199: {
        items: 2,
      }
    },
    navText: [
      '<i class="fas fa-arrow-left" aria-hidden="true"></i>',
      '<i class="fas fa-arrow-right" aria-hidden="true"></i>'
    ],

  })

  // -----testimonial-four-slider
  $('.testimonial-four .owl-carousel, .testimonial-three-tabs .owl-carousel, .testimonial-five .owl-carousel, .testimonial-six .owl-carousel').owlCarousel({
    items: 3,
    loop: true,
    // autoplay: true,
    // autoplayTimeout: 10000,
    // smartSpeed: 2000,
    responsive: {
      0: {
        autoHeight: true,
        items: 1,
      },
      576: {
        autoHeight: true,
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 2,
      },
      1199: {
        autoHeight: true,
        items: 3,
      }
    }
  });

  // -----popular-movie-video-six-slider
  $('.popular-movie-video-six-box').owlCarousel({
    items: 3,
    loop: true,
    margin: 24,
    dots: false,
    // autoplay: true,
    // autoplayTimeout: 3000,
    slideTransition: 'linear',
    nav: true,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 1,
      },
      992: {
        items: 2,
      },
      1199: {
        items: 3,
      },
      1400: {
        items: 3,
      }
    },
    navText: [
      '<i class="fas fa-arrow-left" aria-hidden="true"></i>',
      '<i class="fas fa-arrow-right" aria-hidden="true"></i>'
    ],
  })

  if ($(".wow").length) {
		var wow = new WOW({
			boxClass: "wow", // animated element css class (default is wow)
			animateClass: "animated", // animation css class (default is animated)
			mobile: true, // trigger animations on mobile devices (default is true)
			live: true // act on asynchronously loaded content (default is true)
		});
		wow.init();
	}

  $('body').on('click', 'a[href="#"]', function(e) {e.preventDefault() });
  /*-----scroll-to-top------*/
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('#scroll').fadeIn();
    } else {
      $('#scroll').fadeOut();
    }
  });
  $('#scroll').click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1000);
    return false;
  });

  /*------sticky-header-----*/
  $(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
      $('.main-header, .main-header-two, .main-header-four').addClass("sticky");
    }
    else {
      $('.main-header, .main-header-two, .main-header-four').removeClass("sticky");
    }
  });

  /*------mobile-nav-----*/
  jQuery(function ($) {
    $('.header-right-end, .header-two-right-end').click(function () {
      $('.mobile-nav-wrapper, .mobile-nav-two-wrapper').toggleClass('expanded')
      $("body").toggleClass("locked");
    })
  })
  if ($(".mobile-nav-toggler, .mobile-nav-two-toggler").length) {
    $(".mobile-nav-toggler, .mobile-nav-two-toggler").on("click", function (e) {
      e.preventDefault();
      $(".mobile-nav-wrapper, .mobile-nav-two-wrapper").toggleClass("expanded");
      $("body").toggleClass("locked");
    });
  }
  if ($(".mobile-nav-container .main-menu-list, .mobile-nav-two-container .main-menu-list").length) {
    let dropdownAnchor = $(
      ".mobile-nav-container .main-menu-list .dropdown > a, .mobile-nav-two-container .main-menu-list .dropdown > a"
    );
    dropdownAnchor.each(function () {
      let self = $(this);
      let toggleBtn = document.createElement("BUTTON");
      toggleBtn.setAttribute("aria-label", "dropdown toggler");
      toggleBtn.innerHTML = "<i class='fa fa-angle-down'></i>";
      self.append(function () {
        return toggleBtn;
      });
      self.find("button").on("click", function (e) {
        e.preventDefault();
        let self = $(this);
        self.toggleClass("expanded");
        self.parent().toggleClass("expanded");
        self.parent().parent().children("ul").slideToggle();
      });
    });
  }

  /*------locked-----*/
  jQuery(function ($) {
    $('.side-drawer-toggler-btn').click(function () {
      $('.side-drawer-wrapper').toggleClass('expanded')
      $("body").toggleClass("locked");
    })
  })
  if ($(".side-drawer-toggler").length) {
    $(".side-drawer-toggler").on("click", function (e) {
      e.preventDefault();
      $(".side-drawer-wrapper").toggleClass("expanded");
      $("body").toggleClass("locked");
    });
  }


 /*------search-toggler-----*/
  if ($(".current").length) {
    $(".search-toggler").on("click", function (e) {
      e.preventDefault();
      $(".search-popup").toggleClass("active");
      $("body").toggleClass("locked");
    });
  }

  /*------current-----*/
  function dynamicCurrentMenuClass(selector) {
    let FileName = window.location.href.split("/").reverse()[0];
    selector.find("li").each(function () {
      let anchor = $(this).find("a");
      if ($(anchor).attr("href") == FileName) {
        $(this).addClass("current");
      }
    });
    // if any li has .current elmnt add class
    selector.children("li").each(function () {
      if ($(this).find(".current").length) {
        $(this).addClass("current");
      }
    });
    // if no file name return
    if ("" == FileName) {
      selector.find("li").eq(0).addClass("current");
    }
  }
  if ($(".navbar-nav, .navbar-nav-two").length) {
    // dynamic current class
    let mainNavUL = $(".navbar-nav, .navbar-nav-two");
    dynamicCurrentMenuClass(mainNavUL);
  }
  if ($(".service-details__sidebar-service-list").length) {
    // dynamic current class
    let mainNavUL = $(".service-details__sidebar-service-list");
  }

  // ---------------video-popup
  if ($(".video-popup").length) {
		$('.video-popup').YouTubePopUp();
	}

  // ---------------faq-count
  $('.faq-count').each(function () {
    $(this).prop('Counter', 0).animate({
      Counter: $(this).text()
    }, {
      duration: 9000,
      easing: 'swing',
      step: function (now) {
        $(this).text(Math.ceil(now));
      }
    });
    $('.faq-count').addClass('animated fadeInLeft');
  });

  // ----product-details  Add-to-Cart
  var buttonPlus = $(".qty-btn-plus");
  var buttonMinus = $(".qty-btn-minus");
  var incrementPlus = buttonPlus.click(function () {
    var $n = $(this)
      .parent(".qty-container")
      .find(".input-qty");
    $n.val(Number($n.val()) + 1);
  });
  var incrementMinus = buttonMinus.click(function () {
    var $n = $(this)
      .parent(".qty-container")
      .find(".input-qty");
    var amount = Number($n.val());
    if (amount > 0) {
      $n.val(amount - 1);
    }
  });

  if ($('.testimonial-thumb').length) {
		var review_thumb = new Swiper(".testimonial-thumb",{
			slidesPerView: 3,
			spaceBetween: 0,
		})
	}
	if ($('.testimonial-reviews').length) {
		var review_swiper = new Swiper(".testimonial-reviews",{
			slidesPerView:1,
			loop:true,
			spaceBetween: 0,
			autoplay: {
				delay: 2500,
				disableOnInteraction: false,
			},
			pagination: {
				el: ".swiper-pagination",
				clickable: true,
			},
			thumbs: {
				swiper: review_thumb,
			},
		})
	}


});



// Window load

$(window).on("load", function () {
  /*------preloader-----*/
  if ($(".preloader").length) {
    $(".preloader").fadeOut();
  }

});




