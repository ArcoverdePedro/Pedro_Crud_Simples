pipeline{
    agent any
    environment{
        PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"    
    } 
    stages{
        stage('checkout'){
            steps{
                sh '''
                cd ${PATH}
                git config --global pull.rebase false
                git pull origin main
                '''
                
            } 
        }
        stage('build'){
            steps{
                sh'''
                cd ${PATH}
                docker-compose build --no-cache -t projeto_aerotur
                '''
                
            }
        }
        stage('test'){
            steps{
                sh "cd ${PATH}"
                echo "World"
                sh 'pwd'
                sh 'docker run -d -p 8000:8000 projeto_aerotur'
            }
        }
    }
}

