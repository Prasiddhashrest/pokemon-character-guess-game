"""Generate small, original vector character-inspired portraits (no external downloads).

Run from the repository root: python scripts/generate_character_art.py
"""
from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1] / 'static' / 'characters'
OUTPUT.mkdir(parents=True, exist_ok=True)


def svg(content, bg1='#5141a0', bg2='#261d54'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" role="img">
  <defs><radialGradient id="bg"><stop stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></radialGradient></defs>
  <circle cx="150" cy="150" r="139" fill="url(#bg)"/>
  <circle cx="150" cy="150" r="125" fill="none" stroke="#ffffff" stroke-opacity=".16" stroke-width="3"/>
  {content}
</svg>'''


def head(fill='#f5bd91'):
    return f'<ellipse cx="150" cy="151" rx="60" ry="72" fill="{fill}"/>'


def plumber(cap, letter):
    return svg(f'''
    <path d="M71 267Q66 211 104 202H198Q234 209 234 267Z" fill="#3565ce"/>
    <path d="M100 212l18 51m81-51-18 51" fill="none" stroke="#a4cbff" stroke-width="14"/>
    {head()}
    <ellipse cx="90" cy="165" rx="16" ry="24" fill="#3c2523"/>
    <ellipse cx="210" cy="165" rx="16" ry="24" fill="#3c2523"/>
    <path d="M84 115Q77 70 150 69Q218 71 218 117Z" fill="{cap}"/>
    <ellipse cx="150" cy="116" rx="89" ry="17" fill="{cap}"/>
    <circle cx="151" cy="89" r="21" fill="white"/>
    <text x="151" y="98" text-anchor="middle" font-family="Arial" font-size="27" font-weight="900" fill="{cap}">{letter}</text>
    <ellipse cx="130" cy="152" rx="8" ry="13" fill="#1c2340"/>
    <ellipse cx="171" cy="152" rx="8" ry="13" fill="#1c2340"/>
    <ellipse cx="150" cy="176" rx="17" ry="15" fill="#e8a475"/>
    <path d="M111 188Q123 165 150 190Q178 165 189 188Q182 206 150 198Q120 206 111 188Z" fill="#322026"/>
    ''', '#6d63a7' if letter == 'M' else '#3b8b75')


def sonic():
    return svg('''
    <path d="M90 115L56 71L109 81L124 35L158 72L205 42L202 103L241 86L211 143L234 195L185 188L151 232L112 209L61 228L87 174L51 149Z" fill="#2184df"/>
    <path d="M104 127Q106 96 149 120Q200 96 202 127L188 176L127 181Z" fill="#f0e9d7"/>
    <ellipse cx="132" cy="133" rx="17" ry="27" fill="#fff"/><ellipse cx="168" cy="133" rx="17" ry="27" fill="#fff"/>
    <ellipse cx="138" cy="140" rx="6" ry="12" fill="#203557"/><ellipse cx="163" cy="140" rx="6" ry="12" fill="#203557"/>
    <ellipse cx="152" cy="165" rx="15" ry="9" fill="#1a283b"/>
    <path d="M126 189Q155 207 179 181" stroke="#1a283b" stroke-width="5" fill="none" stroke-linecap="round"/>
    ''', '#349fc2')


def elsa():
    return svg('''
    <path d="M75 260Q79 201 115 201H188Q229 203 233 260Z" fill="#84d9ed"/>
    <path d="M96 152Q66 86 109 60Q156 23 202 72Q241 122 204 189L181 217L104 194Z" fill="#f4e1a2"/>
    <path d="M101 156Q80 108 120 91L188 93Q220 126 199 171L187 197Q158 231 121 201Z" fill="#f8dbca"/>
    <path d="M89 118Q105 57 149 64Q200 60 206 113Q168 80 140 97Q124 123 89 118Z" fill="#fff2c8"/>
    <path d="M200 126Q232 165 200 205L223 227L211 238L187 210" fill="none" stroke="#fff1b2" stroke-width="22"/>
    <ellipse cx="128" cy="154" rx="7" ry="10" fill="#44698a"/><ellipse cx="170" cy="154" rx="7" ry="10" fill="#44698a"/>
    <path d="M140 187Q150 192 161 187" stroke="#d46f8c" fill="none" stroke-width="4" stroke-linecap="round"/>
    <path d="M64 71l9 16m-9 0 9-16m-17 8h34M230 63l8 15m-8 0 8-15m-18 8h37" stroke="#e4fbff" stroke-width="3"/>
    ''', '#68b8d3', '#234968')


def shrek():
    return svg('''
    <path d="M79 265Q87 207 125 199H185Q224 207 228 265Z" fill="#e6e0be"/>
    <path d="M90 227L112 202L192 202L213 227L195 267H109Z" fill="#7b523e"/>
    <path d="M103 125Q51 78 67 64Q85 51 123 112M199 125Q249 78 231 64Q216 52 179 111" fill="#7aaa4d" stroke="#679c42" stroke-width="9" stroke-linecap="round"/>
    <ellipse cx="150" cy="148" rx="70" ry="74" fill="#8bb751"/>
    <path d="M99 153Q117 146 134 157M164 157Q181 146 199 153" stroke="#4b7431" stroke-width="8" fill="none"/>
    <circle cx="122" cy="148" r="7" fill="#293828"/><circle cx="179" cy="148" r="7" fill="#293828"/>
    <ellipse cx="150" cy="175" rx="24" ry="19" fill="#7faa45"/>
    <path d="M129 197Q149 212 174 196" stroke="#4a6a32" stroke-width="5" fill="none" stroke-linecap="round"/>
    ''', '#83aa4f', '#283f3d')


def hermione():
    return svg('''
    <path d="M70 255Q76 205 114 194H189Q231 209 237 255Z" fill="#262c4a"/>
    <path d="M79 111Q72 37 150 49Q223 38 225 112L236 215L202 227L97 231L64 211Z" fill="#5d362f"/>
    <ellipse cx="151" cy="143" rx="61" ry="72" fill="#efd0ad"/>
    <path d="M91 120Q82 60 153 62Q211 65 210 126L179 98L151 110L114 93Z" fill="#714435"/>
    <path d="M79 150l-12 32 22 13-16 32m138-87 14 42-19 14 16 36" fill="none" stroke="#815043" stroke-width="19"/>
    <circle cx="126" cy="147" r="6" fill="#392a36"/><circle cx="174" cy="147" r="6" fill="#392a36"/>
    <path d="M134 184Q150 194 165 184" stroke="#a96962" stroke-width="4" fill="none"/>
    <path d="M103 214l42 43 49-43" fill="none" stroke="#aa324b" stroke-width="15"/>
    <path d="M130 231v40" stroke="#f5d6a4" stroke-width="9"/>
    <rect x="188" y="207" width="39" height="54" rx="3" fill="#ae8c62" transform="rotate(-16 188 207)"/>
    ''', '#845f9d')


def spongebob():
    return svg('''
    <rect x="82" y="47" width="141" height="174" rx="15" fill="#ffe45d" stroke="#e7bb40" stroke-width="5"/>
    <circle cx="103" cy="75" r="10" fill="#efcb43"/><circle cx="196" cy="98" r="9" fill="#efcb43"/><circle cx="108" cy="189" r="9" fill="#efcb43"/>
    <ellipse cx="124" cy="127" rx="26" ry="30" fill="white"/><ellipse cx="173" cy="127" rx="26" ry="30" fill="white"/>
    <circle cx="130" cy="133" r="10" fill="#3caade"/><circle cx="171" cy="133" r="10" fill="#3caade"/>
    <circle cx="131" cy="133" r="5" fill="#15191a"/><circle cx="170" cy="133" r="5" fill="#15191a"/>
    <path d="M113 168Q150 209 190 166" fill="#923e48" stroke="#7a3e49" stroke-width="3"/>
    <path d="M135 184v18h16v-17h14v17h14v-19" fill="white"/>
    <rect x="83" y="218" width="140" height="18" fill="white"/><rect x="83" y="236" width="140" height="17" fill="#965e39"/>
    <path d="M145 221l-10 12 12 13-8 22h22l-8-22 12-13-10-12Z" fill="#d63d45"/>
    ''', '#61b6d0', '#164c77')


def batman():
    return svg('''
    <path d="M45 266Q50 202 105 197L196 197Q244 210 255 266Z" fill="#222a37"/>
    <path d="M100 105L91 39L128 66Q152 56 178 66L207 39L197 114Q219 163 188 205H111Q78 161 100 105Z" fill="#171c29"/>
    <path d="M112 150L142 157L131 168L112 165m76-15-30 7 11 11 19-3" fill="#e7f1fe"/>
    <path d="M121 179Q151 191 180 179L170 205H132Z" fill="#dfb799"/>
    <ellipse cx="150" cy="234" rx="39" ry="18" fill="#b0a34c"/>
    <path d="M115 236l15-10 13 8 7-15 7 15 13-8 15 10-25 3-10 13-10-13Z" fill="#1c2639"/>
    ''', '#575a78', '#131b2d')


def spiderman():
    return svg('''
    <path d="M62 266Q71 212 110 199H191Q236 211 242 266Z" fill="#d93649"/>
    <path d="M80 263l25-38 35 38m82 0-27-38-35 38" fill="#226bbd"/>
    <ellipse cx="150" cy="135" rx="68" ry="81" fill="#d72f41" stroke="#961d36" stroke-width="6"/>
    <path d="M150 60v152M94 112h113M84 155h134M110 77Q145 116 102 189m92-111q-46 37 5 111M88 94Q150 115 210 94M83 177Q150 155 217 177" fill="none" stroke="#722439" stroke-width="2.5"/>
    <path d="M96 133Q115 127 143 146Q125 170 103 162Z" fill="white" stroke="#24272f" stroke-width="6"/>
    <path d="M204 133Q184 127 158 146Q176 170 198 162Z" fill="white" stroke="#24272f" stroke-width="6"/>
    ''', '#b84b67', '#35254c')


def vader():
    return svg('''
    <path d="M57 268Q60 218 100 197H200Q242 219 247 268Z" fill="#151824"/>
    <path d="M82 144Q78 53 149 50Q224 52 216 148L196 214H102Z" fill="#252c3b" stroke="#111722" stroke-width="8"/>
    <path d="M91 132Q112 102 150 115Q189 102 207 132L183 155H113Z" fill="#5e6c7e"/>
    <path d="M112 141l29 6-14 20H102Zm76 0-29 6 14 20h25Z" fill="#0a101b"/>
    <path d="M143 161h15l17 37-25 25-25-25Z" fill="#0e131c" stroke="#758395" stroke-width="5"/>
    <path d="M130 197h41M139 204h23M149 171v54" stroke="#758395" stroke-width="4"/>
    <path d="M82 126l-15 75 42 21m105-96 15 75-42 21" fill="none" stroke="#151924" stroke-width="14"/>
    ''', '#6d5365', '#131423')


def naruto():
    return svg('''
    <path d="M71 267Q74 210 112 196H191Q227 208 238 267Z" fill="#e47b2f"/>
    <path d="M98 219l52 41 48-41" stroke="#1d253d" stroke-width="13" fill="none"/>
    <path d="M78 104L61 74L99 82L106 41L129 70L152 29L170 67L203 42L205 84L239 72L222 111Z" fill="#f4cc43"/>
    {head('#ecc39b')}
    <path d="M95 108h114v31H95Z" fill="#252e47"/>
    <rect x="122" y="110" width="57" height="27" rx="5" fill="#a6bac9"/>
    <path d="M136 122q14-14 28 0l-9 6" fill="none" stroke="#485b69" stroke-width="3"/>
    <ellipse cx="125" cy="160" rx="7" ry="7" fill="#33659b"/><ellipse cx="176" cy="160" rx="7" ry="7" fill="#33659b"/>
    <path d="M93 176l25 6m-25 8 25 1m88-15-25 6m25 8-25 1" stroke="#98633f" stroke-width="3"/>
    <path d="M135 200Q150 210 166 200" fill="none" stroke="#ac685c" stroke-width="4"/>
    ''', '#c88758')


def kirby():
    return svg('''
    <ellipse cx="103" cy="230" rx="36" ry="22" transform="rotate(-26 103 230)" fill="#d84e78"/>
    <ellipse cx="201" cy="230" rx="36" ry="22" transform="rotate(26 201 230)" fill="#d84e78"/>
    <circle cx="152" cy="145" r="82" fill="#ffa2c0" stroke="#f080a8" stroke-width="5"/>
    <ellipse cx="120" cy="136" rx="10" ry="24" fill="#243b68"/><ellipse cx="167" cy="136" rx="10" ry="24" fill="#243b68"/>
    <ellipse cx="122" cy="128" rx="4" ry="11" fill="white"/><ellipse cx="169" cy="128" rx="4" ry="11" fill="white"/>
    <ellipse cx="96" cy="175" rx="20" ry="10" fill="#f478a6"/><ellipse cx="198" cy="175" rx="20" ry="10" fill="#f478a6"/>
    <path d="M139 171Q151 187 165 171Z" fill="#b53d72"/>
    ''', '#c786bb', '#4f376f')


ART = {
    'mario': plumber('#d83248', 'M'),
    'luigi': plumber('#36a966', 'L'),
    'sonic': sonic(),
    'elsa': elsa(),
    'shrek': shrek(),
    'hermione': hermione(),
    'spongebob': spongebob(),
    'batman': batman(),
    'spiderman': spiderman(),
    'vader': vader(),
    'naruto': naruto(),
    'kirby': kirby(),
}

if __name__ == '__main__':
    for key, picture in ART.items():
        (OUTPUT / f'{key}.svg').write_text(picture, encoding='utf-8')
    print(f'Created {len(ART)} character illustrations in {OUTPUT}')
