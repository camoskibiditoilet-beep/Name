import streamlit as st

st.set_page_config(page_title="Sladostrastnaya vafelka", page_icon=":https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.facebook.com%2FHreVsia%2Fposts%2F-%25D0%25BA%25D0%25B0%25D0%25BA%25D0%25BE%25D0%25B9-%25D0%25BF%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%25D1%258B-%25D1%2583-%25D1%2582%25D0%25B5%25D0%25B1%25D1%258F-%25D0%25BA%25D0%25BE%25D1%2582-%25D1%2581%25D0%25BA%25D1%2583%25D1%2584%25D0%25B8%25D0%25BD%25D0%25BA%25D1%2581%2F901275852014351%2F&ved=0CBcQjRxqFwoTCIius5nW0pcDFQAAAAAdAAAAABAF&opi=89978449.png", layout="wide")

st.title("Sladostrastnaya vafelka's secret hideout")

tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])

with tab1:
    st.header("What is sladostrastnoya vafelka's hideout")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.facebook.com%2FHreVsia%2Fposts%2F-%25D0%25BA%25D0%25B0%25D0%25BA%25D0%25BE%25D0%25B9-%25D0%25BF%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%25D1%258B-%25D1%2583-%25D1%2582%25D0%25B5%25D0%25B1%25D1%258F-%25D0%25BA%25D0%25BE%25D1%2582-%25D1%2581%25D0%25BA%25D1%2583%25D1%2584%25D0%25B8%25D0%25BD%25D0%25BA%25D1%2581%2F901275852014351%2F&ved=0CBcQjRxqFwoTCIius5nW0pcDFQAAAAAdAAAAABAF&opi=89978449.png")
        with col2:
            st.subheader("Hello I'm future Python snake")
            st.write("I study at the university of intermidiate pray hunters")

            with st.container():
                st.info("Contact lenses")
                st.markdown("- Email: vafelka@korol.net")
    st.write("This is a place where you can find all the latest updates and news about Sladostrastnaya vafelka.")
