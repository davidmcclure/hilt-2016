# CartoDB

Next we'll look at CartoDB, which, in many ways, is like a much more feature-rich and sophisticated version of Google Fusion tables.

## Create a new map

1. Go to https://cartodb.com. If you don't already have an account, click **Sign Up**. If you've got a Google account, just click **Login with Google** to log in with that; otherwise sign up for a new account on CartoDB.

1. In the top navbar, click **Maps** and then **New Map**.

1. In the "Add datasets" view, click the **Connect dataset** tab, and then **Browse** to open a file picker.

1. Select the same geocoded CSV that we uploaded to Fusion Tables and click the **Connect dataset** button at the bottom.

1. Once the data loads and the new map is created, click on **Untitled Map** at the top of the screen and enter the name of the text that the toponyms were extracted from.

## Configure the info boxes

1. Click on a point on the map. At first, you'll see a notice saying _You haven’t selected any fields to be shown in the infowindow._ Click on the **Select fields** link.

1. In the right panel, under the **Click** tab, flip on the toggle switches for `toponym` and `offset`.

1. In the **Hover** tab, flip on `toponym`. Now, when you hover the cursor over a point, the place name will automatically show, and when you click, the toponym and the start offset will be displayed in the bubble.

## Format the point data

Now, let's use some of CartoDB's built-in "wizards" to change the display format of the points.

1. In the vertical toolbar on the right, click the **wizards** tab.

1. By default, the "Simple" wizard is set, which just shows a single point for each piece of data. Click on the second option, **Cluster**, which clumps together nearby points, and scales the groups by the number of points.

1. Experiment with some of the options for the cluster wizard - tweak the **Buckets** and **Marker size** options.

1. Activate the **Heatmap** wizard, which is similar to the Google Fusion tables heatmap.

1. Last, activate the **Choropleth** wizard, which makes it possible to bucket the data points into groups along a particular axis and color the groups accordingly.

1. In **Column**, select `offset`.

1. In **Color Ramp**, pick a color scheme that makes it easy to see a progression, like the white-to-green palette. Now, since we have more control over the colors used to mark the groups, it's possible to get a better sense of the spatial _movement_ of the text than we were able to get in Fusion Tables.

## Create an animated time series

But, CartoDB can do even better than this with the "Torque" wizard.

1. Activate the **Torque** wizard.

1. Flip on the **Cumulative** option.

1. Under **Time Column**, select `offset`.

1. Now, CartoDB will animate the sequencing of the points, ordered by the value in the `offset` column. This will play on repeat by default, but it's also possible to click and drag on the timeline to speed it up or reverse it.

## Annotate and export the map.

Now that it's possible to see the spatial progression of the toponyms, let's add some simple annotations to the map.

1. Switch back to the **Cluster** wizard.

1. Click **Add Element** at the top left of the screen. Click **Add annotation item**, and then click on the new annotation that appears on the map to edit it.

1. Enter "Beginning" into the box, and then click and drag to move the annotation to the region of the map where the toponyms tend to cluster at the beginning of the text.

1. Repeat this for "Middle" and "End."

1. Once the markers are in place, zoom the map back so that everything is visible and click on **Export Image**.

1. Frame the image around the region that you care about and click **Export**.

1. Click on **View Image** to load the image in the browser.
