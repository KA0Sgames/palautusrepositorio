*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  jaska  salasana1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  salasana1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  oo  salasana1
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  jaska  sala
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  jaska  salasana
    Output Should Contain  Password must contain at least one character outside of a-z

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123