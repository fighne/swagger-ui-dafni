FROM swaggerapi/swagger-ui

ENV ROOT_URL_TYPE 'localhost'
COPY *.yaml /usr/share/nginx/html/
COPY config.py /usr/local/sbin/config.py

RUN /bin/sh /usr/local/sbin/genconfig.sh
ENV CONFIG_URL /dafni-config.json
ENV VALIDATOR_URL nullcd html
