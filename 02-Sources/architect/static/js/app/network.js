/*
  Copyright (c) 2016 Benoit CHAMPOUGNY.  All right reserved.

  This file is part of Arduifarm

  Arduifarm is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Arduifarm is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
      along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>. 2
*/

// Event: user click on a tree element to display detail view.
$('body').on('click', '.network-refresh-detail', function(e){
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
