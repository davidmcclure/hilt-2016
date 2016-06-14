# Analyzing and Presenting Spatial data

Welcome! Over the course of the next four days we're going take a look at a range of tools and techniques for working with spatial data in the humanities. By the end of the week, it's my hope that everyone will be able to build effective spatial humanities projects using off-the-shelf tools, and also know how to get started with more complex or unusual projects that call for some custom data preparation or interface design.

The course is laid out along an axis that I think provides a useful way to think about the range of GIS practices in the humanities. On the one end of the spectrum are tools like Neatline, which, in many ways, are interested in applying traditional methods in the humanities to digital maps - there's a focus on building rich interpretations of specific objects (eg, historic maps), often making use of hand-crafted data that been designed to support a specific narrative or argument. At the other end of the spectrum is a set of practices that more closely resemble GIS as practiced in the (social) sciences - a focus on larger amounts of data, with an eye towards building simple data models that lend themselves to traditional modes of quantitative analysis.

For me, these two ways of thinking about spatial data are excellent complements to each other. Some projects naturally gravitate towards one or the other, but, I think just as often, both can be brought to bear on the same question in interesting ways. We'll run the gamut between the two.

## Course Outline

**Part 1: Neatline**

We'll start out by taking a look at Neatline, a digital mapping framework developed at the University of Virginia that makes it possible to create interactive, map-based exhibits of archival materials. As a test project, we'll create an digital edition of Charles Minard's famous infographic showing the deterioration of Napoleon's army during the 1812 invasion of Russia.

- Use QGIS to georeference a scanned image of Minard's original infographic.
- Import the georeferenced image into GeoServer, a "tiling" server that makes it possible to publish custom maps to the web.
- Install Omeka and Neatline, and pull the map from GeoServer into a Neatline exhibit.
- Use Neatline's drawing tools to create a set of annotations on top of Minard's map.
- Use Neatline's timeline feature to visualize change over time in Minard's image.

**Part 2: Neatline Text**

Next, we'll look at an extension to Neatline called Neatline Text, which makes it possible to connect text documents - primary texts, articles, book chapters, blog posts, etc. - with interactive maps.

- Find a primary text that makes reference to specific locations or has some kind of spatial "footprint."
- Turn the text into a simple HTML document that wraps the place references with tags that can be linked with objects in Neatline.
- Create a Neatline exhibit that plots out the locations.
- Link the text document with the Neatline exhibit.

**Part 3: Named entity extraction and geocoding**

Building on the process of manually identifying place names in a chunk of text, we'll then use the Stanford Named Entity Recognizer to automatically extract these place references - "toponyms" - from novels downloaded from Project Gutenberg.

- Install the Stanford NER software.
- Find a text of interest and extract the place references.
- Write a simple Python script to convert the output into a CSV file.
- Write another script to geocode the place names - convert them into lat/lon points that can be plotted on a map.

**Part 4: Spatial data visualization**

Working with the geocoded place names that we extracted from the novel(s), we'll then plug this data into some visualization tools that are designed to work well this kind of data.

- Get a rough sense of the data by plotting it in Google Fusion Tables.
- Upload the data into CartoDB and create more complex views of it - heatmaps, choropleths, clustered markers, and more.

**Part 5: Simple web map programming**

Last but not least, we'll take a look at the basics of developing custom mapping applications using open-source libraries.

- Create a basic web page with HTML, CSS, and Javascript.
- Install Leaflet, a library that makes it easy to create custom maps.
- Load the place name data extracted from the novels and plot the points on the map.
- Create a custom time-slider that shows the spatial movement of the novel across the "novel time" of the text.
