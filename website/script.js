

function createMap(json) {

  // ** Map

  var map = L.map('map').setView([51.505, -0.09], 2);

  var layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png');

  map.addLayer(layer)

  var group = L.featureGroup();

  // Render the points.
  _.each(json.features, function(f) {

    var lat = f.geometry.coordinates[1];
    var lon = f.geometry.coordinates[0];

    var marker = L.circleMarker([lat, lon], {
      feature: f,
    });

    marker.bindPopup(f.properties.toponym);

    group.addLayer(marker)

  });

  map.addLayer(group);

  // ** Slider

  var input = $('input[type="range"]');

  // Set the last offset as the slider max.
  var maxOffset = _.last(json.features).properties.start;
  input.attr('end', maxOffset);

  input.rangeslider();

}


// Load the point data.
$(function() {
  $.getJSON('data/80d.geojson', createMap);
});
