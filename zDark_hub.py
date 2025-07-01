import tkinter as tk
from apis import MCData

# Inicializa MCData
MCData.clear()
MCData.name("zDark_hub")

# Janela principal
root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry("550x350")
root.configure(bg="#0d0d0d")

# Mover a janela
def start_move(event):
    global root
    root._offsetx = event.x
    root._offsety = event.y

def do_move(event):
    global root
    x = root.winfo_pointerx() - root._offsetx
    y = root.winfo_pointery() - root._offsety
    root.geometry(f'+{x}+{y}')

root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

# Barra de título
title_bar = tk.Frame(root, bg="#0d0d0d")
title_bar.pack(fill='x')

title_label = tk.Label(
    title_bar,
    text="zDark Hub",
    font=('Segoe UI Black', 22),
    fg='white',
    bg="#0d0d0d"
)
title_label.pack(pady=15)

def fechar():
    root.destroy()

close_btn = tk.Button(
    title_bar,
    text="✕",
    command=fechar,
    font=('Segoe UI', 12),
    fg='white',
    bg="#1f1f1f",
    activebackground="#333333",
    activeforeground="white",
    relief='flat',
    borderwidth=0,
    padx=8,
    pady=2
)
close_btn.place(relx=1.0, y=10, anchor='ne', x=-10)

# Cheats
cheats_frame = tk.Frame(root, bg="#0d0d0d")
cheats_frame.pack(pady=10, padx=25, fill='x')

# Estados
god_mode_on = False

# CRIAR FRAMES E BOTÕES (sem command ainda)
def criar_linha(nome):
    global tk, cheats_frame
    frame = tk.Frame(cheats_frame, bg="#0d0d0d")
    frame.pack(fill='x', pady=12)

    label = tk.Label(frame, text=nome, font=('Segoe UI', 13, 'bold'), fg='white', bg="#0d0d0d")
    label.pack(side='left')

    btn = tk.Button(
        frame, text="OFF", font=('Segoe UI', 11), bg="#1f1f1f", fg='white',
        activebackground="#333333", activeforeground='white', width=8,
        relief='flat', borderwidth=0
    )
    btn.pack(side='right')
    return btn

btn_godmode = criar_linha("GodMode")

def toggle_godmode():
    global god_mode_on, btn_godmode, MCData
    god_mode_on = not god_mode_on

    btn_godmode.config(text="ON" if god_mode_on else "OFF",
                    bg="#4caf50" if god_mode_on else "#1f1f1f",
                    activebackground="#388e3c" if god_mode_on else "#333333")
    MCData.clear()
    MCData.scoreboards.set(
        MCData.Entity.all_players(),
            "godmode",
            1 if god_mode_on else 0,
        MCData.Type.loop()
    )
    MCData.extra_inject()

btn_godmode.config(command=toggle_godmode)

# Iniciar app
root.mainloop()
