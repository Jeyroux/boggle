async function getLocalIPs() {
    const rtc = new RTCPeerConnection();
    rtc.createDataChannel('dummy');
  
    rtc.onicecandidate = event => {
      if (event.candidate) {
        console.log('Local IP:', event.candidate.candidate);
      }
    };
  
    await rtc.createOffer().then(offer => rtc.setLocalDescription(offer));
  }
  
getLocalIPs();

fetch('https://api.ipify.org?format=json')
.then(response => response.json())
.then(data => {
document.getElementById('ipAddress').textContent = data.ip;
  })
  .catch(error => {
    console.error('Error fetching IP:', error);
    document.getElementById('ipAddress').textContent = 'Unable to fetch IP.';
  });