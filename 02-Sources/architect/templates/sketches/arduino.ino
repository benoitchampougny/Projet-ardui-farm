/*******************************************************************************
ARDUINO AUTO GENERATED SKETCHES
*******************************************************************************/

/*******************************************************************************
ARDUINO GENERAL HEADERS
*******************************************************************************/
{% for sketch in element.cardModel.sketches.all %}
// Sketch: {{sketch.name}}
{% include sketch.header %}
{% endfor %}


/*******************************************************************************
ARDUINO CONNECTED ELEMENT HEADERS
*******************************************************************************/
{% for connected_element in element.connected_dio_elements %}
  {% for sketch in connected_element.cardModel.sketches.all %}
  // Sketch: {{sketch.name}}
{% include sketch.header %}
  {% endfor %}
{% endfor %}


void setup()
{
  /*******************************************************************************
  ARDUINO GENERAL SETUP
  *******************************************************************************/
  {% for sketch in element.cardModel.sketches.all %}
  // Sketch: {{sketch.name}}
  {% include sketch.setup %}
  {% endfor %}


  /*******************************************************************************
  ARDUINO CONNECTED ELEMENT SETUP
  *******************************************************************************/
  {% for connected_element in element.connected_dio_elements %}
    {% for sketch in connected_element.cardModel.sketches.all %}
    // Sketch: {{sketch.name}}
  {% include sketch.setup %}
    {% endfor %}
  {% endfor %}
}


void loop()
{
  /*******************************************************************************
  ARDUINO GENERAL LOOP
  *******************************************************************************/
  {% for sketch in element.cardModel.sketches.all %}
  // Sketch: {{sketch.name}}
  {% include sketch.loop %}
  {% endfor %}


  /*******************************************************************************
  ARDUINO CONNECTED ELEMENT LOOP
  *******************************************************************************/
  {% for connected_element in element.connected_dio_elements %}
    {% for sketch in connected_element.cardModel.sketches.all %}
    // Sketch: {{sketch.name}}
  {% include sketch.loop %}
    {% endfor %}
  {% endfor %}
}
