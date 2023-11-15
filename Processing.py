from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import os
import numpy as np
import shutil

import scipy.misc

import imageio

from PIL import Image
from numpy import asarray
from datetime import date

class NdviProcess:
    TAG = "ndviprocess.class"
    imagePath_b5 = ""
    image_b5 = None

    imagePath_b4 = ""
    image_b4 = None

    ndvi_avg = None
    ndvi_avg_status = None

    
    def openImage_b5(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b5 = path
            self.image_b5 = openImage
            return True

    def openImage_b4(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b4 = path
            self.image_b4 = openImage
            return True

    def eksekusi(self):
        geotrans_B4=self.image_b4.GetGeoTransform()
        geotrans_B5=self.image_b5.GetGeoTransform()

        data_B4=self.image_b4.GetRasterBand(1).ReadAsArray().astype(np.float32)
        data_B5=self.image_b5.GetRasterBand(1).ReadAsArray().astype(np.float32)

        originX,pixelWidth,empty,finalY,empty2,pixelHeight=geotrans_B5

        cols =  self.image_b5.RasterXSize
        rows =  self.image_b5.RasterYSize

        projection = self.image_b5.GetProjection()

        print("cols :", cols)
        print("rows :", rows)
        print("originX :", originX)
        print("pixelWidth :", pixelWidth)
        print("pixelHeight :", pixelHeight)
        print("====================================================")
        finalX = originX + pixelWidth * cols
        print("finalX :", finalX)
        originY = finalY + pixelHeight * rows
        print("originY :", originY)

        ndvi = np.divide(data_B5 - data_B4, data_B5+ data_B4,where=(data_B5 - data_B4)!=0)

        ndvi[ndvi == 0] = -999

        print(ndvi)

        self.ndvi_avg = np.mean(ndvi)

        if self.ndvi_avg <= 0.92 and self.ndvi_avg >= 0.721:
            print('sangat baik')
            self.ndvi_avg_status = "Sangat Baik"
        elif self.ndvi_avg <= 0.72 and self.ndvi_avg >= 0.421:
            print('baik')
            self.ndvi_avg_status = "Baik"
        elif self.ndvi_avg <= 0.42 and self.ndvi_avg >= 0.221:
            print('normal')
            self.ndvi_avg_status = "Normal"
        elif self.ndvi_avg <= 0.22 and self.ndvi_avg >= 0.11:
            print('buruk')
            self.ndvi_avg_status = "Buruk"


        path_NDVI='ndvi_output.tif'
        self.saveRaster(ndvi,path_NDVI,cols,rows,projection,geotrans_B5)

        self.plotNDVI(path_NDVI,0,'YlGn',originX,finalX,originY,finalY)

        image = Image.open("result.png")

        return image


    def exportResult(self, path):
        # original = os.getcwd()
        # os.chdir = path
        # date_name = str(date.today())
        # original = original.replace("\\\\", "\\")
        # original = original + "\result.png"
        # target = path + "\hasilexportNDVI" + date_name + ".png"
        # target = "G:\Docs\WORD\Tugas Kuliah\Semester 5\Penginderaan Jauh\Vidya\resultfinal.png"
        # shutil.copyfile(original, target)
        self.plotNDVI
        return True


    def saveRaster(self,dataset,datasetPath,cols,rows,projection,geotrans_B5):
        rasterSet = gdal.GetDriverByName('GTiff').Create(datasetPath, cols, rows,1,gdal.GDT_Float32)
        rasterSet.SetProjection(projection)
        rasterSet.SetGeoTransform(geotrans_B5)
        rasterSet.GetRasterBand(1).WriteArray(dataset)
        rasterSet.GetRasterBand(1).SetNoDataValue(-999)
        rasterSet = None

    def plotNDVI(self,ndviImage,vmin,cmap,originX,finalX,originY,finalY):

        extentArray = [originX,finalX,originY,finalY]

        ndvi2 = gdal.Open(ndviImage)
        ndvi_array = ndvi2.ReadAsArray()
        fig=plt.figure(figsize=(10,10), dpi=200)
        im = plt.imshow(ndvi_array, vmin=vmin, cmap=cmap, extent=extentArray)
        
        # plt.colorbar(im, fraction=0.015)
        # im = ax.imshow(np.arange(100).reshape((10,10)))

        plt.xlabel('Selatan')
        plt.ylabel('Barat')
        # ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax = plt.gca()
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="3%", pad=0.1)
        plt.colorbar(im, cax=cax)
        # ax.set_axis_off()
        # fig.add_axes(ax)
        plt.savefig("result.png", bbox_inches='tight')
        # plt.show()
