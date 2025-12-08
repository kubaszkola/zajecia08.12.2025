
Świetnie! Dodanie interaktywności w Streamlit jest nieco inne niż w standardowym Matplotlib w Colab, ponieważ Streamlit działa na zasadzie odświeżania strony przy zmianie stanu (np. kliknięcie przycisku, zmiana suwaka).

Aby uzyskać interaktywną zmianę koloru czapki, użyjemy widgetu Streamlit (np. przycisku lub pola wyboru), a nie bezpośredniego kliknięcia na element Matplotlib.

Oto zmodyfikowany kod, który wykorzystuje przycisk Streamlit do zmiany koloru czapki. 🎨

💻 Kod Python dla Streamlit z Interaktywnością
Zapisz ten kod jako plik np. mikolaj_interactive.py:

Python

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Definicje Kolorów ---
RED = '#CC0000'
BLUE = '#0066CC'
WHITE = '#FFFFFF'
SKIN = '#FADBD8'
BLACK = '#2C3E50'
GOLD = '#FFC300'
BROWN = '#795548'
SACK = '#B08968' 

def narysuj_mikolaja_z_workiem(cap_color):
    """
    Tworzy figurę Matplotlib Mikołaja, akceptując kolor czapki jako argument.
    """
    
    # --- Ustawienia Figury i Osi ---
    fig, ax = plt.subplots(1, figsize=(6, 8))
    ax.set_facecolor('#E0F7FA') # Jasnoniebieskie, zimowe tło
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # --- 1. Mikołaj (Głowa i Ciało) ---
    face = patches.Circle((5, 5.5), 1.2, color=SKIN)
    ax.add_patch(face)
    beard = patches.Ellipse((5, 4.5), 3, 2.5, color=WHITE)
    ax.add_patch(beard)
    ax.plot(4.5, 5.8, 'o', color=BLACK, markersize=5)
    ax.plot(5.5, 5.8, 'o', color=BLACK, markersize=5)
    ax.plot(5.0, 5.3, 'o', color=RED, markersize=8)
    body = patches.Rectangle((3.5, 2.5), 3, 2.5, color=RED)
    ax.add_patch(body)
    belt = patches.Rectangle((3.5, 3.5), 3, 0.3, color=BLACK)
    ax.add_patch(belt)
    buckle = patches.Rectangle((4.8, 3.35), 0.4, 0.6, color=GOLD)
    ax.add_patch(buckle)
    arm_left = patches.Rectangle((2.0, 4.0), 1.5, 0.7, angle=-30, color=RED, rotation_point=(2.75, 4.35))
    ax.add_patch(arm_left)
    arm_right = patches.Rectangle((6.5, 4.0), 1.5, 0.7, angle=30, color=RED, rotation_point=(7.25, 4.35))
    ax.add_patch(arm_right)
    hand_left = patches.Circle((2.2, 3.8), 0.3, color=WHITE)
    ax.add_patch(hand_left)
    hand_right = patches.Circle((7.8, 4.2), 0.3, color=WHITE)
    ax.add_patch(hand_right)

    # --- 2. Czapka (Używamy koloru z argumentu funkcji) ---
    cap_triangle = patches.Polygon([[3.5, 6.5], [6.5, 6.5], [5.5, 9.0]], color=cap_color)
    ax.add_patch(cap_triangle)
    cap_band = patches.Rectangle((3.5, 6.5), 3, 0.5, color=WHITE)
    ax.add_patch(cap_band)
    pompon = patches.Circle((5.5, 9.0), 0.3, color=WHITE)
    ax.add_patch(pompon)
    
    # --- 3. Nogi i Buty ---
    leg_left = patches.Rectangle((4.0, 1.5), 0.5, 1.0, color=BLACK)
    ax.add_patch(leg_left)
    leg_right = patches.Rectangle((5.5, 1.5), 0.5, 1.0, color=BLACK)
    ax.add_patch(leg_right)
    boot_left = patches.Rectangle((3.8, 1.0), 0.7, 0.5, color=BLACK)
    ax.add_patch(boot_left)
    boot_right = patches.Rectangle((5.3, 1.0), 0.7, 0.5, color=BLACK)
    ax.add_patch(boot_right)

    # --- 4. Worek z Prezentami ---
    sack_body = patches.Rectangle((1.5, 2.0), 1.5, 2.5, color=SACK)
    ax.add_patch(sack_body)
    sack_top = patches.Ellipse((2.25, 4.5), 1.7, 0.5, angle=0, color=BROWN)
    ax.add_patch(sack_top)
    ax.plot(2.25, 4.5, 'o', color=WHITE, markersize=10, zorder=5) 

    # --- 5. Napis świąteczny ---
    plt.text(5, 0.5, 'Użyj przycisku, aby zmienić czapkę!', ha='center', fontsize=18, color=cap_color, weight='bold')
    
    # --- 6. Tytuł ---
    plt.title("Świąteczny Mikołaj z Matplotlib", fontsize=20, color=cap_color)
    
    return fig

# --- Główna Aplikacja Streamlit ---
def app():
    st.title("🎅 Mikołaj: Interaktywna Czapka")
    st.markdown("---")
    
    # 1. ZARZĄDZANIE STANEM W STREAMLIT
    # Używamy session_state do śledzenia aktualnego koloru
    if 'cap_is_red' not in st.session_state:
        st.session_state.cap_is_red = True
        
    # 2. PRZYCISK ZMIENIAJĄCY STAN
    # Przycisk zmienia wartość w st.session_state
    if st.button('Zmień kolor czapki!'):
        st.session_state.cap_is_red = not st.session_state.cap_is_red
        
    # 3. PRZEKAZANIE KOLORU
    # Ustawienie koloru, który zostanie przekazany do funkcji rysującej
    current_cap_color = RED if st.session_state.cap_is_red else BLUE
    
    # Wyświetlenie aktualnego koloru
    st.write(f"Aktualny kolor czapki: **{'Czerwony' if st.session_state.cap_is_red else 'Niebieski'}**")

    # 4. RYSOWANIE
    mikolaj_figura = narysuj_mikolaja_z_workiem(current_cap_color)
    st.pyplot(mikolaj_figura)
    
    st.markdown("---")

# Uruchomienie aplikacji
if __name__ == "__main__":
    app()
