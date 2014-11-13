$(document).ready(function () {
    $('.challenge').on('click', function (event) {
        event.preventDefault();
        var $this = $(this);
        var $nextElement = $this.next();
        if ($nextElement && $nextElement.hasClass('challenge-detail')) {
            $nextElement.remove();
        }
        else {
            var xhr = $.get('/api/challenge', {'id': $this.data('id')});
            xhr.done(function (html) {
                var $html = $(html);
                var $container = $html.find('.container');
                $container.hide();
                $this.after($html);
                $container.fadeIn('fast');
            });
        }
    });

    $('#challenges').on('submit', '.challenge-detail form', function (event) {
        event.preventDefault();
        var $target = $(event.target);
        var $xhr = $.post($target.attr('action'), $target.serialize());
        $xhr.done(function (response) {
            // put message on top of the form + reflow alerts
            $target.before(response);
            $(document).foundation('alert', 'reflow');
        });
        $xhr.error(function (response) {
            // extract the form...
            var responseForm = $(response.responseText).find('form').html();
            $target.parents('.challenge-detail').find('form').html(responseForm);
        });

    });
});