(function($) {

    function highlightActiveMenuChoice() {

        var $menuListItems = $('ul.navbar-nav.side-nav li a'),
            location = window.location.pathname,
            activeItem = {
                hrefLength: 0,
                $obj: null
            };

        $menuListItems.each(function () {
            var href = $(this).attr('href'),
                $currentObject = $(this).parent();
            if (location.indexOf(href) === 0) {
                if (href.length > activeItem.hrefLength) {
                    if (activeItem.$obj) {
                        activeItem.$obj.removeClass('active');
                        if (activeItem.$obj.parent().parent().hasClass('dropdown')) {
                            activeItem.$obj.parent().parent().removeClass('open');
                        }
                    }
                    $currentObject.addClass('active');
                    if ($currentObject.parent().parent().hasClass('dropdown')) {
                        $currentObject.parent().parent().addClass('open');
                    }
                    activeItem.hrefLength = href.length;
                    activeItem.$obj = $currentObject;
                }
            }
        });

    }

    $(document).ready(function () {
        highlightActiveMenuChoice();
    });

})(jQuery);