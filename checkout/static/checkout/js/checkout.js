(function () {


 var total = 0
    var policies = 0
    $('#more_pages').on('change', function () {
        console.log($(this).val())
        $('#extra_pages').text($(this).val())
        $('#extra_pages_cost').text($(this).val() * 99)
         total = parseInt($('#total').text()) + parseInt($(this).val() * 99) + policies

        $('#grand_total').text(total)


    })
    $('#policies').on('click', function () {

        if ($(this).is(":checked")) {
             policies = 99
             $('#grand_total').text( parseInt($('#grand_total').text()) + 99)
        } else {
             policies = 0
             $('#grand_total').text(parseInt($('#grand_total').text()) - 99)
        }
         console.log('total '+total)
    })

})()