# Web map development with Javascript

Now that we've spent some time working with existing tools - QGIS, Neatline, Fusion Tables, CartoDB - let's finish by taking a look at what it takes to program some of these visualizations from the ground up with Javascript.

## Set up the development environment

1. Change back into the top-level `Projects` directoy: `cd ~/Projects`

1. Create a new directory with `mkdir website`, and change down into the new directory with `cd website`.

1. Create an empty HTML file with `touch index.html`.

1. Open up the file in Atom and stub in the basic structure for an HTML document:

  ```html
  <!doctype html>
  <html lang="en">

    <head>
      <title>HILT 2016</title>
    </head>

    <body>
      <h1>HILT 2016</h1>
    </body>

  </html>
  ```

## Run a development server

Next, we'll install Node.js, a server side Javascript runtime that will make it easy to start a local server for the page.

---

**MAC**

1. Run `brew install node`

**WINDOWS**

1. Go to https://nodejs.org and click the **v4.4.5 LTS** download button.

1. When the download finishes, run the .msi installer.

---

1. Install the `http-server` module: `npm install -g http-server`

1. Open up a new tab in the terminal and spin up a development server with `http-server`.

1. By default, this will bind to port `8080`. Open up a new tab in your browser and go to `http://localhost:8080`. If everything is wired up correctly, you'll see the "HILT 2016."

## Create a stylesheet

1. Back in the terminal, create a CSS stylesheet: `touch style.css`

1. Open it in Atom, and add a testing CSS rule:

  ```css
  body {
    background: red;
  }
  ```

1. Go back to the `index.html` file in Atom and find the `<title>` element. Right below that, add a `<link>` tag that pulls in our new stylesheet:

  ```html
  <link rel="stylesheet" href="style.css">
  ```

1. Go back to the browser and refresh the page. Now, the background should be bright red!

## Create a Javascript file

1. Back on the terminal, create a file to hold our custom Javascript: `touch script.js`

1. Open up the file, and add a testing `alert()` call, which will make it easy to see if the file is getting loaded.

  ```js
  alert('HILT 2016');
  ```

1. Back in `index.html` find the `<title>` element again. Below it, add a `<script>` tag that pulls in the file:

  ```html
  <script src="script.js"></script>
  ```

1. Refresh the page in the browser, and a little window should appear with "HILT 2016".

## Install Javascript libraries

1. Go to http://leafletjs.com/download.html and download the **Leaflet 1.0.0-rc1** .zip file.

1. Open the .zip archive and copy the `leaflet` folder.

1. Back in the `website` directory, create a new folder called `vendor`. Paste the `leaflet` folder in below of `vendor`.

1. Go to https://github.com/leaflet-extras/leaflet-providers/blob/master/leaflet-providers.js and click **Raw**. Select all of the code on the page with Command+A and then copy it with Command+C. Under `vendor`, create a file called `leaflet-providers.js`, and paste in the code.

1. Go to https://lodash.com/ and click on **Full build(~22 kB gzipped)**. Copy the code, and paste it into file called `vendor/loadsh.js`.

1. One more - go to https://jquery.com/download/ and click the **Download the compressed, production jQuery 3.0.0**.

1. Copy the `jquery-3.0.0.min.js` file into `vendor`.

1. Now, with the Javascript libraries in place - let's include each of them on the page. In `index.html`, update the `<head>` tag to look like this:

  ```html
  <head>

    <title>HILT 2016</title>

    <link rel="stylesheet" href="vendor/leaflet/leaflet.css">
    <link rel="stylesheet" href="style.css">

    <script src="vendor/jquery-3.0.0.min.js"></script>
    <script src="vendor/lodash.js"></script>
    <script src="vendor/leaflet/leaflet.js"></script>
    <script src="vendor/leaflet-providers.js"></script>

    <script src="script.js"></script>

  </head>
  ```

## Implement the map

Now, we're ready to write the code.

1. In `index.html`, get rid of the `<h1>` tag inside of `<body>` and add an empty container element for the map and time slider:

  ```html
  <body>
    <div id="map"></div>
    <input id="slider" type="range" min="0" value="0" />
  </body>
  ```

1. The final `script.js` file:

  ```js
  function createMap(json) {

    // ** Map

    var map = L.map('map').setView([0, 0], 2);

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
  ```

1. And, the final `style.css` file:

  ```css
  body {
    margin: 0;
    background: whitesmoke;
  }

  #map {
    width: 100vw;
    height: 100vh;
  }

  #slider {
    position: fixed;
    top: 1em;
    right: 1em;
    width: 30%;
  }

  path.toponym {
    stroke-width: 0;
    fill: rebeccapurple;
  }
  ```
