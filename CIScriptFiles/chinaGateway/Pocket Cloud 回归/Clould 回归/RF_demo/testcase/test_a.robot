*** Settings ***
Library    Selenium2Library


*** Variable ***
${var1}    set variable     60
${var2}=    evaluate        890
${var3}     create list      hello world
&{var1}     create dictionary      name=jack    pw=123456
@{var}     create list      1  a  8

*** Test Cases ***
修改网关名称
    [Tags]    test
	log to console    BBBBBBBBBBBBBBBB
	log to console    ${var2}

score_test_0004
    [Tags]    test
	log to console    BBBBBBBBBBBBBBBB
	log to console    ${var2}


