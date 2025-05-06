from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
def main():        
        app = QApplication(sys.argv) 
        QApplication.setApplicationName("Web Browser")
        window = WebBrowser() 
        app.exec_()
        
if __name__ == "__main__":
    main()        
            