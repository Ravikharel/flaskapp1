pipeline {
    agent any
    environment{ 
        ansible_user = "vagrant" 
        ansible_ip = "192.168.56.15"
    }

    stages {

        stage('Copy to Ansible Node') {
            steps {
                sh 'scp -r * ${ansible_user}@${ansible_ip}:/home/vagrant/flask-app/'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                sh 'ssh ${ansible_user}@${ansible_ip} "ansible-playbook -i /home/vagrant/ansible/inventory /home/vagrant/ansible/deploy.yml"'
            }
        }
    }
}

