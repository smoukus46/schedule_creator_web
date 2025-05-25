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
            }
        }

       stage('Prepare Server') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ubuntu-server-key',
                    keyFileVariable: 'SSH_KEY'
                    usernameVariable: 'SSH_USER'
                )]) {
                    script {
                        // Создаем директорию на сервере
                        sh """
                            ssh -o StrictHostKeyChecking=no \
                                -i "${SSH_KEY}" \
                                ${SSH_USER}@${SERVER_IP} \
                                "mkdir -p ${PROJECT_DIR} && chmod 777 ${PROJECT_DIR}"
                        """

                        // Копируем файлы
                        sh """
                            scp -o StrictHostKeyChecking=no \
                                -i "${SSH_KEY}" \
                                -r . \
                                ${SSH_USER}@${SERVER_IP}:${PROJECT_DIR}
                        """
                    }
                }
            }
        }

        stage('Deploy with Docker') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ubuntu-server-key',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                    script {
                        sh """
                            ssh -o StrictHostKeyChecking=no \
                                -i "${SSH_KEY}" \
                                ${SSH_USER}@${SERVER_IP} \
                                "cd ${PROJECT_DIR} && \
                                docker-compose down && \
                                docker-compose build --no-cache && \
                                docker-compose up -d"
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deploy finished successful!"
            echo "Backend enable on: http://${SERVER_IP}:8000"
        }
        failure {
            echo "DeployError"
        }
    }
}