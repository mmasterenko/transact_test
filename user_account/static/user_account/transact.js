(function($) {
    $(document).ready(function () {
        var transact_btn = $('#id_transact');
        transact_btn.click(function (e) {
            var data = {
                user_id : $('#id_user').val(),
                summa : $('#id_summa').val(),
                inns : $('#id_to_inns').val(),
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            };
            console.log(data);
            $.post('/validate', data, function (response) {
                if(response['status'] == 'ok') {
                    $.post('/transact', data, function (transact_response) {
                        if(transact_response['status'] == 'ok') {
                            alert('Перевод успешно выполнен !')
                        } else {
                            alert('Ошибка перевода')
                        }
                    })
                } else {
                    alert(response['msg'])
                }
            });
        });
    });
})(jQuery);
