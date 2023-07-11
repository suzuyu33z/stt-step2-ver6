
import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート


# 言語選択と、APIが認識する言語の変換リストを作成
set_language_list = {
    "日本語" :"ja",
    "英語" :"en-US",
}

# デフォルトの言語を設定
set_language = "日本語"




# 音声ファイルと音声認識の言語を引数に音声認識をする


st.title("文字起こしアプリ") # タイトル
st.write("音声認識する言語を選んでください。") # 案内を表示
set_language = st.selectbox("音声認識する言語を選んでください。",set_language_list.keys()) # 音声認識に使う言語を選択肢として表示
current_language_state = st.empty() # 選択肢を表示するための箱を準備
current_language_state.write("選択中の言語:" + set_language) # 選択肢を表示するための箱に選択した言語を表示
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。",type=["wav"]) # アップローダーを設定し、wavファイルだけ許可する設定にする

# ファイルアップロードされた場合、file_uploadがNoneではなくなる
if (file_upload !=None):
    
    st.write("音声認識結果:") # 案内表示
    result_text = "aa" # アップロードされたファイルと選択した言語を元に音声認識開始
    st.write(result_text) # メソッドから返ってきた値を表示
    st.audio(file_upload) # アップロードした音声をきける形で表示


st.write("マイクでの音声認識はこちらのボタンから") # 案内表示


