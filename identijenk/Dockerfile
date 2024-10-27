FROM jenkins/jenkins:jdk17

ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false

USER root

RUN apt-get update \
    && apt-get install -yq apt-transport-https software-properties-common sudo \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install -yq docker-ce containerd.io

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN curl -L https://github.com/docker/compose/releases/download/1.4.1/docker-compose-`uname -s`-`uname -m` \
    > /usr/local/bin/docker-compose; \
    chmod +x /usr/local/bin/docker-compose
    
USER jenkins
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt