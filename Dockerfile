FROM webdevops/php-apache:7.3
COPY maeforsai/ /app/
RUN chmod 777 -Rf /app/#
