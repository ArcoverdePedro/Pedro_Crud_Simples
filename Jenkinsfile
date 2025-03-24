pipeline{
    agent any
    environment{
        PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"    
    } 
    stages{

        stage('build'){
            steps{
                sh"""
                cd ${PATH}
                docker-compose build --no-cache
                """
                
            }
        }
        stage('test'){
            steps{
                sh "cd ${PATH}"
                echo "World"
                sh "pwd"
                sh "docker run -d -p 8000:8000 projeto_aerotur"
            }
        }
    }
}

