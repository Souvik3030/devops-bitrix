terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # Best to pin a major version
    }
    tls = {
      source = "hashicorp/tls"
    }
  }
}

provider "aws" {
  region = "us-east-1" # You can change this to any valid region like us-west-2
}

# 1. Automatically find the latest CentOS Stream 9 AMI
data "aws_ami" "centos9" {
  most_recent = true
  owners      = ["125523088429"] # Official CentOS Project Account

  filter {
    name   = "name"
    values = ["CentOS Stream 9*x86_64*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# 2. Key Pair Generation
resource "tls_private_key" "main" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "ssh_key" {
  content         = tls_private_key.main.private_key_pem
  filename        = "${path.module}/aws_key.pem"
  file_permission = "0600"
}

resource "aws_key_pair" "deployer" {
  key_name   = "centos-key"
  public_key = tls_private_key.main.public_key_openssh
}

# 3. Security Group for Specified Ports
resource "aws_security_group" "centos_sg" {
  name        = "centos_stream_sg"
  description = "Allow SSH, Web, and Custom App Ports"

  dynamic "ingress" {
    for_each = [22, 80, 443, 8890, 8891, 8893, 8894]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 4. Instances with 50GB Storage
resource "aws_instance" "servers" {
  count         = 2
  ami           = data.aws_ami.centos9.id
  instance_type = "t3.small"
  key_name      = aws_key_pair.deployer.key_name

  vpc_security_group_ids = [aws_security_group.centos_sg.id]

  root_block_device {
    volume_size = 50
    volume_type = "gp3"
  }

  tags = {
    Name = "server${count.index + 1}"
  }
}

# 5. Elastic IPs (Fixed Public IPs)
resource "aws_eip" "static_ip" {
  count    = 2
  instance = aws_instance.servers[count.index].id
  domain   = "vpc"
}

output "instance_ips" {
  value = aws_eip.static_ip[*].public_ip
}

