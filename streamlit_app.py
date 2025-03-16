import streamlit as st
import json
import uuid
import os

DATA_FILE = "data.json"

# 데이터 불러오기 함수
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# 데이터 저장 함수
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 글 작성 함수
def create_post(title, content):
    data = load_data()
    post_id = str(uuid.uuid4())[:8]  # 8자리 랜덤 ID 생성
    new_post = {"id": post_id, "title": title, "content": content}
    data.append(new_post)
    save_data(data)
    return new_post

# 글 목록 가져오기
def get_posts():
    return load_data()

# Streamlit UI 구성
st.title("📝 대나무숲")

# 글 작성 UI
st.subheader("새 글 작성")
title = st.text_input("제목")
content = st.text_area("본문")

if st.button("글 작성"):
    if title and content:
        new_post = create_post(title, content)
        st.success(f"글이 작성되었습니다! (ID: {new_post['id']})")
    else:
        st.warning("제목과 본문을 입력하세요.")

st.markdown("---")

# 글 목록 표시
st.subheader("📜 작성된 글 목록")
posts = get_posts()

if posts:
    for post in reversed(posts):
        st.write(f"### {post['title']}")
        st.write(post['content'])
        st.caption(f"글 ID: {post['id']}")
        st.markdown("---")
else:
    st.info("아직 작성된 글이 없습니다.")

