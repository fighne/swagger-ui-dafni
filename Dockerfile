FROM swaggerapi/swagger-ui

ENV ROOT_URL 'localhost'
COPY *.yaml /usr/share/nginx/html/
COPY genconfig.sh /usr/local/sbin/genconfig.sh

RUN /bin/sh /usr/local/sbin/genconfig.sh
ENV CONFIG_URL /dafni-config.json
ENV VALIDATOR_URL nullcd html
