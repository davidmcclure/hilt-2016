# Analyzing and Presenting Spatial data

Welcome! Over the course of the next four days we're going take a look at a wide range of tools and techniques for working with spatial data in the humanities. By the end of the week, it's my hope that everyone will be able to build effective spatial humanities projects using off-the-shelf tools, and also know how to get started with more complex or unusual projects that call for some custom data preparation or interface design.

In a conceptual sense, the course is laid out along a kind of conceptual axis that I think provides a useful way to think about the range of GIS praxis in the humanities. On one end is a set of methodologies that might be thought of as deliberately "small data" - hand-crafted data, Drucker and Nowviskie's notion of "graphesis," a mode of knowing in the humanities that arises from very close consideration of spatially-inflected materials and information. At the other end of the spectrum is a set of practices that more closely resemble GIS as practiced in the sciences, the social sciences, government, and industry - a focus on large amounts of data, with an eye towards building data models that are simple and tractable at very large scales. In many ways this echoes the distinction in computational text analysis between traditional "close reading" and "distant reading," which makes it possible to ask questions at a much larger scale, but often with the tradeoff that the questions themselves tend to become somewhat more specific, structured, and empirical - which, depending on the goals of the project, can be either a good or a bad thing. both ends of this continuum have their advantages, and neither offers a complete set of solutions - indeed, as we'll see over the course of the next few days, both approaches (and everything in between) have real shortcomings, and I tend to think it's best to think of them as complements - two different hammers in the toolbox, suitable for different projects and even at different stages of the same project.

