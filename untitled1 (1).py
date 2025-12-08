








import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Definicje Kolorów ---
RED = '#CC0000'
BLUE = '#0066CC' # Nowy kolor niebieski
WHITE = '#FFFFFF'
SKIN = '#FADBD8'
BLACK = '#2C3E50'
GOLD = '#FFC300'
BROWN = '#795548'
SACK = '#B08968'

# --- Zmienne Globalne dla Elementów Graficznych ---
# Musimy przechowywać referencje do elementów, które będziemy zmieniać
global cap_triangle, cap_band, pompon, is_red, sack_patch

is_red = True # Flaga do śledzenia aktualnego koloru

def on_click(event):
    """
    Funkcja obsługująca zdarzenie kliknięcia myszą.
    Sprawdza, czy kliknięcie nastąpiło w obszarze worka.
    """
    global is_red, cap_triangle, cap_band, pompon

    # Sprawdzenie, czy kliknięcie nastąpiło na osi 'ax'
    if event.inaxes != sack_patch.axes:
        return

    # Sprawdzenie, czy kliknięcie nastąpiło wewnątrz obiektu 'sack_patch' (worka)
    # Wykorzystujemy 'contains' do sprawdzenia, czy kliknięcie jest w granicach obiektu
    cont, _ = sack_patch.contains(event) 
    
    if cont:
        # Zmiana flagi koloru
        is_red = not is_red
        
        # Wybór nowego koloru na podstawie flagi
        new_color = RED if is_red else BLUE

        # Zmiana koloru czerwonych elementów czapki
        cap_triangle.set_color(new_color)
        
        # Opcjonalnie: zmiana koloru tytulu
        plt.gcf().suptitle("Świąteczny Mikołaj z Matplotlib", fontsize=20, color=new_color)

        # Wymuszenie ponownego narysowania figury
        plt.draw()
        
        # Dodatkowa informacja zwrotna w konsoli
        print(f"Kolor czapki zmieniony na: {'Czerwony' if is_red else 'Niebieski'}")


def narysuj_mikolaja_interaktywnego():
    """Tworzy figurę Mikołaja i ustawia obsługę interakcji."""
    global cap_triangle, cap_band, pompon, sack_patch

    # --- Ustawienia Figury i Osi ---
    fig, ax = plt.subplots(1, figsize=(6, 8))
    ax.set_facecolor('#E0F7FA')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # --- 1. Mikołaj (Głowa i Ciało - bez zmian) ---
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

    # --- 2. Czapka (Przypisujemy do zmiennych globalnych) ---
    # Czerwona część (referencja globalna)
    cap_triangle = patches.Polygon([[3.5, 6.5], [6.5, 6.5], [5.5, 9.0]], color=RED)
    ax.add_patch(cap_triangle)

    # Biały pasek czapki (referencja globalna - opcjonalnie)
    cap_band = patches.Rectangle((3.5, 6.5), 3, 0.5, color=WHITE)
    ax.add_patch(cap_band)

    # Biały pompon (referencja globalna - opcjonalnie)
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

    # --- 4. Worek z Prezentami (Referencja globalna do worka) ---
    # Worek (sack_patch musi być globalne, żeby funkcja on_click mogła je sprawdzić)
    sack_patch = patches.Rectangle((1.5, 2.0), 1.5, 2.5, color=SACK)
    ax.add_patch(sack_patch)

    sack_top = patches.Ellipse((2.25, 4.5), 1.7, 0.5, angle=0, color=BROWN)
    ax.add_patch(sack_top)
    ax.plot(2.25, 4.5, 'o', color=WHITE, markersize=10, zorder=5)

    # --- 5. Napis świąteczny ---
    plt.text(5, 0.5, 'Kliknij Worek!', ha='center', fontsize=18, color=RED, weight='bold')

    # --- 6. Wyświetlenie i Interakcja ---
    # Ustawienie tytułu figury
    fig.suptitle("Świąteczny Mikołaj z Matplotlib", fontsize=20, color=RED)
    
    # Podłączenie funkcji on_click do zdarzeń naciśnięcia przycisku myszy
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()

# Wywołanie funkcji, aby uruchomić rysowanie
narysuj_mikolaja_interaktywnego()
