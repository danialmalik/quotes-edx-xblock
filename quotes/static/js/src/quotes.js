/* Javascript for QuotesXBlock. */
function QuotesXBlock(runtime, element) {

    function updateQuote(result) {
        $('.quote', element).text(result.quote);
    }

    var handlerUrl = runtime.handlerUrl(element, 'save_quote');

    $('.saveQuote', element).click(function(eventObject) {
        var quoteData = $('.quote').val()
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"quote": quoteData}),
            success: updateQuote
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
