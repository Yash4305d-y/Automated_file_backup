<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<div class="container">

<h1>📁 Automated File Backup (Python)</h1>

<p>
This project is a Python-based automated file backup system that copies files
from a source folder to a destination folder either:
</p>

<ul>
    <li>⏰ Automatically every day at a scheduled time</li>
    <li>⚡ Instantly when triggered manually</li>
</ul>

<hr>

<h2>🚀 Features</h2>
<ul>
    <li>Automatic daily backups</li>
    <li>Manual backup option</li>
    <li>Supports all file types</li>
    <li>Fast and efficient copying</li>
    <li>Easy configuration</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
project/
│
├── backup.py        # Main Python script
├── config.json      # Configuration file (paths & schedule)
└── README.html      # This file
</pre>

<hr>

<h2>⚙️ Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Required libraries:</li>
</ul>

<pre>
pip install schedule
</pre>

<hr>

<h2>🛠️ Configuration</h2>
<p>Edit the <code>config.json</code> file:</p>

<pre>
{
    "source_folder": "C:/Users/YourName/Documents",
    "destination_folder": "D:/Backup",
    "backup_time": "20:00"
}
</pre>

<ul>
    <li><b>source_folder:</b> Folder to copy files from</li>
    <li><b>destination_folder:</b> Backup location</li>
    <li><b>backup_time:</b> Time in 24-hour format</li>
</ul>

<hr>

<h2>▶️ Usage</h2>

<h3>Run automatic backup:</h3>
<pre>
python backup.py
</pre>

<h3>Run instant backup:</h3>
<pre>
python backup.py --now
</pre>

<hr>

<h2>🧠 How It Works</h2>
<ul>
    <li>Uses Python <code>shutil</code> for copying files</li>
    <li>Uses <code>schedule</code> library for timing</li>
    <li>Runs continuously and checks time every second</li>
</ul>

<hr>

<h2>📌 Example Code Snippet</h2>

<pre>
import shutil
import os

def backup(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for file in os.listdir(source):
        src_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)

    print("Backup completed!")
</pre>

<hr>

<h2>📢 Notes</h2>
<ul>
    <li>Ensure paths are correct</li>
    <li>Run script continuously for scheduled backups</li>
    <li>Use Task Scheduler / Cron for background execution (optional)</li>
</ul>

<hr>

<h2>📄 License</h2>
<p>This project is open-source and free to use.</p>

</div>

</body>
</html>
