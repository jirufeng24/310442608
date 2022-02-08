pipeline {
    agent any
	options {
        timeout (200)
    }
    stages {
        stage('pull code') {
            
            steps {
                echo '开始拉取代码'
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'cb3ae9aa-a44b-4b2c-a972-50e3706891fb', url: 'https://github.com/jirufeng24/310442608.git']]])
                echo '拉取代码结束'
            }
        }
        stage('copy the Jflash file') {
			steps {
			    echo '开始拷贝Jflash需要的文件'
				bat """D:\\python\\python.exe E:\\demo\\Copy_JLink_File.py"""
				echo '拷贝结束'
			}
		}
		stage('run jflash program') {
			steps {
			    echo 'Jflash开始烧录'
				bat """D:\\python\\python.exe E:\\demo\\Load_JLink1.py"""
				echo 'Jflash脚本运行结束'
			}
		}   
    }
	 post { 
        always { 
            emailext( 
                subject: '构建通知：${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!', 
                body: '${FILE,path="email.html"}', 
                to: 'a17521031790@163.com',
                from: 'a17521031790@163.com'
                ) 
            
        } 
        
    }
}