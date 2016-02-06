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
