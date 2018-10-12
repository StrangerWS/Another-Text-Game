﻿label start:
    call init_classes from _call_init_classes

    scene bg autumn leaves with Dissolve (3)
    nvl clear
    hide screen nvl
    $ renpy.pause()

    window show dissolve
    call access_inventory from _call_access_inventory

    "Эта история началась много лет назад."
    "Едва вернув престол и отбив атаку Хаметской Империи, правитель Кельгарра Колетт Ниакар, направил распоряжение в исторический корпус университета."
    "Распояжение было чёткое и краткое:"
    king "Приказываю немедленно собрать экспедицию в Пустоши и исследовать Заброшенный Город. Взамен обещаю неслыханное богатство и невиданную честь."
    "Надо ли говорить, что в историческом корпусе творился настоящий хаос? Каждый, кто хоть краем уха слышал об экспедиции, бежал прямиком в университет."
    "Бард Вермес, направлявшийся из Дрекора в Мавенфелл, столицу Кельгарра, тут же забеспокоился."
    bard "Бедный Куатрис, представляю, какая толпа сейчас у него в кабинете."
    "Куатрис, декан истроического корпуса, был хорошим другом Вермеса. Они часто вместе путешествовали, и Вермесу даже была оказана честь присоединиться к некоторым экспедициям."
    "Вермес решил отложить все свои выступления, пока не встретится с другом. Он толкнул извозчика и попросил доставить его прямиком в исторический корпус."
    "Молодой тощий паренёк вздохнул:"
    boy "И вы туда же, господин. Очнитесь, не даруют вам неслыханных богатств. Страна-то только войну закончила."
    bard "О, нет, милейший. Я еду к другу, на которого весь этот ад и свлалися."
    boy "Э... простите, господин. Сию секунду довезу."

    call restrict_inventory from _call_restrict_inventory
    nvl clear

    kuat "Никто никуда не поедет! Успокойтесь вы!"
    "Куатрис был явно взбешён: на площади исторического корпуса уже неделю собирались {a=call:vocab_kel}кели{/a} и требовали взять их в поход. Некоторые уже начали ставить палатки, надеясь, что в какой-то момент декан смилостивится и они отправятся в путешествие."
    kuat "И о чём они думали, когда назначали меня ответственным за эту экспедицию?"
    "Вермес, пробирающийся сквозь толпу, остался незамеченным деканом. И поэтому, когда бард начал вещать своим низким и громогласным голосом, эльф подпрыгнул:"
    bard "Граждане! Прошу всех разойтись, ибо экспедиция уже собрана и отправлена в путешествие!"
    man "А что ж он никуда не поехал? Ты думаешь, мы поверим, что Куатрис не поедет с экспедицией?"
    thgt "Да, об этом я не подумал... Ну, что ж, была не была!"
    "Вермес начал напевно вещать:"
    bard """
    {i}Вы не верите мне, так поверьте другим.\n
    В путь далёкий отправились девять мужчин.\n
    Всех я встретил, извозчик не даст мне соврать,\n
    А теперь попрошу вас палатки убрать.{/i}
    """

    "Все, кто слышал эти напевы, стали разбредаться. Кто-то грустно опустив голову, кто-то яростно жестикулируя, некоторые не стеснялись в выражениях. Вермес же наконец-то протянул руку Куатрису."
    bard "Теперь ты должен взять меня с собой."
    "Усмехнулся бард."
    kuat "И ты туда же, хитрец!"
    "Куатрис пожал протянутую руку и жестом пригласил Вермеса зайти."

    return
