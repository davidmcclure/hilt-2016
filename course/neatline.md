# Georeference Minard's map in QGIS

So, to get started with our Neatline edition of Mianrd's Napoleon infographic.

1. First, grab the raw image of the inforgraphic from Wikipedia - https://commons.wikimedia.org/wiki/File:Minard.png. Click on the preview to get the full-size version, and then right click, choose "Save Image As," and save it somewhere easy to find.

1. Next, we'll download QGIS ("Quantum GIS"), an open-source GIS suite that provides much of the functionality offered by more heavyweight (and expensive) solutions like ArcGIS. Go to http://www.qgis.org/, click **Download Now**, and select the downloader for your operating system.

---

**MAC**

1. If you're on Mac, you'll get taken to KyngChaos downloads page. Download the **QGIS 2.14.3-1** file and open up the DMG archive.

1. Open the DMG file. Inside, you'll see four different `.pkg` files, labeled 1 to 4. QGIS is the final one, but you'll need to install each of these in order to get all of the required dependencies.

**WINDOWS**

1. On the downloads page, click **QGIS Standalone Installer Version 2.14 (64 bit)**.

1. When the download finishes, open the .exe file to run the installer.

---

1. Once the install finishes, open up QGIS. First, we need to add a modern-geography base layer to QGIS as a baseline to georeference against. The easiest way to do this is to install a plugin for QGIS called QuickMapServices. Open the plugins manager by clicking on **Plugins > Manage and Install Plugins**.

1. Search for "QuickMapServices," click the row, and then click **Install**.

1. Close out of the plugins manager and click on the **Web > QuickMapServices > OSM > OSM Mapnick**. This will add a basic OpenStreetMap base layer to the project.

1. Now, the georeferencing. Click on **Raster > Georeferencer > Georeferencer**.

1. Click on the right-most button in the main menu bar with the green "+" icon and select the image of Minard's infographic that we downloaded from Wikipedia. In the "Coordinate Reference System Selector" window that appears, leave the defaults as is (WGS 84 / Pseudo Mercator) and click OK.

1. Now, to georectify the image, we just have to lay down a set of control points that link locations on Minard's map with spatial coordinates on the modern base layer. Click on the "Add Point" button, and then click once on the image just to the left of the "Kowno" label on the left side of the image.

1. In the window that appears, click on **From map canvas**. The georectifier will disappear, showing the OpenStreetMap in the QGIS project. Hold down the space bar and move the cursor to drag the map over to Kaunas in the middle of modern-day Lithuania. Click once on the middle of the city to lay down a corresponding point on the map.

1. Repeat this process for Moscow, on the other side of the image - click once right on the meeting point between the beige and black flowchart segments, click **From map canvas**, find Moscow on the base layer, and click on it to lock in the association. Now, with two points, we've given the georeferenced enough information to position, scale, and rotate Minard's image so that it roughly lines up with the corresponding geography on the base layer. Before we export the rectified image, though, let's create a directory to house the various files we'll be working with on this project.

---

**MAC**

1. Click on the search button at the top right of the screen, search for "terminal," and open up the **Terminal** application. First, create general-purpose `Projects` directory with `mkdir Projects`.

1. Change down into the new directory with `cd Projects`, and create a sub-directory called `minard` with `mkdir minard`.

**WINDOWS**

1. In the "Cortana" search box, search for "command," and open the **Command Prompt**.

1. Create a `Projects` directory with `mkdir Projects`.

1. Change down into the new directory with `cd Projects`, and create a sub-directory called `minard` with `mkdir minard`.

---

1. Back in georeferencer, click on the yellow gear button to open the "Transformation Settings" dialog.

1. In "Transformation type," choose "Helmert."

1. Click the "..." button next to "Output Raster," find the `minard` dierctory that we created above, and enter `minard` as the name for the exported file.

1. Click **OK** to save the settings, and click the "play" button to export the file.

1. Now, we can open up the exported image in QGIS and check the rectification. Go back to regular QGIS and click the "Add Raster Layer" button in the vertical toolbar on the left. Find the `~/Projects/minard` directory and select the new `minard.tif` produced by the Georeferencer. Click **Open**, and the rectified image will appear on the map.

