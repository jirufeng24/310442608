import hudson.model.*;
println env.JOB_NAME
println env.BUILD_NUMBER

pipeline {
    agent any
    options {
        timeout(time:60, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
		disableConcurrentBuilds()
    }
    //triggers {
        //pollSCM('H/1 * * * *') 
    //}
    stages {
        stage('step1--Download Jflash and bin files required for the upgrade.') {
			steps {
			    echo '开始拷贝脚本需要的Jflash脚本需要的和bin文件.'
				bat """D:\\python\\python.exe E:\\burn_test\\public\\copy_files_demo.py"""
				echo '脚本文件拷贝结束.'
			}
        }
        stage('step2--Pull the testcase scripts.') {
            steps {
                retry(3){
                    echo '开始拉取script代码'
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'cb3ae9aa-a44b-4b2c-a972-50e3706891fb', url: 'https://github.com/jirufeng24/310442608.git']]])
                    echo '拉取script代码结束'
                        }
                    }
        //stage('step3--Automatically install the libraries required by the test scripts.') {
            
           // steps {}
		}
		stage('step4--Run the test script.') {
			steps {
			    script{
                    try {
        			    echo '开始烧录脚本执行'
        			    //bat """cd C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\test_jflash_script\\burn_test"""
        				bat """pytest --alluredir=result -s -v C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\test_burn_core\\burn_test"""
        				echo '烧录脚本执行结束'
                    } catch (Exception e) {
			            println e
                        }
		            }
	            }
        }
    }
    post('step5--Work after executing the test script.') { 
        always { 
            script{// 集成allure，目录需要和保存的results保持一致，注意此处目录为job工作目录之后的目录，Jenkins会自动将根目录与path进行拼接
                allure includeProperties: false, jdk: '', report: 'report', results: [[path: 'result']]
                    } 
            echo "clear workspace......"
            //deleteDir()
            emailext( 
                subject: '构建通知：${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!', 
                body: '${FILE,path="email.html"}', 
                to: 'a17521031790@163.com',
                from: 'a17521031790@163.com'
                    ) 
                }   
    }
}