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
});
