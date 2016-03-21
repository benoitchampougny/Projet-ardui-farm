
function app_alert_message(message){
  var alert_message = $("#alert-text-message");
  var alert_box = $(alert_message).closest('.alert');
  $("#alert-text-message").html(message);
  $(alert_box).addClass('in');
  window.setTimeout(function () {
      $(alert_box).removeClass('in');
  }, 3000);
}
