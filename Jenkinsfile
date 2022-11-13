pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'echo $PODPIVAS_TOKEN > config'
                sh 'docker build -t podpivasnik:1.0 .'
            }
        }
        stage('Docker Image Run') {
            steps {
                sh 'docker run podpivasnik:1.0 -d'
            }
        }
    }
}