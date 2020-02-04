    if a == "del" or a == "delete":
        delid = b
        if delid == "1":
            await ctx.send ("Timer 1 is a permanent timer to simplify programmatic looping. You can ask Jordan if you want to know more.")
            return
        else:
            timerdata = open("/home/disbotren/test/discordtimers.csv", "rt")
            newtimerdata = open("/home/disbotren/test/discordtimers1.csv", "a", newline='')
            reader = csv.reader(timerdata, delimiter=",")
            writer = csv.writer(newtimerdata)
            for row in reader:
                if delid != row[0]:
                    writer.writerow(row)
            timerdata.close()
            newtimerdata.close()
            os.system('rm /home/disbotren/test/discordtimers.csv')
            os.system('mv /home/disbotren/test/discordtimers1.csv /home/disbotren/test/discordtimers.csv')
            await ctx.send("Timer #" + delid + " deleted.")
            return