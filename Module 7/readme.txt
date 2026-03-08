Name: Zakiya Williams

Module Info: Module 7 Assignment: WMATA Accessibility Due on 03/02/2026

Approach: 
For Part 1, the approach I took was to use the output of one API call to feed into the next. First, the WMATA Incidents API was called to get a list of current outages, extracting just the unique station codes into a set to avoid duplicates. Those station codes were then used to call the WMATA Station Info API to look up the geographic coordinates for each affected station. Finally, those coordinates were converted into GeoJSON format and passed to the MapBox Static Images API to produce a visual map of all the affected locations.

For Part 2, the approach was more straightforward I added requirements directly into the OpenAPI 3.0.3 YAML syntax, making sure all the required fields matched exactly, including the title, version, endpoint path, parameter names, response codes, and schema properties.

Known Bugs: n/a 
Citations: n/a
