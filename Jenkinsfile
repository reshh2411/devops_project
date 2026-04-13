pipeline {
    agent any

    environment {
        IMAGE = "bresh2411/devops_project:v1.0"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/reshh2411/devops_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t devops_project .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'sudo docker tag devops_project $IMAGE'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'PASS')]) {
                    sh '''
                    echo $PASS | sudo docker login -u bresh2411 --password-stdin
                    sudo docker push $IMAGE
                    '''
                }
            }
        }
    }
}
