---
title: Flask deployment steps
category: Academic
priority: Medium
starred: None
created: 2025-11-08T16:52:10.114820
updated: 2025-11-08T16:54:27.145895
dg-publish: true
---
# Flask deployment steps

**Priority:** Medium

## Conversation

### Assistant

Minimal Flask deployment workflow for your current setup (MariaDB + Flask):  

---

## 1. Setup environment on the VM
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

Create project folder:
```bash
mkdir ~/flask_app && cd ~/flask_app
```

Clone your repo:
```bash
git clone <your_repo_url> .
```

Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:
```bash
nano .env
```
Paste:
```
FLASK_ENV=production
DB_HOST=db-5308.cs.dal.ca
DB_NAME=CSCI5308_1_DEVINT
DB_USER=CSCI5308_1_DEVINT_USER
DB_PASSWORD=Pohcoo5tig
AIRPORT_NAME=Halifax
```

---

## 2. Use Gunicorn instead of `flask run`
Install:
```bash
pip install gunicorn
```

Test:
```bash
gunicorn -w 3 -b 0.0.0.0:5000 app:app
```
(`app:app` means file `app.py` and Flask instance named `app`.)

If you see your app running on port 5000, this part is good.

---

## 3. Configure Nginx reverse proxy
Edit config:
```bash
sudo nano /etc/nginx/sites-available/flask_app
```
Add:
```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

---

## 4. Make Flask app run on boot
Create a service file:
```bash
sudo nano /etc/systemd/system/flask_app.service
```
Add:
```
[Unit]
Description=Gunicorn instance for Flask app
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/flask_app
Environment="PATH=/home/ubuntu/flask_app/venv/bin"
ExecStart=/home/ubuntu/flask_app/venv/bin/gunicorn -w 3 -b 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable flask_app
sudo systemctl start flask_app
sudo systemctl status flask_app
```

---

## 5. Verify
Visit `http://your_server_ip/`.  
If you see your Flask homepage, it’s deployed.

---

Would you like me to give a simplified version (just enough to run Flask permanently via `systemd`, skipping Nginx)?

---

