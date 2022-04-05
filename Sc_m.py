import datetime     ## 오늘 날짜를 구하기 위해 사용
from neispy import Neispy
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

T_day = str(datetime.datetime.now())        # 오늘 날짜를 구함

D_day = T_day[:4] + T_day[5:7] + T_day[8:10]       # 오늘 날짜를 바탕으로 "년월일" 을 구함
DD_day = T_day[:10]         # 오늘 날짜를 바탕으로 "년-월-일" 을 구함

W_day = ["월", "화", "수", "목" ,"금"]      # datetime 모듈을 이용하여 숫자로 구한 요일을 텍스트 형테로 변환
WN_day = datetime.datetime.today().weekday()    # datetime 모듈을 이용하여 오늘의 요일을 숫자로 구함

name = "성일고등학교"

neis = Neispy.sync()

print(dir(neis))

scinfo = neis.schoolInfo(SCHUL_NM=name)     # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
AE = scinfo[0].ATPT_OFCDC_SC_CODE       # 교육청코드
SE = scinfo[0].SD_SCHUL_CODE        # 학교코드

scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=D_day)         # 학교코드와 교육청 코드로 2022년 04월 01일의 급식 정보 요청
meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

current = datetime.datetime.now()       # 오늘 날짜를 구함
tomorrow = current + datetime.timedelta(days=1)     # 내일 날짜를 구함
s_tm = str(tomorrow)        #str형태로 변경
ST_day = s_tm[:4] + s_tm[5:7] + s_tm[8:10]      # 오늘 날짜를 "년월일" 형태로 구함
STT_day = s_tm[:10]     # 오늘 날짜를 "년-월-일" 형태로 구함


W2_day = ["화", "수", "목", "금" ,"월"]      # datetime 모듈을 이용하여 숫자로 구한 요일을 텍스트 형테로 변환
WN2_day = datetime.datetime.today().weekday()    # datetime 모듈을 이용하여 오늘의 요일을 숫자로 구함

name = "성일고등학교"

neis = Neispy.sync()

print(dir(neis))

scinfo = neis.schoolInfo(SCHUL_NM=name)     # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
AE = scinfo[0].ATPT_OFCDC_SC_CODE       # 교육청코드
SE = scinfo[0].SD_SCHUL_CODE        # 학교코드

scmeal_2 = neis.mealServiceDietInfo(AE, SE, MLSV_FROM_YMD=ST_day)
meal_2 = scmeal_2[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

# print("[ 성일정보고등학교 급식 ]"+"\n"+DD_day+" ("+(W_day[WN_day])+")\n[중식]")
# print(meal)

## 텔레그램 봇
token = "5151400483:AAHtsEuBlBF64ccaQiYf4-4Yceov0BFmIhM"
M_1 = "5271328836"
M_2 = "5174190629"

# for i in bot.getUpdates():    CHAT_ID
#     print(i.message)          CHAT_ID
 
bot = telegram.Bot(token)
 
# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
 

def handler(update, context):
    """
    사용자가 보낸 메세지를 읽어들이고, 답장을 보내는 함수입니다.
    """
    # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    user_text = update.message.text

    # 사용자가 보낸 메세지가 "오늘급식"일 경우
    if user_text == "오늘급식": 
        bot.send_message(chat_id=M_2, text="[ 성일정보고등학교 급식 ]"+"\n"+DD_day+" ("+(W_day[WN_day])+")\n[중식]\n"+meal)
#         bot.send_message(chat_id=M_2, text="[ 성일정보고등학교 급식 ]"+"\n"+DD_day+" ("+(W_day[WN_day])+")\n[중식]\n"+meal)
    
    # 사용자가 보낸 메세지가 "내일급식"일 경우
    elif user_text == "내일급식":
        bot.send_message(chat_id=M_2, text="[ 성일정보고등학교 급식 ]"+"\n"+STT_day+" ("+(W2_day[WN2_day])+")\n[중식]\n"+meal_2)
#         bot.send_message(chat_id=M_2, text="[ 성일정보고등학교 급식 ]"+"\n"+STT_day+" ("+(W2_day[WN2_day])+")\n[중식]\n"+meal_2)

    elif user_text == "!오늘급식":
        bot.send_message(chat_id=M_1, text="[ 성일정보고등학교 급식 ]"+"\n"+DD_day+" ("+(W_day[WN_day])+")\n[중식]\n"+meal)
 
    elif user_text == "!내일급식":
        bot.send_message(chat_id=M_1, text="[ 성일정보고등학교 급식 ]"+"\n"+STT_day+" ("+(W2_day[WN2_day])+")\n[중식]\n"+meal_2)
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

