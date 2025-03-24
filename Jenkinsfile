pipeline{
    agent any 
    stages{
        stage('build'){
            steps{
                dir('/home/pedro/Documentos/gittyup/projeto_aerotur/'){
                    sh '''
                    ls -l
                    pwd
                    echo "Hello World"

                    
                    
                    '''

                }
            }
        }
        stage('test'){
            steps{
                echo "World"
                sh 'pwd'
            }
        }
    }
}

