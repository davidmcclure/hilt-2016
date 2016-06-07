

$(function() {

  var map = L.map('map').setView([51.505, -0.09], 13);

  var layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png');

  map.addLayer(layer)

  // Load the point data.
  $.getJSON('data/80d.geojson', function(json) {

    _.each(json.features, function(f) {

      console.log(f.geometry);
      var lat = f.geometry.coordinates[1];
      var lon = f.geometry.coordinates[0];

      var marker = L.circleMarker([lat, lon]);

      marker.bindPopup(f.properties.toponym);

      map.addLayer(marker)

    });

  });

});
