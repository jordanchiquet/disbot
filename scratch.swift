    func getThroughPermissionsHappy() {
        sleep(1)
        print("starting bluetooth")
        permSwitch(permSwitch: "bluetooth", permissionTier: "Allow")
        permSwitch(permSwitch: "camera", permissionTier: "off")
        permSwitch(permSwitch: "contact", permissionTier: "Allow")
        permSwitch(permSwitch: "notification", permissionTier: "off")
        permSwitch(permSwitch: "location", permissionTier: "Allow")
        sleep(1)
        truce.alerts["Login Process"].buttons["Complete permission setup"].tap()
    }
