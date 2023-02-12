from numpy import reciprocal
import requests
import json
import datetime
import pandas as pd
import streamlit as st

st.title('為替表示:一週間平均')

# Open Exchange RatesのAPIキーを設定
app_id = 'f982ac5b81d74f84952cb0e46639a459'

# 10日間の為替レートを取得
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=10)

url = f'https://openexchangerates.org/api/historical/{start_date.strftime("%Y-%m-%d")}.json?app_id={app_id}'

response = requests.get(url)
data = json.loads(response.text)

# 円とドルの為替レートを取得
jpy_rate = data['rates']['JPY']
usd_rate = data['rates']['USD']#ドル
uae_rate = data['rates']['AED']#ディルハム
#afn_rate = data['rates']['AFN']#アフガニ
#all_rate = data['rates']['ALL']#レク
#amd_rate = data['rates']['AMD']#ドラム
#ang_rate = data['rates']['ANG']#ギルター
aoa_rate = data['rates']['AOA']#クワンザ
ars_rate = data['rates']['ARS']#ペソ
aud_rate = data['rates']['AUD']#オーストラリアドル
#awg_rate = data['rates']['AWG']#フロリン
azn_rate = data['rates']['ARS']#アゼルバイジャン・マナト

bam_rate = data['rates']['BAM']#マルク
#bbd_rate = data['rates']['BBD']#バルバトス・ドル
bdt_rate = data['rates']['BDT']#タカ
bgn_rate = data['rates']['BGN']#レフ
bhd_rate = data['rates']['BHD']#バーレーン・ディナール
#bif_rate = data['rates']['BIF']#ブルンジ・フラン
#bmd_rate = data['rates']['BMD']#バミューダ・ドル
#bob_rate = data['rates']['BOB']#ボリビアーノ
brl_rate = data['rates']['BRL']#レアル
#bsd_rate = data['rates']['BD']#バハマ・ドル
btn_rate = data['rates']['BTN']#ニュルタム
#bwp_rate = data['rates']['BWP']#プラ
#bzd_rate = data['rates']['BZD']#ベリーズ・ドル

cad_rate = data['rates']['CAD']#カナダ・ドル
chf_rate = data['rates']['CHF']#スイス・フラン
clf_rate = data['rates']['CLF']#チリ・ペソ
cny_rate = data['rates']['CNY']#元
cop_rate = data['rates']['COP']#コロンビア・ペソ
cup_rate = data['rates']['CUP']#キューバ・ペソ
czk_rate = data['rates']['CZK']#コルナ

dkk_rate = data['rates']['DKK']#クローネ
dop_rate = data['rates']['DOP']#ドミニカ・ペソ

egp_rate = data['rates']['EGP']#エジプト・ポンド
eur_rate = data['rates']['EUR']#ユーロ

gbp_rate = data['rates']['GBP']#ポンド
ghs_rate = data['rates']['GHS']#セディ

hkd_rate = data['rates']['HKD']#香港・ドル
hrk_rate = data['rates']['HRK']#クーナ
huf_rate = data['rates']['HUF']#フォリント

idr_rate = data['rates']['IDR']#ルピア
inr_rate = data['rates']['INR']#ルピー
isk_rate = data['rates']['ISK']#アイスランド

jmd_rate = data['rates']['JMD']#ジャマイカ・ドル

khr_rate = data['rates']['KHR']#カンボジア
krw_rate = data['rates']['KRW']#韓国

lkr_rate = data['rates']['LKR']#スリランカ

mad_rate = data['rates']['MAD']#モロッコ
mga_rate = data['rates']['MGA']#マダガスカル
mnt_rate = data['rates']['MNT']#モンゴル
mop_rate = data['rates']['MOP']#マカオ
mvr_rate = data['rates']['MVR']#モルディブ
mxn_rate = data['rates']['MXN']#メキシコ
mzn_rate = data['rates']['MZN']#モザンピーク

nok_rate = data['rates']['NOK']#ノルウェー

sek_rate = data['rates']['SEK']#スウェーデン
sgd_rate = data['rates']['SGD']#シンガポール

thb_rate = data['rates']['THB']#タイ
try_rate = data['rates']['TRY']#トルコ
twd_rate = data['rates']['TWD']#スイス・フラン

