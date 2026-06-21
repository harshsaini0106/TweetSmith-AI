import streamlit as st
from workflow import workflow

st.set_page_config(
page_title="TweetSmith AI",
page_icon="",
layout="centered"
)

st.title(" TweetSmith AI")
st.subheader("Generate Viral Tweets using LangGraph")

topic = st.text_input("Enter a Topic")

if st.button("Generate Tweet"):


    if topic:

        with st.spinner("Generating Tweet..."):

            result = workflow.invoke(
                {
                    "topic": topic,
                    "iteration": 1,
                    "max_iteration": 3
                }
            )

        st.success("Tweet Generated")

        st.markdown("###  Tweet")
        st.write(result["tweet"])

    

    else:
        st.warning("Please enter a topic.")
