*** Settings ***
Library      SeleniumLibrary
Library      DataDriver
...          file=C:/Users/thiru/PycharmProjects/PythonAdvanceProject/RobotFramework/TestData/ddtLogindata.xlsx
...          sheet_name=ddtLogindata

Test Template     Login Test
Suite Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Suite Teardown    Close Browser


*** Test Cases ***
Login with valid users


*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}

    Go To    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

    Wait Until Element Is Visible    xpath://input[@name='username']    15s

    Input Text    xpath://input[@name='username']    ${username}
    Input Text    xpath://input[@name='password']    ${password}

    Click Element    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[text()='Dashboard']    15s

    # Logout after successful login
    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Click Element    xpath://a[text()='Logout']