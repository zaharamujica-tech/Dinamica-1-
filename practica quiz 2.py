red_social = [
    ["@viajero", [1200, 500]],
    ["@chef_luis", [40, 50, 30, 20]],
    ["@tech_news", [3000]],
    ["@influencer_top", [15000, 12000, 18000, 20000, 14000, 16000]],
    ["@gatitos_virales", [50000]],
    ["@usuario_fantasma", []],
    ["@memes_diarios", [10, 5, 12, 8, 15, 20, 5]]
]
def usuarios_activos (red_social):
    user_fotos=""
    mas_fotos=-1
    user_likes=""
    mas_likes_promedio=-1
    promedio_likes=0
    for cuenta in red_social:
        nombre=cuenta[0]
        likes= cuenta[1]
        cantidad_fotos= len(likes)
        if cantidad_fotos>mas_fotos:
            user_fotos=nombre
            mas_fotos= cantidad_fotos
        if len(likes)>0:
            promedio_likes= sum(likes)/len(likes)
            if promedio_likes>mas_likes_promedio:
                user_likes=nombre
                mas_likes_promedio=promedio_likes
    return user_fotos, user_likes, mas_likes_promedio, mas_fotos
user_fotos, user_likes, mas_likes_promedio, mas_fotos= usuarios_activos (red_social)
print(f"Con {mas_fotos}, el usurio con más fotos es {user_fotos}")
print(f"Con {round(mas_likes_promedio,2)}, el usurio con más likes es {user_likes}")