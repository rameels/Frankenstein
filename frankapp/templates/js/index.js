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
});
