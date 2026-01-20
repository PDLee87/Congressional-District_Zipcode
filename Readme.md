# ZIP Code–Congressional District Mapping (117th Congress)

## Overview

This script constructs a ZIP code to congressional district mapping using official U.S. Census Bureau TIGER/Line shapefiles. Specifically, it links ZIP Code Tabulation Areas (ZCTAs) to U.S. congressional districts through a spatial intersection. The output is an Excel file that records all congressional districts intersecting each ZIP code.

---

## Data Sources (https://www2.census.gov/geo/tiger)

### 1. ZIP Code Tabulation Areas (ZCTAs) from U.S. Census Bureau TIGER/Line at 

* **Example File**: `tl_2018_us_zcta510.shp`

### 2. Congressional District Boundaries

* **Example File**: `tl_2018_us_cd116.shp`

---

## Methodology

1. **Load Shapefiles**
   The script loads ZCTA and congressional district shapefiles using `geopandas`.

2. **Coordinate Reference System (CRS) Alignment**
   Both shapefiles are projected into the same CRS to ensure accurate spatial operations.

3. **Spatial Join**
   A spatial join (`predicate="intersects"`) is performed to identify all congressional districts that intersect each ZCTA.

4. **Multiple Districts per ZIP Code**
   Because ZIP codes are not designed to nest within congressional districts, a single ZIP code may intersect multiple districts. The script **retains all valid ZIP–district overlaps** rather than imposing a one-to-one assignment.

5. **State Identification**
   State FIPS codes are mapped to standard two-letter state abbreviations.

6. **Output Generation**
   The resulting ZIP–district mapping is exported to an Excel file.

---

## Output File

**Filename**

```
us_zip_districts_2018_116th.xlsx
```

**Columns**

* `ZIP Code` – 5-digit ZIP Code Tabulation Area
* `State` – State abbreviation
* `District` – Congressional district number (as defined for the 116th/117th Congress)

Each row represents a **ZIP code–district intersection**.

---

## Software Requirements

* Python 3.9+
* Required packages:

  * `geopandas`
  * `pandas`
  * `shapely`
  * `fiona`
  * `openpyxl`

Install dependencies via:

```bash
pip install geopandas pandas openpyxl
```


The approach avoids measurement error by preserving all valid ZIP–district overlaps and aligning geographic definitions with the correct congressional term.
