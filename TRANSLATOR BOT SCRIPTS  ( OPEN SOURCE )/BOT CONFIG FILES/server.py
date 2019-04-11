from bot import telegram_chatbot
import translator_script

bot = telegram_chatbot("config.cfg")

###################LANGUAGE CODE DICTIONARY HERE######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

lang_dict = {"afrikaans" : 'af' , "albania" : 'sq' , "arabic" : 'ar' , "azerbaijani" : 'az' , "basque" : 'eu' , "bengali" : 'bn' , "belarusian" : 'be' , "bulgarian" : 'bg' , "catalan" : 'ca' , "chinese-simplified" : 'zh-CN'  , "bhinese-traditional" : 'zh-TW'  , "croatian" : 'hr' , "czech" : 'cs' , "danish" : 'da'  , "dutch" : 'nl'  , "english" : 'en' , "esperanto" : 'eo' , "estonian" : 'et' , "filipino" : 'tl', "finnish" : 'fi' , "french" : 'fr' , "galician" : 'gl' , "georgian" : 'ka', "german" : 'de'  , "greek" : 'el', "gujarati" : 'gu', "haitian-creole" : 'ht' , "hebrew" : 'iw', "hindi" : 'hi' , "hungarian" : 'hu'  , "icelandic" : 'is' , "indonesian" : 'id' , "irish" : 'ga' , "italian" : 'it' , "japanese" : 'ja' , "kannada" : 'kn' , "korean" : 'ko' , "latin" : 'la' , "latvia" : 'lv' , "lithuanian" : 'lt' , "macedonian" : 'mk' , "malay" : 'ms' , "maltese" : 'mt' , "norwegian" : 'no' , "persian" : 'fa' , "polish" : 'pl' , "polishrtuguese" : 'pt' , "romanian" : 'ro' , "russian" : 'ru' , "serbian" : 'sr' , "slovak" : 'sk' , "slovenian" : 'sl' , "spanish" : 'es' , "swahili" : 'sw' , "swedish" : 'sv' , "tamil" : 'ta' , "telugu" : 'te' , "thai" : 'th' , "turkish" : 'tr' , "ukrainian" : 'uk' , "Urdu" : 'ur' , "vietnamese" : 'vi' , "welsh" : 'cy' , "yiddish" : 'yi'}

######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


###################LANGUAGE LIST DICTIONARY HERE######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

lang_list = """ **** LANGUAGE LIST ( NOT CASE SENSITIVE ) ****\n\tAlbania             \n\tArabic              \n\tAzerbaijani         \n\tBasque              \n\tBengali             \n\tBelarusian          \n\tBulgarian           \n\tCatalan             \n\tChinese-Simplified  \n\tChinese-Traditional \n\tCroatian            \n\tCzech               \n\tDanish              \n\tDutch               \n\tEnglish             \n\tEsperanto           \n\tEstonian            \n\tFilipino            \n\tFinnish             \n\tFrench              \n\tGalician            \n\tGeorgian            \n\tGerman              \n\tGreek               \n\tGujarati            \n\tHaitian-Creole      \n\tHebrew              \n\tHindi               \n\tHungarian           \n\tIcelandic           \n\tIndonesian          \n\tItalian             \n\tJapanese            \n\tKannada             \n\tKorean              \n\tLatin               \n\tLatvia              \n\tLithuanian          \n\tMacedonian          \n\tMalay               \n\tMaltese             \n\tNorwegian           \n\tPersian             \n\tPolish              \n\tPolishrtuguese      \n\tRomanian            \n\tRussian             \n\tSerbian             \n\tSlovak              \n\tSlovenian           \n\tSpanish             \n\tSwahili             \n\tSwedish             \n\tTamil               \n\tTelugu              \n\tThai                \n\tTurkish             \n\tUkrainian           \n\tUrdu                \n\tVietnamese          \n\tWelsh               \n\tYiddish"""

######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


def make_reply(msg):
    reply = None
    msg = msg.lower()
    if msg == "languages":
        reply = lang_list
        return reply
    elif msg == "/start":
        reply = '**** Welcome To Translator Bot ****,\nSend /help or click on it for help...\nSend /languages or click on it to get supported list of languages...'
        return reply
    elif msg == "/help":
        reply = """**** Welcome To Translation Bot ****\n\n1)To use the bot use following format :\n\n\tFrom_Language To_language  Data\n\t\tFor example,\n\t\tEnglish Spanish Hello there\n\n2)For recieveing supported language list, send\n\t /languages to us or click on... """
        return reply
    elif msg == "/languages":
        return lang_list

    else:
        try:
            my_list = msg.split()
            lang1 = lang_dict[my_list[0].lower()]
            lang2 = lang_dict[my_list[1].lower()]
            text = ""
            for i in range(2, len(my_list)):
                text += my_list[i] + " "
            
            reply = translator_script.text(lang1, lang2, text)
            return reply    
        
        except Exception as e:
            reply = "! ! ! ! Enter According To Format Please ! ! ! !"
            return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates['result']

    if updates:
        for item in updates[len(updates)-1:]:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            try:
                print("try")
                from_ = item["message"]["from"]["id"]
            except Exception as e:
                print("catch block")
                from_ = item["edited_message"]["from"]["id"]
            
            reply = make_reply(message)
            bot.send_message(reply, from_)
            print("STATUS : Message Sent Successfully ")
