import streamlit as st
from ppt_lib import *
import base64

def create_download_link(data, filename):
    b64 = base64.b64encode(data).decode()  # 將檔案數據轉換為 base64 編碼
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64}" download="{filename}">點此下載</a>'
    return href

def split_list(input_list, chunk_size):
    return [input_list[i: i+chunk_size] for i in range(0, len(input_list), chunk_size)]

if __name__ == '__main__':
    st.set_page_config(layout = 'wide')
    
    st.title('ChatPPT投影片自動產生系統')
    
    title = st.text_input("請輸入首頁標題", value = '要如何學習人工智慧')
    sub_title = st.text_input("請輸入首頁副標題", value = '李文豪/嘉義大學')
    context = st.text_area("請輸入投影片內文:", value = '''當然！這裡有15個關於學習人工智慧的建議：

1. 閱讀經典的人工智慧相關書籍，如《人工智慧：一種現代方法》（Artificial Intelligence: A Modern Approach）。
2. 學習機器學習的基本概念，如監督學習、非監督學習和強化學習。
3. 掌握常見的機器學習算法，如線性回歸、決策樹、支持向量機和隨機森林。
4. 學習深度學習的基礎知識，包括神經網絡結構和常見的深度學習模型。
5. 使用Python等編程語言進行機器學習和深度學習的實作。
6. 學習如何處理和應用結構化和非結構化數據。
7. 瞭解自然語言處理（Natural Language Processing，NLP）和計算机視覺（Computer Vision）等特定領域的應用。
8. 實踐專案，運用所學知識解決真實世界的問題。
9. 學習使用常用的機器學習和深度學習庫，如Scikit-learn、TensorFlow和PyTorch。
10. 參與線上課程、教學視頻和MOOC（大規模開放式在線課程），如Coursera上的《深度學習專項課程》（Deep Learning Specialization）。
11. 加入人工智慧相關的社群和論壇，與其他學習者和專業人士交流和分享經驗。
12. 學習如何進行數據預處理、特徵工程和模型評估，以提高機器學習模型的性能。
13. 跟踪人工智慧領域的最新趨勢和研究成果，閱讀相關的期刊論文和研討會報告。
14. 學習適當的優化技術和超參數調整方法，以改進模型的訓練和性能。
15. 不斷實踐、練習和追求對人工智慧

的熟練掌握，並保持對新技術和應用的好奇心。

希望這些建議能夠幫助你在學習人工智慧的旅程中前進！祝你好運！''', height = 170)
    
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    num = col1.number_input("投影片每頁要列出幾點", value = 5)
    
    if st.button("PPT自動產生"):
        prs = Presentation()
        
        sub_title = sub_title.replace('/', '\n')
        
        create_title(prs, title, sub_title)
        
        item_list = []
        
        for line in context.splitlines():
            if len(line) > 0:
                item_list.append(line.strip())
                
        chunk_lists = split_list(item_list, num)
                
        slides = []
        #slides.append({'title': '大綱', 'content': item_list})
        
        for sublist in chunk_lists:
            slides.append({'title': '大綱', 'content': sublist})
        
        create_body(prs, slides)
        
        filename = title + '.pptx'
        prs.save(filename)
        
        #st.success('投影片已產生!')
        
        with open(filename, 'rb') as f:
            data = f.read()
            
        #顯示下載連結
        st.markdown(create_download_link(data, filename), unsafe_allow_html=True)