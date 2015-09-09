def extract_band(hdf_image_id, working_directory, hdf_file, output_directory, band):
    '''
    Функция извлекает указанный канал из изображения, преобразует в проекцию и сохраняет в указанную директорию
    :param working_directory: Рабочая директория, в которой находится файл
    :param hdf_file: Имя изображения
    :param output_directory: Выходной путь
    :param band: Указанный канал для экспорта
    :return: Bool
    '''
    import os
    import ImagesBandsCtrl as ImagesBandsCtrl
    try:
        os.chdir(working_directory)
        os.system('''gdalwarp \
                        -t_srs "+proj=longlat +ellps=wgs84 +datum=wgs84" -multi \
                        -co COMPRESS=DEFLATE -co "TILED=YES" \
                        -overwrite \
                        -of GTiff 'HDF4_EOS:EOS_GRID:"{0}{1}":{4}' \
                        {2}{3}_"{4}".tif'''.format(working_directory, hdf_file, output_directory, hdf_file[:-4], band))

        filename = hdf_file[:-4]+'_'+band+'.tif'
        size = os.stat(output_directory + filename).st_size
        print('ImagesBands')
        ImagesBandsCtrl.create(filename, hdf_image_id, band, size, output_directory)
        return True

    except Exception as e:
        print(e)
        return False
