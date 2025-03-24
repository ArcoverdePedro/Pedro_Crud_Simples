pipeline{
    agent any
    environments{
        PATH ="/home/pedro/Documentos/gittyup/projeto_aerotur/"    
    } 
    stages{
        stage('build'){
            steps{
                dir('/home/pedro/Documentos/gittyup/projeto_aerotur/'){
                    sh '''
                    ls -l
                    pwd
                    echo "Hello World"
                    docker build -t projeto_aerotur .
                    '''

                }
            }
        }
        stage('test'){
            steps{
                sh "cd /home/pedro/Documentos/gittyup/projeto_aerotur/"
                echo "World"
                sh 'pwd'
                sh 'docker run -d -p 8000:8000 projeto_aerotur'
            }
        }
    }
}

