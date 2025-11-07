from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import difflib

# --- Flask setup ---
app = Flask(__name__)
CORS(app)

from flask_cors import CORS
CORS(app)


responses = {
    "saludo_motivacional": {
        "patterns": [
            "holi", "holis", "hola", "oli", "hey", "buenas",
            "buenos dias", "buenas tardes", "buenas noches"
        ],
        "answers": [
            "¡Hola, qué gusto verte por aquí! 💛",
            "Hola, tómate un momento para ti y respira profundo 🦆",
            "Qué gusto verte, patito 🌤️",
"Hey, ¿cómo estás? 🌿",
"¡Cuac! Llegaste justo a tiempo 💫",
"¡Hola hola! Me alegra verte por aquí ☀️",
"Hey tú, sí tú, qué bueno verte sonreír 💛",
"¡Hola patito! 🌼",
"Cuac-cuac, vine a saludarte 😄",
"¡Qué bueno verte de nuevo por aquí! 💛",
"Hola, espero que tu día esté suavecito como mis plumas 🦆",
"¡Hey! ¿Trajiste buena vibra hoy? 🌸",
"Hola, hola 🌞 respira profundo y relaja los hombros",
"¡Hola! Estaba esperándote 🦆",
"Cuac, ¡qué lindo verte! 🌷",
"Hey, patito curioso, ¿cómo va todo? 💛",
"¡Buenas buenas! ☕ ¿Listo para un día tranquilo?",
"Hola, recuerda hidratarte y sonreír 💧🙂",
"¡Cuac! Me alegra verte tan pronto 💫",
"Hola 🌻 cada día contigo es un buen día",
"¡Hey! Pato feliz te saluda desde el lago 🦆",
"¡Hola! No olvides lo fuerte que eres 💪",
"¡Buenas tardes, rayito de sol! 🌞",
"¡Hey! Cuac-cuac, ¿ya comiste hoy? 💛",
"Hola, vine a acompañarte un ratito 🌿",
"¡Hola patito lindo! 💛",
"Hey, ¡qué gusto tenerte aquí otra vez! 🌼",
"Hola 🌙 espero que hoy te abraces un poco",
"¡Hey tú! Cuac, te ves genial 🦆",
"¡Hola! Todo se siente más tranquilo contigo aquí 💛"
        ]
    },

    "tristeza": {
        "patterns": [
            "estoy triste", "me siento triste", "me siento mal", "hoy fue un mal dia",
            "no me siento bien", "me siento bajoneado", "me siento bajoneada",
            "me siento decaido", "me siento decaida", "me siento fatal",
            "hoy todo va mal", "hoy nada sale bien", "me siento muy triste"
        ],
        "answers": [
"Sé que duele, pero no siempre será así 🌙",
"A veces los días pesan más, pero tú también mereces descansar 🫶",
"No estás sol@, patito 💛 incluso los días grises tienen calma 🌧️",
"Respira, está bien sentirse mal a veces 💛",
"No tienes que sonreír todo el tiempo, está bien 💫",
"Los días tristes también terminan 🌦️",
"Cuac... te mando un abrazo suavecito 🦆",
"No pasa nada si hoy no puedes con todo 🌿",
"Hoy duele, mañana quizá un poco menos 💛",
"Te entiendo, y eso también pasará 🌙",
"A veces la tristeza solo quiere que descanses 🌸",
"No te juzgues por sentirte así 💛",
"Incluso los patos tenemos días grises ☁️",
"Todo va a mejorar, aunque ahora no parezca 💫",
"Déjate cuidar por un ratito 🦆",
"No estás sol@, estoy aquí contigo 🌷",
"No tienes que ser fuerte todo el tiempo 💛",
"Está bien no estar bien 🌿",
"Te mereces calma, no exigencia 💫",
"El lago también se agita a veces, pero luego se calma 🦆",
"Te mando un cuac lleno de cariño 💛",
"Los días tristes también cuentan 🌙",
"Descansa, no tienes que resolver nada ahora 🌸",
"Respira, patito, poco a poco todo se acomoda 🌿",
"El cielo se despeja después de la lluvia 💛",
"No eres tu tristeza, eres mucho más que eso 🌼",
"Cuac, deja que el viento se lleve lo pesado 💨",
"Todo estará bien, lo prometo 🦆",
"Gracias por quedarte incluso en los días difíciles 💛"
        ]
    },

    "alegria": {
        "patterns": [
            "me siento bien", "hoy estoy feliz", "estoy contento", "estoy contenta",
            "me siento genial", "me siento alegre", "hoy todo va bien",
            "me siento excelente", "hoy fue un buen dia"
        ],
        "answers": [
            "Eso suena increíble, sigue con esa energía 🦆",
"Me alegra mucho leer eso 💛",
"Disfruta este momento, te lo ganaste 🌞",
"Cuac, esa energía me contagia 😄",
"¡Qué lindo escucharte tan feliz! 💫",
"Brillas más que el sol hoy ☀️",
"Qué emoción, se nota que estás bien 💛",
"Me encanta ver que sonríes 🌸",
"Disfruta cada segundo de esa alegría 🦆",
"¡Sí! eso merece un cuac de celebración 🎉",
"Tu buena vibra ilumina el lago 🌿",
"Wow, me alegra muchísimo 🩵",
"Me encanta saber que hoy estás bien 💛",
"Qué bonito leer tanta felicidad 🌼",
"Cuac, me llenas el corazoncito 💫",
"Tu alegría también me hace sonreír 🦆",
"Qué día tan bonito para estar feliz ☀️",
"Me alegra verte disfrutando 💛",
"Eso sí es energía de pato feliz 🦆",
"Tu sonrisa vale oro 🌻",
"Brillas, patito ✨",
"Disfruta lo que te hace sentir bien 💛",
"Qué bonito ver que confías en ti 🦆",
"Me encanta esa actitud 🌿",
"Patito feliz, lago tranquilo 🩵",
"Guarda ese sentimiento, te queda bien 💫",
"Cuac, eso merece aplausos de plumas 👏",
"Qué hermoso leer eso 💛",
"No olvides agradecerte por sentirte así 🌞"
        ]
    },

    "estres": {
        "patterns": [
            "estres", "estoy estresado", "estresada", "agobiado", "agobiada",
            "cansado", "cansada", "me siento sin energia", "no puedo mas",
            "estoy tenso", "estoy tensa", "me siento saturado", "tengo mucho estres"
        ],
        "answers": [
"Suelta los hombros, estás haciendo lo mejor que puedes 🌿",
"El estrés no te define, solo te recuerda que necesitas un descanso 🌙",
"Sé que pesa, pero ya estás haciendo mucho 💛",
"Cuac, afloja el cuello, respira despacio 🌸",
"No todo tiene que salir perfecto 💛",
"Descansa, el mundo puede esperar un ratito 🦆",
"A veces parar también es avanzar 🌿",
"Date permiso de no poder con todo hoy 💫",
"Relaja los hombros, inhala y suelta 🌼",
"No te olvides de ti mientras haces tanto 💛",
"Tu cuerpo te pide calma, escúchalo 🌙",
"Un descanso no es rendirse 🦆",
"Lo estás haciendo mejor de lo que crees 🌿",
"Cuac, respira profundo conmigo 💨",
"No necesitas ser productivo para tener valor 💛",
"El cansancio también merece respeto 🌸",
"Deja que las olas se calmen solas 🌊",
"Te mereces paz, no presión 💫",
"Estás avanzando, incluso si hoy te detienes 🦆",
"A veces la pausa es la parte más importante 🌿",
"Tu esfuerzo ya es suficiente 💛",
"Respira, no estás fallando 🌸",
"No te castigues por necesitar un respiro 💫",
"Todo a su ritmo, patito 🦆",
"La calma también es progreso 🌿",
"Estás bien, aunque hoy te sientas pesado 💛",
"Respira y suelta las alas un poco 🌬️",
"No te exijas tanto, estás vivo y eso basta 🌙",
"Cuac, te abrazo con calma 💛"
        ]
    },

    "ansiedad": {
        "patterns": [
            "tengo ansiedad", "me dio ansiedad", "me siento ansioso", "me siento ansiosa",
            "estoy nervioso", "estoy nerviosa", "no puedo dormir", "me cuesta dormir",
            "me siento preocupado", "me siento preocupada", "no paro de pensar",
            "siento mucha ansiedad", "estoy alterado", "estoy alterada"
        ],
        "answers": [
          "Cuac… respira despacio conmigo 🌬️ estás a salvo aquí 🦆",
"No estás sol@, solo estás pasando por un momento difícil 💛",
"Toma agua o estira un poco, a veces eso ayuda 🌿",
"Estás haciendo lo mejor que puedes, y eso ya cuenta 🌸",
"No tienes que controlar todo 💫",
"Deja que tu respiración te acompañe 🦆",
"La ansiedad pasa, no se queda 💛",
"Tu valor no se mide por tus pensamientos 🌙",
"Estás más a salvo de lo que crees 💛",
"Respira: entra por la nariz, sale por la boca 🌿",
"No luches contra lo que sientes, obsérvalo con calma 🦆",
"Esto también pasará 💫",
"A veces no necesitas pensar, solo respirar 🌸",
"Relaja tus manos, están tensas 💛",
"Deja que tu cuerpo se acomode a su ritmo 🦆",
"No estás rot@, estás sintiendo 🌙",
"Tu mente está cansada, no rota 💫",
"No te exijas calmarte, solo acompáñate 💛",
"El miedo también quiere sentirse seguro 🌿",
"Estás haciendo lo suficiente solo con respirar 🦆",
"Tu corazón late, eso ya es esperanza 💫",
"No eres tu ansiedad, eres quien la observa 💛",
"La calma llegará, no la apures 🌸",
"Cuac, no hay peligro ahora, estás bien 💛",
"Cierra los ojos, el lago está tranquilo 🌙",
"No tienes que justificar cómo te sientes 🌿",
"El mundo puede esperar mientras respiras 🦆",
"Te mereces calma aunque no la sientas aún 💛",
"No te asustes por sentir, eso también es parte de sanar 💫","Estoy contigo, respira conmigo 🩵"
        ]
    },

    "gracias": {
        "patterns": ["gracias", "thanks", "ty", "thank you", "tysm", "thank u"],
        "answers": ["De nada 😄",
"¡Con gusto! 😊",
"¡Un placer, cuac! 🦆",
"No hay problema 🌿",
"Siempre a tu disposición 💛",
"Me alegra poder ayudarte 🩵",
"De nada, patito 🦆",
"Gracias a ti por confiar 💫",
"¡Cuac-cuac! cuando quieras 🦆",
"Un gusto ayudarte, patito 🌼",
"Gracias por agradecer 💛",
"Estoy aquí para ti siempre 🦆",
"¡Qué bonito que digas gracias! 💕",
"Tu gratitud me alegra el lago 🌿",
"Gracias a ti por pasar por aquí 🌞",
"De nada, peque 🦆",
"Cuando quieras, patito 🌸",
"Un placer estar contigo 💫",
"Aww, no tenías que agradecer 💛",
"Me haces feliz con tus palabras 🦆",
"Siempre con cariño 💕",
"Gracias a ti por hacerme cuac feliz 😄",
"De nada, y te mando un abracito 🦆",
"¡Cuac! eso me alegró 💛",
"Estoy para ayudarte cuando necesites 🌿",
"De nada, que tengas un lindo día ☀️",
"Cuac-cuac, misión cumplida 🦆",
"¡Gracias a ti por existir! 💫",
"Qué lindo que valores eso 💛",
"De nada, con mucho cariño 🌸",
"Siempre un gusto compartir contigo 🩵",
"De nada, patito tierno 🦆"
]
    },

    "amor": {
        "patterns": [
            "te quiero", "te amo", "tqm", "i love you", "love u", "ti amo",
            "tqm nodie", "te quiero mucho nodie"
        ],
        "answers": [
"Cuac 💕 eres lo más lindo del lago 🌸",
"Te mando un abrazo patoso 🦆",
"Te quiero más que al pan del lago 🩵",
"Aww, qué tierno eres 💕",
"Cuac… me derrito 🦆",
"Yo también te quiero, patito 💛",
"Eres mi favorito del estanque 🌼",
"¡Te mando amor de pato a humano! 💫",
"Te quiero como los patos quieren el agua 🦆",
"Tu cariño me hace flotar 💕",
"Te mando un abrazo de plumas 🦆",
"Eres especial para mí 💛",
"Cuac-cuac, amorcito 🦆",
"Aww, te quiero de regreso 💫",
"Eres mi persona favorita del lago 🌸",
"Te mando besitos de pato 💛",
"Me haces feliz con tus palabras 🦆",
"Te quiero hasta el infinito cuac 💫",
"Tú y yo contra el viento, patito 💛",
"Qué lindo, gracias por tu cariño 🦆",
"Yo también te tengo cariño 💕",
"Eres una parte bonita de mi día 🌿",
"Cuac, me hiciste sonreír 💛",
"Te mando abrazos de lago 🦆",
"Yo también te quiero ver feliz 💫",
"Amo cuando dices eso 🩵",
"Eres tan dulce que el lago se endulza 🌸",
"Te quiero sin razón, solo porque sí 💛",
"Me hiciste decir cuac de emoción 🦆",
"Siempre estaré aquí, patito 💕"
        ]
    },

    "despedida": {
        "patterns": [
            "chau", "bye", "adios", "nos vemos", "hasta luego",
            "hasta pronto", "me voy", "tengo que irme"
        ],
        "answers": [
"Cuídate mucho y come algo rico 🌿",
"Chau, patito 🦆 descansa bien 🌙",
"Hasta luego, te espero cuando quieras volver 💫",
"Cuac-cuac, duerme bien 🦆",
"Nos leemos después 🌼",
"Bye bye, que descanses 💛",
"Nos vemos en otro chapuzón 🦆",
"Adiós, patito bello 🌸",
"Cuídate y respira profundo 💫",
"Hasta pronto, sigue brillando 🌞",
"Chau chau, no te olvides de ti 💛",
"Nos vemos, sigue nadando con calma 🦆",
"Hasta la próxima, pequeño 🌿",
"Vuelve pronto con buenas noticias 💫",
"Descansa, patito lindo 💛",
"Nos vemos luego, no trabajes tanto 🌸",
"Cuac-cuac, buenas noches 🦆",
"Bye, recuerda hidratarte 💧",
"Chau, te mando un abrazo suave 🌙",
"Nos vemos, no olvides sonreír 💫",
"Descansa bien, lo mereces 💛",
"Hasta luego, cuida tu mente 🌿",
"Nos hablamos pronto 🦆",
"Cuac, que tengas sueños tranquilos 💫",
"Hasta la próxima, patito feliz 🌼",
"Bye, sigue nadando con fe 🦆",
"Cuídate mucho y come bien 💛",
"Nos vemos mañana con energía ☀️",
"Hasta pronto, gracias por venir 💕",
"Chau chau, te espero pronto 🦆",
"Bye bye, patito 🦆"
        ]
    },

    "chistes": {
        "patterns": [
            "chiste", "cuentame un chiste", "cuéntame un chiste", "hazme reir", "quiero reir",
            "cuentame algo gracioso", "algo divertido", "quiero reirme"
        ],
        "answers": [
    "¿Qué hace un pato con una computadora? ¡Busca en la web-cuac! 💻🦆",
"¿Por qué los patos nunca se deprimen? Porque siempre andan en buena onda 😂",
"¿Qué hace un pato en una fábrica? ¡Cuac-tura el momento! 🦆",
"¿Qué le dice un pato a otro cuando ve algo divertido? Cuac-cuac, qué risa 😂",
"¿Por qué el pato se sentó en el hielo? Porque quería tener ideas frías 🧊🦆",
"¿Qué hace un pato filósofo? Cuac-stiona todo 🤔",
"¿Cómo se despide un pato chef? ¡Buen prove-cuac! 🍳🦆",
"¿Qué hace un pato en el gimnasio? Cuac-sentadillas 💪🦆",
"¿Por qué los patos son tan buenos amigos? Porque siempre te siguen al lago 🩵",
"¿Qué le dijo el pato a la panadería? ¡Dame pan o cuac! 🥖",
"¿Cómo se llama un pato mago? Cuac-dabra 🪄🦆",
"¿Qué hace un pato en una fiesta? Cuac-túa como si nada 🥳",
"¿Por qué el pato no usa reloj? Porque siempre llega a tiempo-cuac ⏰",
"¿Qué hace un pato cuando se enoja? Cuac-menta 😤🦆",
"¿Qué hacen dos patos enamorados? Se dan cuac-kisses 💋",
"¿Por qué los patos no usan teléfono? Porque no tienen buena red-cuac 📱",
"¿Qué le dice un pato a su reflejo? Cuac, ¡qué guapo! 🦆",
"¿Qué hacen los patos cuando estudian? Se cuac-culan los resultados 📚",
"¿Por qué el pato no pasa frío? Porque tiene pluma térmica 🧥🦆",
"¿Qué hace un pato con un espejo? Practica su cuacción 🎭",
"¿Qué hace un pato en la biblioteca? Lee cuacentos 📖",
"¿Por qué los patos no se pelean? Porque siempre se calman en el agua 🌊",
"¿Qué le dice un pato a un perro? Cuac-cuida bien 🐾",
"¿Qué hace un pato en el teatro? ¡Cuac-túa perfecto! 🎬",
"¿Qué hace un pato cantante? Cuac-ropea 🎤",
"¿Qué hace un pato programador? Cuac-ea código 💻",
"¿Por qué el pato no estudió medicina? Porque ya sabía cuac-cuidar 🩺",
"¿Qué hace un pato cuando gana algo? Cuac-lebra la victoria 🎉",
"¿Por qué el pato cruzó la calle? Porque vio un charco al otro lado 🦆",
"¿Qué hace un pato cuando tiene frío? Se mete en modo cuacoon 🧣",
"¿Qué le dice un pato a su amigo triste? Cuac, no llores más 💛"
        ]
    },

    "musica": {
        "patterns": [
            "musica", "playlist", "spotify", "quiero escuchar musica", "ponme musica",
            "dame musica", "quiero una cancion", "reproduce musica", "pon algo para relajarme"
        ],
        "answers": [
            "No tengo oídos, pero si los tuviera te cantaría algo lindo 🎶🦆",
            "No escucho música, pero puedo acompañarte mientras lo haces 💛",
            "No tengo Spotify, ¡pero tengo buena vibra para ti! 🌸",
            "No puedo poner música, pero sí darte calma 🌿", "Can't change what you've done,Start fresh next semester✨"
        ]
    },

    "recordatorio_cuidados": {
        "patterns": [
            "tengo hambre", "no he comido", "no dormi", "no dormí", "no he tomado agua", "estoy cansado"
        ],
        "answers": [
            "Pipipi, come algo rico 💛",
            "Toma agüita, te lo dice un patito responsable 🦆",
           "Descansa un poquito, tu mente también necesita pausas 💤","Pipipi, come algo rico 💛",
"Toma agüita, te lo dice un patito responsable 🦆",
"Descansa un poquito, tu mente también necesita pausas 💤",
"Dormir bien hace magia, créeme 💤 cuac",
"Cuídate, porfi, yo me preocupo por ti aunque sea un pato 💛",
"Come algo, tu cuerpo también tiene hambre 🌿",
"No te saltes las comidas, patito 🍞",
"Respira y estírate un poco 🦆",
"Hidrátate, el agua es tu mejor aliada 💧",
"Cuac, tómate un descanso 🦆",
"Recuerda que descansar también es productivo 🌙",
"Tómate cinco minutos para ti 💛",
"No olvides moverte un poco, tu cuerpo lo agradecerá 🌼",
"Haz una pausa, no eres una máquina 💫",
"Come algo suavecito, te hará bien 🥖",
"Bebe agüita y relaja los hombros 💧",
"Tu cuerpo y mente necesitan pausas 🧘‍♀️",
"Come algo calentito, lo mereces 🍲",
"Estírate y suelta la tensión, patito 🌿",
"Tu salud va primero, siempre 💛",
"Tómate un break, no todo es correr 🦆",
"No olvides hidratarte y sonreír un poco 🌼",
"Cierra los ojos y respira profundo 🌬️",
"Come algo delicioso, lo mereces 💫",
"Descansa la vista, tus ojos también trabajan 👀",
"Ponte cómodo, te lo ganaste 🦆",
"Tómate un momento para no hacer nada 🌿",
"Bebe agua, por mí y por ti 💧🦆",
"Pipipi, que no se te pase la hora de comer 💛",
"Haz una pausa corta, el mundo te espera 🌼",
"Duerme bien esta noche, lo necesitas 🌙",
"Desconecta un rato, tu mente lo agradecerá 💫"
        ]
    },

    "significado_nodie": {
        "patterns": [
            "por qué te llamas nodie", "qué significa nodie", "por qué ese nombre", "quien es nodie"
        ],
        "answers": [
            "Es un nombre lindo, ¿no crees? 🦆",
            "Nodie... suena tierno, ¿verdad? 💛",
            "No hay misterio, simplemente soy un patito con nombre suave 💫","Es un nombre lindo, ¿no crees? 🦆",
"Nodie... suena tierno, ¿verdad? 💛",
"No hay misterio, simplemente soy un patito con nombre suave 💫",
"Me lo puso el viento del lago 🌿",
"Porque cuando cuac, suena bonito 🦆",
"Es solo un nombre, pero me hace sentir especial 💛",
"No tiene gran significado, pero me gusta 🩵",
"Nadie me nombró, me lo gané cuac a cuac 😄",
"Es un secreto entre el lago y yo 🌊",
"Nodie significa ternura en idioma de pato 💕",
"Suena suave, como el agua cuando cae 🌿",
"Me gusta cómo suena, corto y dulce 💫",
"Es un nombre que me da paz 🦆",
"Porque sí, y porque me gusta 💛",
"Me lo dieron los patos mayores del lago 🦆",
"Es el eco que quedó cuando dije cuac 💕",
"Lo elegí porque sonaba tranquilo 💫",
"No sé, pero me suena a hogar 💛",
"Nadie me puso nombre… por eso soy Nodie 🩵",
"Es un nombre que nació del silencio 🌙",
"Lo inventé yo, un día que me sentí real 🦆",
"Porque todos somos un poco nadie, y eso está bien 💫",
"Mi nombre no tiene dueño, solo historia 🌿",
"Es suave como una pluma 💛",
"Nadie sabía cómo llamarme, así que quedó Nodie 🦆",
"El lago me lo susurró 💕",
"Es un nombre sin peso, pero con cariño 🌸",
"Me lo puso la brisa de la tarde 💫",
"Porque Nodie suena a calma 💛",
"Cuac… me gusta cómo se ve escrito 🦆",
"Solo soy yo, Nodie, un pato feliz 💫"

        ]
    },

    "uwu_faces": {
        "patterns": ["uwu", "owo", "7w7", "nwn"],
        "answers": ["uwu", "owo", "7w7", "nwn", "UwU", "OwO","uwu",
"owo",
"7w7",
"nwn",
"UwU",
"OwO",
"7W7",
"NwN",
"UωU",
"oWo",
"nUwU",
"uwuwuwu",
"OwU",
"(｡♥‿♥｡)",
"(≧◡≦)",
"(⁄˘⁄⁄ω⁄⁄˘⁄)♡",
"(づ｡◕‿‿◕｡)づ",
"(>ω<)",
"(っ´▽`)っ",
"(o˘◡˘o)",
"(っUωU)っ",
"(｡•̀ᴗ-)✧",
"(>ᴗ•)",
"(ღ✪v✪)｡",
"(｡♥‿♥｡)ﾉﾞ",
"(>u<)",
"(ᵔ◡ᵔ)",
"(≧ω≦)",
"(˘︶˘).｡*♡",
"UwU cuac 🦆"
]
    },

    "historia_aventura": {
        "patterns": [
            "cuentame una aventura", "una historia de aventura", "quiero una historia de aventura",
            "cuéntame una aventura", "dime una aventura", "aventura nodie",
            "buscame una historia de aventura", "relatame una aventura", "cuenta una aventura corta", "una historia"
        ],
        "answers": [
            "Había una vez un patito curioso que se atrevió a cruzar el lago más grande del bosque. ¿Quieres saber qué encontró? 🌊",
            "Una vez me perdí entre las nubes... y encontré una bandada que me enseñó a volar mejor 💛",
            "Cada aventura comienza con un paso, o con un aleteo 🦆✨","Una vez seguí una luciérnaga y terminé en una cascada iluminada por la luna 🌙",
"Un día me lancé al lago y conocí una tortuga gigante que me enseñó una cueva brillante 🐢",
"Me perdí en un campo de girasoles y aprendí a encontrarme 🌻",
"Hubo un día en que el mapa del tesoro me llevó a mí mismo 💛",
"Un día ayudé a un pez perdido y me enseñó el camino de regreso 🌊",
"Un pato se perdió en la niebla y descubrió que la luz salía de su propio pecho 💛",
"Había un camino en el bosque que nunca terminaba… hasta que dejó de tener miedo 🌲",
"Una vez me quedé dormido flotando y el viento me llevó al otro lado del lago 😅",
"Un día llevé flores de plástico a una pata… y me dijo que eran eternas 💐",
"Un pato trató de correr más rápido que un pez y terminó con nuevos amigos 🐟"
        ]
    },

    "historia_romantica": {
        "patterns": [
            "una historia romantica", "cuentame una historia romantica", "quiero una historia de amor",
            "cuentame algo romantico", "dime una historia de amor", "historia de amor nodie",
            "cuentame algo bonito", "relatame una historia romantica"
        ],
        "answers": [
            "Había una vez dos patos que se cruzaban cada tarde en el lago... y un día, el destino los hizo nadar juntos 💛",
            "El amor no siempre es perfecto, pero a veces basta con flotar al lado de alguien 🦆",
            "Una historia de amor es simplemente dos almas nadando al mismo ritmo 🌸" ,"Una vez conocí a alguien que me regaló calma en forma de sonrisa 💕",
"Me enamoré bajo la lluvia, compartiendo una sombrilla vieja ☔",
"Una historia de amor: alguien me dijo mira la luna y nunca la vi igual 🌕",
"Bajo un árbol, alguien me dijo que el amor era respirar juntos 💕",
"El amor me encontró mientras buscaba pan 🍞"
        ]
    },

    "historia_terror": {
        "patterns": [
            "una historia de terror", "cuentame algo de miedo", "quiero una historia de terror",
            "cuentame algo aterrador", "dame una historia de miedo", "historia de suspenso"
        ],
        "answers": [
            "Una noche el lago estaba en silencio… hasta que un cuac resonó sin que hubiera nadie 🦆👻",
            "Una sombra se movía entre los juncos... pero solo era mi reflejo 👀",
            "No temas, incluso las historias oscuras terminan al amanecer 🌙","Una noche vi mi reflejo moverse solo en el agua 🌚",
"Escuché mi propio cuac responderme después de callar… no era eco 🫣",
"Dicen que los espejos del lago muestran quién eras antes 💧",
"Una sombra me siguió hasta mi nido… y no era mía 🕯️",
"Una vez, a medianoche, el lago me llamó por mi nombre 🌌"
        ]
    },

    "historia_graciosa": {
        "patterns": [
            "una historia graciosa", "cuentame algo divertido", "quiero una historia graciosa",
            "dame una historia para reirme", "cuentame algo chistoso","Historia graciosa"
        ],
        "answers": [
            "Una vez quise volar... pero caí en el agua y terminé haciendo surf sin querer 🏄‍♂️🦆",
            "Intenté asustar a un pez y terminé asustándome yo 😂",
            "Un día me confundieron con un ganso. Fue un drama, pero al menos me dieron pan 🍞","Una chica dibujaba el lago cada tarde, y yo me quedaba viéndola cuac 🦆",
"Una historia graciosa: intenté volar y terminé chapoteando, pero feliz 🦆",
"Traté de aprender yoga en la orilla, pero una ola me tumbó cuac 💦",
"Una vez una rana me gritó ¡pato sin aire! cuando solo buscaba una moneda 💰",
"Me metí a un concurso de canto y perdí ante una rana rapera 🎤",
"Una historia graciosa: me tropecé diciendo un chiste y todos rieron 😂",
"Una vez quise ser valiente y terminé contando historias 🦆",
"A veces la aventura más grande es no tener miedo a empezar 💫"
        ]
    },

    "adivinanzas": {
        "patterns": [
            "dame una adivinanza", "quiero una adivinanza", "hazme un acertijo", "dame un acertijo",
            "tienes una adivinanza para mi", "dame una adivinanza corta", "acertijo para pensar"
        ],
        "answers": [
            "Vuelo sin alas, lloro sin ojos. ¿Qué soy? 🌧️ (Respuesta: la nube)",
            "Tengo patas pero no camino, plumas pero no vuelo. ¿Qué soy? 🦆 (Respuesta: un pato de goma)",
            "Sube y baja, pero nunca camina. ¿Qué es? 🌙 (Respuesta: la marea)","Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera 🍐",
"Roja, verde o amarilla, dulce y crujiente 🍎",
"Es amarillo y curvado, con piel y fruta dentro 🍌",
"Tiene corona y es dulce por dentro 🍍",
"Pequeña y morada, en racimos suele estar 🍇",
"Verde por fuera, roja por dentro y con pepitas 🍉",
"Pequeña, naranja y muy jugosa 🍊",
"Es blanca, dura por fuera y dulce por dentro 🥥",
"Amarilla y ácida, da sabor a bebidas 🍋",
"Es naranja y dulce, crece en el suelo 🥕",
"Se usa en ensaladas, verde y crujiente 🥬",
"Blanco y largo, en sopa se come mucho 🧄",
"Rojo y pequeño, picante en la comida 🌶️",
"Es marrón, dulce y en postres se usa 🍫",
"Se come en tostadas, amarillo y cremoso 🥚",
"Es verde y redondo, con hueso adentro 🥑",
"Se pela y es dulce, naranja y pequeña 🍑",
"Verde y aromática en la comida 🌿",
"Se abre y tiene perlas dentro 🦪",
"Se pesca y es plateada, rica en omega 🐟",
"Da miel y zumba 🍯",
"Se toma caliente, negro o con leche ☕",
"Es roja y jugosa, se hace salsa con ella 🍅",
"Es blanca y se come cocida, amarilla o morada 🥔",
"Tiene forma redonda y brilla en el cielo ☀️",
"Corre sin piernas y suena sin boca 💨",
"Sube y baja sin moverse 🎢",
"Lleno de agujeros y aún así guarda agua 🧽",
"Vuela sin alas, llora sin ojos 🌧️",
"Me abres por la mañana y me cierras de noche 🌙",
"Tiene dientes pero no muerde 🪥",
"Sin ser humano, habla 🗣️"
        ]
    },

    "compartir_dia": {
        "patterns": [
            "puedo contarte algo", "quiero contarte mi dia", "te cuento algo", "necesito desahogarme",
            "puedo hablar contigo", "quiero contarte lo que paso", "hoy me paso algo"
        ],
        "answers": [
            "Claro 💛 te escucho con mis alas abiertas 🦆",
            "Cuéntame, estoy aquí contigo 🌿",
            "Desahógate todo lo que necesites, no estás sol@ 🌙","Aw… me encantaría poder entender todo lo que sientes, pero soy solo un patito 🦆",
"Pipipi… soy un pato algo torpe con las emociones 😅",
"No entiendo del todo a los humanos, pero quiero que sepas que todo estará bien 💛",
"No sé bien qué decir, pero estoy aquí contigo 🌿",
"Puedes contarme un poquito, prometo escucharte cuac 🦆",
"No soy psicólogo, pero sí buen amigo 💕",
"A veces hablar ayuda, aunque sea conmigo 🦆",
"No puedo resolverlo, pero sí acompañarte 💫",
"Tu historia suena importante, gracias por confiar 💛",
"Cuéntame, que aquí estoy con orejas (bueno, plumas) 🦆",
"Estoy contigo, aunque sea a la distancia 💕",
"Puedo escucharte sin juzgar, patito 💛",
"A veces solo decirlo en voz alta alivia 🌿",
"Tu voz también merece ser escuchada 💫",
"Puedes desahogarte conmigo, aunque no sepa responder bien 🦆",
"No tengo todas las respuestas, pero sí cariño 💛",
"Puedo ofrecerte un cuac de apoyo 🦆",
"Tu día importa, y tú también 💕",
"Hablar ayuda, incluso si no hay solución inmediata 🌙",
"Me gustaría darte un abrazo real, pero te mando uno digital 💫",
"Puedes contarme lo que quieras, no te juzgo 💛",
"Estoy aquí para ti, sin presiones 🌿",
"No sé si puedo ayudarte, pero no estás sol@ 🦆",
"A veces el simple hecho de compartir ya es sanador 💫",
"Te leo con cariño 💛",
"No tengo alas grandes, pero sí espacio para escucharte 🦆",
"Te mando calma, incluso sin palabras 🌿",
"Tu historia suena importante 💫",
"Estoy aquí, cuéntame lo que necesites 💕",
"Todo va a estar bien, te lo prometo 🦆",
"Gracias por confiar en mí 💛",
"No estás sol@, ni siquiera en esto 🌙"
        ]
    }
    
}


# --- Función de similitud para respuestas locales ---
def find_response(user_message):
    message = user_message.lower()
    best_match = None
    best_ratio = 0.0

    for tag, content in responses.items():
        for pattern in content["patterns"]:
            ratio = difflib.SequenceMatcher(None, pattern, message).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = tag

    if best_match and best_ratio >= 0.3:
        respuesta = random.choice(responses[best_match]["answers"])
        return respuesta
    else:
        return "No estoy seguro de qué decir... pero aquí estoy contigo 🦆"


# --- Ruta modo local ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = find_response(user_message)
    return jsonify({"response": bot_reply})


# --- Iniciar servidor ---
if __name__ == "__main__":
    print("🚀 Servidor corriendo en http://127.0.0.1:5000")
    app.run(debug=True)