vnd_rate = data['rates']['VND']#ベトナム


# 平均為替レートを計算
average_rate = usd_rate / jpy_rate
average_rate = reciprocal(average_rate)

average_rate1 = uae_rate / jpy_rate
average_rate1 = reciprocal(average_rate1)

average_rate2 = aud_rate / jpy_rate
average_rate2 = reciprocal(average_rate2)

average_rate3 = bam_rate / jpy_rate
average_rate3 = reciprocal(average_rate3)

average_rate4 = bdt_rate / jpy_rate
average_rate4 = reciprocal(average_rate4)

average_rate5 = bgn_rate / jpy_rate
average_rate5 = reciprocal(average_rate5)

average_rate6 = brl_rate / jpy_rate
average_rate6 = reciprocal(average_rate6)

average_rate7 = btn_rate / jpy_rate
average_rate7 = reciprocal(average_rate7)

#average_rate8 = byr_rate / jpy_rate
#average_rate8 = reciprocal(average_rate8)

#average_rate9 = bzd_rate / jpy_rate
#average_rate9 = reciprocal(average_rate9)

average_rate10 = cad_rate / jpy_rate
average_rate10 = reciprocal(average_rate10)

average_rate11 = chf_rate / jpy_rate
average_rate11 = reciprocal(average_rate11)

average_rate12 = cny_rate / jpy_rate
average_rate12 = reciprocal(average_rate12)

average_rate13 = cop_rate / jpy_rate
average_rate13 = reciprocal(average_rate13)

average_rate14 = cup_rate / jpy_rate
average_rate14 = reciprocal(average_rate14)

average_rate15 = cup_rate / jpy_rate
average_rate15 = reciprocal(average_rate15)

average_rate16 = czk_rate / jpy_rate
average_rate16 = reciprocal(average_rate16)

average_rate17 = dkk_rate / jpy_rate
average_rate17 = reciprocal(average_rate17)

average_rate18 = dop_rate / jpy_rate
average_rate18 = reciprocal(average_rate18)

average_rate19 = egp_rate / jpy_rate
average_rate19 = reciprocal(average_rate19)

average_rate20 = eur_rate / jpy_rate
average_rate20 = reciprocal(average_rate20)

average_rate21 = gbp_rate / jpy_rate
average_rate21 = reciprocal(average_rate21)

average_rate22 = ghs_rate / jpy_rate
average_rate22 = reciprocal(average_rate22)

average_rate23 = hkd_rate / jpy_rate
average_rate23 = reciprocal(average_rate23)

average_rate24 = hrk_rate / jpy_rate
average_rate24 = reciprocal(average_rate24)

average_rate25 = huf_rate / jpy_rate
average_rate25 = reciprocal(average_rate25)

average_rate26 = idr_rate / jpy_rate
average_rate26 = reciprocal(average_rate26)

average_rate27 = inr_rate / jpy_rate
average_rate27 = reciprocal(average_rate27)

average_rate28 = isk_rate / jpy_rate
average_rate28 = reciprocal(average_rate28)

average_rate29 = isk_rate / jpy_rate
average_rate29 = reciprocal(average_rate29)

average_rate30 = jmd_rate / jpy_rate
average_rate30 = reciprocal(average_rate30)

average_rate31 = krw_rate / jpy_rate
average_rate31 = reciprocal(average_rate31)

average_rate32 = lkr_rate / jpy_rate
average_rate32 = reciprocal(average_rate32)

average_rate33 = mvr_rate / jpy_rate
average_rate33 = reciprocal(average_rate33)

average_rate34 = mxn_rate / jpy_rate
average_rate34 = reciprocal(average_rate34)

# 結果を出力


data={'アメリカ':[average_rate],'UAE':[average_rate1],'オーストラリア':[average_rate2],
       'ボスニア・ヘルツェゴビナ':[average_rate3],'バングラデシュ':[average_rate4],'ブルガリア':[average_rate5],
       'ブラジル':[average_rate6],'ブータン':[average_rate7],'カナダ':[average_rate10],
       'スイス':[average_rate11],'中国':[average_rate12],'コロンビア':[average_rate14],
       'キューバチェコ':[average_rate14],'チェコ':[average_rate16],'デンマーク':[average_rate17],}
df = pd.DataFrame.from_dict(data)
st.write(df)
