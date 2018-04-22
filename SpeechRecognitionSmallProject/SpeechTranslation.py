#语音翻译
from win32com.client import constants
import os
import win32com.client
import pythoncom

speaker = win32com.client.Dispatch("SAPI.SPVOICE")


class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("You are talking to ", newResult.PhraseInfo.GetText())
        speechstr=newResult.PhraseInfo.GetText()
        if  speechstr=="张三":
            speaker.Speak("zhaodahai  love  fengjie")
        elif  speechstr=="你好":
            speaker.Speak("hello world")
        elif  speechstr=="国庆快乐":
            speaker.Speak("Happy   nationalday")
        elif  speechstr=="新年快乐":
            speaker.Speak("happy  New Year")
        elif  speechstr=="李四":
            speaker.Speak("a  beauty baby")
        elif  speechstr=="王五":
            speaker.Speak("a  little boy")
        elif  speechstr=="彭大":
            speaker.Speak("a  boy  can  coding")
        elif  speechstr=="马剑":
            speaker.Speak("shit,  horse")
        elif  speechstr=="孟六":
            speaker.Speak("go go  go")
        elif  speechstr=="徐二":
                speaker.Speak("a  boy  in the  sky")
        elif  speechstr=="陈小":
            speaker.Speak("strong  man  ")
        else:
            pass

if __name__ == '__main__':

    speaker.Speak("Speech recognition Open")
    wordsToAdd = ["张三",
                  "你好",
                  "国庆快乐",
                  "新年快乐",
                  "王五",
                  "李四",
                  "彭大",
                  "马剑",
                  "孟六"  ,
                   "徐二",
                  "陈小"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
