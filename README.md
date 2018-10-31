# Shadowsocks-libev over Raspberry ZERO PI W

## Install

Installing operating system images  
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Mount the boot partition of the SD card

    sudo diskutil mount /dev/disk2s1

You'll have to locate the boot directory, on my Mac it's in `/Volumes/`.  
In the boot directory, create an empty file called `ssh`.

    touch ssh

If this file exists, ssh will be enabled when the pi is booted.  
Use a text editor to open up the `config.txt` file that is in the boot directory. Go to the bottom and add `dtoverlay=dwc2as` the last line.

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    dtoverlay=dwc2

Then open up `cmdline.txt` After rootwait (the last word on the first line) add a space and then `modules-load=dwc2,g_ether`

    dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=ee25660b-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet init=/usr/lib/raspi-config/init_resize.sh

Plug in a MicroUSB cable from your Pi Zero's USB port to your computer. then SSH in to `raspberrypi.local` and execute the bash command

    sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.origin
    sudo sh -c "wpa_passphrase YOUR_WIFI_SSID >> /etc/wpa_supplicant/wpa_supplicant.conf"
    sudo sed -i "1icountry=CN" /etc/wpa_supplicant/wpa_supplicant.conf

Reboot the ZERO PI. And then clone this repo

    sudo apt-get update
    sudo apt-get install git
    
    git clone https://github.com/codemeow5/ss_over_zero_pi.git
    
    sudo apt-get install python-pip
    sudo pip install Flask

Paste `FLASK_DEBUG=1 /usr/bin/nohup /usr/bin/python /home/pi/ss_over_zero_pi/webadmin.py > /home/pi/webadmin.log 2>&1 &` to `/etc/rc.local`.  
Then execute the command

    sudo chmod u+x /home/pi/ss_over_zero_pi/shadowsocks_nat_install.sh
    sudo /home/pi/ss_over_zero_pi/shadowsocks_nat_install.sh

Install shadowsocks-libev and configure iptables.

## Usage

Plug in a MicroUSB cable from your Pi Zero's USB port to your computer. And then access `http://raspberrypi.local/` from your browser.

Configure WiFi. Reboot Pi and configure your iPhone.

