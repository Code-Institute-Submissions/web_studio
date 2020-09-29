(function () {

/*ANIMATION TO FADE OUT ELEMENTS FROM SVG TO REVEAL TEXT
*
* IF YOU CAN IMAGINE IT YOU CAN HAVE IT
*
* AND WE ARE COMPANY TO HELP YOU BUILD IT
* */
    setTimeout(start, 1350)

//https://stackoverflow.com/a/6274381
    function shuffle(a) {
        for (let i = a.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [a[i], a[j]] = [a[j], a[i]];
        }
        return a;
    }

    var time = 350
    $('#text,.text').fadeOut(0)
    var elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'z', 'x', 'y', 'w', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']

    function start() {


        for (var element in shuffle(elements)) {


            setTimeout(fadeOutElement(elements[element], time), time)
            time = (elements.length - element) * 350

        }
    }

    setTimeout(fadeInText(elements.length), elements.length * 350)

    function fadeInText(time) {

        $('#text').fadeIn((time + 5) * 350)
        $('.text').fadeIn((time * 3) * 350)
    }

    function fadeOutElement(element, time) {
        $('#' + element + '_1_').fadeOut(time)

    }

})()