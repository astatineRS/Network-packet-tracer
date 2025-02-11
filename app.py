from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

def parse_packet_file(filename):
    packets = []
    if os.path.exists(filename):
        print(f"Reading file: {filename}")  # Debugging statement
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                print("Raw Line:", line.strip())  # Debugging
                if len(parts) >= 14:
                    packet = {
                        'timestamp': parts[0],
                        'src_mac': parts[1],
                        'dst_mac': parts[3],
                        'protocol': filename.split('/')[-1].split('.')[0].upper(),
                        'length': parts[8],
                        'src_ip': parts[11] if 'ARP' not in filename else parts[11],
                        'dst_ip': parts[13] if 'ARP' not in filename else parts[13]
                    }
                    packets.append(packet)
    else:
        print(f"File not found: {filename}")  # Debugging statement
    return packets

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/packets/<protocol>')
def get_packets(protocol):
    filename = f'data/{protocol.lower()}.txt'
    if not os.path.exists(filename):
        return jsonify({"error": f"File {filename} not found"}), 404
    
    packets = parse_packet_file(filename)
    return jsonify(packets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
