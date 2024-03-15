
function handleClick() {
    alert('Button clicked!');
}

// Example of using jQuery for a smoother scrolling effect
$(document).ready(function() {
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();

        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500, 'linear');
    });
});
