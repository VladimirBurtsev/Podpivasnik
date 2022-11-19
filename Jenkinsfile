pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'echo $PODPIVAS_TOKEN > config'
                sh 'docker build -t podpivasnik:1.0 .'
            }
        }
        containers = sh 'docker ps -a -q'
        
        stage('Docker Image Run') {
            steps {
                sh 'docker rm -f $containers'
                sh 'docker run --name podpivasnik -d podpivasnik:1.0'
            }
        }
    }
}