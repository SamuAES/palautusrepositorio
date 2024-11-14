*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Variables ***
${USERNAME}        joniman
${PASSWORD}        asdasd123

*** Test Cases ***

Register With Valid Username And Password
    Create User With Valid Inputs
    Register Should Success

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  asdasd123
    Set Password Confirmation  asdasd123
    Submit Credentials
    Register Should Fail With Message  Username must be at least three characters long.

Register With Valid Username And Too Short Password
    Set Username  joniman
    Set Password  asd
    Set Password Confirmation  asd
    Submit Credentials
    Register Should Fail With Message  Password must be at least eight characters long.

Register With Valid Username And Invalid Password
    Set Username  joniman
    Set Password  asdasdasd
    Set Password Confirmation  asdasdasd
    Submit Credentials
    Register Should Fail With Message  Password must have atleast one number.

Register With Nonmatching Password And Password Confirmation
    Set Username  joniman
    Set Password  asdasd123
    Set Password Confirmation  asdasd111
    Submit Credentials
    Register Should Fail With Message  Passwords didn't match.

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  asdasd123
    Set Password Confirmation  asdasd123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Create User With Valid Inputs
    Move To Main Page And Logout
    Login with created username
    Login Should Succeed

Login After Failed Registration
    Set Username  joniman
    Set Password  asdasdasd
    Set Password Confirmation  asdasdasd
    Submit Credentials
    Click Link  Login
    Set Username  joniman
    Set Password  asdasdasd
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

    

*** Keywords ***
Create User With Valid Inputs
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD}
    Submit Credentials

Register Should Success
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Login with created username
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Move To Main Page And Logout
    Click Link  Continue to main page
    Click Button  Logout

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

