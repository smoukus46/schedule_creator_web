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
                sshagent([SSH_CREDS]) {
                    script {
                        // Создаем рабочую директорию на сервере
                        bat """
                            ssh -o StrictHostKeyChecking=no ${SERVER_IP} "
                            mkdir -p ${PROJECT_DIR} &&
                            rm -rf ${PROJECT_DIR}/*
                            "
                        """

                        // Копируем файлы на сервер
                        bat """
                            scp -o StrictHostKeyChecking=no -r . ${SERVER_IP}:${PROJECT_DIR}
                        """
                    }
                }
            }
        }

        stage('Build & Deploy') {
            steps {
                sshagent([SSH_CREDS]) {
                    script {
                        // Запускаем docker-compose
                        bat """
                            ssh -o StrictHostKeyChecking=no ${SERVER_IP} "
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

        stage('Health Check') {
            steps {
                sshagent([SSH_CREDS]) {
                    script {
                        // Проверяем работу контейнеров
                        bat """
                            ssh -o StrictHostKeyChecking=no ${SERVER_IP} "
                            docker ps --filter 'name=schedule_creator' &&
                            curl -s http://localhost:${FRONTEND_PORT}/health || echo 'Frontend not ready' &&
                            curl -s http://localhost:${BACKEND_PORT}/health || echo 'Backend not ready'
                            "
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            bat """
                echo "Деплой успешно завершен!"
                echo "Frontend: http://${SERVER_IP}:${FRONTEND_PORT}"
                echo "Backend: http://${SERVER_IP}:${BACKEND_PORT}"
            """
        }
        failure {
            bat 'echo "Ошибка при деплое!"'
            // Дополнительные действия при ошибке
        }
        always {
            // Очистка ресурсов при необходимости
        }
    }
}