import geopandas as gpd
import pandas as pd

# Load ZCTA shapefile ***Change file accordingly
zcta_fp = "Your depositary\\tl_2018_us_zcta510.shp"
zcta = gpd.read_file(zcta_fp)

# Load 116th congressional districts shapefile ***Change file accordingly
cd_fp = "Your depositary\\tl_2018_us_cd116.shp"
cd = gpd.read_file(cd_fp)

# Ensure same CRS
zcta = zcta.to_crs(cd.crs)

# Spatial join: which ZCTAs intersect which congressional districts
zcta_cd = gpd.sjoin(zcta, cd, how="left", predicate="intersects")

# Select relevant columns ***Change ZCTA and CD accordingly
df = zcta_cd[['ZCTA5CE10', 'STATEFP', 'CD116FP']].copy()
df.rename(columns={
    'ZCTA5CE10': 'ZIP Code',
    'STATEFP': 'State FIPS',
    'CD116FP': 'District'
}, inplace=True)

# Optional: map FIPS to state abbreviation
state_map = {
    '01': 'AL','02': 'AK','04': 'AZ','05': 'AR','06': 'CA','08': 'CO','09': 'CT','10': 'DE','11': 'DC',
    '12': 'FL','13': 'GA','15': 'HI','16': 'ID','17': 'IL','18': 'IN','19': 'IA','20': 'KS','21': 'KY',
    '22': 'LA','23': 'ME','24': 'MD','25': 'MA','26': 'MI','27': 'MN','28': 'MS','29': 'MO','30': 'MT',
    '31': 'NE','32': 'NV','33': 'NH','34': 'NJ','35': 'NM','36': 'NY','37': 'NC','38': 'ND','39': 'OH',
    '40': 'OK','41': 'OR','42': 'PA','44': 'RI','45': 'SC','46': 'SD','47': 'TN','48': 'TX','49': 'UT',
    '50': 'VT','51': 'VA','53': 'WA','54': 'WV','55': 'WI','56': 'WY'
}

df['State'] = df['State FIPS'].map(state_map)

# Drop FIPS column
df = df[['ZIP Code', 'State', 'District']]

# Save to Excel  ***Change accordingly
df.to_excel("us_zip_districts_2018_116th.xlsx", index=False)
print("Excel file generated: us_zip_districts_116th.xlsx")
