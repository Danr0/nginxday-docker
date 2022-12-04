ARG PYTHON_VERSION=2
FROM python:${PYTHON_VERSION}-alpine

COPY ./nginx-ldap/nginx-ldap-auth-daemon.py /usr/src/app/

WORKDIR /usr/src/app/

RUN adduser --system --no-create-home nonroot
# Install required software
RUN \
    apk --no-cache add openldap-dev && \
    apk --no-cache add --virtual build-dependencies build-base && \
    pip install python-ldap && \
    apk del build-dependencies

USER nonroot
EXPOSE 8888
CMD ["python", "/usr/src/app/nginx-ldap-auth-daemon.py", "--host", "0.0.0.0","-p", "8888", "-u", "ldap://openldap:1389","-w", "@dminpasswordisverysecure!2", "-D","cn=admin,dc=example,dc=org", "-b","dc=example,dc=org"]