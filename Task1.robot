## Task 1
### Myntra Automation using Robot Framework
#1. Launch the browser (Chrome) and navigate to Myntra https://www.myntra.com/
#2. Maximize the browser window for better visibility.
#3. Hover the mouse over the Women section in the top navigation menu.
#4. Click on the Lehenga Choli category.
#5. Once the product listing page is loaded, scroll down to the filter section.
#6. Locate and select the Blue or your fav color filter option.
#7. Store the name/text of a specific product (e.g., Madhuram Floral Embroidered Choli with Skirt).
#8. Print the captured product name in the console.
#9. Close the browser.

*** Settings ***
Library  SeleniumLibrary
Documentation  Myntra Automation using Robot Framework

*** Variables ***
${url}  https://www.myntra.com/

*** Test Cases ***
Performing Myntra Automation
    [Documentation]  Myntra Automation
    Open Browser  ${url}  chrome
    Maximize Browser Window

    #hovering over women section
    Mouse Over    xpath=//a[text()="Women"]

    #clicking on Lehenga Cholis category
    Click Element    xpath=//a[text()="Lehenga Cholis"]

    #scrolling to the colors filter
    Scroll Element Into View    xpath=//span[text()="Color"]

    #selecting color filter
    Click Element    xpath=//input[@value="Pink"]/following-sibling::div

    #Storing product brand and description
    ${product_Brand}=  Get Text    //div[@class="search-searchProductsContainer row-base"]/descendant::h3
    ${product_Desc}=  Get Text    //div[@class="search-searchProductsContainer row-base"]/descendant::h4

    #printing to console
    Log To Console    ${product_Brand} ${product_Desc}

    #Closing browser
    Close Browser

