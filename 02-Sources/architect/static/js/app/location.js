
// Event: user click on a tree element to display detail view.
$('body').on('click', '.location-refresh-detail', function(e){
  e.preventDefault();
  var targetElement = $(this).attr('data-target');
  var url = $(this).attr('data-ajax-url');
  $.ajax({
    url: url,
    dataType: "html",
  })
  .done(function(data){
    $(targetElement).html(data);
    $('.tree_element').removeClass("active");
    $(".tree_element[data-ajax-url='"+url+"']").addClass("active");
  })
  .fail(function(data, textStatus, errorThrown ){
    var message="<strong>" + textStatus + "</strong> " + errorThrown
    app_alert_message(message);
  })
});
$('body').on('click', '.create-component', function(e){
  e.preventDefault();
  var targetElement = $(this).attr('data-target');
  var url = $(this).attr('data-ajax-url');
  $.ajax({
    url: url,
    dataType: "html",
  })
  .done(function(data){
    $(targetElement).html(data);
    $(targetElement).modal('show');
  })
  .fail(function(data, textStatus, errorThrown ){
    var message="<strong>" + textStatus + "</strong> " + errorThrown
    app_alert_message(message);
  })
});
