import streamlit as st


def ten_largest(values: list[int]) -> list[int]:
    return sorted(values, reverse=True)[:10]


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


st.set_page_config(page_title="Algorithms Lab Test Tutor 402", page_icon="🧠", layout="wide")

st.title("🧠 Algorithms Lab Test Tutor — Section 402")
st.write(
    "This tutor app turns the section 402 lab test into a study tool for top-k array logic, recursive palindrome checking, and linked-list structure."
)

tab1, tab2, tab3 = st.tabs(["Top Ten Finder", "Palindrome Check", "Linked List Idea"])

with tab1:
    raw = st.text_input("Enter integers", "5, 12, 3, 19, 25, 7, 30, 1, 50, 9, 11, 8, 60")
    values = [int(x.strip()) for x in raw.split(",") if x.strip()]
    st.write("Top ten values:", ten_largest(values))

with tab2:
    text = st.text_input("Enter text to test", "madam")
    st.metric("Palindrome?", "Yes" if is_palindrome(text) else "No")
    st.caption("The Java recursion checks matching characters from the outside inward.")

with tab3:
    st.write("A singly linked list is useful when insertions are based on node connections instead of array indices.")
    st.code("Head -> Node(value) -> Node(value) -> Node(value) -> null", language="text")
