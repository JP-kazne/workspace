n = 498934084350094415783044823223130007435556803301613073259727203199325937230080661117917023582579699673759861892703348357714077684549303787581429366922208568924252052118455313229534699860304480039147103608782140303489222166267907007839021544433148286217133494762766492655602977085105487216032806292874190551319
e = 134901827939710543990222584187396847806193644190423846456160711527109836908087675183249532946675670587286594441908191054495871501233678465783530503352727362726294270065122447852357566161748618195216611965946646411519602447104878893524856862722902833460104389620397589021732407447981724307130484482495521398799
c = 100132888193232309251839777842498074992587507373917163874335385921940537055226546911990198769720313749286675018486390873216490470403470144298153410686092752282228631590006943913867497072931343354481759219425807850047083814816718302223434388744485547550941814186146959750515114700335721173624212499886218608818

from Crypto.Util.number import *

c_fracs = continued_fraction(e / n).convergents()

test_plain = int.from_bytes("hoge".encode('utf-8'), 'big') 
test_cipher = pow(test_plain, e, n)

for i in range(len(c_fracs)):
    if pow(test_cipher, c_fracs[i].denom(), n) == test_plain:
        d = c_fracs[i].denom()
        break

plain = pow(c, d, n)

print(long_to_bytes(plain))
# we get
# b'e=2,c=9019127052844164572606928250741960583163943438936945828390420331200602392329'

e = 2
c = 9019127052844164572606928250741960583163943438936945828390420331200602392329

print(long_to_bytes(c^(1/e)))