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

## Create the map

1. In `index.html`, get rid of the `<h1>` tag inside of `<body>` and add an empty container element for the map:

  ```html
  <body>
    <div id="map"></div>
  </body>
  ```


- add map markup
- install leaflet, leaflet providers, lodash
- add slider
