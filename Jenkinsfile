pipeline {
    agent any

    environment {
        // Настройки сервера
        SERVER_IP = '195.133.66.33'  // Ваш IP сервера Ubuntu
        SSH_CREDS = 'ubuntu-server-key' // ID SSH-ключей из Jenkins
        PROJECT_DIR = '/root/schedule_creator' // Директория на сервере

        // Переменные окружения (адаптируйте под ваши нужды)
        BACKEND_PORT = '8000'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                     url: 'https://github.com/smoukus46/schedule_creator_web.git'
                // Исправляем кодировку для русских символов
                bat 'chcp 65001 > nul'
            }
        }

       stage('Prepare Server') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ubuntu-server-key',
                    keyFileVariable: 'SSH_KEY'
                )]) {
                    script {
                        // Используем plink вместо ssh-agent
                        bat """
                            set PLINK_PATH=C:\\Program Files\\PuTTY\\plink.exe
                            "%PLINK_PATH%" -i "%SSH_KEY%" -ssh ubuntu@${SERVER_IP} "
                            mkdir -p ${PROJECT_DIR} &&
                            rm -rf ${PROJECT_DIR}/*
                            "
                        """

                        // Копируем файлы через pscp
                        bat """
                            set PSCP_PATH=C:\\Program Files\\PuTTY\\pscp.exe
                            "%PSCP_PATH%" -i "%SSH_KEY%" -r . ubuntu@${SERVER_IP}:${PROJECT_DIR}
                        """
                    }
                }
            }
        }

        stage('Build & Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ubuntu-server-key',
                    keyFileVariable: 'SSH_KEY'
                )]) {
                    script {
                        bat """
                            set PLINK_PATH=C:\\Program Files\\PuTTY\\plink.exe
                            "%PLINK_PATH%" -i "%SSH_KEY%" -ssh ubuntu@${SERVER_IP} "
                            cd ${PROJECT_DIR} &&
                            docker-compose down &&
                            docker-compose build --no-cache &&
                            docker-compose up -d
                            "
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            bat 'chcp 65001 > nul && echo "Deploy finished successful!"'
            bat """
                chcp 65001 > nul && echo "Frontend: http://${SERVER_IP}:3000" &&
                echo "Backend: http://${SERVER_IP}:8000"
            """
        }
        failure {
            bat 'chcp 65001 > nul && echo "DeployError"'
        }
    }
}