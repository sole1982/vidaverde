from django.shortcuts import render

def acerca_de(request):
    
    miembros = [
        {'nombre': 'Soledad', 'descripcion': 'Soledad es una estudiante apasionada del "Informatorio", destacándose en el desarrollo web con Python. Su enfoque meticuloso y su habilidad para resolver problemas complejos la convierten en una desarrolladora web competente. Ella disfruta explorando nuevas tecnologías y está comprometida con mejorar constantemente sus habilidades.', 'imagen': '/static/img/Soledad.jpg'},
        {'nombre': 'Valentino', 'descripcion': 'Valentino es un estudiante enérgico del "Informatorio" con un enfoque especial en el desarrollo web utilizando Python. Su creatividad centrada en el usuario lo distinguen en la creación de experiencias web atractivas. Constantemente busca nuevas formas de mejorar la usabilidad y el diseño de sus aplicaciones web.', 'imagen': '/static/img/Valentin.jpeg'},
        {'nombre': 'Ariel', 'descripcion': 'Ariel es un desarrollador web en formación dentro del "Informatorio" con una fuerte inclinación hacia el diseño de interfaces de usuario. Su habilidad para combinar la estética con la funcionalidad lo hace destacar en la creación de sitios web visualmente atractivos y fácilmente navegables. Ariel está siempre interesado en aprender nuevas técnicas y tecnologías para mejorar sus habilidades.', 'imagen' : '/static/img/Ariel.jpg'},
        {'nombre': 'Matías', 'descripcion': 'Matías es un estudiante comprometido del "Informatorio", especializado en el desarrollo backend con Python. Su enfoque pragmático y su atención a los detalles lo destacan en la creación de sistemas web robustos y eficientes. Matías está constantemente actualizando sus conocimientos para asegurarse de aplicar las mejores prácticas en el desarrollo web.', 'imagen': '/static/img/cambio.jpg'},
    ]

    context = {
        'miembros': miembros,
    }

    return render(request, 'acerca_de/acerca_de.html', context)
