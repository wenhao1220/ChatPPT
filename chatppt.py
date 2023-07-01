import streamlit as st
from ppt_lib import *
import base64

def create_download_link(data, filename):
    b64 = base64.b64encode(data).decode()  # 將檔案數據轉換為 base64 編碼
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64}" download="{filename}">點此下載</a>'
    return href

if __name__ == '__main__':
    st.set_page_config(layout = 'wide')
    
    st.title('ChatPPT投影片自動產生系統')
    
    title = st.text_input("請輸入首頁標題", value = '要如何學習人工智慧')
    sub_title = st.text_input("請輸入首頁副標題", value = '李文豪/嘉義大學')
    context = st.text_area("請輸入投影片內文:", value = '''學習人工智慧（Artificial Intelligence，AI）是一個廣泛的領域，涵蓋了多個子領域和技術。以下是一些步驟和資源，可以幫助你開始學習人工智慧：

1. 建立基礎知識：了解人工智慧的基本概念、技術和應用是入門的第一步。閱讀相關的書籍、研究報告、網絡資源和教學視頻，可以幫助你建立起相關的背景知識。

2. 學習數學和統計學：人工智慧涉及許多數學和統計學概念，例如線性代數、微積分、概率論和統計學。學習這些基礎知識對於深入理解人工智慧算法和模型是非常重要的。

3. 掌握編程和算法：編程是實現人工智慧應用的關鍵技能之一。選擇一種主要的編程語言（例如Python），並學習如何使用該語言進行開發。同時，瞭解常用的機器學習和深度學習算法，例如回歸、分類、神經網絡等。

4. 學習機器學習和深度學習：機器學習和深度學習是人工智慧的重要分支。了解不同的機器學習算法、深度學習架構和相關的工具庫（例如Scikit-learn、TensorFlow、PyTorch等）是非常重要的。

5. 實踐和建立專案：通過實踐，應用你所學的知識於實際問題中。嘗試參與人工智慧相關的競賽、解決問題或者自己開發一個專案。這樣能夠提供寶貴的經驗和實踐機會，並加強你的技能。

6. 持續學習和跟踪最新發展：人工智慧領域發展迅速，新技術和方法層出不窮。繼續學習和保持與最新趨勢和

研究成果的同步是非常重要的。閱讀期刊論文、參加研討會、追蹤專業網絡和社群等，可以幫助你不斷更新知識。

除了以上步驟，還有許多在人工智慧領域深入學習的進階課程和證書。一些知名的在線學習平台（例如Coursera、edX、Udacity等）提供了人工智慧相關的課程和學位，可以作為你學習的資源。

最重要的是保持耐心和持續努力，人工智慧是一個深入且不斷演進的領域，需要持續學習和實踐。''', height = 170)
    
    if st.button("PPT自動產生"):
        prs = Presentation()
        
        sub_title = sub_title.replace('/', '\n')
        
        create_title(prs, title, sub_title)
        
        item_list = []
        
        for line in context.splitlines():
            if len(line) > 0 and line[0].isdigit() and line[1] == '.':
                item_list.append(line[2:].strip())
                
        slides = []
        slides.append({'title': '大綱', 'content': item_list})
        
        create_body(prs, slides)
        
        filename = title + '.pptx'
        prs.save(filename)
        
        #st.success('投影片已產生!')
        
        with open(filename, 'rb') as f:
            data = f.read()
            
        #顯示下載連結
        st.markdown(create_download_link(data, filename), unsafe_allow_html=True)