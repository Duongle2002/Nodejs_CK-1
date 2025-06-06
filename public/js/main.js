(function($) {

	"use strict";

	$(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll'
  });


	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	var loader = function() {
		setTimeout(function() { 
			if($('#ftco-loader').length > 0) {
				$('#ftco-loader').removeClass('show');
			}
		}, 1);
	};
	loader();

	var carousel = function() {
		$('.carousel-testimony').owlCarousel({
			center: true,
			loop: true,
			autoplay: true,
			autoplaySpeed:2000,
			items:1,
			margin: 30,
			stagePadding: 0,
			nav: false,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive:{
				0:{
					items: 1
				},
				600:{
					items: 2
				},
				1000:{
					items: 3
				}
			}
		});

	};
	carousel();

	$('nav .dropdown').hover(function(){
		var $this = $(this);
		// 	 timer;
		// clearTimeout(timer);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').addClass('show');
	}, function(){
		var $this = $(this);
			// timer;
		// timer = setTimeout(function(){
			$this.removeClass('show');
			$this.find('> a').attr('aria-expanded', false);
			// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
			$this.find('.dropdown-menu').removeClass('show');
		// }, 100);
	});


	$('#dropdown04').on('show.bs.dropdown', function () {
	  console.log('show');
	});

	// scroll
	var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.ftco_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');	
				}
			} 
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			} 
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');	
				}
				
				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();

	var counter = function() {
		
		$('#section-counter, .wrap-about, .ftco-counter').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {

				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
				$('.number').each(function(){
					var $this = $(this),
						num = $this.data('number');
						console.log(num);
					$this.animateNumber(
					  {
					    number: num,
					    numberStep: comma_separator_number_step
					  }, 7000
					);
				});
				
			}

		} , { offset: '95%' } );

	}
	counter();


	var contentWayPoint = function() {
		var i = 0;
		$('.ftco-animate').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .ftco-animate.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn ftco-animated');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft ftco-animated');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight ftco-animated');
							} else {
								el.addClass('fadeInUp ftco-animated');
							}
							el.removeClass('item-animate');
						},  k * 50, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '95%' } );
	};
	contentWayPoint();


	
	// magnific popup
	$('.image-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    closeBtnInside: false,
    fixedContentPos: true,
    mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
     gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      verticalFit: true
    },
    zoom: {
      enabled: true,
      duration: 300 // don't foget to change the duration also in CSS
    }
  });

  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,

    fixedContentPos: false
  });

  $('[data-toggle="popover"]').popover()
	$('[data-toggle="tooltip"]').tooltip()

})(jQuery);

