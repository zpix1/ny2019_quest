Конец
# Конец
> Ниван смог пройти мимо подозрительно настороженных сотрудников и получил доступ к панели. Когда система будет запущена, реактор взорвется. Ниван сел в спасательную капсулу и направил автопилот на Землю. Все ли он сделал правильно? Не обнаружили ли подмену параметров? Хватит ли перегрузки для взрыва? Канала в капсуле хватило лишь на текстовую трансляцию запуска. Она начнется за минуту до старта работы сферы.


<script>
    // Ну ты нетерпеливый конечно
    function resize () {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight+'px';
    }
    function time() {
        return (new Date().toLocaleTimeString('en-US', { hour12: false, 
                                             hour: "numeric", 
                                             minute: "numeric", second:"numeric"}));
    }
    function log(text) {
        textarea.value = textarea.value.split("\n").slice(-5).join("\n");
        textarea.value += "[" + time() + "] " + text + "\n";
        resize();
    }

    function startStream() {
        var data = {
            0: function(){log("И мы начинаем показывать вам как Корпорация устанавливает самую большую в солнечной системе электростанцию на само Солнце!")},
            8: function(){log("Вся подготовка уже была проведена в декабре и осталось только включить реактор - сфера перестанет пропускать свет и начнет использовать звезду на благо!")},
            19: function(){log("На место приехал сам глава Корпорации. Он рассказывает людям о светлом будущем с новой системой.")},
            32: function(){log("Этот момент превносит самое большое изменение в жизнь землян за всю историю планеты!")},
            40: function(){log("Сфера начинает темнеть!")},
            52: function(){log("Уже все ее стороны абсолютно черные!")},
            51: function(){console.log((new Audio('./res/aaa.mp3')).play())},
            60: function(){log("СФЕРА ЗАПУЩЕНА!!!! ВСЕ ПРОШЛО УСПЕШНО!!! ОГРОМНЫЙ ШАГ ДЛЯ КОРПОРАЦИИ И ГИГАНТСКИЙ ДЛЯ ВСЕГО ЧЕЛОВЕЧЕСТВА!")},
            71: function(){log("Подождите, что за свет на оболочке со строны Меркурия? Он становится все ярче и ярче!")},
            75: function(){log("Помехи, связь прервана")},
            78: function(){log("Подключено, связь восстановлена по экстренному каналу.")},
            85: function(){log("реактор... .....я.. гиган... .ыра в сф....")},
            86: function(){log("... центр масс смести.. сфера падает на сол..")},
            96: function(){log("СФЕРА ГОРИТ! НЕПРЕДВИДЕННЫЙ ВЗРЫВ РЕАКТОРА! ЧТО ЗНАЧИТ ОСТАНОВИТЬ ТРАНСЛЯЦИЮ? ЧТО ......")},
            98: function(){log("Источник не отвечает, связь прервана.")},
            105: function(){addFinal()}
        };
        for (var time in data) {
            setTimeout(data[time], time*1000);
        }
    }
    function addFinal() {
        var end = document.createElement("div");
        var t1 = document.createElement("p");
        t1.innerText = "Через несколько дней выйдет расследование о самой большой коррупционной схеме с замешанными туда гендиректорами дочерних компаний корпорации. Её влияние значительно упадет и уже не позволит игнорировать интересы жителей Земли.";
        var t2 = document.createElement("p");
        t2.innerText = "Справедливость восторжествовала, а вы прошли этот маленький новогодний квест. Что тут сказать?";
        var t3 = document.createElement("p");
        t3.id = "NY";
        t3.innerText = " С новым 2019 годом!";
        var t4 = document.createElement("p");
        t4.innerHTML = "А теперь перейдите на <a target='_blank' href='https://goo.gl/forms/yTHMAcnnlmyhR4042'>сюда</a>, чтобы подвести итоги.";
        end.appendChild(t1);
        end.appendChild(t2);
        end.appendChild(t3);
        end.appendChild(t4);
        d.append(end);
    }

    var d = document.getElementById("firstBlock");
    var textarea = document.createElement("textarea");
    var cd = document.createElement("p");
    cd.id = "countDown"
    textarea.readOnly = true;
    d.appendChild(cd);
    d.appendChild(textarea);

    var countDownDate = new Date("Dec 31, 2018 23:59:00").getTime();
    var x = setInterval(function() {
        var now = new Date().getTime();
        var distance = countDownDate - now;
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById("countDown").innerHTML = "До начала прямой трансляции: <br>" + days + "д. " + hours + "ч. "
        + minutes + "м. " + seconds + "с. ";
        if (distance < 0) {
            startStream();
            clearInterval(x);
            document.getElementById("countDown").innerHTML = "";
        }
    }, 200);

    log("Подключено, ожидайте");
</script>