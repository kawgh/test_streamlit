import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DateFrame')

st.write('プログレスバーの表示')
'スタート'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!'

df1 = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]  
})

st.dataframe(df1.style.highlight_max(axis=0), width=1000, height=200)

st.table(df1.style.highlight_max(axis=0))

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)
df2

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat','lon']
)
st.map(df3)

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='sample', use_column_width=True)

option =  st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です。'

##st.write('Interactive Widget')


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ1回答')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ2回答')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ3回答')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味: ', text

condition = st.slider('あなたの今の調子は？', 0, 10, 5)
'コンディション', condition



"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""