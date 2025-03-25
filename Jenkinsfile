pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
        CONTAINER_NAME = "projeto_aerotur_container" // Nome do seu container
        IMAGE_NAME = "projeto_aerotur" // Nome da sua imagem
    }
    stages {
        stage('Limpeza Containers e Imagens') {
            steps {
                script {
                    sh '''
                        // Para o container em execução
                        docker stop ${CONTAINER_NAME}
                        // Remove o container
                        docker rm ${CONTAINER_NAME}
                        // Remove a imagem antiga
                        docker rmi ${IMAGE_NAME}
                        // Limpa imagens órfãs e containers não utilizados
                        docker system prune -af
                    '''
                }
            }
        }
        stage('build') {
            steps {
                script {
                    sh '''
                        echo "Current REPO_PATH: ${REPO_PATH}"
                        cd ${REPO_PATH}
                        docker build --no-cache -t ${IMAGE_NAME} .
                    '''
                }
            }
        }
        stage('test') {
            steps {
                script {
                    sh '''
                        echo "Test Stage"
                        cd ${REPO_PATH}
                        echo 'World'
                        docker run -p 8000:8000 --name ${CONTAINER_NAME} -d ${IMAGE_NAME}
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou!'
        }
    }
}