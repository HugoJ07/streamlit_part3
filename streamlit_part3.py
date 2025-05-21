import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd


lesDonneesDesComptes = {
            'usernames': {}
}


log_connexion = pd.read_csv("https://raw.githubusercontent.com/HugoJ07/streamlit_part3/refs/heads/main/info_connexion.csv", sep=";", index_col='Unnamed: 0')


for index, row in log_connexion.iterrows():

    lesDonneesDesComptes['usernames'][index] = {                                   
                            'name': row['name'],
                            'password': row['password'],
                            'email': row['Email'],
                            'failed_login_attemps': row['failed_login_attemps'], # Sera géré automatiquement
                            'logged_in': row['logged_in'],          # Sera géré automatiquement
                            'role': row['Role']                          
    }


authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)


def accueil():
    st.title("Bienvenu sur la page réservée aux plus grands fans d'Arsenal")

    st.image("https://res.cloudinary.com/dtljonz0f/image/upload/f_auto/q_auto/v1/gc-v1/london-pass/blog/Emirates-Stadium-Tour-6-Stadium-Interior.jpg")


authenticator.login()


if st.session_state["authentication_status"]:

    with st.sidebar:

        authenticator.logout("Déconnexion")

        st.write(f"Bienvenue {st.session_state.get('username')}")

        selection = option_menu(
                                menu_title=None,
                                options=['Accueil', "Les joueurs d'Arsenal"],
                                icons= ['house', 'people']
        )

    if selection == 'Accueil':
        accueil()

    if selection == "Les joueurs d'Arsenal":
        st.header(":red[Découvrez] quelque :red[joueurs] emblématiques", divider='red')

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Thierry Henry")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMz-Dl_o0RIBIzA18IUaK8g-7B1VW10jT6mw&s")

        with col2:
            st.subheader("Bukayo Saka")
            st.image("https://ichef.bbci.co.uk/ace/standard/1024/cpsprodpb/1607A/production/_129843209_gettyimages-1474601216.jpg")

        with col3:
            st.subheader("Robert Pires")
            st.image("https://e0.365dm.com/15/12/2048x1152/robert-pires-arsenal_3383882.jpg?20151201190451")


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