While we're thinking in dialectical terms, another useful way of slicing and dicing spatial humanities projects is along whether they make use of existing tools - frameworks like Neatline, CartoDB, ESRI StoryMap, Odyssey.js, etc - or if they're programmed from scratch. again, there's no right or wrong answer here. the tools are enormously useful - when you have a project that fits well into the capabilities of one of these existing frameworks, it's often possible to go from nothing to a more-or-less complete project in a really short amount of time - just days or weeks, where programming the equivalent functionality from scratch would take months or even years. but, the tools also impose a particular set of assumptions and constrains onto a project - the type of information that can be modeled, how it's presented, the range of things that the reader of the project is able to do with the data, etc. many times these constrains are a small price to pay for the gains in productivity, ease-of-use, and sustainability. but other times the constraints can be stifling - some projects just don't fit neatly within the set of imagined use cases the that tools cater towards, and when this is the case it's often actually faster to just program something from scratch instead of trying to coax an existing framework to do something that it wasn't really designed to do. In the same way that we'll run the whole gamut from small data to big data, we'll also work at different points along this axis, from the most off-the-shelf - say, Google Fusion Tables - to the most bespoke - writing custom data extraction scripts in Python and using of Javascript libraries like Leaflet and d3 to make custom visualizations.

 Last, before we dive in, a quick note about the technical details of the course. More often than not, I think it makes sense to walk through the whole process of getting set up with the computing environment necessary to do the task at hand - installing software, getting set up with high-quality code editors, configuring the development rigs that make it easy to write custom code, etc. As opposed to, say, working with pre-configured virtual machines or doing everything through centrally-hosted web services. (Though, we'll do some of that too.) This setup process can be annoying at times, since things invariably go wrong - different operating systems, different versions of the same operating systems, different combinations of software installed on different machines - all conspire to make it difficult to draw up a single list of steps that will work without fail on all systems. But, in the long run, I think this is time well-spent - debugging software configuration problems is sort of an unavoidable tax levied on pretty much any kind of computational work, I think. (I certainly spend a huge amount of time doing it myself.) And, at the end of the process - there's something liberating about having as close to full control as possible over the means of production in these kinds of projects. When you know how all the pieces fit together, it's easier to know where to look and what questions to ask when things go wrong. It also decouples you somewhat from capabilities and bandwidth of the IT services available at your institution, which can make it easier to get up and running with new projects without having to go through formal channels for support.

# Course outline

**Part 1: Graphesis, Minard**

We'll start out by looking at Neatline, a digital mapping framework developed at the University of Virginia between 2012 and 2015. Neatline was designed around Drucker's notion of "graphesis," and is designed to make it possible to create hand-crafted, richly humanistic interactions with maps and spatial information. We'll start out by creating a digital edition of Charles Minard's famous infographic of Napoleon's 1812 invasion of Russia - we'll use QGIS to georeference a digital scan of the original image, load the prepared image into Geoserver (an open-source geospatial tile server that makes it possible to publish georeferenced images on the web), import the web-accessible image into Neatline as an overlay, and then finally use Neatline's vector annotation tools to create a set of interactive overlays on top of Minard's original map.

**Part 2: Spatial texts, Whitman**

Next, we'll look at a set of extensions for Neatline that were developed to make it possible to create interactive spatial editions of text documents, a requirement that came up again and again in the process of using Neatline with faculty and students. We'll each take a stanza of "Salut au Monde" - one of Whitman's largest and most intricate "spatial catalogues" from _Leaves of Grass_ - and create a set of Neatline exhibits that plot out the locations (often delightfully fuzzy and imprecise) mentioned in the poem. At the end, we'll take all of the individual exhibits and merge them together into a single exhibit for the whole poem.

**Part 3: Data extraction, cleaning, and formatting**

Building on the (painstaking, slow) process of manually picking out place references from Whitman - in the second day we'll use a Python package called Polyglot to do named entity extraction (NER) on a set of novels downloaded from the Project Gutenberg corpus. Once we've pulled out a list of toponyms from the raw text, we'll use the Data Science Toolkit to geocode each of place names, which will assign a regular longitude / latitude coordinate to each place name and make it possible to plot them on a map.

**Part 4: Spatial data visualizations**

Next, working with the data extracted from the novels, we'll take the lists of toponyms and use a series of off-the-shelf tools that are well-suited for visualizing this type of well-structured spatial data - starting with simple solutions like geojson.io and Google Fusion Tables and then spending more time with CartoDB, a full-featured framework (similar to Neatline in some respects) that makes it possible to create custom layers, query the data in interesting ways, and publish maps to the web.

**Part 5: Web map programming**

Last, we'll end by dipping back into the code and learning the basics of building custom web mapping applications using HTML, CSS, and Javascript, which can come in handy when the existing tools don't do exactly what you want. After plotting the locations extracted from a novel on an interactive map, we'll build a time slider that makes it possible to visualize the progression of the toponyms over the course of the "novel time" of the text.

---

# Georeference Minard's map in QGIS

So, to get started with our Neatline edition of Mianrd's Napoleon infographic.

1. First, grab the raw image of the inforgraphic from Wikipedia - https://commons.wikimedia.org/wiki/File:Minard.png. Click on the preview to get the full-size version, and then right click, choose "Save Image As," and save it somewhere easy to find.

1. Next, we'll download QGIS ("Quantum GIS"), an open-source GIS suite that provides much of the functionality offered by more heavyweight (and expensive) solutions like ArcGIS. Go to http://www.qgis.org/, click **Download Now**, and select the downloader for your operating system.

1. **MAC** If you're on Mac, you'll get taken to KyngChaos downloads page. Download the **QGIS 2.14.3-1** file and open up the DMG archive. Inside, you'll see four different `.pkg` files, labeled 1 to 4. QGIS is the final one, but you'll need to install each of these in order to get all of the required dependencies.

1. **WINDOWS** TODO

1. Once the install finishes, open up QGIS. First, we need to add a modern-geography base layer to QGIS as a baseline to georeference against. The easiest way to do this is to install a plugin for QGIS called QuickMapServices. Open the plugins manager by clicking on **Plugins > Manage and Install Plugins**.

1. Search for "QuickMapServices," click the row, and then click **Install**.

1. Close out of the plugins manager and click on the **Web > QuickMapServices > OSM > OSM Mapnick**. This will add a basic OpenStreetMap base layer to the project.

1. Now, the georeferencing. Click on **Raster > Georeferencer > Georeferencer**.

1. Click on the right-most button in the main menu bar with the green "+" icon and select the image of Minard's infographic that we downloaded from Wikipedia. In the "Coordinate Reference System Selector" window that appears, leave the defaults as is (WGS 84 / Pseudo Mercator) and click OK.

1. Now, to georectify the image, we just have to lay down a set of control points that link locations on Minard's map with spatial coordinates on the modern base layer. Click on the "Add Point" button, and then click once on the image just to the left of the "Kowno" label on the left side of the image.

1. In the window that appears, click on **From map canvas**. The georectifier will disappear, showing the OpenStreetMap in the QGIS project. Hold down the space bar and move the cursor to drag the map over to Kaunas in the middle of modern-day Lithuania. Click once on the middle of the city to lay down a corresponding point on the map.

1. Repeat this process for Moscow, on the other side of the image - click once right on the meeting point between the beige and black flowchart segments, click **From map canvas**, find Moscow on the base layer, and click on it to lock in the association. Now, with two points, we've given the georeferenced enough information to position, scale, and rotate Minard's image so that it roughly lines up with the corresponding geography on the base layer. Before we export the rectified image, though, let's create a directory to house the various files we'll be working with on this project.

1. **MAC** Click on the search button at the top right of the screen, search for "terminal," and open up the Terminal application. I generally like to organize things into a top-level `Projects` directory in my user's home directory. If you don't already have something like this, go ahead and create this directory with: `mkdir Projects`. Then, change down into the new directory with `cd Projects`, and create a sub-directory called `minard` with `mkdir minard`.

1. **WINDOWS** TODO

Click on the yellow geat button to open the "Transformation Settings" dialog.

1. In "Transformation type," choose "Helmert."

1. Click the "..." button next to "Output Raster," find the `minard` dierctory that we created above, and enter `minard` as the name for the exported file.

1. Click **OK** to save the settings, and click the "play" button to export the file.

1. Now, we can open up the exported image in QGIS and check the rectification. Go back to regular QGIS and click the "Add Raster Layer" button in the vertical toolbar on the left. Find the `~/Projects/minard` directory and select the new `minard.tif` produced by the Georeferencer. Click **Open**, and the rectified image will appear on the map.

So - what's up with those ugly black borders around the image? When an image is georeferenced, it often ends up getting rotated away from its original orientation, as was the case here. In the final image, QGIS will fill in the gaps between the image and the containing rectangle with "0-value" pixels, which, annoyingly, results in the black borders around the image when it gets displayed on a map. We can fix this, though, by using a command-line utility called GDAL to replace these black pixels with transparent pixels, which gets rid of the borders. GDAL is great - it's kind of like a swiss-army knife for working with spatial data, and comes in handy in lots of different contexts.

1. Use this `gdalwarp` command to strip off the black borders:

`gdalwarp -srcnodata 0 -dstalpha minard.tif minard-noborders.tif`

Now we've got a georectified and cleaned-up GeoTIFF, which can be brought into Neatline for annotation and display.

# Upload the georectified map to Geoserver

Before we can import the map into Neatline, though, we first need to upload it to a special type of web server that dynamically splits the image up into smaller "tiles," which can be laid on top of a regular base layer. We'll be using GeoServer, an open-source tiling server that powers the spatial data repositories at places like UVa, Stanford, Harvard, and elsewhere. GeoServer hosting is often provided at an institutional level by universities - often through the library - and it's also possible to buy commercial hosting from providers like AcuGIS. For now, though, we can just download it onto our own computers and run a development instance of the server.

1. Go to http://geoserver.org/release/stable and download the release for your operating system.

1. **MAC** Open the .dmg file and drag the GeoServer icon into the Applications folder. From Applications, run GeoServer and click on **Server > Start**.

1. **WINDOWS** TODO

1. Once the server is running, you'll get taken to the login screen for the administrative console. Log in with **admin / geoserver**.

Now, with GeoServer up and running, we can upload the georeferenced image.

1. Click on **Workspaces** and then **Add new workspace**.

1. Enter `hilt` into the "Name" field, and put some kind of URL into "Namespace URI" - a personal website, department homepage, etc, (Doesn't matter what - just has to be a valid URL.) Click **Submit** to create the new workspace.

1. Click on **Stores**, **Add new store**, and then **GeoTIFF**.

1. Select the new `hilt` workspace you just created and enter `minard` in the "Data Source Name" field.

1. Click **Browse...** next to the "URL" field, and then select **Home directory** from the dropdown at the top of the dialog. Find the `Projects/minard` directory that we created before, and select the `minard-noborders.tif` file.

1. From the next screen, click **Publish**.

1. In the "Name" field, just enter `minard`.

1. Scroll down to the "Coordinate Reference Systems" field set and click **Find...** next to "Declared SRS." Search for "900913" (hint - this looks like "Google," if you squint your eyes, which isn't a coincidence!) and click the **900913** link under "Code" for the "WGS84 / Google Mercator" listing.

1. Click **Save** to add the new layer. To confirm that the layer is up and running, click on the **Layer Preview** link in the left column and find the `hilt:minard` layer. Click on the **OpenLayers** link to display the tiled layer in an interactive map.

# Install Omeka + Neatline

Ok - now we've got our map georeferenced and uploaded into a tile server that can broadcast the image out onto the web. Next, we'll install Omeka and Neatline into a local development sandbox, which is generally the easiest way to get up and running at the start of a new project. Once you've got something that you want to put on the web and share with others, it's easy to just copy the files and database from the local installation, move them onto a web-facing server, and pick up where you left off.

## Install MAMP

First up we'll install MAMP, a free piece of software that automates the process of running a development "LAMP stack" (Linux, Apache, MySQL, PHP) server on your computer. There's a "pro" version that you have to pay money for, but the free version works just fine.

1. Go to http://mamp.info/ and click on the "Download" links.

1. When the file finishes downloading, run the .pkg file, which will open up a regular Mac installer program. Click through the steps to install the package.

1. Once MAMP is installed, you'll have a new folder in your `Applications` directory called `MAMP`. Open up that folder, and you'll see a listing for `MAMP`, which is the actual program that manages the server. Double-click on that to launch the configuration utility, and then click on **Start Servers** to spin up the server.

## Install Omeka

1. Go to http://omeka.org/ and click on the **Download Omeka** link.

1. On the downloads page, click **Download Omeka 2.4.1**.

1. Find the omeka-2.2.2.zip file in the `Downloads` directory and double click to uncompress it. You'll end up with a regular directory called `omeka-2.4.1`.

1. Click on the folder that was extracted from the .zip archive and copy it to the clipboard by pressing Command+C.

1. In Finder, go to `Applications/MAMP/htdocs` and paste in the Omeka folder.

1. Right click on the folder and click on **Get Info**. In the "Name and Extension" input, change `omeka-2.4.1` to just plain `omeka`. This isn't required, but it will make the URLs in your development environment a bit less cluttered.

1. Open up a browser and go to `http://localhost:8888/MAMP`, the configuration home page for MAMP. At the top of the screen, select **Tools > phpMyAdmin**. phpMyAdmin is a configuraton interface for the MySQL database that will store the data that gets added to the Omeka site.

1. First, we need to create a new database. Click on the **Databases** tab at the top of the screen, and find the **Create Database** input. Type omeka, and then hit **Create**.

1. Next, we'll create a user than can connect to the database. Click on the **Users** tab along the top, and then click the **Add user** link at the bottom.

1. Type a name into the **User name** field. This can be anything you like - in development, I just use `omeka`, which is easy to remember.

1. Click on the dropdown next to "Host" and select "Local."

1. Type a password into the "Password" field. On a production server, this should be a strong, secure password. But, in development I just use `omeka` again.

1. Re-type the password in the last field.

1. In the "Global privileges" panel at the bottom of the page, just click the **Check All** input. This basically makes the user into a "super user" who can do anything.

1. Next, we need to tell Omeka where to find the database. Go back to the `omeka` folder in Finder, open it up, and open the `db.ini` file. **Note**: If you don't already have some kind of text editor for editing source code, go to https://atom.io/ and download Atom, a really nice, unobtrusive code editor with lots of cool features.

1. In db.ini, you'll see this:

  ```ini
  [database]
  host     = "XXXXXXX"
  username = "XXXXXXX"
  password = "XXXXXXX"
  dbname   = "XXXXXXX"
  prefix   = "omeka_"
  charset  = "utf8"
  ;port     = ""
  ```

  Fill in `host`, `username`, `password`, and `dbname` with the values that we set in phpMyAdmin:

  ```
  [database]
  host     = "localhost"
  username = "omeka"
  password = "omeka"
  dbname   = "omeka"
  prefix   = "omeka_"
  charset  = "utf8"
  ;port     = ""
  ```

  And, save this file to lock in the new settings.

1. Last, we just need to run Omeka's web-based installer. Go to http://localhost:8888/omeka and fill out all of the required fields (Username, Password, Email, Administrator Email, and Site Title). Then, click the **Install** button, and, if all goes well, you'll see a page that says "Success!" with links to the public site and admin dashboard.

1. Click on "Admin Dashboard," which is where we'll need to be for the last step.

## Install Neatline

Last - Neatline, which is a plugin that sits inside of Omeka.

1. Go back to omeka.org and click on "Add-Ons" in the main menu.

1. On the right side of the screen, click on **All Plugins**, and then scroll down to the listing for "Neatline." Click on the **Download v2.5.1** link.

1. When the .zip archive finishes downloading, find it in the Downloads folder and double-click it to extract the `Neatline` folder, which contains the source code.

1. Click on `Neatline` and press Command+C to copy it to the clipboard.

1. Go back to the Omeka folder at `Applications/MAMP/htdocs/omeka` and open up the plugin folder. Paste in the Neatline folder, so that the final directory structure is `Applications/MAMP/htdocs/omeka/plugins/Neatline`.

1. Go back to the Omeka admin dashboard in the browser an click on the **Plugins** link at the top of the screen. Find the listing for "Neatline," and click the **Install** button.

# Minard + Napoleon

Now that Neatline is up and running, let's build our interactive edition of Minard's infographic.

## Part 1: Import Minard's Map

First, we'll create a new Neatline exhibit.

### Create an exhibit.

1. Click on the **Neatline** tab at the bottom of the vertical menu on the left.

1. Click on the **Create an Exhibit** link at the top of the screen. This opens up a form where you can enter basic information about the new exhibit.

1. Enter a title into the Title field. Something like - "Minard + Napoleon." For now, don't worry about the URL slug (Neatline will automatically generate a value based on your title) or the Narrative field.

1. Click **Save Exhibit**. You’ll be taken back to the main list of exhibits, where you'll see a listing for your new exhibit.

1. Click on the title to open the Neatline editing interface.

### Set the default map focus

Before we start adding content, we’ll need to set the default focus location and zoom level that are displayed when the exhibit starts.

1. Start by panning and zooming the map to exactly the location that you want to use as the default. Since we’re going to be working with the Minard map, click and drag on the map to focus on western Russia, and then use the zoom buttons (or the scroll wheel on the mouse) to zoom in until the space between Kaunas and Moscow takes up most of the screen.

1. Once you’ve got the map in the right place, click on the **Styles** tab at the top of the editing panel on the left side of the screen and scroll down to the "Default Map Focus" and "Default Map Zoom" fields. Click the **Use Current Viewport** as Default button to automatically populate the two fields with values that correspond to the current position of the map.

1. Click on **Save** to lock in the new defaults. Now, when you refresh the page (or when a visitor comes to the exhibit), the map will start at this location.

### Import Minard's map

Now, let’s add some content. We’ll start by importing the WMS layer of Minard's map that we created in Geoserver.

1. Click back to the **Records** tab at the top of the screen and then click on the big **New Record** button.

1. In the Title field, enter "Minard's Map." Since this record is just going to be used to represent the map, and won’t have any exposed text information in the exhibit, the title doesn't really matter - it's mostly just a way to label it and keep track of things in the editor.

1. Click over to the **Style** tab in the top row and scroll down to the Imagery field set. In the WMS Address field, enter:

  `http://localhost:8080/geoserver/hilt/wms`

1. And, in the WMS Layers field, enter `minard`.

1. Click **Save** at the bottom of the form, and the map will appear as a translucent overlay on top of the satellite imagery.

1. Next, we'll want to bump up the opacity of the layer so we can see it better. Scroll up to the Opacities field set and change **Fill Opacity** to about 0.8 and **Fill Opacity (Selected)** to about 0.9. You can type directly into the form input, or you can click and drag up and down on the page to smoothly change the value of the input.

1. Once you're done, click **Save** at the bottom of the form, and then go back to the list of records by clicking the X button at the top of the form.

## Part 2: Annotate the map

Now, with the map in place - let's annotate it.

### Annotate the text

First things first - I don't speak French, so let's transcribe the title and description printed across the top of Minard's graphic. For reference, here's the English translation:

  Figurative Map of the successive losses in men of the French Army in the Russian campaign 1812-1813.

  Drawn up by M. Minard, Inspector General of Bridges and Roads in retirement.

  Paris, November 20, 1869.

  The numbers of men present are represented by the widths of the colored zones at a rate of one millimeter for every ten-thousand men; they are further written across the zones. The information which has served to draw up the map has been extracted from the works of M. M. Thiers, of Segur, of Fezensac, of Chambray, and the unpublished diary of Jacob, pharmacist of the army since October 28th. In order to better judge with the eye the diminution of the army, I have assumed that the troops of prince Jerome and of Marshal Davoush who had been detached at Minsk and Moghilev and have rejoined around Orcha and Vitebsk, had always marched with the army.

1. Click on **New Record** and enter in the full text of Minard's title into Neatline's "Title" field.

1. Click on the **Map** tab to display the geometry editing controls. Activate the **Draw Polygon** option and then move the cursor onto the map. Now that a drawing mode is activated, a little point will trail the cursor.

1. To start, draw a long, skinny rectangle around the text of the title along the top of the image - click down on the map and release to lay a point. When you come to the last point, double-click to "seal" the shape and stop drawing new points.

1. By default, opacity of the polygon is rather high, and makes it bit distracting when layered on top of the text. To make it easier on the eyes, click over into the **Style** tab and find the **Fill Color** option. Click on the input to open the color picker, and change the color to solid white. Do the same for the **Fill Color (Selected)** field, which controls the color of the shape when the cursor is hovered on top of it.

1. We can do even better than this - what if, by default, the annotation were invisible, and only displayed when the reader pointed the cursor at the text? We can make this happen by dropping the **Fill Opacity** and **Stroke Opacity** down to 0, which makes the record effectively invisible until it's switched into "selected" mode when the cursor hovers on it.

1. When the record looks good, click the **Save** button at the bottom of the screen to lock in the changes, and then close out the record with the **X** at the top of the form.

1. Repeat this process for the byline, the date, and the description - for each, create a new record, trace out the text with a polygon, and set the styles.




TODO:
  - plot kaunas and Moscow
  - trace neman
  - trace flowchart segments
