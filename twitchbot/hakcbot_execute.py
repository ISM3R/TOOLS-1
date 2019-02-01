#!/usr/bin/python3


import re
import threading
from config import *
import time

uList = []

class Execute:
    def __init__(self, Hakcbot):
        self.Hakcbot = Hakcbot
        self.regusr = r'yourmom\((.*?)\)'
        self.regusr3 = r'yourmum\((.*?)\)'
        self.regflag = r'flag\((.*?)\)'
        self.regunflag = r'flag\((.*?)\)'
        
        self.hakcinfo = True
        self.hakccommands = True
        self.hakcyoutube = True
        self.hakcdiscord = True
        self.hakcgithub = True
        self.hakcsub = True
        self.hakctime = True
        self.hakcyourmom = True
        self.hakcyourmum = True
                
    def Main(self, line):
        self.line = line
        command = None
        try:     
            self.format_line()
            try:
                command, CD = self.Comms()
            except Exception:
                pass
            
            if ('hakcbot()' in self.msg and self.hakcinfo == True):
                command, CD = self.HakcbotInfo()
            elif ('commands()' in self.msg and self.hakccommands == True):
                command, CD = self.Commands()
            elif ('youtube()' in self.msg and self.hakcyoutube == True):
                command, CD = self.Youtube()
            elif ('discord()' in self.msg and self.hakcdiscord == True):
                command, CD = self.Discord() 
            elif ('github()' in self.msg and self.hakcgithub == True):
               command, CD =  self.Github()
            elif ('sub()' in self.msg and self.hakcgithub == True):
               command, CD =  self.Sub()            
            elif ('time()' in self.msg and self.hakctime == True):
               command, CD =  self.Time()
            
            if (command):
                threading.Thread(target=self.Cooldown, args=(command, CD)).start()
            else:
                pass           
        except Exception as E:
            pass

                                               
    def HakcbotInfo(self):
        message = 'I will be finishing this bot later on stream'
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakcinfo', 180)
                      
    def Commands(self):
        message = '<c> playlist() > music. - discord() > discord link - github() > github link - parrot() > why I use parrot - sub() > subscirbe link - commands() > command list :D </c>'
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakccommands', 180)
    
    def Youtube(self):
        message = "Check out DOWRIGHT's YouTube here: https://www.youtube.com/channel/UCKAiTcsiD50oZvf9h0xbvCg"
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakcyoutube', 180)
        
    def Discord(self):
        message = 'Join the Discord --> https://Discord.gg/KSCHNfa'
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakcdiscord', 180)
        
    def Github(self):
        message = "Check out DOWRIGHT's GitHub here: https://github.com/DOWRIGHTTV/TOOLS"
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakcgithub', 180)

    def Sub(self):
        message = "Subscribe to DOWRIGHT here: https://www.twitch.tv/subs/dowright"
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakcsub', 180)        
                            
    def Time(self):
        current_time = time.localtime()
        time.strftime('%Y-%m-%d %A', current_time)
        message = "DOWRIGHT's time is {}".format(time.strftime('%H:%M:%S', current_time))
        self.sendMessage(message)
        print('hakcbot: {}'.format(message))
        return('hakctime', 300)

    def Comms(self):
#        if(self.user in modList):
        if (self.user == 'dowright'):
            if ('unflag(' in self.msg):
                if ('!' in self.msg or '/' in self.msg or '.' in self.msg or ' ' in self.msg):
                    pass
                else:
                    self.arG = re.findall(self.regunflag, self.msg)[0]
                    uList.remove('{}'.format(self.arG))
                    print('Unflagged {}'.format(self.arG))
                    
            elif ('flag(' in self.msg):
                if ('!' in self.msg or '/' in self.msg or '.' in self.msg or ' ' in self.msg):
                    pass
                else:
                    self.arG = re.findall(self.regflag, self.msg)[0]
                    uList.append(self.arG)
                    print('Flagged {}'.format(self.arG))
        else:
            pass
            
        for user in uList:
            if (user == self.user):
                message = 'lol, {} iz a nerd'.format(user)
                self.sendMessage(message)
                print('hakcbot: {}'.format(message))
              
        if ('yourmom(' in self.msg and self.hakcyourmom == True):
            if ('!' in self.msg or '/' in self.msg or '.' in self.msg or ' ' in self.msg):
                pass
            else:    
                self.arG = re.findall(self.regusr, self.msg)[0]
                message = "{}'s mom goes to college".format(self.arG)
                self.sendMessage(message)
                print('hakcbot: {}'.format(message))
                return('hakcyourmom', 360)

        elif ('yourmum(' in self.msg and self.hakcyourmum == True):
            if ('!' in self.msg or '/' in self.msg or '.' in self.msg or ' ' in self.msg):
                pass
            else:    
                self.arG = re.findall(self.regusr3, self.msg)[0]
                message = "{}'s mum goes to college".format(self.arG)
                self.sendMessage(message)
                print('hakcbot: {}'.format(message))
                return('hakcyourmum', 360)  
                           
    def sendMessage(self, message):
        mT = 'PRIVMSG #{} :{}'.format(CHANNEL, message)
        self.Hakcbot.s.send('{}\r\n'.format(mT).encode("utf-8"))
        
    def format_line(self):
        try:
            line = self.line.split(':', 2)
            user = line[1].split('!')
            self.user = user[0]
            self.msg = line[2]
            print('{}: {}'.format(self.user, self.msg))
        except Exception:
            raise Exception('Format Line Error')

    def Cooldown(self, command, CD):
        print('Putting {} on cooldown'.format(command))
        setattr(self, command, False)
        time.sleep(CD)
        print("Removing {}'s cooldown".format(command))
        setattr(self, command, True)
