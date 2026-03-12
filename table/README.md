# CSV Data Table Viewer

An interactive web-based table viewer for CSV data with advanced filtering, sorting, and visualization features.

## Features

### Data Display
- **Dynamic CSV Loading**: Automatically loads and parses `data.csv` using D3's dsv library
- **Responsive Table**: Built with [Tabulator](http://tabulator.info/) for a modern, feature-rich table experience
- **Virtual DOM**: Efficiently handles large datasets with virtual DOM rendering

### Filtering & Search
- **Global Search**: Search across all columns simultaneously
- **Column Filters**: Individual header filters for each column with real-time search
- **Clear Filters**: One-click button to reset all filters and sorting

### Sorting & Grouping
- **Multi-Column Sorting**: Click column headers to sort data (alphanumeric sorting)
- **Group By Column**: Dynamically group rows by any column with collapsible groups
- **Group Statistics**: View row counts for each group

### Image Handling
- **Image Preview**: Columns containing image filenames automatically display thumbnail previews
- **Modal View**: Click any image to view it in a full-size modal overlay
- **Auto-Configuration**: Images are loaded from the `images/` folder

### Data Export
- **Download CSV**: Export the current table data (including filtered results) as a CSV file

### Statistics
- **Row Count**: Real-time display of total rows
- **Group Count**: Shows number of groups when grouping is active

## File Structure

```
table/
├── index.html          # Main HTML structure
├── script.js           # Application logic and Tabulator configuration
├── styles.css          # Custom styling
├── data.csv            # CSV data file to be visualized
├── images/             # Folder containing images referenced in the CSV
└── README.md           # This file
```

## Configuration

### Changing the Data Source

Edit the configuration at the top of `script.js`:

```javascript
const CSV_FILE = 'data.csv';              // Your CSV file name
const IMAGE_COLUMNS = ['image_name'];     // Columns containing image filenames
const IMAGE_FOLDER = 'images';            // Folder where images are stored
```

### CSV Format Requirements

- The first row must contain column headers
- Each subsequent row represents a data entry
- No special formatting needed - standard CSV format is supported

## Usage

1. **Open the viewer**: Open `index.html` in a web browser
2. **Wait for data to load**: The loading indicator will disappear when ready
3. **Search globally**: Type in the "Global Search" field to filter all columns
4. **Filter columns**: Use the filter inputs in each column header
5. **Sort**: Click any column header to sort by that column
6. **Group**: Select a column from the "Group By Column" dropdown
7. **View images**: Click any image thumbnail to see it full-size
8. **Export**: Click "Download CSV" to export the current table data

## Dependencies

All dependencies are loaded via CDN:

- [D3-DSV](https://github.com/d3/d3-dsv) (v3.0.1) - CSV parsing
- [Tabulator](http://tabulator.info/) (v6.2.5) - Interactive table functionality

## Browser Compatibility

Works in all modern browsers that support:
- ES6+ JavaScript features (async/await, arrow functions, etc.)
- CSS Grid and Flexbox
- Fetch API

## Customization

### Styling
Modify `styles.css` to customize colors, spacing, and layout.

### Column Configuration
Additional column options can be configured in the `setupTable()` function in `script.js`. See [Tabulator documentation](http://tabulator.info/docs/6.2/columns) for all available column options.

## Error Handling

The viewer includes error handling for:
- Missing or inaccessible CSV files
- Empty CSV files
- Failed image loads (images that fail to load are automatically hidden)

Errors are displayed in a prominent error container at the top of the page.
