from flask import Flask, request
from jinja2 import Template

import os

app = Flask(__name__)

script_dir = os.path.dirname(__file__)

def get_ip_address(ifname):
	cmd = "ifconfig %s | grep 'inet ' | cut -d: -f2 | awk '{ print $2}'"
	ip_v4 = os.popen(cmd % ifname)
	ip_v4 = ip_v4.read().strip()
	if ip_v4 is None or len(ip_v4) == 0:
		return 'not set'
	return ip_v4

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == 'GET':
		resp = 'Error'
		with open(os.path.join(script_dir, 'index.html.jinja2')) as f:
			template = Template(f.read())
			ip_address = get_ip_address('wlan0')
			resp = template.render(ip_address=ip_address)
		return resp
	ssid = request.form.get('ssid')
	pwd = request.form.get('pwd')
	if ssid is None or pwd is None:
		return 'Invalid parameters'
	if len(ssid) == 0 or len(pwd) == 0:
		return 'Invalid parameters'
	wpa_conf = ''
	with open(os.path.join(script_dir, 'wpa_supplicant.conf.jinjia2')) as f:
		template = Template(f.read())
		wpa_conf = template.render(ssid=ssid, pwd=pwd)
	if len(wpa_conf) > 0:
		with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
			f.write(wpa_conf)
	return 'SUCCESS! Please reboot your ZERO PI(reconnect the usb cabe).'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
