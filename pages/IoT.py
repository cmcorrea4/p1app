import streamlit as st
import webbrowser
import streamlit.components.v1 as components
#import streamlit_authenticator as stauth
#import pickle5 as pickle
#from pathlib import Path

st.title('Monitoreo de Sensores.')

st.header('Temperatura')
components.html('''
<object class="grafana-iframe"
            data="http://157.230.214.127:3000/d-solo/kDD_nDN4z/iwta-sensors?orgId=1&refresh=10s&  \
            from=now-2h&to=now&&panelId=4&theme=light" width="600" height="200"></object>


''', width=600, height=200, scrolling=False
)

components.html('''
<object class="grafana-iframe"
            data="http://157.230.214.127:3000/d-solo/kDD_nDN4z/iwta-sensors?orgId=1&refresh=10s&  \
            from=now-2h&to=now&&panelId=2&theme=light" width="600" height="400"></object>


''', width=600, height=400, scrolling=False
)



st.header('Humedad Relativa.')
components.html('''
<object class="grafana-iframe"
            data="http://157.230.214.127:3000/d-solo/kDD_nDN4z/iwta-sensors?orgId=1&refresh=10s&  \
            from=now-4h&to=now&panelId=5&theme=light" width="600" height="200"></object>


''', width=600, height=200, scrolling=False
)

components.html('''
<object class="grafana-iframe"
            data="http://157.230.214.127:3000/d-solo/kDD_nDN4z/iwta-sensors?orgId=1&refresh=10s&  \
            from=now-4h&to=now&panelId=3&theme=light" width="600" height="400"></object>


''', width=600, height=400, scrolling=False
)
