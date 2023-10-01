import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tyson = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Frank Bruno', url='https://www.youtube.com/watch?v=Rxeyq3cvudY&t=484s')],
[InlineKeyboardButton(text='Trevor Berbick', url='https://www.youtube.com/watch?v=QKFhSnX9LzM')],
[InlineKeyboardButton(text='Mitch Green', url='https://www.youtube.com/watch?v=R31ybJBXWcA')],
[InlineKeyboardButton(text='Tony Tucker', url='https://www.youtube.com/watch?v=hPengw-N_j4')],
[InlineKeyboardButton(text='Lennox Lewis ', url='https://www.youtube.com/watch?v=Vewmp2JigcQ')],
[InlineKeyboardButton(text='Buster Douglas', url='https://www.youtube.com/watch?v=OmRv6HWpmgE')],
[InlineKeyboardButton(text='Evander Holyfield 1', url='https://www.youtube.com/watch?v=F4HXeZi2t3Q')],
[InlineKeyboardButton(text='Evander Holyfield 2', url='https://www.youtube.com/watch?v=Ak3rYm-faZc')],
[InlineKeyboardButton(text='Tyrell Biggs ', url='https://www.youtube.com/watch?v=Bd_gMw4LjFc')],
[InlineKeyboardButton(text='Danny Williams', url='https://www.youtube.com/watch?v=I6WCLselSVU')]])


sugar = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Thomas Hearns 1', url='https://www.youtube.com/watch?v=jZ-7SIpdgfI')],
[InlineKeyboardButton(text='Thomas Hearns 2',url='https://www.youtube.com/watch?v=PY1aIAEpUUg')],
[InlineKeyboardButton(text='Marvin Hagler', url='https://www.youtube.com/watch?v=lko_QAxKcc0')],
[InlineKeyboardButton(text='Roberto Duran', url='https://www.youtube.com/watch?v=ZuGZVkYuHM4')],
[InlineKeyboardButton(text='Ayub Kalule', url='https://www.youtube.com/watch?v=Rk0qRD7N59I')],
[InlineKeyboardButton(text='Wilfred Benitez ', url='https://www.youtube.com/watch?v=ejyQTgB9fYI')],
[InlineKeyboardButton(text='Marcos Geraldo', url='https://www.youtube.com/watch?v=sYvbZtPUovY')],
[InlineKeyboardButton(text='Davey Boy Green', url='https://www.youtube.com/watch?v=Tku9I-duCQE')],
[InlineKeyboardButton(text='Frank Santore', url='https://www.youtube.com/watch?v=viNeDicKCiU')],
[InlineKeyboardButton(text='Larry Bonds', url='https://www.youtube.com/watch?v=JHItQT51Ij0')]])



ali = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='George Foreman', url='https://www.youtube.com/watch?v=55AasOJZzDE')],
[InlineKeyboardButton(text='Zora Folley', url='https://www.youtube.com/watch?v=VFFDe9FQL3s')],
[InlineKeyboardButton(text='Joe Frazier 1', url='https://www.youtube.com/watch?v=eIm2eK5uuVA')],
[InlineKeyboardButton(text='Joe Frazier 2', url='https://www.youtube.com/watch?v=NEjaAiNWv24')],
[InlineKeyboardButton(text='Larry Holmes', url='https://www.youtube.com/watch?v=23vQICdr1M8')],
[InlineKeyboardButton(text='Jimmy Ellis', url='https://www.youtube.com/watch?v=tq0ofSlssUI&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=20')],
[InlineKeyboardButton(text='Mac Foster', url='https://www.youtube.com/watch?v=X9e7NduxFjA&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=23')],
[InlineKeyboardButton(text='Alvin Lewis', url='https://www.youtube.com/watch?v=K0z0BmpA_h0&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=26')],
[InlineKeyboardButton(text='Ken Norton 1', url='https://www.youtube.com/watch?v=vbYtHaduVZ8&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=30')],
[InlineKeyboardButton(text='Ken Norton 2', url='https://www.youtube.com/watch?v=TfxGUbAMrNQ&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=31')]])


