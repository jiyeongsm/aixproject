import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlit 페이지 설정
st.set_page_config(page_title="학생 성적 시각화", page_icon="📊", layout="wide")

# 데이터 준비
data = {
    "name": ["lee", "park", "kim"],
    "grade": [2, 2, 2],
    "number": [1, 2, 3],
    "kor": [90, 88, 99],
    "eng": [91, 89, 99],
    "math": [81, 77, 99],
    "info": [100, 100, 100]
}
df = pd.DataFrame(data)

# 웹앱 제목
st.title("학생 성적 시각화 대시보드")

# 사이드바: 과목 선택
st.sidebar.header("시각화 옵션")
subject = st.sidebar.selectbox("시각화할 과목 선택", ["kor", "eng", "math", "info"], index=0)

# 데이터프레임 표시
st.subheader("학생 성적 데이터")
st.dataframe(df)

# 막대그래프: 선택한 과목의 성적
st.subheader(f"{subject.upper()} 과목 성적 (막대그래프)")
fig_bar = px.bar(df, x="name", y=subject, color="name", title=f"{subject.upper()} 성적 비교",
                 labels={"name": "학생 이름", subject: "점수"},
                 color_discrete_sequence=px.colors.qualitative.Plotly)
fig_bar.update_layout(showlegend=False)
st.plotly_chart(fig_bar, use_container_width=True)

# 선그래프: 모든 과목 성적 비교
st.subheader("모든 과목 성적 비교 (선그래프)")
df_melt = df.melt(id_vars=["name"], value_vars=["kor", "eng", "math", "info"],
                  var_name="subject", value_name="score")
fig_line = px.line(df_melt, x="subject", y="score", color="name", markers=True,
                   title="학생별 모든 과목 성적",
                   labels={"subject": "과목", "score": "점수"})
st.plotly_chart(fig_line, use_container_width=True)

# 산점도: 두 과목 간 상관관계 (예: kor vs eng)
st.subheader("국어와 영어 성적 상관관계 (산점도)")
fig_scatter = px.scatter(df, x="kor", y="eng", color="name", size="math",
                         hover_data=["name", "number"], title="국어 vs 영어 성적",
                         labels={"kor": "국어 점수", "eng": "영어 점수"})
st.plotly_chart(fig_scatter, use_container_width=True)

# 통계 요약
st.subheader("성적 통계 요약")
st.write(df[["kor", "eng", "math", "info"]].describe())

# 추가 설명
st.markdown("""
### 웹앱 설명
- **데이터**: 학생 이름, 학년, 번호, 국어, 영어, 수학, 정보 과목의 성적 데이터를 사용.
- **시각화**:
  - **막대그래프**: 선택한 과목의 학생별 성적 비교.
  - **선그래프**: 학생별 모든 과목 성적을 선으로 표시.
  - **산점도**: 국어와 영어 성적의 상관관계, 수학 점수로 점 크기 조정.
- **인터랙션**: 사이드바에서 과목을 선택하여 막대그래프를 동적으로 업데이트.
""")