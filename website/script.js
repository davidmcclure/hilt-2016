

function createMap(json) {

  // ** Map

  var map = L.map('map').setView([51.505, -0.09], 2);

  var layer = L.tileLayer.provider('Esri.WorldGrayCanvas');

  map.addLayer(layer)

  var markers = []

  // Loop through the points.
  _.each(json.features, function(f) {

    var lat = f.geometry.coordinates[1];
    var lon = f.geometry.coordinates[0];

    // Create the marker.
    var marker = L.circleMarker([lat, lon], {
      start: Number(f.properties.start),
      radius: 5,
      className: 'toponym',
    });

    // Attach the tooltip.
    marker.bindPopup(f.properties.toponym);

    map.addLayer(marker);
    markers.push(marker);

  });

  // ** Slider

  var input = $('#slider');

  // Set the last offset as the slider max value.
  var maxOffset = _.last(json.features).properties.start;
  input.attr('max', maxOffset);

  // When the slider is moved:
  input.on('input', function() {

    var val = input.val();

    _.each(markers, function(m) {

      // Show the marker if the slider is dragged beyond it's offset.
      if (m.options.start < val) {
        map.addLayer(m);
      }

      // Otherwise, hide it.
      else {
        map.removeLayer(m);
      }

    });

  });

  input.trigger('input');

}


// Load the point data.
$(function() {
  $.getJSON('data/80d.geojson', createMap);
});
