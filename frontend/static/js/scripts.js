document.addEventListener('DOMContentLoaded', function () {
    const categoryTitles = document.querySelectorAll('.category-title');
    categoryTitles.forEach(function (title) {
        title.addEventListener('click', function () {
            const items = title.nextElementSibling;
            if (items.style.display === 'none' || items.style.display === '') {
                items.style.display = 'block';
            } else {
                items.style.display = 'none';
            }
        });
    });
});
