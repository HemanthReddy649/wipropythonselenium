*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Process

*** Variables ***
${url}      https://practice.automationtesting.in/

*** Test Cases ***
verify login
        Open Browser        ${url}      firefox
        Maximize Browser Window
        
        Wait Until Element Is Visible    (//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket'])[1]
        Click Element    (//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket'])[1]

        Wait Until Element Is Visible    (//a[normalize-space()='View Basket'])[1]
        Click Element    (//a[normalize-space()='View Basket'])[1]
        Sleep    5s

        Wait Until Element Is Visible    //a[@class='checkout-button button alt wc-forward']
        Click Element    //a[@class='checkout-button button alt wc-forward']
        Sleep    5s
        
        Wait Until Element Is Visible    //input[@id='billing_first_name']

        Input Text    billing_first_name    varun
        Input Text    billing_last_name     varun
        Input Text    billing_email         varun@gmail.com
        Input Text    billing_phone         9876543210
        Input Text    billing_address_1     varun-varun
        Input Text    billing_city          varun-e
        Input Text    billing_postcode      12345
        
        Click Element    //input[@id='payment_method_cod']
        

        Scroll Element Into View    //input[@id='place_order']
        Wait Until Element Is Visible    //input[@id='place_order']
        Click Element    //input[@id='place_order']

        Sleep    5s

        Close Browser



