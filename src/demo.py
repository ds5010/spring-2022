# Folium demo with Qt using Stamen maps
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import io
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = folium.Map(
        location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13
    )

    print(type(m))

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(640, 480)
    w.show()

    sys.exit(app.exec_())
