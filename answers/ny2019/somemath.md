Немного математики
# Немного математики
> Ниван стучал, но дверь открывать похоже никто не собирался. Дело срочное, поэтому нетерпеливый ученый пнул ее ногой - дверь распахнулась. Просто опилки в косяке перегнили, и задвижка замка их выбила. Ниван вошел в дом, и только тогда появился Джон Б. с бумажкой и ручкой. 

> Он подошел к Нивану и всунул ему эти предметы: "Помоги мне решить задачку, а потом уже спрашивай, что тебе нужно."

Помоги Нивану и Джону получить ответ:

> Найдите все значения a, при каждом из которых система уравнений
> ![a](https://i.imgur.com/55zlQJB.png)
> имеет ровно два различных решения.

Убери из правильно записанного ответа все символы кроме цифр (включая минусы) и запиши его в компьютер Джона:
<script>
    // Ты думал ты самый умный? Ну пойди, разберись
    // По сложности то же самое
    // Ну или меньше, не знаю
    const encrypted = "燪燶燻熾燬燻燿燽燪燱燬熾燱燸熾燪燶燻熾燭燮燶燻燬燻熾燩燿燭熾燼燫燷燲燪熾燿燽燽燱燬燺燷燰燹熾燪燱熾燪燶燻熾燱燲燺熾燺燬燿燩燷燰燹燭熲熾燪燶燻燬燻熾燷燭熾燿熾燭燮燻燽燷燿燲燲燧熾燳燿燺燻熾燳燷燭燪燿燵燻熰熾燮燿燭燭燩燱燬燺熾燷燭熾燰燱燪燿燲燲燻燬燬燱燬燭燿燬燻燿燽燽燷燺燻燰燪燿燲";
    function crypt(str, key){
        var encryptedText = '';
        for(let i = 0; i < str.length; i++) {
            let char = str.charCodeAt(i) ^ key;
            encryptedText += String.fromCharCode(char);
        }
        return encryptedText;
    }
    function decrypt() {
        var key = document.getElementById("keyInput").value;
        if (key.length === 0) {
            alert("No key error");
        } else if (key.length !== 6) {
            alert("Wrong key length");
        } else {
            alert(crypt(encrypted, key))
        }
    }

    var d = document.getElementById("firstBlock");
    var v = document.createElement("div");
    v.className = "johnPCDiv"
    var button = document.createElement("button");
    button.onclick = decrypt;
    button.innerText = "Decrypt"
    var input = document.createElement("input");
    input.id = "keyInput";

    v.appendChild(input);
    v.appendChild(button);

    d.appendChild(v);
</script>

WriteUp

http://bit.ly/notallerrorsareaccidental -> [value](reactorerror.html)


`a = (-6; 1) and {8} and [9; 10]`

618910

https://ege.sdamgia.ru/problem?id=509206


the reactor of the sphere was built according to the old drawings, there is a specially made mistake. password is notallerrorsareaccidental