marciano = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Jersey Joe Walcott 1', url='https://www.youtube.com/watch?v=TPKFt4Y7UaQ')],
[InlineKeyboardButton(text='Archie Moore', url='https://www.youtube.com/watch?v=k1xaQI6njJ0')],
[InlineKeyboardButton(text='Joe Louis ', url='https://www.youtube.com/watch?v=wXBhbmrCo5M&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=4')],
[InlineKeyboardButton(text='Ezzard Charles', url='https://www.youtube.com/watch?v=HnvtDcpPpMI&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=10')],
[InlineKeyboardButton(text='Roland La Starza 1', url='https://www.youtube.com/watch?v=wDbNLDVSkR4&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=3')],
[InlineKeyboardButton(text='Roland La Starza 2', url='https://www.youtube.com/watch?v=6qccyxaTeK0&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=9')],
[InlineKeyboardButton(text='Jersey Joe Walcott 2', url='https://www.youtube.com/watch?v=uYP7OkjzHiQ&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=11')],
[InlineKeyboardButton(text='Harry Mathews', url='https://www.youtube.com/watch?v=a1IOPl_8iWQ&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=13')],
[InlineKeyboardButton(text='Rex Layne', url='https://www.youtube.com/watch?v=4Cnl87BZOvU')],
[InlineKeyboardButton(text='Don Cockell', url='https://www.youtube.com/watch?v=Q9P6ZWoymT8')]])


mayweather = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Oscar De La Hoya', url='https://www.youtube.com/watch?v=PiQhc9jEq2s')],
[InlineKeyboardButton(text='Manny Pacquiao', url='https://www.youtube.com/watch?v=39zhhfMGNRk&t=2s')],
[InlineKeyboardButton(text='Marcos Maidana 1', url='https://www.youtube.com/watch?v=KYvOC7MBuUw&t=2s')],
[InlineKeyboardButton(text='Manuel Marquez', url='https://www.youtube.com/watch?v=3DpkVOvuA0Y&t=1s')],
[InlineKeyboardButton(text='Marcos Maidana 2', url='https://www.youtube.com/watch?v=mysd0uyNo7M')],
[InlineKeyboardButton(text='Miguel Cotto ', url='https://www.youtube.com/watch?v=fKiGQfpupRA')],
[InlineKeyboardButton(text='Arturo Gatti', url='https://www.youtube.com/watch?v=THojnKPFpFA&t=164s')],
[InlineKeyboardButton(text='Henry Bruseles', url='https://www.youtube.com/watch?v=7aVc0nFcEVE&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=31')],
[InlineKeyboardButton(text='Sharmba Mitchell', url='https://www.youtube.com/watch?v=Q8Vo_bJZCCg&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=33')],
[InlineKeyboardButton(text='Ricky Hatton', url='https://www.youtube.com/watch?v=sHN6sdhhO38&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=37')]])



hearns = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Randy Shields', url='https://www.youtube.com/watch?v=kGz6xsEBCR8')],
[InlineKeyboardButton(text='Mike Colbert', url='https://www.youtube.com/watch?v=WSZgg7ax4DQ&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=6')],
[InlineKeyboardButton(text='Ernie Singletary', url='https://www.youtube.com/watch?v=E2HVza7MPyQ&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=15')],
[InlineKeyboardButton(text='Jeff McCracken', url='https://www.youtube.com/watch?v=uHPbAUyl2wg&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=17')],
[InlineKeyboardButton(text='Murray Sutherland', url='https://www.youtube.com/watch?v=l5B_JtZS6zE&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=18')],
[InlineKeyboardButton(text='Luigi Minchillo ', url='https://www.youtube.com/watch?v=N7ebobBtXec&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=19')],
[InlineKeyboardButton(text='Mark Medal', url='https://www.youtube.com/watch?v=evvP0ftE3tA&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=20')],
[InlineKeyboardButton(text='Dennis Andries', url='https://www.youtube.com/watch?v=h5Rwj7AKA54&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=21')],
[InlineKeyboardButton(text='Sugar Ray 1', url='https://www.youtube.com/watch?v=jZ-7SIpdgfI')],
[InlineKeyboardButton(text='Sugar Ray 2',url='https://www.youtube.com/watch?v=PY1aIAEpUUg')]])


jones = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Julio Cesar', url='https://www.youtube.com/watch?v=EgOmrlWYotk')],
[InlineKeyboardButton(text='Bernard Hopkins 2', url='https://www.youtube.com/watch?v=0gG37BOcX1Y')],
[InlineKeyboardButton(text='Bernard Hopkins 1', url='https://www.youtube.com/watch?v=uE3t6BBgVpE')],
[InlineKeyboardButton(text='James Toney', url='https://www.youtube.com/watch?v=2o9edGBRIpk')],
[InlineKeyboardButton(text='Stephan Johnson', url='https://www.youtube.com/watch?v=iKT7AvS-Fss&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=2')],
[InlineKeyboardButton(text='Ron Amundsen', url='https://www.youtube.com/watch?v=IJPg_SSqTTM&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=3')],
[InlineKeyboardButton(text='Jorge Castro', url='https://www.youtube.com/watch?v=DxZzAWZ-_fQ&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=15')],
[InlineKeyboardButton(text='Mike McCallum', url='https://www.youtube.com/watch?v=qMGU8GE4AWk&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=23')],
[InlineKeyboardButton(text='Vinny Pazienza', url='https://www.youtube.com/watch?v=oLcYb3o6buE&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=21')],
[InlineKeyboardButton(text='Tony Thornton', url='https://www.youtube.com/watch?v=eyxwNHQWOK8&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=22')]])



