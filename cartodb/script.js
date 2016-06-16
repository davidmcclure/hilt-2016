

function createMap() {


  // ** Map

  var map = L.map('map').setView([0, 0], 2);

  var layer = L.tileLayer.provider('Esri.WorldGrayCanvas');

  map.addLayer(layer)

  var layerUrl = 'https://davidwilliammcclure.cartodb.com/api/v2/viz/e9d13f1c-3305-11e6-8260-0e3a376473ab/viz.json';
  cartodb.createLayer(map, layerUrl).addTo(map);


}


// Load the point data.
$(function() {
  createMap();
});
