sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

# Add the permission
# Create the docker group
sudo groupadd docker
# Add user to the docker group
sudo usermod -aG docker $USER
# Add the changes to the group
newgrp docker

# check the version
docker -v

# Example
echo "Running docker command ..."
docker run hello-world
