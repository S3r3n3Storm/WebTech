sudo rm /etc/nginx/sites-enabled/default /etc/nginx/nginx.conf
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_django.conf   /etc/gunicorn.d/test2
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start