So - what's up with those ugly black borders around the image? When an image is georeferenced, it often ends up getting rotated away from its original orientation, as was the case here. In the final image, QGIS will fill in the gaps between the image and the containing rectangle with "0-value" pixels, which, annoyingly, results in the black borders around the image when it gets displayed on a map. We can fix this, though, by using a command-line utility called GDAL to replace these black pixels with transparent pixels, which gets rid of the borders. GDAL is great - it's kind of like a swiss-army knife for working with spatial data, and comes in handy in lots of different contexts.

---

**WINDOWS**

1. GDAL is automatically installed with QGIS on Mac, but on Windows we have to install it separately. Go to http://trac.osgeo.org/osgeo4w/wiki and download the **64 bit** OSGeo4W network installer.

1. Run the installer, and then search for "osgeo" in the search bar. Open **OSGeo4W Shell**.

1. Change down into the `minard` directory: `cd Users\<username>\Projects\minard`

---

1. Use the `gdalwarp` command to strip off the black borders:

`gdalwarp -srcnodata 0 -dstalpha minard.tif minard-noborders.tif`

Now we've got a georectified and cleaned-up GeoTIFF, which can be brought into Neatline for annotation and display.

# Upload the georectified map to Geoserver

Before we can import the map into Neatline, though, we first need to upload it to a special type of web server that dynamically splits the image up into smaller "tiles," which can be laid on top of a regular base layer. We'll be using GeoServer, an open-source tiling server that powers the spatial data repositories at places like UVa, Stanford, Harvard, and elsewhere. GeoServer hosting is often provided at an institutional level by universities - often through the library - and it's also possible to buy commercial hosting from providers like AcuGIS. For now, though, we can just download it onto our own computers and run a development instance of the server.

1. Go to http://geoserver.org/release/stable and download the release for your operating system.

---

**MAC**

1. Open the .dmg file and drag the GeoServer icon into the `Applications` folder.

1. From `Applications`, run GeoServer and click on **Server > Start**.

**WINDOWS**

1. Go to http://java.com/en/download/, download the latest version of Java, and run the installer.

1. Run the GeoServer installer.

1. Search for "geoserver," and run **Start GeoServer**. Click **Allow Access** if a notice appears.

1. Minimize the command prompt and leave it running in the background.

---

1. Once the server is running, open up a browser tab and go to http://localhost:8080/geoserver.

1. Log in with **admin / geoserver**.

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

1. Click on **New Record** and enter in the English text of Minard's title into Neatline's "Title" field.

1. Click on the **Map** tab to display the geometry editing controls. Select the **Draw Polygon** option and then move the cursor onto the map. Now that one of the drawing modes is activated, a little point will trail the cursor.

1. To start, draw a long, skinny rectangle around the text of the title along the top of the image. To start drawing the shape, put the cursor where you want to lay down the first point, click once, and then click again for each of the corners in the rectangle. When you come to the last point, double-click to "close" the shape and stop drawing new points. (It's always possible to modify geometries after the fact, so don't worry about being too precise on the first pass.)

1. By default, opacity of the polygon is rather high, and makes it bit distracting when layered on top of the text. To make it easier on the eyes, click over into the **Style** tab and find the **Fill Color** option. Click on the input to open the color picker, and change the color to solid white. Do the same for the **Fill Color (Selected)** field, which controls the color of the shape when the cursor is hovered on top of it.

1. We can do even better than this - what if, by default, the annotation were invisible, and only displayed when the reader pointed the cursor at the text? We can make this happen by dropping the **Fill Opacity** and **Stroke Opacity** down to 0, which makes the record effectively invisible until it's switched into "selected" mode when the cursor hovers on it.

1. When the record looks good, click the **Save** button at the bottom of the screen to lock in the changes, and then close out the record with the **X** at the top of the form.

1. Repeat this process for the byline and date - create a new record, trace out the text with a polygon, and set the styles.

1. For the description - which is longer, and might look a bit cramped if we put the whole thing in the title field - just enter the first couple words into the title, and then paste the rest into the "Description" field. This way, when the user hovers on the annotation on the map, the snippet in the title will appear, and the rest of the text will be displayed on click.

1. When you're finished, close out of the last record and go back to the record browse view.

### Plot the beginning of the invasion - Kaunas

Next, let's add interactive annotations to the two endpoints of Minard's visualization - Kaunas in the west, and Moscow in the east.

1. Pan to the western edge of Minard's map until you find Kaunas, right at the base of the first and largest of the boxes that represent the size of the Grande Army. Click on **New Record** and enter "Kaunas" in the Title field.

