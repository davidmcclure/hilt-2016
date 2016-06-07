

$(function() {

  var map = L.map('map').setView([51.505, -0.09], 2);

  var layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png');

  map.addLayer(layer)

  var group = L.featureGroup();

  // Load the point data.
  $.getJSON('data/80d.geojson', function(json) {

    _.each(json.features, function(f) {

      var lat = f.geometry.coordinates[1];
      var lon = f.geometry.coordinates[0];

      var marker = L.circleMarker([lat, lon]);

      marker.bindPopup(f.properties.toponym);

      group.addLayer(marker)

    });

    map.addLayer(group);

  });

});
