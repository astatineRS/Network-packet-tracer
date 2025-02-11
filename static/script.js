function loadPackets(protocol) {
    fetch(`/api/packets/${protocol}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('packet-data');
            tbody.innerHTML = '';

            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7">No data found</td></tr>';
                return;
            }

            data.forEach(packet => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${packet.timestamp}</td>
                    <td>${packet.protocol}</td>
                    <td>${packet.src_mac}</td>
                    <td>${packet.dst_mac}</td>
                    <td>${packet.src_ip}</td>
                    <td>${packet.dst_ip}</td>
                    <td>${packet.length}</td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(error => console.error('Fetch error:', error));
}