1. Click on the **Map** tab to display the geometry editing controls. Activate the **Draw Point** option in the list of editing modes.

1. Click once on Kaunas to lay down a single point. Once the point is in place, reactivate the default **Navigate** mode so that you don’t accidentally drop another point the next time you click on the map.

1. Switch to the **Style** tab and scroll down to the **Dimensions** field set. Click on the **Point Radius** input and drag up to make the point a bit larger. As the value changes in the form, the point on the map will resize to preview the new value.

1. Once you're done, click **Save** and go back to the list of records by clicking the **X** at the top of the form.

### Plot the end of the invasion - Moscow

Let’s do the same thing for Moscow. This time, though, we’ll use the point as a trigger to display an image and some descriptive text.

1. Click on **New Record** again, enter "Moscow" into the **Title** field, and use the **Draw Point** tool to lay down a point on Moscow.

1. Once the point is in place, click back to the **Text** tab. Next to the label on the Body field, click the **Edit HTML** button to open up a fullscreen text editor.

1. To get some testing content, open up a new tab and go to the Wikipedia page for the French invasion of Russia (http://en.wikipedia.org/wiki/French_invasion_of_Russia) and scroll down to the "Fire of Moscow" section. Click on the painting on the left, and then click on the image in the pop-up window to open the raw image file. Then, right click on the image, click **Copy Image URL**, and then switch back to the tab with the Neatline editor.

1. Click on the **Image** button and paste the image location into the URL input.

1. Delete the value that gets automatically populated into the **Width** input (this can be useful if you want really precise control over the layout of the image, but for now we'll just let the browser do what it thinks is best).

1. Click **OK** to insert the image into the document.

1. Head back over to the Wikipedia page and copy the two paragraphs under the "Fire of Moscow" heading. Switch back into the editor and paste the content under the image, just like you would in a desktop text editor like Microsoft Word.

1. Click **Minimize** to close the editor. Notice that the HTML markup generated by the text editor has been copied into the "Body" field.

1. Click **Save** to lock in the changes and then close the form.

### Outline the Neman River

Next, let’s use the line-drawing tool to outline the Neman River on Minard’s map:

1. Pan to the east end of the map and find the Neman river, which runs through the point that we placed on Kaunas. Click **New Record** and enter "Neman River" in the Title field.

1. Click the **Map** tab and select **Draw** Line. Once the control is active, you can draw segmented lines on the map by clicking on the locations where you want the points to be. Like with the polygon tool - once all the points are in place, you can "close" the line by double-clicking at the location of the final point. In this case, start by clicking once where the river leaves the map to the north, and then move the cursor down and double click on the point where the river intersects with the top of Minard’s temperature graph. This will draw a straight line between the two points.

1. Now, we'll trace out the actual path of the river by successively bisecting the line and dragging the points into position on the river. Click on the **Modify Shape** radio button and then click on the line that you just created on the map. Three control points will appear – two at the ends of the line (the points that we've already added) and a third, more transparent point in the middle of the line.

1. Click the middle point and split the line into two segments by dragging the point towards the eastward bend in the river south of Kaunas.

1. Continue bisecting the segments and refining the path until you have a good outline of the river. If you make a mistake and want to get rid of a point, hover the cursor over the point and press the "D" button on the keyboard.

1. When you're finished, click the **Save** button at the bottom of the form.

1. Now we have the path in position, but it's really hard to see because the default line color (black) blends in to the color of Minard’s original line. To fix that, click over to the **Style** tab and scroll down to the **Colors** field set. Click on the **Stroke Color** input to open a color-picker widget and choose some sort of bluish hue that goes well with the surrounding color scheme on the map.
Let's also make the line a bit thicker so that it's more noticeable. Scroll down to the Stroke Width input and drag the value up to around 5 or 6.

1. As always, click **Save** to commit the changes and close the form with the **X** button.

### Annotate the flowchart

Last, we'll use Neatline's polygon-drawing tool to outline the flowchart boxes that Minard uses to visualize the gradual shrinking of the army over the course of the campaign.

1. Create a new record called "Invasion." Pan to the eastern end of the map and zoom in so that you can clearly see the outline of the flowchart.

1. Click the Map tab and activate the **Draw Polygon** mode.

1. Start by outlining the first segment in the flowchart, the initial force of 422,000 that crossed the Neman. Click one to lay down points on the first three corners of the shape, and then double-click on the fourth corner to freeze the polygon. Like with the line tool, you can use the **Modify Shape** tool to push around the vertices if you want to edit the shape.

1. Once you're happy with the outline, click over to the **Style** tab and scroll down to the **Colors** section. Fiddle around with the color until you find something that fits in well with the color palette of Minard's map

1. Then, drop down the **Fill Opacity** field to about 0.3, and change the Select Opacity to ~0.6. This makes it easy to see that there's an interactive annotation on top of Minard's image, but you can still see through to the image and base layer below.

1. At this point, if you're feeling ambitious, you could go through and create separate records and annotations for each of the segments. To keep things quick, though I'm just going to outline all of the remaining segments in the eastbound flowchart with a single shape.

1. Once you've outlined the invasion flowchart, create a new record called "Retreat" and repeat the same process for the segments leading from Moscow back towards Kaunas.

## Part 3: Change over time

Last, we'll experiment with the basic mechanics of the functionality in Neatline that makes it possible to visualize how elements on maps change over time. First, we'll need to install the SIMILE Timeline extension for Neatline, which adds a timeline to the exhibit that can be populated with content in the same way that we’ve been adding records to the map.

### Install and enable SIMILE Timeline

1. Go back to http://omeka.org/add-ons/plugins/ and find the listing for NeatlineSimile. Click **Download v2.0.4**.

1. Open the .zip file and copy (Command+C) the `NeatlineSimile` folder. Paste this into the `Applications/MAMP/htdocs/omeka/plugins` directory, alongside `Neatline`.

1. In the Omeka admin, click **Plugins** and install Neatline SIMILE.

1. Then, go back to the **Neatline** tab and find the listing for your exhibit. Click on the **Exhibit Settings** link to open the same form that we originally used to create the exhibit.

1. Scroll down to the **Widgets** field. Click on the input and select the **SIMILE Timeline** option.

1. Click **Save Exhibit**, which will take you back to the browse exhibits view. Click on the title of your exhibit to re-open the Neatline editor.

### Configure the Timeline

Next, let's customize the timeline's default focus and zoom level.

1. Click the **Plugins** drop down at the top of the editing panel and select the **SIMILE Timeline** option.

1. Enter "1812" into the **Default Date** field. This is the date that the timeline will automatically focus on when the exhibit starts.

1. Select the "Month" option in the **Interval Unit** drop down. This has the effect of configuring the zoom level or granularity of the timeline - the unit used to delimit the horizontal axis.

1. Drag the **Interval Pixels** down to around 80. This determines the width between the tick marks on the X-axis.

1. Finally, set the **Tape Height** to 20. This sets the vertical height of the "span" graphics used to represent durations events on the timeline.

### Plot the invasion on the timeline

Once the timeline is configured, we can start adding records to it just like we added the vector annotations to the map. First, we'll add some date information to the two records that we used to represent the segments in Minard's flow chart.

1. Open the "Invasion" record, click on the **Styles** tab, and scroll down to the **Dates** field set.

1. Enter "1812-06-24" into **Start Date** and "1812-09-14" into **End Date**.

1. Now go back to the top of the form and find the **Widgets** drop down. Add the record to the timeline by clicking the listing for **SIMILE Timeline**.

1. Click **Save** at the bottom of the form, and the record will appear as a span between June and September.

1. Do the same thing for the "Retreat" record - use "1812-10-18" as the **Start Date** and "1812-12-14" as the **End Date**, and save the record to update the timeline.

### Toggle the map annotations with visibility intervals

In addition to plotting the records on the timeline, we can also use the timeline as a mechanism to control which elements are visible on the map at any given moment. This makes it possible to string together complex time-series animations and progressions. To start, we'll add a second set of dates to the two records that control when the records should be displayed on the map:

1. Open up the "Invasion" record and go back to the **Dates** field set under the **Style** tab. For now, just copy the value from the **Start Date** field into the **After Date** field and save the record. Then, drag the timeline back before June 24, 1812 - the corresponding annotation on the map disappears, and then reappears when the timeline is dragged back to the right of the threshold date.

1. Likewise, copy the **End Date** value into the **Before Date** field. Now, when you drag the timeline past December 14, the map annotation disappears. When used together, the before and after dates make it possible to define a bounded window of time within which an object is visible on the map.
