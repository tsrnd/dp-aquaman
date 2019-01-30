$(document).ready(function () {
    $.ajax({
        url: 'http://localhost:8000/api/brands/',
        type: 'GET',
        success: function (data) {
            var brands = data['result']
            if (Array.isArray(brands) && brands.length) {
                brands.forEach(function (brand) {
                    $('#list-brand ul')
                        .append('<li><a href="?brand_id='+brand['id']+'">'+brand['brand_name']+'</a></li>')
                })
            }
        }
    })
})