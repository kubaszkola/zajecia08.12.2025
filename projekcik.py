import streamlit as st
from supabase import create_client

# --- KONFIGURACJA ---
URL = "https://sjnajzkuhvvmvygykkht.supabase.co"
KEY = "sb_publishable_74dGB7251z2xPIIBCTdHSQ_vvnnfgWB"

@st.cache_resource
def init_connection():
    return create_client(URL, KEY)

try:
    supabase = init_connection()
except Exception as e:
    st.error(f"Błąd połączenia z Supabase: {e}")
    st.stop()

st.set_page_config(page_title="🎬 Oceny Filmów", layout="centered")
st.title("🎬 System Oceny Filmów")

# --- ZAKŁADKI ---
tab1, tab2, tab3 = st.tabs([
    "🎥 Dodaj Film",
    "🎭 Dodaj Gatunek",
    "📊 Ranking i Statystyki"
])

# --- DODAWANIE GATUNKU (Kategorie) ---
with tab2:
    st.header("🎭 Nowy Gatunek Filmowy")

    with st.form("genre_form", clear_on_submit=True):
        gatunek = st.text_input("Nazwa gatunku (np. Thriller)")
        opis = st.text_area("Opis gatunku")
        submit = st.form_submit_button("Dodaj gatunek")

        if submit and gatunek:
            supabase.table("Kategorie").insert({
                "nazwa": gatunek,
                "opis": opis
            }).execute()
            st.success(f"Dodano gatunek: {gatunek}")

# --- DODAWANIE FILMU (Produkty) ---
with tab1:
    st.header("🎥 Nowy Film")

    try:
        genres = supabase.table("Kategorie").select("id, nazwa").execute().data
    except:
        genres = []

    if not genres:
        st.warning("Najpierw dodaj gatunek filmu.")
    else:
        genre_map = {g["nazwa"]: g["id"] for g in genres}

        with st.form("movie_form", clear_on_submit=True):
            tytul = st.text_input("Tytuł filmu")
            ocena = st.slider("Ocena (1–10)", 1, 10, 5)
            obejrzenia = st.number_input("Liczba obejrzeń", min_value=0, step=1)
            gatunek = st.selectbox("Gatunek", list(genre_map.keys()))
            submit = st.form_submit_button("Dodaj film")

            if submit and tytul:
                supabase.table("Produkty").insert({
                    "nazwa": tytul,
                    "cena": float(ocena),
                    "liczba": obejrzenia,
                    "kategorie_id": genre_map[gatunek]
                }).execute()
                st.success(f"Dodano film: {tytul}")

# --- RANKING I STATYSTYKI ---
with tab3:
    st.header("📊 Ranking Filmów")

    movies = supabase.table("Produkty").select(
        "nazwa, cena, liczba, kategorie_id"
    ).execute().data

    genres = supabase.table("Kategorie").select("id, nazwa").execute().data
    genre_map = {g["id"]: g["nazwa"] for g in genres}

    for m in movies:
        m["gatunek"] = genre_map.get(m["kategorie_id"], "Nieznany")

    if movies:
        # Ranking wg oceny
        top = sorted(movies, key=lambda x: x["cena"], reverse=True)

        st.subheader("⭐ Najlepiej oceniane filmy")
        for m in top[:5]:
            st.write(
                f"🎬 **{m['nazwa']}** | "
                f"Gatunek: {m['gatunek']} | "
                f"⭐ {m['cena']} | 👁️ {m['liczba']} obejrzeń"
            )

        avg = sum(m["cena"] for m in movies) / len(movies)
        st.metric("Średnia ocena filmów", round(avg, 2))
    else:
        st.info("Brak filmów w bazie.")

