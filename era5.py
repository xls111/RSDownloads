import cdsapi

dataset = "reanalysis-era5-land"
request = {
    "variable": ["2m_temperature"],
    "year": "2025",
    "month": "02",
    "day": ["11"],
    "time": ["13:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
}

client = cdsapi.Client()
client.retrieve(dataset, request).download("./data/20250211_1300.nc")
