# PDF Report Generation 

This project is currently used to generate PDF reports for the MU News Bureau. PDF Reports are created for every news release, contain the date the release was published, the title of the original news release, a link to the original news release, a list of the state placements, national placements, and international placements. 

Each placement is on a single line, contains the date the placement was published, the name of the placement's publication, a link to the placement if available, what the potential reach was of the placement, and the country if an international placement. 

At the bottom of the report, the totals are available: total number of placements, total number of potential reach, and total social media impressions. 

To see an example report, see [here](./ChadRose.pdf).

The files that generate this report are [`server.py`](./flask_proj/server.py), [`index.html`](./flask_proj/templates/index.html), and [`t.py`](./flask_proj/t.py).

`t.py` is the file that creates and generates the PDF, as well as cleaning the data from the uploaded CSV file.

`index.html` is the file containing the webpage where the users input their information.

`server.py` is the file that connects `index.html` and `t.py` so that the webpage can run the python script with the information gathered from the webpage. 