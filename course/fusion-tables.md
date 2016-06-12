# Google Fusion Tables

Now that we've got a CSV with geocoded toponyms extracted from the text, let's take a look at some off-the-shelf tools that can be used to visualize this type of data. First up is the Fusion Tables product that's build into Google Docs, which is a dead-simple way of getting a rough sense of the spatial layout of a data set.

## Create a fusion table

1. Go to https://drive.google.com and click on **New > More**.

1. If you don't already have "Google Fusion Tables" in the list, click on **Connect more apps** and search for "fusion." Find the "Fusion Tables (experimental)" row, and click the **Connect** button.

1. Go back to **New > More** and click on **Google Fusion Tables**.

  ![](images/python/create-table.jpg)

1. Click **Choose File** and select one of the geocoded CSV files that we created in the last session. Leave the rest of the fields as-is, and click **Next**.

1. On the next screen, you'll see a preview of the rows in the table. Check that everything looks correct, and click **Next**.

1. In the next screen, enter the title of the novel into **Table name**, and click **Next**.

1. Now, in the newly-created table, click over into **Map of latitude**. Fusion tables will automatically recognize the `latitude` and `longitude` column headers in the CSV file and plot the locations on the map.

  ![](images/python/basic-points.jpg)

## Change the marker styles

Fusion tables makes it possible to make some simple edits to the appearance of the markers.

1. In the left column, click on **Change feature styles**.

1. In the "Marker Icon" section, click the dropdown for **Use one icon**, change the selection, and click **Save**. This will change the appearance of all the points in bulk.

  ![](images/python/change-marker-style.jpg)

1. What if we wanted to get a rough sense of the progression of the toponyms over the course of the text, the movement from start to finish? We can start to get an approximation of this by grouping the points into buckets according to the `offset` attribute - which captures their offset position in the text. Go back to **Change feature styles** and then click into the **Buckets** tab.

1. Click on the **Divide into...** option, and select **4** buckets.

1. In **Column**, select `offset`, and then click the **use this range** link.

  ![](images/python/buckets.jpg)

1. Click **Save** to apply the change. Now, the points will be grouped into five buckets, each representing a fifth of the text. This is a step forward, but not great, since there colors don't do much to show the ordering of the buckets.

## Create a heatmap

Fusion tables also makes it possible to create simple heatmaps.

1. In the left column, click on **Heatmap**.

1. Drag around the **Radius** know, which changes the size of the heatmap "clumps" on the map.

1. And, drag the **Opacity** knob, which just changes the extent to which it's possible to see through to the base map.

  ![](images/python/heatmap.jpg)
