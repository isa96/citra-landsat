# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Processing import NdviProcess

import numpy

from PIL import Image

###########################################################################
## Class MyFrameRoot
###########################################################################

class MyFrameRoot ( wx.Frame ):

	export_dir = None

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Main Frame UI Penginderaan Jauh", pos = wx.DefaultPosition, size = wx.Size( 752,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizerFrameRoot = wx.BoxSizer( wx.VERTICAL )

		bSizerRootFrame = wx.BoxSizer( wx.VERTICAL )

		StaticBoxPersiapanCitra = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Persiapan Citra" ), wx.HORIZONTAL )

		StaticBoxBand4 = wx.StaticBoxSizer( wx.StaticBox( StaticBoxPersiapanCitra.GetStaticBox(), wx.ID_ANY, u"Citra Band 4 (Red Reflectance)" ), wx.VERTICAL )

		BoxCitra4 = wx.BoxSizer( wx.VERTICAL )

		self.InputBand4 = wx.FilePickerCtrl( StaticBoxBand4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		BoxCitra4.Add( self.InputBand4, 0, wx.EXPAND, 5 )

		self.CitraBand4 = wx.StaticBitmap( StaticBoxBand4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
		self.CitraBand4.SetBackgroundColour( wx.Colour( 225, 255, 225 ) )

		BoxCitra4.Add( self.CitraBand4, 1, wx.EXPAND, 5 )


		StaticBoxBand4.Add( BoxCitra4, 1, wx.EXPAND, 5 )


		StaticBoxPersiapanCitra.Add( StaticBoxBand4, 1, wx.EXPAND, 5 )

		StaticBoxBand5 = wx.StaticBoxSizer( wx.StaticBox( StaticBoxPersiapanCitra.GetStaticBox(), wx.ID_ANY, u"Citra Band 5  (Near Infrared Reflectance)" ), wx.VERTICAL )

		BoxCitra5 = wx.BoxSizer( wx.VERTICAL )

		self.InputBand5 = wx.FilePickerCtrl( StaticBoxBand5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		BoxCitra5.Add( self.InputBand5, 0, wx.EXPAND, 5 )

		self.CitraBand5 = wx.StaticBitmap( StaticBoxBand5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
		self.CitraBand5.SetBackgroundColour( wx.Colour( 225, 255, 225 ) )

		BoxCitra5.Add( self.CitraBand5, 1, wx.EXPAND, 5 )


		StaticBoxBand5.Add( BoxCitra5, 1, wx.EXPAND, 0 )


		StaticBoxPersiapanCitra.Add( StaticBoxBand5, 1, wx.EXPAND, 5 )


		bSizerRootFrame.Add( StaticBoxPersiapanCitra, 1, wx.EXPAND, 5 )

		StaticBoxPemrosesanCitra = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pemrosesan Citra" ), wx.HORIZONTAL )

		StaticBoxRumus = wx.StaticBoxSizer( wx.StaticBox( StaticBoxPemrosesanCitra.GetStaticBox(), wx.ID_ANY, u"Rumus NDVI" ), wx.VERTICAL )

		self.TextLabelRumusNDVI = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Normalized Difference Vegetation Index (Rouse et al. 1974)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelRumusNDVI.Wrap( -1 )

		self.TextLabelRumusNDVI.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.TextLabelRumusNDVI.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		StaticBoxRumus.Add( self.TextLabelRumusNDVI, 0, wx.EXPAND, 5 )

		self.TextRumusNDVI = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"NDVI = (NIR - R) / (NIR + R)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextRumusNDVI.Wrap( -1 )

		self.TextRumusNDVI.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		StaticBoxRumus.Add( self.TextRumusNDVI, 0, 0, 5 )


		StaticBoxRumus.Add( ( 0, 17), 0, 0, 5 )

		self.TextLabelKeteranganRumus = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Keterangan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelKeteranganRumus.Wrap( -1 )

		self.TextLabelKeteranganRumus.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.TextLabelKeteranganRumus.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		StaticBoxRumus.Add( self.TextLabelKeteranganRumus, 0, 0, 5 )

		self.TextKeteranganRumus = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"NIR  : Nilai spektral saluran Near Infrared\nR      : Nilai spektral saluran Red.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextKeteranganRumus.Wrap( -1 )

		self.TextKeteranganRumus.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		StaticBoxRumus.Add( self.TextKeteranganRumus, 0, 0, 5 )


		StaticBoxRumus.Add( ( 0, 15), 0, 0, 5 )

		self.BtnStartProcess = wx.Button( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Start Process", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.BORDER_THEME )
		self.BtnStartProcess.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.BtnStartProcess.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.BtnStartProcess.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.BtnStartProcess.SetMinSize( wx.Size( 100,30 ) )

		StaticBoxRumus.Add( self.BtnStartProcess, 0, wx.ALIGN_RIGHT, 5 )


		StaticBoxRumus.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		self.Pembatas = wx.StaticLine( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		StaticBoxRumus.Add( self.Pembatas, 0, wx.EXPAND, 5 )

		BoxNilaiNDVI = wx.BoxSizer( wx.VERTICAL )

		self.TextLabelNilaiNDVI = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Nilai NDVI :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelNilaiNDVI.Wrap( -1 )

		self.TextLabelNilaiNDVI.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.TextLabelNilaiNDVI.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		BoxNilaiNDVI.Add( self.TextLabelNilaiNDVI, 0, 0, 5 )

		self.TextNilaiNDVI = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"0.000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextNilaiNDVI.Wrap( -1 )

		self.TextNilaiNDVI.SetForegroundColour( wx.Colour( 6, 13, 96 ) )

		BoxNilaiNDVI.Add( self.TextNilaiNDVI, 0, 0, 5 )


		BoxNilaiNDVI.Add( ( 0, 20), 1, 0, 5 )

		self.TextLabelHasilKlasifikasi = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Hasil KlasifikasiI :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelHasilKlasifikasi.Wrap( -1 )

		self.TextLabelHasilKlasifikasi.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.TextLabelHasilKlasifikasi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		BoxNilaiNDVI.Add( self.TextLabelHasilKlasifikasi, 0, 0, 5 )

		self.TextHasilKlasifikasi = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextHasilKlasifikasi.Wrap( -1 )

		self.TextHasilKlasifikasi.SetForegroundColour( wx.Colour( 6, 19, 36 ) )

		BoxNilaiNDVI.Add( self.TextHasilKlasifikasi, 0, 0, 5 )


		BoxNilaiNDVI.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		self.Pembatas1 = wx.StaticLine( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		BoxNilaiNDVI.Add( self.Pembatas1, 0, wx.EXPAND |wx.ALL, 5 )


		StaticBoxRumus.Add( BoxNilaiNDVI, 0, wx.EXPAND, 5 )

		BoxKlasifikasiKesehatan = wx.BoxSizer( wx.VERTICAL )

		self.TextLabelKlasifikasiKesehatan = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"Klasifikasi Kesehatan Tanaman Padi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelKlasifikasiKesehatan.Wrap( -1 )

		self.TextLabelKlasifikasiKesehatan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.TextLabelKlasifikasiKesehatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		BoxKlasifikasiKesehatan.Add( self.TextLabelKlasifikasiKesehatan, 0, 0, 5 )

		self.TextKlasifikasiKesehatan = wx.StaticText( StaticBoxRumus.GetStaticBox(), wx.ID_ANY, u"0.721 – 0.92  : Sangat Baik \n0.421 – 0.72  : Baik\n0.221 – 0.42  : Normal \n0.11 – 0.22    : Buruk ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextKlasifikasiKesehatan.Wrap( -1 )

		self.TextKlasifikasiKesehatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		BoxKlasifikasiKesehatan.Add( self.TextKlasifikasiKesehatan, 0, 0, 5 )


		StaticBoxRumus.Add( BoxKlasifikasiKesehatan, 1, wx.EXPAND, 5 )


		StaticBoxPemrosesanCitra.Add( StaticBoxRumus, 1, wx.EXPAND, 5 )

		StaticBoxHasilCitra = wx.StaticBoxSizer( wx.StaticBox( StaticBoxPemrosesanCitra.GetStaticBox(), wx.ID_ANY, u"Hasil Citra" ), wx.VERTICAL )

		self.HasilCitraNDVI = wx.StaticBitmap( StaticBoxHasilCitra.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
		self.HasilCitraNDVI.SetBackgroundColour( wx.Colour( 221, 255, 255 ) )

		StaticBoxHasilCitra.Add( self.HasilCitraNDVI, 1, wx.EXPAND, 5 )

		self.TextLabelPenyimpananCitra = wx.StaticText( StaticBoxHasilCitra.GetStaticBox(), wx.ID_ANY, u"Pilh Folder Tempat Menyimpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextLabelPenyimpananCitra.Wrap( -1 )

		self.TextLabelPenyimpananCitra.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		StaticBoxHasilCitra.Add( self.TextLabelPenyimpananCitra, 0, wx.ALL, 5 )

		self.ExportCitra = wx.DirPickerCtrl( StaticBoxHasilCitra.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE )
		StaticBoxHasilCitra.Add( self.ExportCitra, 0, wx.EXPAND, 5 )


		StaticBoxHasilCitra.Add( ( 0, 8), 0, 0, 5 )

		self.BtnExport = wx.Button( StaticBoxHasilCitra.GetStaticBox(), wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.BtnExport.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.BtnExport.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.BtnExport.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )
		self.BtnExport.SetMinSize( wx.Size( 100,30 ) )

		StaticBoxHasilCitra.Add( self.BtnExport, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		StaticBoxPemrosesanCitra.Add( StaticBoxHasilCitra, 1, wx.EXPAND, 5 )


		bSizerRootFrame.Add( StaticBoxPemrosesanCitra, 1, wx.ALL|wx.EXPAND, 0 )


		bSizerFrameRoot.Add( bSizerRootFrame, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerFrameRoot )
		self.Layout()
		self.m_statusBar3 = self.CreateStatusBar( 1, 0, wx.ID_ANY )

		self.Centre( wx.BOTH )

		self.InputBand4.Bind( wx.EVT_FILEPICKER_CHANGED, self.InputBand4OnFileChanged )
		self.InputBand5.Bind( wx.EVT_FILEPICKER_CHANGED, self.InputBand5OnFileChanged )
		self.ExportCitra.Bind( wx.EVT_DIRPICKER_CHANGED, self.ExportCitraOnFileChanged )

		self.BtnStartProcess.Bind( wx.EVT_BUTTON, self.BtnStartProcessOnButtonClick )
		self.BtnExport.Bind( wx.EVT_BUTTON, self.BtnExportOnButtonClick )

	def __del__( self ):
		pass

	ndviprocess = NdviProcess()

	def ExportCitraOnFileChanged(self, event ):
		self.export_dir = event.GetPath()
		print(event.GetPath())
	
	def BtnExportOnButtonClick(self, event ):
		print(self.export_dir)
		self.ndviprocess.exportResult(self.export_dir)
		self.BtnExport.SetLabelText("Export Berhasil")
		event.skip()

	def InputBand4OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.ndviprocess.openImage_b4(path)
		if isImage:
			# loadImage = Image.open(path)
			# rgb_img = loadImage.convert('RGB')
			# rgb_img.save("previewband4.png", "JPEG", quality=100)
			# img_preview_jpg = Image.open('previewband4.png')
			# arrayimg = numpy.array(img_preview_jpg)
			# img = self.convertToImage(arrayimg, 200, 200, False)
			# bitmapImage = wx.Bitmap(img)
			# self.CitraBand4.SetBitmap(bitmapImage)
			# bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
			bitmap = wx.Bitmap(event.GetPath())
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(350, 350, wx.IMAGE_QUALITY_HIGH)
			result = wx.BitmapFromImage(image)
			self.CitraBand4.SetBitmap(result)
		event.Skip()

	def InputBand5OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.ndviprocess.openImage_b5(path)
		if isImage:
			# loadImage = Image.open(path)
			# arrayimg = numpy.array(loadImage)
			# img = self.convertToImage(arrayimg, 350, 350, False)
			# bitmapImage = wx.Bitmap(img)
			# self.CitraBand5.SetBitmap(bitmapImage)
			# bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
			bitmap = wx.Bitmap(event.GetPath())
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(350, 350, wx.IMAGE_QUALITY_HIGH)
			result = wx.BitmapFromImage(image)
			self.CitraBand5.SetBitmap(result)
		event.Skip()


	def convertToImage(self, array, w_in, h_in, isFloat):
		newW = w_in
		newH = h_in
		# print(self.segmen.TAG, "Declaring RGB")

		if isFloat:
			rgb = array * 32
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(rgb).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
			
		else:
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(array).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
		
		# print(self.segmen.TAG, "Resize Image")
		H = image.GetHeight()
		W = image.GetWidth()
		if (W > H):
			newH = newH * H / W
		else:
			newW = newW * W / H
		image = image.Scale(newW, newH)
		return image

	def BtnStartProcessOnButtonClick(self, event):
		gambar = self.ndviprocess.eksekusi()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 400, 400, False)
		bitmapImage = wx.Bitmap(img)
		self.HasilCitraNDVI.SetBitmap(bitmapImage)

		nilaiNDVI = self.ndviprocess.ndvi_avg
		statusNDVI = self.ndviprocess.ndvi_avg_status

		self.TextNilaiNDVI.SetLabelText(str(nilaiNDVI))
		self.TextHasilKlasifikasi.SetLabelText(str(statusNDVI))

		event.Skip()

class MainApp(wx.App):
    def OnInit(self):
        myframe = MyFrameRoot(None)
        myframe.Show(True)
        return True


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()

