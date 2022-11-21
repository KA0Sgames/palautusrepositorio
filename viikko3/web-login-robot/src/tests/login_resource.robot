*** Settings ***
Resource  resource.robot

*** Variables ***
${USERNAME}  aapo
${ANOTHER_USERNAME}  markku
${VALID_PASSWORD}  aapo1234
${INVALID_PASSWORD}  ssana

*** Keywords ***
Login With Valid Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Valid Username
    Set Valid Password
    Submit Credentials

Login With Invalid Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Another Username
    Set Invalid Password
    Submit Credentials

Set Valid Username
    Input Text  username  ${USERNAME}

Set Another Username
    Input Text  username  ${ANOTHER_USERNAME}

Set Valid Password
    Input Text  password  ${VALID_PASSWORD}

Set Invalid Password
    Input Text  password  ${INVALID_PASSWORD}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}