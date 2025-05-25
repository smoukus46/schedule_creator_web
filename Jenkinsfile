pipeline {
    agent any

    environment {
        // Настройки сервера
        SERVER_IP = '195.133.66.33'
        SSH_CREDS = 'ubuntu-server-key'
        PROJECT_DIR = '/root/schedule_creator'
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
                        writeFile file: 'prepare_server.sh', text: """#!/bin/bash
                            chmod 600 "\$SSH_KEY"
                            ssh -o StrictHostKeyChecking=no \\
                                -i "\$SSH_KEY" \\
                                "\$SSH_USER"@"\$SERVER_IP" \\
                                "mkdir -p \$PROJECT_DIR && chmod 777 \$PROJECT_DIR"

                            scp -o StrictHostKeyChecking=no \\
                                -i "\$SSH_KEY" \\
                                -r ./* \\
                                "\$SSH_USER"@"\$SERVER_IP":"\$PROJECT_DIR"
                        """
                        bat 'type prepare_server.sh' // Для отладки
                        bat "\"%GIT_BASH%\" prepare_server.sh"
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
                        writeFile file: 'deploy_docker.sh', text: """#!/bin/bash
                            chmod 600 "\$SSH_KEY"
                            ssh -i "${SSH_KEY}" ${SSH_USER}@${SERVER_IP} "
                                cd ${PROJECT_DIR} &&
                                docker-compose down --remove-orphans &&
                                docker system prune -af &&  # Очистка кеша Docker
                                git pull origin main &&    # Обновление кода
                                docker-compose build --no-cache &&
                                docker-compose up -d
                            "
                        """
                        bat "\"%GIT_BASH%\" deploy_docker.sh"
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