FROM ubuntu
RUN apt update && apt install tzdata -y
ENV TZ="Asia/Taipei"
RUN apt install apache2 -y
RUN apt install php -y
RUN apt install libapache2-mod-php -y
RUN php -version
RUN mkdir /secert
RUN chgrp -R www-data /secert
RUN chmod -R g+w /secert
COPY src/index-secret.php /secert/index.php
COPY src/index.php /var/www/html/index.php
COPY sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN a2ensite default-ssl
RUN service apache2 restart