import sys
import os
import subprocess
from PySide2.QtWidgets import (QApplication, QMainWindow)
from gui.main import Ui_MainAppWindow
from utils import converter_utils


class MainAppWindow(QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainAppWindow.__init__(self)
        self.setupUi(self)
        self.movFolderButton.setDisabled(True)
        self.conversionButton.setDisabled(True)
        self.mov_folder_path = ""
        self.exr_folder_path = ""
        self.exrFolderButton.clicked.connect(self.open_exr_folder)
        self.movFolderButton.clicked.connect(self.open_mov_folder)
        self.conversionButton.clicked.connect(self.convert_exr_to_mov)

    def convert_exr_to_mov(self):

        converted_video_name = "mov_converted"
        converted_video_extension = ".mov"
        abs_mov_file_path = os.path.join(self.mov_folder_path, converted_video_name + converted_video_extension).replace("\\","/")
        # Get the first file name of the exr sequences
        single_exr_file_path = sorted(os.listdir(self.exr_folder_path))[0]
        abs_single_exr_file_path = os.path.join(self.exr_folder_path, single_exr_file_path).replace("\\","/")
        start_frame_number, abs_path_with_padding = converter_utils.get_frame_number_and_path(abs_single_exr_file_path)
        print(start_frame_number,abs_path_with_padding,abs_mov_file_path)
        fmpg_cmd=['ffmpeg', '-hide_banner', '-loglevel', 'quiet', '-y', '-start_number',start_frame_number, '-i',abs_path_with_padding, '-vcodec', 'mpeg4', abs_mov_file_path]
        return_code =subprocess.call(fmpg_cmd)

        
    def open_mov_folder(self):
        
        self.mov_folder_path = converter_utils.file_open_dialog()

        self.conversionButton.setEnabled(True)
        self.lineEdit_2.setText(self.mov_folder_path)
    def open_exr_folder(self):

        self.exr_folder_path = converter_utils.file_open_dialog()

        self.movFolderButton.setEnabled(True)
        self.lineEdit.setText(str(self.exr_folder_path))
        
if __name__ == '__main__':
    app = QApplication()
    mainAppWindow = MainAppWindow()
    mainAppWindow.show()
    sys.exit(app.exec_())
