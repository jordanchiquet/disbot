import modules.sqlHandler as mek

def getServerSetting(serverid: int, setting):
    output = mek.sqlMektanixDevilDog(purpose='read',table='serversettings',resultColumn=setting,queryColumn='serverid',queryField=serverid)
    if output:
        output = output[0]
    return(output)

    
