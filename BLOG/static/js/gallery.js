$(document).ready(function(){
    $('.list').click(function(){
        const value = $(this).attr('data-filter');
        if (value=='all'){
            $('.dogbox').show('1000');
        }
        else{
            $('.dogbox').not('.'+value).hide('1000');
            $('.dogbox').filter('.'+value).show('1000');
        }
    })
    $('.list').click(function(){
        $(this).addClass('active').siblings().removeClass('active')
    })
})