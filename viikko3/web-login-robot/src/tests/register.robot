*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jaska
    Set Password  jaska123
    Set Confirmation  jaska123
    Submit Information
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  oo
    Set Password  salasana1
    Set Confirmation  salasana1
    Submit Information
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  jaska
    Set Password  ssana
    Set Confirmation  ssana
    Submit Information
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  jaska
    Set Password  jaska123
    Set Confirmation  salasana1
    Submit Information
    Register Should Fail With Message  Password and confirmation don't match

Login After Successful Registration
    Set Username  ${USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Confirmation  ${VALID_PASSWORD}
    Submit Information
    Register Should Succeed
    Login With Valid Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ${ANOTHER_USERNAME}
    Set Password  ${INVALID_PASSWORD}
    Set Confirmation  ${INVALID_PASSWORD}
    Submit Information
    Register Should Fail With Message  Password is too short
    Login With Invalid Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Text  password_confirmation  ${confirmation}

Submit Information
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}