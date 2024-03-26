pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('wog')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image('wog').withRun('-p 8777:30000 -v C:\Users\OfriZacks\PycharmProjects\wogrepo\Scores.txt') {
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('wog2').inside('-p 8777:30000 -v C:\Users\OfriZacks\PycharmProjects\wogrepo\Scores.txt') {
                        sh 'python e2e.py'
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop $(docker ps -aq)'
                    sh 'docker rm $(docker ps -aq)'
                        docker.image('wog').push('latest')
                        docker.image('wog2').push('latest')
                    }
                }
            }
        }
    }
}
