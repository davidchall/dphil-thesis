#!/usr/bin/env python

from datetime import datetime

# Read TeXcount output file
fin  = open("macros/texcount_output.txt", "r")
fout = open("macros/wordcount.txt", "a")
chapterWordCount = []
for line in fin:
    # Get individual chapter word counts
    if "Chapter:" in line:
        words = line.split()
        chapterWordCount.append("['" + ' '.join(words[4:]) + "', " + words[0] + "]")

    # Write out timestamped total word count
    elif "Words:" in line:
        now = datetime.now().replace(microsecond=0)
        fout.write(str(now) + " " + line.split()[1] + "\n")
fin.close()
fout.close()

# Read in list of timestamps
fin = open("macros/wordcount.txt", "r")
timeWordCount = []
for line in fin:
    words = line.split()
    timestamp = datetime.strptime(words[0]+" "+words[1], "%Y-%m-%d %H:%M:%S")
    timeWordCount.append("[new Date(" + 
                         str(timestamp.year)   + ", " +
                         str(timestamp.month)  + ", " +
                         str(timestamp.day)    + ", " +
                         str(timestamp.hour)   + ", " +
                         str(timestamp.minute) + ", " +
                         str(timestamp.second) + 
                         "), " + words[2] + "]")


# String containing chapter word count data
chapterData = """
// Data containing chapter word counts
var chapterData = new google.visualization.DataTable();
chapterData.addColumn('string', 'Chapter');
chapterData.addColumn('number', 'Words');
chapterData.addRows([
"""
chapterData += ",\n".join(chapterWordCount)
chapterData += "\n]);"

# String containing timestamped word count data
timestampData = """
// Data containing timestamped word counts
var timestampData = new google.visualization.DataTable();
timestampData.addColumn('datetime', 'Commit Date');
timestampData.addColumn('number', 'Words');
timestampData.addRows([
"""
timestampData += ",\n".join(timeWordCount)
timestampData += "\n]);"


# Output HTML file
string = """<html>
<head>
<!--Load the AJAX API-->
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript">

// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);
function drawChart() {
"""
string += chapterData
string +="""
// Set chart options
var chapterOptions = {'title':'Chapter word counts',
'width':800,
'height':400
};

// Instantiate and draw our chart, passing in some options.
var chapterChart = new google.visualization.PieChart(document.getElementById('chapterChart_div'));
chapterChart.draw(chapterData, chapterOptions);

"""
string += timestampData
string += """
var timestampOptions = {'title':'Word count vs time',
'width':800,
'height':500,
legend:{position:'none'}
};
var timestampChart = new google.visualization.LineChart(document.getElementById('timestampChart_div'));
timestampChart.draw(timestampData, timestampOptions);
}

</script>
</head>

<body>
<div id="chapterChart_div"></div>
<div id="timestampChart_div"></div>
</body>
</html>"""

html = open("macros/stats.html", "w")
html.write(string)
html.close()
