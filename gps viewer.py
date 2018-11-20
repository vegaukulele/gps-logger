# -*- coding:utf-8 -*-
# このスクリプトは、[This iPhone]の直下に置くこと
import ui,os
from urllib.parse import urljoin

file_path = 'gps_map.html'
file_path = urljoin('file://', os.path.abspath(file_path))
w = ui.WebView()
w.load_url(file_path)
w.present()

