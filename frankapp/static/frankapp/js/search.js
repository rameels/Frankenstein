$(document).ready(function() {
  $('.search-tab').on('click', function() {
    $(this).removeClass('inactive-tab');
    $(this).siblings().addClass('inactive-tab');

    $('.active-tab-content').removeClass('active-tab-content');
    var tabContentClass = $(this).attr('data-tab');
    $('.' + tabContentClass).addClass('active-tab-content');
  });

  $('.performing-start-date, .performing-end-date').datepicker();
  $('.event-start-date, .event-end-date').datepicker();

  $('.people-type-checkbox').on('change', function(e) {
    if ($('.people-type-checkbox:checked').length == 0) {
      $(this).prop('checked', true);
    }
  });

  $('.people-search-button').on('click', function() {
    var url = '/search/people';
    var types = [];
    $('.people-type-checkbox:checked').each(function() {
      types.push($(this).attr('value'));
    });
    url += '?types=[' + types + ']';

    var name = $('.people-name-input').val();
    if (name) {
      url += '&name=' + name;
    }

    var startDate = $('.performing-start-date').val();
    if (startDate) {
      url += '&startDate=' + encodeURIComponent(startDate);
    }

    var endDate = $('.performing-end-date').val();
    if (endDate) {
      url += '&endDate=' + encodeURIComponent(endDate);
    }

    window.location = url;
  });

  var count = 1;
  $('.search-result').each(function() {
    var $slider = $(this).children().first();
    $slider.attr('id', 'slider-' + count);
    var slider = slidr.create('slider-' + count, {
      controls: 'none',
      fade: false,
      pause: false,
      theme: '#222',
      touch: true,
      transition: 'linear'
    });
    slider.start();

    $(this).find('.slider-right').on('click', function(e) {
      e.preventDefault();

      slider.slide('right');
      $(this).hide();
      $(this).next('.slider-left').show();
    });

    $(this).find('.slider-left').hide();
    $(this).find('.slider-left').on('click', function(e) {
      e.preventDefault();

      slider.slide('left');
      $(this).hide();
      $(this).prev('.slider-right').show();
    });

    count += 1;
  });


  $('.actor-image').each(function() {
    var photoSource = '../images/actor' + Math.floor((Math.random() * 5) + 1) + '.jpg';
    $(this).find('img').attr('src', photoSource);
  });
});
