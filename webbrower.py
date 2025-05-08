from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser,self).__init__()
        self.browser = QWebEngineView()
        
        self.base_url = "http://localhost:8085"
        
        self.browser.setUrl(QUrl(self.base_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setFixedHeight(50)
        backButton = QAction("Back",self)
        backButton.triggered.connect(self.browser.back)
        navbar.addAction(backButton)
        fwdButton = QAction("Forward",self)
        fwdButton.triggered.connect(self.browser.forward)
        navbar.addAction(fwdButton)
        self.link_Input = QLineEdit()
        self.link_Input.setPlaceholderText("Enter URL")
        self.link_Input.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.link_Input)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.link_Input.text()

        if url == "index":
             url = f"{self.base_url}"
             self.browser.setUrl(QUrl(url))
        elif url == "register":
            url = f"{self.base_url}/register"
            self.browser.setUrl(QUrl(url))
            
        elif url.startswith("http://") or url.startswith("https://"):
            url = url
            self.browser.setUrl(QUrl(url))    
        else:
            self.last_query = url
            notFound =f"""
            <html>
            <head><title>Page Not Found</title></head>
            <body><h1>Page Not Found</h1>
            <p>No local page found: <b>{self.last_query}</b></p>
            <p>Search online instead:</p>
            <a href='https://www.google.com/search?q={self.last_query}'>Search on Google</a>
            </body>
            </html>
            """
            self.browser.setHtml(notFound)
        
    def update_url(self, url):
        self.link_Input.setText(url.toString())    
 
 
def main():        
        app = QApplication(sys.argv) 
        QApplication.setApplicationName("Web Browser")
        window = WebBrowser() 
        app.exec_()
        
if __name__ == "__main__":
    main()        
            