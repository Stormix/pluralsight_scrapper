# @Author: Anas Mazouni <Stormix>
# @Date:   2017-05-18T04:07:02+01:00
# @Email:  madadj4@gmail.com
# @Project: PluralSight Scraper V1.0
# @Last modified by:   Stormix
# @Last modified time: 2017-05-18T16:28:30+01:00
#
import scraper as ps
# Example course !
title = "Building Web Applications with Node.js and Express 4.0"
link = "https://app.pluralsight.com/player?course=nodejs-express-web-applications&author=jonathan-mills&name=nodejs-express-web-applications-m1&clip=0&mode=live"
course = ps.PluralCourse(link)
course.delay = 5 # You can change this if you feel that it's not enough.
course.launchBrowser()
course.login() # Don't forget to create a config.py and put your username & password inside it !
log = course.downloadEpisodes()
# The following part is completely useless, but I wanted to add it :3
logFile = open('log.txt','w')
logFile.write("Course : "+title+"\n")
logFile.write("*"*(9+len(title))+"\n")
for title in log.keys():
    logFile.write('# '+ title +"\n")
    for episode in log[title]:
        logFile.write('    -- '+ episode +"\n")
