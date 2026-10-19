Website Monitor

Simple Python application for monitoring website availability.

Features

Checks multiple websites continuously
Displays HTTP status code
Measures response time
Detects UP/DOWN status
Writes all results to a log file
Runs locally or inside Docker
Project Structure

. ├── main.py ├── website.txt ├── monitor.txt └── Dockerfile

Requirements

Python 3.10+
requests
Install dependencies:

pip install requests

Configuration

Add one website per line in website.txt:

https://google.com https://github.com https://microsoft.com

Run Locally

python main.py

The application will continuously check all configured websites and write results to:

monitor.txt

Example output:

2026-10-19 09:00:01 | https://google.com | UP | 200 | 0.25s 2026-10-19 09:00:01 | https://github.com | UP | 200 | 0.31s 2026-10-19 09:00:01 | https://site.invalid | DOWN | ERROR

Run with Docker

Build image:

docker build -t website-monitor .

Run container:

docker run -d --name website-monitor website-monitor

View logs:

docker logs -f website-monitor

Stop container:

docker stop website-monitor

Remove container:

docker rm website-monitor

Export Docker Image

docker save -o website-monitor.tar website-monitor

Import Docker Image

docker load -i website-monitor.tar

Future Improvements

Email notifications
Telegram alerts
Excel reports
Web dashboard
Historical statistics
Docker Compose support
Kubernetes deployment
Author

Yordan Kozhuharov
