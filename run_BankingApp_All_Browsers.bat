call "D:\software Testing\Cred Automation testing 2025\07_BankingApp_Framework\.venv\Scripts\activate.bat"
python -m pytest -s -n=auto --browser "firefox" --html=".\HtmlReports\BankingApp_html_report_firefox_27_Feb_2026.html" --alluredir=AllureReports 
python -m pytest -s -n=auto --browser "chrome" --html=".\HtmlReports\BankingApp_html_report_chrome_27_Feb_2026.html" --alluredir=AllureReports
python -m pytest -s --browser "edge" --html=".\HtmlReports\BankingApp_html_report_edge_27_Feb_2026.html" --alluredir=AllureReports
python -m pytest -s --html=".\HtmlReports\BankingApp_html_report__NoBrowser_27_Feb_2026.html" --alluredir=AllureReports