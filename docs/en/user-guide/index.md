# Maps and Data Visualization {#map-viewer-as-user}

The map viewer and data visualization tool can be used in the following ways:

- Interactively explore a resource from the catalog.

- As a cartographic application for creating maps that can also be registered in the catalog.

!!! Note

Instead of the built-in map viewer, GeoNetwork can use an external map viewer (for example, an existing WebGIS structure in the organization). The administrator can configure GeoNetwork to connect to an external web map application. In this case, all actions with the map are transferred to the external application. See the [Map Application] section (../../administrator-guide/configuring-the-catalog/user-interface-configuration.md#user-interface-config-mappage).

## Map Viewer

You can open the map viewer directly from a metadata record or directly from the `Map` tab in the main menu. The right toolbar displays a list of tools. Hovering over the tools displays a tooltip explaining their meaning. The available tools are configured by the administrator, see the [Map Application] section (../../administrator-guide/configuring-the-catalog/user-interface-configuration.md#user-interface-config-mappage).

Tools for working with the map that the user can find in the map viewer interface: ***some tools may be missing***:

| **Tool** | **Description** |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Annotations | Allows the user to add their own objects to the map: markers, lines, polygons, text, and circles to highlight information. |
| Map Views | Allows you to create and save multiple map "scenes" (with a specific scale, layers, camera angle in 3D) and move between them sequentially, as in a presentation. |
| Widgets | Allows you to create dynamic charts, tables, counters, and text boxes based on layer data for visualization and analysis of information. |
| Coordinate System Selection | Allows you to change the coordinate system (projection) of the map. |
| Background Map Selection | Allows you to switch between different base maps (e.g. OpenStreetMap, satellite imagery) and add new ones from remote services. |
| Geolocation | Finds and centers the map on the user's current location. |
| File Import | Allows you to add data to the map by importing local files such as vector data (Shapefile, KML, GeoJSON) or map context files. |
| Identification | Retrieves and displays attribute information about objects on the map at the point of mouse click. |
| Geoprocessing Tool | Performs server-side geoprocessing operations, such as creating buffer zones and finding intersections between features. |
| Measurements | Allows you to measure distances, areas, azimuths, angles, and slopes on both 2D and 3D maps. |
| Zoom and Navigation | A set of tools for controlling the map view: zoom in/out, go full screen, navigate through extent history, and return to maximum coverage. |
| Service Catalog | Provides access to remote geospatial services (WMS, WFS, CSW, etc.) to search for and add new layers to the map. |
| Layer Settings | A set of functions for managing the properties of individual layers, including general information, display options, styling, and configuring the response of the Identify tool. |
| Resource Sharing | Provides options for sharing a map, information panel, or geostory via a direct link, social media, permalink, or by generating an embed code. |
| Table of Contents (TOC) | Allows you to control the visibility and order of layers, add/remove