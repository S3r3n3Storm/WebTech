sudo rm /etc/nginx/sites-enabled/default /etc/nginx/nginx.conf
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -sh /home/box/web/etc/gunicorn.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start