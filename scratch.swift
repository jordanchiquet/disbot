    func testquickLogin() {
        loginView(country: nil, loginNumber: "9979991000")
        sleep(2)
        getThroughPermissionsHappy()
        sleep(5)
        
        let app = XCUIApplication()
        let elementsQuery = app.alerts["Verification Message Sent!"].scrollViews.otherElements
        elementsQuery.staticTexts["Verification Message Sent!"].tap()
        elementsQuery.buttons["Ok"].tap()
        
        let elementsQuery2 = app.alerts["Enter Verification Code"].scrollViews.otherElements
        elementsQuery2.staticTexts["Enter Verification Code"].tap()
        elementsQuery2.staticTexts["Please enter Verification Code recieved via text"].tap()
        elementsQuery2.collectionViews.cells.children(matching: .other).element.children(matching: .other).element.children(matching: .other).element.children(matching: .other).element(boundBy: 1).tap()
        app/*@START_MENU_TOKEN@*/.keys["v"]/*[[".keyboards.keys[\"v\"]",".keys[\"v\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/.tap()
        app/*@START_MENU_TOKEN@*/.keys["g"]/*[[".keyboards.keys[\"g\"]",".keys[\"g\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/.tap()
        
        let hKey = app/*@START_MENU_TOKEN@*/.keys["h"]/*[[".keyboards.keys[\"h\"]",".keys[\"h\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/
        hKey.tap()
        hKey.tap()
        elementsQuery2.buttons["Submit"].tap()
        app.alerts["Verification Code Incorrect"].scrollViews.otherElements.buttons["Ok"].tap()
                
    }