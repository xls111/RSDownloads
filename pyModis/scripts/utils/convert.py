import enum
from osgeo import gdal
import os
import glob

from scipy.fft import dst

def convert_hdf_to_tif(hdf_file, tif_file, band_id = 0, dst_srs = 'EPSG:4326'):
    datasets = gdal.Open(hdf_file)
    
    # Metadata = datasets.GetMetadata()
    #  打印元数据
    # for key,value in Metadata.items():
    #     print('{key}:{value}'.format(key = key, value = value))
    #  获取要转换的子数据集
    # 0:LST_Day_1km 4:LST_Night_1km
    # for i, ds in enumerate(datasets.GetSubDatasets()):
    #     data = ds[0]
    #     print(i, data.split(':')[-1])
    
    data = datasets.GetSubDatasets()[band_id][0]
    Raster_DATA = gdal.Open(data)
    DATA_Array = Raster_DATA.ReadAsArray()
    geoData = gdal.Warp(tif_file, Raster_DATA,
                        dstSRS = dst_srs, format = 'GTiff',
                        resampleAlg = gdal.GRA_Bilinear)
    del geoData

if __name__ == '__main__':

    data_dir = r"H:\Temp\Downloads\Modis\h28v06"
    os.chdir(data_dir)
    file_list = glob.glob("*.hdf")
    for i in file_list:
        TifName = os.path.join(data_dir, os.path.splitext(os.path.basename(i))[0] + ".tif")
        convert_hdf_to_tif(i, TifName, band_id = 0, dst_srs = 'EPSG:4326')
    
        
 
    