louis = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Rocky Marciano', url='https://www.youtube.com/watch?v=wXBhbmrCo5M&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=4')],
[InlineKeyboardButton(text='Ezzard Charles', url='https://www.youtube.com/watch?v=HnvtDcpPpMI')],
[InlineKeyboardButton(text='Tony Galento', url='https://www.youtube.com/watch?v=-4GKIjOtF5g')],
[InlineKeyboardButton(text='Omelio A. (skip 10s)', url='https://www.youtube.com/watch?v=Hh2G_rjHNqc&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=3')],
[InlineKeyboardButton(text='James Braddock', url='https://www.youtube.com/watch?v=LNfHZF5GoUg&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=4')],
[InlineKeyboardButton(text='Arturo Godoy', url='https://www.youtube.com/watch?v=M5AVLku4VRI&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=14')],
[InlineKeyboardButton(text='Max Schmeling', url='https://www.youtube.com/watch?v=igoidtPyy6g&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=15')],
[InlineKeyboardButton(text='Billy Conn', url='https://www.youtube.com/watch?v=Li4gwjT2Ibs')],
[InlineKeyboardButton(text='Max Baer', url='https://www.youtube.com/watch?v=2aaebPmnx7E')],
[InlineKeyboardButton(text='Primo Carnera', url='https://www.youtube.com/watch?v=ls8a5ybJRHg')]])




foreman = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Muhammad ali', url='https://www.youtube.com/watch?v=55AasOJZzDE')],
[InlineKeyboardButton(text='Ron Lyle', url='https://www.youtube.com/watch?v=l8AVcEyyMco')],
[InlineKeyboardButton(text='Tommy Morrison', url='https://www.youtube.com/watch?v=GKF9V9C21K4')],
[InlineKeyboardButton(text='Ken Norton', url='https://www.youtube.com/watch?v=QDXY3wMkyuc&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=12')],
[InlineKeyboardButton(text='Joe Frazier 1', url='https://www.youtube.com/watch?v=EtacibssAPg&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=10')],
[InlineKeyboardButton(text='Joe Frazier 2', url='https://www.youtube.com/watch?v=3NmvPRP6NlA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=15')],
[InlineKeyboardButton(text='John Denis', url='https://www.youtube.com/watch?v=RFYMp4neZ98&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=16')],
[InlineKeyboardButton(text='Mark Young', url='https://www.youtube.com/watch?v=pdnwMayOjuA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=25')],
[InlineKeyboardButton(text='Everett Martin', url='https://www.youtube.com/watch?v=susaIBTYcSo&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=27')],
[InlineKeyboardButton(text='Lou SAVARESE', url='https://www.youtube.com/watch?v=W6tD24FlfJw&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=34')]])

frazier = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Floyd Cummings', url='https://www.youtube.com/watch?v=pG_vN9w0_8I&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=17')],
[InlineKeyboardButton(text='Muhammad Ali 1', url='https://www.youtube.com/watch?v=eIm2eK5uuVA')],
[InlineKeyboardButton(text='Muhammad Ali 2', url='https://www.youtube.com/watch?v=NEjaAiNWv24')],
[InlineKeyboardButton(text='Muhammad Ali 3', url='https://www.youtube.com/watch?v=olp9gsmD_A0')],
[InlineKeyboardButton(text='George Foreman 1', url='https://www.youtube.com/watch?v=EtacibssAPg&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=10')],
[InlineKeyboardButton(text='George Foreman 2', url='https://www.youtube.com/watch?v=3NmvPRP6NlA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=15')],
[InlineKeyboardButton(text='Ron Stander', url='https://www.youtube.com/watch?v=1CkmiKle4qs')],
[InlineKeyboardButton(text='Oscar Bonavena', url='https://www.youtube.com/watch?v=TTlHViwE8_4&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=2')],
[InlineKeyboardButton(text='Jerry Quarry', url='https://www.youtube.com/watch?v=fWS3ls52-r0&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=7')],
[InlineKeyboardButton(text='Eddie Machen', url='https://www.youtube.com/watch?v=94jZXt1EQ38&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=3')]])


