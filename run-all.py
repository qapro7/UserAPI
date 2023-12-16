import os
import sys
from datetime import datetime

# Get the current timestamp in the format 'yymmddhm'.
timestamp = datetime.now().strftime("%y%m%d%H%M%S")

# Run pytest with the HTML formatter and specify the output directory.
report_path = os.path.join('reports', f'test-results-{timestamp}.html')
os.system(f'pytest -v --html={report_path}')