$(document).ready(function() {
	// Hàm debounce
	function debounce(func, wait) {
	  let timeout;
	  return function(...args) {
		clearTimeout(timeout);
		timeout = setTimeout(() => func.apply(this, args), wait);
	  };
	}
  
	// Khởi tạo slider giá
	$("#price-range").slider({
	  range: true,
	  min: 0,
	  max: parseFloat($("#hiddenMaxPrice").val()) || 1000, // Lấy max từ DB
	  values: [parseFloat($("#hiddenMinPrice").val()) || 0, parseFloat($("#hiddenMaxPrice").val()) || 1000],
	  slide: function(event, ui) {
		$("#price-values").text(`$${ui.values[0]} - $${ui.values[1]}`);
		$("#hiddenMinPrice").val(ui.values[0]);
		$("#hiddenMaxPrice").val(ui.values[1]);
		if (ui.values[0] > ui.values[1]) {
		  $("#price-error").show();
		} else {
		  $("#price-error").hide();
		  debouncedUpdate();
		}
	  }
	});
	$("#price-values").text(`$${$("#price-range").slider("values", 0)} - $${$("#price-range").slider("values", 1)}`);
  
	// Khởi tạo autocomplete
	$('input[name="search"]').autocomplete({
	  source: function(request, response) {
		$.ajax({
		  url: '/product/autocomplete',
		  data: { term: request.term },
		  success: function(data) {
			response(data);
		  },
		  error: function() {
			response([]);
		  }
		});
	  },
	  minLength: 2,
	  select: function(event, ui) {
		$('input[name="search"]').val(ui.item.value);
		updateProductList(1);
	  }
	});
  
	// Lưu trạng thái vào localStorage
	function saveFilters() {
	  const filters = {
		search: $('input[name="search"]').val(),
		category: $('#categorySelect').val(),
		sort: $('#sortSelect').val(),
		page: $('#pagination .active a').data('page') || 1,
		minPrice: $("#hiddenMinPrice").val(),
		maxPrice: $("#hiddenMaxPrice").val(),
		status: $('#statusSelect').val() || [],
	  };
	  localStorage.setItem('productFilters', JSON.stringify(filters));
	}
  
	// Tải trạng thái từ localStorage
	function loadFilters() {
	  const savedFilters = JSON.parse(localStorage.getItem('productFilters'));
	  if (savedFilters) {
		$('input[name="search"]').val(savedFilters.search || '');
		$('#categorySelect').val(savedFilters.category || '');
		$('#sortSelect').val(savedFilters.sort || '');
		$("#hiddenMinPrice").val(savedFilters.minPrice || 0);
		$("#hiddenMaxPrice").val(savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val()));
		$("#price-range").slider("values", [savedFilters.minPrice || 0, savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val())]);
		$("#price-values").text(`$${savedFilters.minPrice || 0} - $${savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val())}`);
		$('#statusSelect').val(savedFilters.status || []);
		updateProductList(savedFilters.page || 1);
	  }
	}
  
	// Cập nhật danh sách sản phẩm bằng AJAX
	function updateProductList(page) {
		const search = $('input[name="search"]').val();
		const category = $('#categorySelect').val();
		const sort = $('#sortSelect').val();
		const minPrice = $("#hiddenMinPrice").val();
		const maxPrice = $("#hiddenMaxPrice").val();
		
		// Lấy giá trị từ các checkbox
		const status = [];
		$('input[name="status"]:checked').each(function() {
		  status.push($(this).val());
		});
	  
		if (parseFloat(minPrice) > parseFloat(maxPrice)) {
		  $("#price-error").show();
		  return;
		}
	  
		$('.spinner').show();
		$('#productList').fadeOut(200);
	  
		$.ajax({
		  url: '/product',
		  method: 'GET',
		  data: { page, search, category, sort, minPrice, maxPrice, status },
		  success: function(data) {
			// Logic render sản phẩm giữ nguyên
			$('#productList').empty();
			if (!data.products || data.products.length === 0) {
			  $('#productList').html('<p>No products found.</p>');
			} else {
			  data.products.forEach(product => {
				const productHtml = `
				  <div class="col-md-4 d-flex">
					<div class="product ftco-animate">
					  <div class="img d-flex align-items-center justify-content-center" style="background-image: url('${product.image || '/images/default.jpg'}'); min-height: 200px; background-size: cover;">
						<div class="desc">
						  <p class="meta-prod d-flex">
							<a href="#" class="btn-add-to-cart d-flex align-items-center justify-content-center" data-product-id="${product._id}">
							  <span class="flaticon-shopping-bag"></span>
							</a>
							<a href="#" class="d-flex align-items-center justify-content-center">
							  <span class="flaticon-heart"></span>
							</a>
							<a href="/single_product/${product._id}" class="d-flex align-items-center justify-content-center">
							  <span class="flaticon-visibility"></span>
							</a>
						  </p>
						</div>
					  </div>
					  <div class="text text-center">
						${product.sale ? '<span class="sale">Sale</span>' : 
						  product.newArrival ? '<span class="new">New Arrival</span>' : 
						  product.bestSeller ? '<span class="seller">Best Seller</span>' : ''}
						<span class="category">${product.category || 'N/A'}</span>
						<h2>${product.name || 'Unnamed Product'}</h2>
						${product.originalPrice ? 
						  `<p class="mb-0"><span class="price price-sale">$${product.originalPrice}</span> <span class="price">$${product.price}</span></p>` : 
						  `<span class="price">$${product.price}</span>`}
					  </div>
					</div>
				  </div>`;
				$('#productList').append(productHtml);
			  });
			}
	  
			$('#pagination ul').empty();
			if (data.currentPage > 1) {
			  $('#pagination ul').append(`<li><a href="#" data-page="${data.currentPage - 1}"><</a></li>`);
			}
			for (let i = 1; i <= data.totalPages; i++) {
			  $('#pagination ul').append(`<li class="${data.currentPage === i ? 'active' : ''}"><a href="#" data-page="${i}">${i}</a></li>`);
			}
			if (data.currentPage < data.totalPages) {
			  $('#pagination ul').append(`<li><a href="#" data-page="${data.currentPage + 1}">></a></li>`);
			}
	  
			$('.product-count').text(`Showing ${(data.currentPage - 1) * 9 + 1} - ${Math.min(data.currentPage * 9, data.totalProducts)} of ${data.totalProducts} products`);
			$('#productList').fadeIn(200);
			$('.spinner').hide();
			saveFilters();
		  },
		  error: function(xhr) {
			console.error('AJAX Error:', xhr);
			$('#productList').html('<p>Error loading products.</p>');
			$('.spinner').hide();
		  }
		});
	  }
	  
	  // Cập nhật sự kiện thay đổi cho checkbox
	  $('input[name="status"]').change(function() {
		updateProductList(1);
	  });
	  
	  // Cập nhật hàm saveFilters và loadFilters
	  function saveFilters() {
		const filters = {
		  search: $('input[name="search"]').val(),
		  category: $('#categorySelect').val(),
		  sort: $('#sortSelect').val(),
		  page: $('#pagination .active a').data('page') || 1,
		  minPrice: $("#hiddenMinPrice").val(),
		  maxPrice: $("#hiddenMaxPrice").val(),
		  status: [],
		};
		$('input[name="status"]:checked').each(function() {
		  filters.status.push($(this).val());
		});
		localStorage.setItem('productFilters', JSON.stringify(filters));
	  }
	  
	  function loadFilters() {
		const savedFilters = JSON.parse(localStorage.getItem('productFilters'));
		if (savedFilters) {
		  $('input[name="search"]').val(savedFilters.search || '');
		  $('#categorySelect').val(savedFilters.category || '');
		  $('#sortSelect').val(savedFilters.sort || '');
		  $("#hiddenMinPrice").val(savedFilters.minPrice || 0);
		  $("#hiddenMaxPrice").val(savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val()));
		  $("#price-range").slider("values", [savedFilters.minPrice || 0, savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val())]);
		  $("#price-values").text(`$${savedFilters.minPrice || 0} - $${savedFilters.maxPrice || parseFloat($("#hiddenMaxPrice").val())}`);
		  if (savedFilters.status && savedFilters.status.length > 0) {
			savedFilters.status.forEach(status => {
			  $(`input[name="status"][value="${status}"]`).prop('checked', true);
			});
		  }
		  updateProductList(savedFilters.page || 1);
		}
	  }
  
	// Xử lý tìm kiếm với debounce
	const debouncedUpdate = debounce(() => updateProductList(1), 500);
	$('input[name="search"]').on('input', debouncedUpdate);
	$('#searchForm').submit(function(e) {
	  e.preventDefault();
	  updateProductList(1);
	});
  
	// Xử lý thay đổi danh mục, sắp xếp, trạng thái
	$('#categorySelect, #sortSelect, #statusSelect').change(function() {
	  updateProductList(1);
	});
  
	// Xử lý phân trang
	$('#pagination').on('click', 'a', function(e) {
	  e.preventDefault();
	  const page = $(this).data('page');
	  updateProductList(page);
	});
  
	// Xử lý thêm vào giỏ hàng
	$('#productList').on('click', '.btn-add-to-cart', function(e) {
	  e.preventDefault();
	  const button = $(this);
	  const productId = button.data('product-id');
  
	  if (!productId) {
		console.error('Không tìm thấy productId');
		return;
	  }
  
	  button.prop('disabled', true);
	  button.find('span').removeClass('flaticon-shopping-bag').addClass('fa fa-spinner fa-spin');
  
	  $.ajax({
		url: '/add-to-cart',
		method: 'POST',
		contentType: 'application/json',
		data: JSON.stringify({ productId: productId, quantity: 1 }),
		success: function(response) {
		  $('#cart-message').html(
			`<div class="alert alert-success alert-dismissible fade show" role="alert">
			  ${response.message}
			  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">×</span>
			  </button>
			</div>`
		  );
		  if (response.cart && response.cart.totalItems) {
			$('#cart-count').text(response.cart.totalItems);
		  }
		  setTimeout(() => $('#cart-message').empty(), 3000);
		},
		error: function(xhr) {
		  const errorMsg = xhr.responseJSON?.message || 'Đã xảy ra lỗi khi thêm vào giỏ hàng';
		  $('#cart-message').html(
			`<div class="alert alert-danger alert-dismissible fade show" role="alert">
			  ${errorMsg}
			  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">×</span>
			  </button>
			</div>`
		  );
		},
		complete: function() {
		  button.prop('disabled', false);
		  button.find('span').removeClass('fa fa-spinner fa-spin').addClass('flaticon-shopping-bag');
		}
	  });
	});
  
	// Xử lý reset bộ lọc
	$('#resetFilters').click(function(e) {
	  e.preventDefault();
	  $('input[name="search"]').val('');
	  $('#categorySelect').val('');
	  $('#sortSelect').val('');
	  $("#hiddenMinPrice").val(0);
	  $("#hiddenMaxPrice").val(parseFloat($("#hiddenMaxPrice").val()));
	  $("#price-range").slider("values", [0, parseFloat($("#hiddenMaxPrice").val())]);
	  $("#price-values").text(`$0 - $${parseFloat($("#hiddenMaxPrice").val())}`);
	  $('#statusSelect').val([]);
	  $("#price-error").hide();
	  localStorage.removeItem('productFilters');
	  updateProductList(1);
	});
  
	// Tải trạng thái khi vào trang
	loadFilters();
  });