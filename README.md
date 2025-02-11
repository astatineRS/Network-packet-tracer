# Network Packet Tracer

A simple network packet analyzer built using Flask and `tcpdump`. This tool captures and displays ARP, TCP, and UDP packets from the network in real time.

## Features
- Captures **ARP**, **TCP**, and **UDP** packets.
- Displays captured packets with details like **timestamp, MAC addresses, IP addresses, and packet length**.
- Simple web interface to filter and view packet details.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/astatineRS/Network-packet-tracer.git
cd Network-packet-tracer
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\\Scripts\\activate'
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Packet Capture Script
```bash
sudo ./capture.sh
```

### 5. Start the Flask Server
```bash
python app.py
```

### 6. Access the Web Interface
Open a browser and go to:
```
http://127.0.0.1:5000/
```

## File Structure
```
📂 Network-packet-tracer
├── 📂 data             # Stores captured packets
├── 📂 static           # Contains CSS and JavaScript files
├── 📂 templates        # HTML templates for web interface
├── app.py             # Flask backend
├── capture.sh         # Script to capture network packets
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Troubleshooting
- **Permission Issues:** Run `chmod +x capture.sh` before executing it.
- **Flask App Not Running?** Ensure dependencies are installed and the virtual environment is activated.
- **No Packets Captured?** Ensure `tcpdump` is installed and you have root permissions.

## License
This project is open-source and available under the MIT License.

---
🚀 Developed by **astatineRS**

