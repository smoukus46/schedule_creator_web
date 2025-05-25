pipeline {
    agent any

    environment {
        // Настройки сервера
        SERVER_IP = '195.133.66.33'
        SSH_CREDS = 'ubuntu-server-key'
        PROJECT_DIR = '/root/schedule_creator_web'
        BACKEND_PORT = '8000'

        // Путь к Git Bash
        GIT_BASH = 'C:\\Program Files\\Git\\bin\\bash.exe'
    }

   stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                     url: 'https://github.com/smoukus46/schedule_creator_web.git'
            }
        }

        stage('Prepare Server') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ubuntu-server-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    ),
                    string(credentialsId: 'SERVER_IP', variable: 'SERVER_IP'),
                    string(credentialsId: 'PROJECT_DIR', variable: 'PROJECT_DIR')
                ]) {
                    script {
                        bat """
                            "%GIT_BASH%" -c '
                            ssh -o StrictHostKeyChecking=no -i "${SSH_KEY}" ${SSH_USER}@${SERVER_IP} \
                                "mkdir -p ${PROJECT_DIR}"

                            scp -o StrictHostKeyChecking=no -i "${SSH_KEY}" -r ./* \
                                ${SSH_USER}@${SERVER_IP}:${PROJECT_DIR}
                            '
                        """
                    }
                }
            }
        }

        stage('Deploy with Docker') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ubuntu-server-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    ),
                    string(credentialsId: 'SERVER_IP', variable: 'SERVER_IP'),
                    string(credentialsId: 'PROJECT_DIR', variable: 'PROJECT_DIR')
                ]) {
                    script {
                          bat """
                            "%GIT_BASH%" -c '
                            ssh -o StrictHostKeyChecking=no -i "${SSH_KEY}" ${SSH_USER}@${SERVER_IP} \
                                "cd ${PROJECT_DIR} && \
                                docker-compose down && \
                                docker system prune -af && \
                                docker-compose build --no-cache && \
                                docker-compose up -d"
                            '
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deploy finished successful!"
            script {
                withCredentials([string(credentialsId: 'SERVER_IP', variable: 'SERVER_IP')]) {
                    echo "Backend available on: http://${SERVER_IP}:8000"
                }
            }
        }
        failure {
            echo "DeployError"
        }
    }
}