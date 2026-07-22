from flask import Flask, render_template_string, jsonify
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps Dashboard</title>
    <style>
        body{
            background:#0f172a;
            color:white;
            font-family:Arial;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            margin:0;
        }
        .card{
            width:700px;
            background:#1e293b;
            padding:30px;
            border-radius:15px;
            box-shadow:0 0 15px rgba(0,0,0,.4);
        }
        h1{
            text-align:center;
            color:#38bdf8;
        }
        table{
            width:100%;
            border-collapse:collapse;
            margin-top:20px;
        }
        td{
            padding:12px;
            border-bottom:1px solid #334155;
        }
        td:first-child{
            font-weight:bold;
        }
        .status{
            color:#22c55e;
            font-weight:bold;
        }
    </style>
</head>
<body>

<div class="card">
<h1>🚀 DevSecOps Monitoring Dashboard</h1>

<table>
<tr><td>Status</td><td class="status">ONLINE</td></tr>
<tr><td>Hostname</td><td>{{ hostname }}</td></tr>
<tr><td>Operating System</td><td>{{ os }}</td></tr>
<tr><td>Python Version</td><td>{{ python }}</td></tr>
<tr><td>CPU Usage</td><td>{{ cpu }}%</td></tr>
<tr><td>Memory Usage</td><td>{{ memory }}%</td></tr>
<tr><td>Current Time</td><td>{{ time }}</td></tr>
</table>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        hostname=socket.gethostname(),
        os=platform.platform(),
        python=platform.python_version(),
        cpu=psutil.cpu_percent(interval=1),
        memory=psutil.virtual_memory().percent,
        time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
