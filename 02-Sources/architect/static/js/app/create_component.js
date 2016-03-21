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

// SELECT COMPONENT MODEL
var xhr;
var select_component_type, $select_component_type;
var select_component_model, $select_component_model;

console.log("hello");

$select_component_type = $('#select-component-type').selectize({
    onChange: function(value) {
        if (!value.length) return;
        var api_url = $('#select-component-type').attr('data-api-url');
        console.log(api_url);
        select_component_model.disable();
        select_component_model.clearOptions();
        select_component_model.load(function(callback) {
          $.ajax({
            url: api_url,
            data: {'component_type': value},
            dataType: "json",
          })
          .done(function(data){
              select_component_model.enable();
              var formattedData=[];
              $.each(JSON.parse(data), function(i, n){
                formattedData.push({'name': n.fields.name, 'pk': n.pk});
              });
              console.log(formattedData);
              callback(formattedData);
          })
          .fail(function(data, textStatus, errorThrown ){
              callback();
          })
        });
    }
});

$select_component_model = $('#select-component-model').selectize({
    valueField: 'pk',
    labelField: 'name',
    searchField: ['name']
});

select_component_model  = $select_component_model[0].selectize;
select_component_type = $select_component_type[0].selectize;

select_component_model.disable();
