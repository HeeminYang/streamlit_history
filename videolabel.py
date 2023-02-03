import pandas as pd

import streamlit as st
import os

video_list = os.listdir('/home/projects/Metaverse2021/video_seg_edu')
table = pd.read_excel('/home/projects/Metaverse2021/edu_label.xlsx', engine='openpyxl', index_col=0)

def main() :

    col1, col2, col3, col4 = st.columns(4)

    index= st.number_input('Index', min_value=0, step = 1)

    emotion = ['Negative', 'Positive', 'Neutral', 'None']

    with col1:
        if st.button('Negative'):
            st.write('Negative을 선택하셨습니다.')
            label = emotion[0]
            table['label'][index] = label
            table['file'][index] = video_list[index]
            table.to_excel('/home/projects/Metaverse2021/edu_label.xlsx')
    with col2:
        if st.button('Positive'):
            st.write('Positive을 선택하셨습니다.')
            label = emotion[1]
            table['label'][index] = label
            table['file'][index] = video_list[index]
            table.to_excel('/home/projects/Metaverse2021/edu_label.xlsx')
    with col3:
        if st.button('Neutral'):
            st.write('Neutral을 선택하셨습니다.')
            label = emotion[2]
            table['label'][index] = label
            table['file'][index] = video_list[index]
            table.to_excel('/home/projects/Metaverse2021/edu_label.xlsx')
    with col4:
        if st.button('None'):
            st.write('None을 선택하셨습니다.')
            label = emotion[3]
            table['label'][index] = label
            table['file'][index] = video_list[index]
            table.to_excel('/home/projects/Metaverse2021/edu_label.xlsx')

    st.write(f'Index: {index}')
    
    index = int(index)
    video_file = open('/home/projects/Metaverse2021/video_seg_edu/'+video_list[index], 'rb')
    st.video(video_file, format='video/mp4', start_time=0)

    # emotion = ['Negative', 'Positive', 'Neutral', 'None']
    # emo_choice = st.selectbox('select Emotion', emotion)
    # if emo_choice == emotion[0] :
    #     st.write('Negative을 선택하셨습니다.')
    #     label = emotion[0]
    # elif emo_choice == emotion[1] :
    #     st.write('Positive를 선택하셨습니다.')
    #     label = emotion[1]
    # elif emo_choice == emotion[2] :
    #     st.write('Neutral를 선택하셨습니다')
    #     label = emotion[2]
    # elif emo_choice == emotion[3] :
    #     st.write('None를 선택하셨습니다')
    #     label = emotion[3]
    



if __name__ == "__main__" :
    main()
